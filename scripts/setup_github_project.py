#!/usr/bin/env python3
"""
GitHub Project Setup Script

This script creates a GitHub repository and project for a course instance.
It sets up labels, creates issues from templates, and configures the project board.

Usage:
    python setup_github_project.py --config ../course-info.yaml [options]

Requirements:
    - GITHUB_TOKEN environment variable must be set with appropriate permissions
    - course-info.yaml must be properly configured
"""

import os
import sys
import argparse
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml
import json
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class GitHubSetup:
    """Setup GitHub repository and project for course."""

    def __init__(self, token: str, config: Dict):
        self.token = token
        self.config = config
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        self.org = config['github']['organization']
        self.repo_name = self._format_repo_name()
        self.repo_full_name = None
        self.project_id = None

    def _format_repo_name(self) -> str:
        """Generate repository name from template."""
        template = self.config['github']['repo_name_template']
        return template.format(
            semester=self.config['course']['semester'],
            section=self.config['course']['section'],
            course_number=self.config['course']['course_number'].replace('-', ''),
            crn=self.config['course']['crn']
        )

    def setup_repository(self) -> None:
        """Create or update GitHub repository."""
        print(f"Setting up GitHub repository: {self.org}/{self.repo_name}")

        # Check if repo exists
        repo_url = f"https://api.github.com/repos/{self.org}/{self.repo_name}"
        response = self.session.get(repo_url)

        if response.status_code == 200:
            print(f"  ✓ Repository already exists")
            repo = response.json()
            self.repo_full_name = repo['full_name']
            return

        # Create new repository
        create_url = f"https://api.github.com/orgs/{self.org}/repos"
        repo_data = {
            'name': self.repo_name,
            'description': f"{self.config['course']['title']} - {self.config['course']['semester']} Section {self.config['course']['section']}",
            'private': self.config['github'].get('private_repo', True),
            'has_issues': True,
            'has_projects': True,
            'has_wiki': False,
            'auto_init': True
        }

        response = self.session.post(create_url, json=repo_data)
        response.raise_for_status()

        repo = response.json()
        self.repo_full_name = repo['full_name']
        print(f"  ✓ Created repository: {repo['html_url']}")

    def setup_labels(self) -> None:
        """Create issue labels in repository."""
        print("Setting up labels...")

        labels_config = self.config['github']['project'].get('labels', [])
        if not labels_config:
            print("  No labels to create")
            return

        url = f"https://api.github.com/repos/{self.org}/{self.repo_name}/labels"

        for label in labels_config:
            label_data = {
                'name': label['name'],
                'color': label['color'].lstrip('#'),
                'description': label.get('description', '')
            }

            response = self.session.post(url, json=label_data)

            if response.status_code == 201:
                print(f"  ✓ Created label: {label['name']}")
            elif response.status_code == 422:
                # Label already exists, update it
                update_url = f"{url}/{label['name']}"
                response = self.session.patch(update_url, json=label_data)
                if response.status_code == 200:
                    print(f"  ✓ Updated label: {label['name']}")
                else:
                    print(f"  ⚠ Could not update label {label['name']}: {response.text}")
            else:
                print(f"  ✗ Error creating label {label['name']}: {response.text}")

    def create_issues_from_templates(self, issues_dir: Path) -> List[int]:
        """Create GitHub issues from template files."""
        print("Creating issues from templates...")

        if not issues_dir.exists():
            print("  Issues directory not found")
            return []

        issue_files = sorted(issues_dir.glob('*.md'))
        if not issue_files:
            print("  No issue templates found")
            return []

        created_issues = []

        for filepath in issue_files:
            with open(filepath, 'r') as f:
                content = f.read()

            # Parse frontmatter
            metadata, body = self._parse_frontmatter(content)

            # Create issue
            issue_data = {
                'title': metadata.get('title', filepath.stem),
                'body': self._substitute_variables(body),
                'labels': metadata.get('labels', [])
            }

            # Add assignees if specified
            if 'assignees' in metadata:
                issue_data['assignees'] = metadata['assignees']

            # Add milestone if specified
            if 'milestone' in metadata:
                issue_data['milestone'] = metadata['milestone']

            url = f"https://api.github.com/repos/{self.org}/{self.repo_name}/issues"
            response = self.session.post(url, json=issue_data)

            if response.status_code == 201:
                issue = response.json()
                created_issues.append(issue['number'])
                print(f"  ✓ Created issue #{issue['number']}: {issue['title']}")
            else:
                print(f"  ✗ Error creating issue from {filepath.name}: {response.text}")

        return created_issues

    def create_project(self) -> None:
        """Create GitHub Project (Classic) for course."""
        if not self.config['github']['project'].get('create_project', False):
            print("Project creation disabled in config")
            return

        print("Creating GitHub Project...")

        project_name = self.config['github']['project']['project_name_template'].format(
            semester=self.config['course']['semester'],
            section=self.config['course']['section']
        )

        # Use Projects V2 API (newer GraphQL API)
        # Note: This requires different authentication and approach
        # For now, we'll use the classic projects API

        url = f"https://api.github.com/repos/{self.org}/{self.repo_name}/projects"
        project_data = {
            'name': project_name,
            'body': f"Course planning and tracking for {self.config['course']['title']}",
        }

        # Need to use Projects V2 accept header
        headers = self.headers.copy()
        headers['Accept'] = 'application/vnd.github.inertia-preview+json'

        response = self.session.post(url, json=project_data, headers=headers)

        if response.status_code == 201:
            project = response.json()
            self.project_id = project['id']
            print(f"  ✓ Created project: {project['name']}")
            print(f"    URL: {project['html_url']}")

            # Create default columns
            self._create_project_columns(project['id'])
        else:
            print(f"  ✗ Error creating project: {response.text}")

    def _create_project_columns(self, project_id: int) -> None:
        """Create default columns for the project board."""
        print("  Creating project columns...")

        columns = [
            'To Do',
            'In Progress',
            'Done'
        ]

        url = f"https://api.github.com/projects/{project_id}/columns"
        headers = self.headers.copy()
        headers['Accept'] = 'application/vnd.github.inertia-preview+json'

        for column_name in columns:
            column_data = {'name': column_name}
            response = self.session.post(url, json=column_data, headers=headers)

            if response.status_code == 201:
                print(f"    ✓ Created column: {column_name}")
            else:
                print(f"    ✗ Error creating column {column_name}: {response.text}")

    def _substitute_variables(self, text: str) -> str:
        """Substitute template variables with values from config."""
        if not text:
            return text

        import re

        # Find all {variable} patterns
        pattern = r'\{([^}]+)\}'

        def replace_var(match):
            var_path = match.group(1).strip()
            value = self._get_nested_value(self.config, var_path)
            return str(value) if value is not None else match.group(0)

        return re.sub(pattern, replace_var, text)

    def _get_nested_value(self, data: Dict, path: str) -> Any:
        """Get a value from nested dict using dot notation."""
        keys = path.split('.')
        value = data

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None

        return value

    @staticmethod
    def _parse_frontmatter(content: str) -> tuple:
        """Parse YAML frontmatter from markdown content."""
        import re

        # Match YAML frontmatter between --- markers
        pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(pattern, content, re.DOTALL)

        if match:
            yaml_content = match.group(1)
            body = match.group(2)
            metadata = yaml.safe_load(yaml_content) or {}
            return metadata, body
        else:
            return {}, content


