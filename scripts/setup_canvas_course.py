#!/usr/bin/env python3
"""
DEPRECATED: This script has been superseded by MosTidy's `canvas insert` command.
Run: mostidy canvas insert <template_dir> -c <course_id> --config <config.yaml>
See: https://github.com/oss-slu/MosTidy

This file is preserved for historical reference only.

---

Canvas Course Setup Script

This script sets up a new Canvas course instance using templated materials.
It creates modules, uploads assignments, quizzes, and pages based on the
configuration in course-info.yaml and the template files.

Usage:
    python setup_canvas_course.py --config ../course-info.yaml [options]

Requirements:
    - CANVAS_API_TOKEN environment variable must be set
    - course-info.yaml must be properly configured
"""

import os
import sys
import argparse
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml
from datetime import datetime, timezone
import re
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class CanvasSetup:
    """Setup Canvas course from templates."""

    def __init__(self, instance_url: str, api_token: str, course_id: str, config: Dict):
        self.instance_url = instance_url.rstrip('/')
        self.api_token = api_token
        self.course_id = course_id
        self.config = config
        self.base_url = f"{self.instance_url}/api/v1"
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        # Cache for created items
        self.assignment_cache = {}
        self.quiz_cache = {}
        self.page_cache = {}
        self.file_cache = {}

    def setup_course(self, templates_dir: Path, publish: bool = False) -> None:
        """Run the complete course setup."""
        print(f"Setting up Canvas course {self.course_id}")
        print(f"Templates directory: {templates_dir}\n")

        # 1. Upload assignments
        assignments_dir = templates_dir / 'assignments'
        if assignments_dir.exists():
            self.upload_assignments(assignments_dir)

        # 2. Upload quizzes
        quizzes_dir = templates_dir / 'quizzes'
        if quizzes_dir.exists():
            self.upload_quizzes(quizzes_dir)

        # 3. Upload pages
        content_dir = templates_dir / 'content'
        if content_dir.exists():
            self.upload_pages(content_dir)

        # 4. Create modules
        modules_file = templates_dir / 'modules.yaml'
        if modules_file.exists():
            self.create_modules(modules_file, publish)

        print("\n✓ Course setup complete!")

    def upload_assignments(self, assignments_dir: Path) -> None:
        """Upload all assignments from templates."""
        print("Uploading assignments...")

        assignment_files = list(assignments_dir.glob('*.md'))
        if not assignment_files:
            print("  No assignment files found")
            return

        for filepath in assignment_files:
            with open(filepath, 'r') as f:
                content = f.read()

            # Parse YAML frontmatter
            metadata, description = self._parse_frontmatter(content)

            # Substitute variables in content
            description = self._substitute_variables(description)

            # Create assignment
            assignment_data = {
                'assignment': {
                    'name': metadata.get('title', filepath.stem),
                    'description': description,
                    'points_possible': metadata.get('points_possible'),
                    'submission_types': metadata.get('submission_types', ['online_text_entry']),
                    'allowed_extensions': metadata.get('allowed_extensions', []),
                    'published': metadata.get('published', False),
                    'grading_type': metadata.get('grading_type', 'points')
                }
            }

            # Add dates if specified
            for date_field in ['due_at', 'unlock_at', 'lock_at']:
                if date_field in metadata and metadata[date_field]:
                    assignment_data['assignment'][date_field] = metadata[date_field]

            # Remove None values
            assignment_data['assignment'] = {
                k: v for k, v in assignment_data['assignment'].items()
                if v is not None
            }

            # Create assignment via API
            url = f"{self.base_url}/courses/{self.course_id}/assignments"
            response = self.session.post(url, json=assignment_data)
            response.raise_for_status()

            assignment = response.json()
            assignment_name = filepath.stem
            self.assignment_cache[assignment_name] = assignment['id']

            print(f"  ✓ {assignment['name']} (ID: {assignment['id']})")

        print(f"✓ Uploaded {len(assignment_files)} assignments")

    def upload_quizzes(self, quizzes_dir: Path) -> None:
        """Upload all quizzes from templates."""
        print("Uploading quizzes...")

        quiz_files = list(quizzes_dir.glob('*.md'))
        if not quiz_files:
            print("  No quiz files found")
            return

        for filepath in quiz_files:
            with open(filepath, 'r') as f:
                content = f.read()

            # Parse YAML frontmatter
            metadata, description = self._parse_frontmatter(content)

            # Substitute variables in content
            description = self._substitute_variables(description)

            # Create quiz
            quiz_data = {
                'quiz': {
                    'title': metadata.get('title', filepath.stem),
                    'description': description,
                    'quiz_type': metadata.get('quiz_type', 'assignment'),
                    'points_possible': metadata.get('points_possible'),
                    'time_limit': metadata.get('time_limit'),
                    'allowed_attempts': metadata.get('allowed_attempts', 1),
                    'shuffle_answers': metadata.get('shuffle_answers', False),
                    'show_correct_answers': metadata.get('show_correct_answers', True),
                    'scoring_policy': metadata.get('scoring_policy', 'keep_highest'),
                    'published': metadata.get('published', False)
                }
            }

            # Add dates if specified
            for date_field in ['due_at', 'unlock_at', 'lock_at']:
                if date_field in metadata and metadata[date_field]:
                    quiz_data['quiz'][date_field] = metadata[date_field]

            # Remove None values
            quiz_data['quiz'] = {
                k: v for k, v in quiz_data['quiz'].items()
                if v is not None
            }

            # Create quiz via API
            url = f"{self.base_url}/courses/{self.course_id}/quizzes"
            response = self.session.post(url, json=quiz_data)
            response.raise_for_status()

            quiz = response.json()
            quiz_name = filepath.stem
            self.quiz_cache[quiz_name] = quiz['id']

            print(f"  ✓ {quiz['title']} (ID: {quiz['id']})")

            # TODO: Parse and add quiz questions if present in the markdown

        print(f"✓ Uploaded {len(quiz_files)} quizzes")

    def upload_pages(self, content_dir: Path) -> None:
        """Upload all pages from templates."""
        print("Uploading pages...")

        page_files = list(content_dir.glob('*.md'))
        if not page_files:
            print("  No page files found")
            return

        for filepath in page_files:
            with open(filepath, 'r') as f:
                content = f.read()

            # Parse YAML frontmatter
            metadata, body = self._parse_frontmatter(content)

            # Substitute variables in content
            body = self._substitute_variables(body)

            # Create page
            page_data = {
                'wiki_page': {
                    'title': metadata.get('title', filepath.stem),
                    'body': body,
                    'published': metadata.get('published', False),
                    'front_page': metadata.get('front_page', False)
                }
            }

            # Create page via API
            url = f"{self.base_url}/courses/{self.course_id}/pages"
            response = self.session.post(url, json=page_data)
            response.raise_for_status()

            page = response.json()
            page_name = filepath.stem
            self.page_cache[page_name] = page['url']

            print(f"  ✓ {page['title']} (URL: {page['url']})")

        print(f"✓ Uploaded {len(page_files)} pages")

    def create_modules(self, modules_file: Path, publish: bool = False) -> None:
        """Create course modules from template."""
        print("Creating course modules...")

        with open(modules_file, 'r') as f:
            modules_data = yaml.safe_load(f)

        if 'modules' not in modules_data:
            print("  No modules found in modules.yaml")
            return

        for module_data in modules_data['modules']:
            # Create module
            module_create_data = {
                'module': {
                    'name': self._substitute_variables(module_data['name']),
                    'position': module_data.get('position')
                }
            }

            url = f"{self.base_url}/courses/{self.course_id}/modules"
            response = self.session.post(url, json=module_create_data)
            response.raise_for_status()

            module = response.json()
            print(f"\n  Module: {module['name']} (ID: {module['id']})")

            # Add module items
            if 'items' in module_data:
                for item_data in module_data['items']:
                    self._create_module_item(module['id'], item_data)

            # Publish module if requested
            if publish:
                self._publish_module(module['id'])

        print(f"\n✓ Created {len(modules_data['modules'])} modules")

    def _create_module_item(self, module_id: str, item_data: Dict) -> None:
        """Create a single module item."""
        item_name = self._substitute_variables(item_data['name'])
        item_type = item_data['type']

        module_item_data = {
            'module_item': {
                'title': item_name,
                'type': self._map_item_type(item_type),
                'position': item_data.get('position')
            }
        }

        # Add type-specific data
        if item_type == 'assignment':
            assignment_key = item_data.get('assignment')
            if assignment_key in self.assignment_cache:
                module_item_data['module_item']['content_id'] = self.assignment_cache[assignment_key]
            else:
                print(f"    ⚠ Assignment not found: {assignment_key}")
                return

        elif item_type == 'quiz':
            quiz_key = item_data.get('quiz')
            if quiz_key in self.quiz_cache:
                module_item_data['module_item']['content_id'] = self.quiz_cache[quiz_key]
            else:
                print(f"    ⚠ Quiz not found: {quiz_key}")
                return

        elif item_type == 'content':
            page_key = item_data.get('content')
            if page_key in self.page_cache:
                module_item_data['module_item']['page_url'] = self.page_cache[page_key]
            else:
                print(f"    ⚠ Page not found: {page_key}")
                return

        elif item_type == 'link':
            link = item_data.get('link', '')
            if link:
                module_item_data['module_item']['external_url'] = self._substitute_variables(link)
            else:
                print(f"    ⚠ No link provided for: {item_name}")
                return

        elif item_type == 'file':
            # File items need to reference uploaded files
            # For now, create as text header
            module_item_data['module_item']['type'] = 'SubHeader'

        elif item_type == 'label':
            module_item_data['module_item']['type'] = 'SubHeader'

        # Remove None values
        module_item_data['module_item'] = {
            k: v for k, v in module_item_data['module_item'].items()
            if v is not None
        }

        # Create module item
        url = f"{self.base_url}/courses/{self.course_id}/modules/{module_id}/items"
        response = self.session.post(url, json=module_item_data)

        if response.status_code == 200 or response.status_code == 201:
            item = response.json()
            print(f"    ✓ {item_name}")
        else:
            print(f"    ✗ Failed to create: {item_name} - {response.text}")

    def _publish_module(self, module_id: str) -> None:
        """Publish a module."""
        url = f"{self.base_url}/courses/{self.course_id}/modules/{module_id}"
        response = self.session.put(url, json={'module': {'published': True}})
        response.raise_for_status()

    def _substitute_variables(self, text: str) -> str:
        """Substitute template variables with values from config."""
        if not text:
            return text

        # Find all {variable} patterns
        pattern = r'\{([^}]+)\}'

        def replace_var(match):
            var_path = match.group(1).strip()

            # Handle special sprint video variables
            sprint_video_match = re.match(r'sprint_(\d+)\.weekly_video_(\d+)', var_path)
            if sprint_video_match:
                sprint_num = int(sprint_video_match.group(1))
                video_num = int(sprint_video_match.group(2))
                sprints = self.config.get('sprints', [])

                for sprint in sprints:
                    if sprint.get('number') == sprint_num:
                        video_key = f'weekly_video_{video_num}'
                        if video_key in sprint:
                            return sprint[video_key].get('title', '') or sprint[video_key].get('link', '')
                return match.group(0)

            # Handle sprint dates format
            sprint_dates_match = re.match(r'sprint_(\d+)_dates', var_path)
            if sprint_dates_match:
                sprint_num = int(sprint_dates_match.group(1))
                sprints = self.config.get('sprints', [])

                for sprint in sprints:
                    if sprint.get('number') == sprint_num:
                        start = sprint.get('start_date', '')
                        end = sprint.get('end_date', '')
                        if start and end:
                            return f"{start} to {end}"
                return match.group(0)

            # Handle launch dates
            if var_path == 'launch_dates':
                return self.config.get('launch', {}).get('dates', match.group(0))

            # Handle standard nested values
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
            elif isinstance(value, list):
                # Handle array indices
                try:
                    idx = int(key)
                    value = value[idx]
                except (ValueError, IndexError):
                    return None
            else:
                return None

        return value

    @staticmethod
    def _parse_frontmatter(content: str) -> tuple:
        """Parse YAML frontmatter from markdown content."""
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

    @staticmethod
    def _map_item_type(template_type: str) -> str:
        """Map template item types to Canvas module item types."""
        mapping = {
            'assignment': 'Assignment',
            'quiz': 'Quiz',
            'link': 'ExternalUrl',
            'file': 'File',
            'content': 'Page',
            'label': 'SubHeader'
        }
        return mapping.get(template_type, 'ExternalUrl')