def load_config(config_path: Path) -> Dict:
    """Load and validate course configuration."""
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Validate required fields
    required_fields = [
        ('course', 'semester'),
        ('course', 'section'),
        ('github', 'organization'),
        ('github', 'repo_name_template')
    ]

    for section, field in required_fields:
        if section not in config or field not in config[section]:
            raise ValueError(f"Required field missing in config: {section}.{field}")

    return config


def main():
    parser = argparse.ArgumentParser(
        description='Setup GitHub repository and project for course'
    )
    parser.add_argument(
        '--config',
        required=True,
        type=Path,
        help='Path to course-info.yaml configuration file'
    )
    parser.add_argument(
        '--issues-dir',
        type=Path,
        help='Directory containing issue templates (default: ../issues relative to config)'
    )
    parser.add_argument(
        '--skip-repo',
        action='store_true',
        help='Skip repository creation'
    )
    parser.add_argument(
        '--skip-issues',
        action='store_true',
        help='Skip issue creation'
    )
    parser.add_argument(
        '--skip-project',
        action='store_true',
        help='Skip project creation'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )

    args = parser.parse_args()

    # Load configuration
    try:
        config = load_config(args.config)
    except Exception as e:
        print(f"Error loading configuration: {e}", file=sys.stderr)
        sys.exit(1)

    # Get GitHub token from environment
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Determine issues directory
    if args.issues_dir:
        issues_dir = args.issues_dir
    else:
        issues_dir = args.config.parent / 'issues'

    if args.dry_run:
        print("DRY RUN MODE - No changes will be made\n")
        setup = GitHubSetup(github_token, config)
        print(f"Would create repository: {setup.org}/{setup.repo_name}")
        print(f"Would use issues from: {issues_dir}")
        sys.exit(0)

    # Initialize setup
    setup = GitHubSetup(github_token, config)

    try:
        # Create repository
        if not args.skip_repo:
            setup.setup_repository()
            setup.setup_labels()

        # Create issues from templates
        if not args.skip_issues:
            created_issues = setup.create_issues_from_templates(issues_dir)
            print(f"\n✓ Created {len(created_issues)} issues")

        # Create project board
        if not args.skip_project:
            setup.create_project()

        print(f"\n✓ GitHub setup complete!")
        print(f"Repository: https://github.com/{setup.org}/{setup.repo_name}")

    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error communicating with GitHub: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