def load_config(config_path: Path) -> Dict:
    """Load and validate course configuration."""
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Validate required fields
    required_fields = [
        ('course', 'course_number'),
        ('course', 'section'),
        ('course', 'semester'),
        ('canvas', 'instance_url'),
        ('canvas', 'course_id')
    ]

    for section, field in required_fields:
        if section not in config or field not in config[section]:
            raise ValueError(f"Required field missing in config: {section}.{field}")

    return config


def main():
    parser = argparse.ArgumentParser(
        description='Setup Canvas course from templates'
    )
    parser.add_argument(
        '--config',
        required=True,
        type=Path,
        help='Path to course-info.yaml configuration file'
    )
    parser.add_argument(
        '--templates-dir',
        type=Path,
        help='Directory containing template files (default: parent of config file)'
    )
    parser.add_argument(
        '--publish',
        action='store_true',
        help='Publish modules after creation'
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

    # Get API token from environment
    api_token = os.environ.get('CANVAS_API_TOKEN')
    if not api_token:
        print("Error: CANVAS_API_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Determine templates directory
    if args.templates_dir:
        templates_dir = args.templates_dir
    else:
        templates_dir = args.config.parent

    if not templates_dir.exists():
        print(f"Error: Templates directory not found: {templates_dir}", file=sys.stderr)
        sys.exit(1)

    # Get Canvas instance URL and course ID from config
    instance_url = config['canvas']['instance_url']
    course_id = str(config['canvas']['course_id'])

    # Use publish_on_create from config if --publish not specified
    publish = args.publish or config.get('canvas', {}).get('publish_on_create', False)

    if args.dry_run:
        print("DRY RUN MODE - No changes will be made\n")
        print(f"Would setup course {course_id} at {instance_url}")
        print(f"Using templates from: {templates_dir}")
        print(f"Publish modules: {publish}")
        sys.exit(0)

    # Initialize setup
    setup = CanvasSetup(instance_url, api_token, course_id, config)

    # Run setup
    try:
        setup.setup_course(templates_dir, publish=publish)
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error communicating with Canvas: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
