#!/usr/bin/env python3
"""
DEPRECATED: This script has been superseded by MosTidy's `canvas extract` command.
Run: mostidy canvas extract <course_id> -o <output_dir>
See: https://github.com/oss-slu/MosTidy

This file is preserved for historical reference only.

---

Canvas Content Downloader

This script downloads existing content, assignments, and quizzes from a Canvas course
and saves them as templated materials for future use.

Usage:
    python download_canvas_content.py --course-id <COURSE_ID> [options]

Requirements:
    - CANVAS_API_TOKEN environment variable must be set
    - CANVAS_INSTANCE_URL environment variable must be set (e.g., https://yourschool.instructure.com)
"""

import os
import sys
import json
import argparse
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class CanvasDownloader:
    """Download content from Canvas and save as templates."""

    def __init__(self, instance_url: str, api_token: str, course_id: str):
        self.instance_url = instance_url.rstrip('/')
        self.api_token = api_token
        self.course_id = course_id
        self.base_url = f"{self.instance_url}/api/v1"
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _get_paginated(self, url: str, params: Optional[Dict] = None) -> List[Dict]:
        """Handle Canvas API pagination."""
        results = []
        params = params or {}
        params['per_page'] = 100

        while url:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            results.extend(response.json())

            # Check for next page
            links = response.links
            url = links.get('next', {}).get('url')
            params = {}  # URL already contains params

        return results

    def download_modules(self, output_file: Path) -> None:
        """Download course modules structure."""
        print("Downloading course modules...")
        url = f"{self.base_url}/courses/{self.course_id}/modules"
        params = {'include[]': ['items', 'content_details']}
        modules = self._get_paginated(url, params)

        modules_data = {'modules': []}

        for module in modules:
            module_dict = {
                'name': module['name'],
                'position': module.get('position', 0),
                'items': []
            }

            # Get module items
            if 'items' in module:
                for item in module['items']:
                    item_dict = {
                        'name': item['title'],
                        'type': self._map_item_type(item['type']),
                        'position': item.get('position', 0)
                    }

                    # Add type-specific details
                    if item['type'] == 'Assignment':
                        item_dict['assignment'] = item.get('content_id')
                    elif item['type'] == 'Quiz':
                        item_dict['quiz'] = item.get('content_id')
                    elif item['type'] == 'ExternalUrl':
                        item_dict['link'] = item.get('external_url', '')
                    elif item['type'] == 'File':
                        item_dict['file'] = item.get('title', '')
                    elif item['type'] == 'Page':
                        item_dict['content'] = item.get('page_url', '')

                    # Add due date if available
                    if 'content_details' in item and item['content_details'].get('due_at'):
                        item_dict['due_date'] = item['content_details']['due_at']

                    module_dict['items'].append(item_dict)

            modules_data['modules'].append(module_dict)

        # Sort modules by position
        modules_data['modules'].sort(key=lambda x: x['position'])

        # Write to YAML file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            yaml.dump(modules_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        print(f"✓ Saved modules to {output_file}")

    def download_assignments(self, output_dir: Path) -> None:
        """Download all assignments as markdown files with YAML frontmatter."""
        print("Downloading assignments...")
        url = f"{self.base_url}/courses/{self.course_id}/assignments"
        assignments = self._get_paginated(url)

        output_dir.mkdir(parents=True, exist_ok=True)

        for assignment in assignments:
            filename = self._sanitize_filename(assignment['name']) + '.md'
            filepath = output_dir / filename

            # Create YAML frontmatter
            metadata = {
                'title': assignment['name'],
                'points_possible': assignment.get('points_possible'),
                'due_at': assignment.get('due_at'),
                'unlock_at': assignment.get('unlock_at'),
                'lock_at': assignment.get('lock_at'),
                'submission_types': assignment.get('submission_types', []),
                'allowed_extensions': assignment.get('allowed_extensions', []),
                'published': assignment.get('published', False),
                'assignment_group_id': assignment.get('assignment_group_id'),
                'grading_type': assignment.get('grading_type', 'points'),
                'canvas_id': assignment['id']
            }

            # Remove None values
            metadata = {k: v for k, v in metadata.items() if v is not None}

            # Get description (HTML content)
            description = assignment.get('description', '')

            # Write markdown file
            with open(filepath, 'w') as f:
                f.write('---\n')
                yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
                f.write('---\n\n')
                f.write(description)

            print(f"  ✓ {assignment['name']}")

        print(f"✓ Saved {len(assignments)} assignments to {output_dir}")

    def download_quizzes(self, output_dir: Path) -> None:
        """Download all quizzes as markdown files with YAML frontmatter."""
        print("Downloading quizzes...")
        url = f"{self.base_url}/courses/{self.course_id}/quizzes"
        quizzes = self._get_paginated(url)

        output_dir.mkdir(parents=True, exist_ok=True)

        for quiz in quizzes:
            filename = self._sanitize_filename(quiz['title']) + '.md'
            filepath = output_dir / filename

            # Get quiz questions
            questions = []
            if quiz['question_count'] > 0:
                questions_url = f"{self.base_url}/courses/{self.course_id}/quizzes/{quiz['id']}/questions"
                try:
                    questions = self._get_paginated(questions_url)
                except Exception as e:
                    print(f"  ⚠ Could not fetch questions for {quiz['title']}: {e}")

            # Create YAML frontmatter
            metadata = {
                'title': quiz['title'],
                'quiz_type': quiz.get('quiz_type', 'assignment'),
                'points_possible': quiz.get('points_possible'),
                'time_limit': quiz.get('time_limit'),
                'allowed_attempts': quiz.get('allowed_attempts', 1),
                'shuffle_answers': quiz.get('shuffle_answers', False),
                'show_correct_answers': quiz.get('show_correct_answers', True),
                'scoring_policy': quiz.get('scoring_policy', 'keep_highest'),
                'due_at': quiz.get('due_at'),
                'unlock_at': quiz.get('unlock_at'),
                'lock_at': quiz.get('lock_at'),
                'published': quiz.get('published', False),
                'canvas_id': quiz['id'],
                'question_count': quiz.get('question_count', 0)
            }

            # Remove None values
            metadata = {k: v for k, v in metadata.items() if v is not None}

            # Get description
            description = quiz.get('description', '')

            # Write markdown file
            with open(filepath, 'w') as f:
                f.write('---\n')
                yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
                f.write('---\n\n')
                f.write(description)

                # Add questions section
                if questions:
                    f.write('\n\n## Questions\n\n')
                    for i, q in enumerate(questions, 1):
                        f.write(f"### Question {i}\n\n")
                        f.write(f"**Type:** {q.get('question_type', 'unknown')}\n\n")
                        f.write(f"**Points:** {q.get('points_possible', 0)}\n\n")
                        f.write(f"{q.get('question_text', '')}\n\n")

                        # Add answers if available
                        if 'answers' in q and q['answers']:
                            f.write("**Answers:**\n\n")
                            for ans in q['answers']:
                                correct = '✓' if ans.get('weight', 0) > 0 else ' '
                                f.write(f"- [{correct}] {ans.get('text', '')}\n")
                            f.write('\n')

            print(f"  ✓ {quiz['title']}")

        print(f"✓ Saved {len(quizzes)} quizzes to {output_dir}")

    def download_pages(self, output_dir: Path) -> None:
        """Download course pages as markdown files."""
        print("Downloading course pages...")
        url = f"{self.base_url}/courses/{self.course_id}/pages"
        pages = self._get_paginated(url)

        output_dir.mkdir(parents=True, exist_ok=True)

        for page in pages:
            # Get full page content
            page_url = f"{self.base_url}/courses/{self.course_id}/pages/{page['url']}"
            response = self.session.get(page_url)
            response.raise_for_status()
            page_data = response.json()

            filename = self._sanitize_filename(page_data['title']) + '.md'
            filepath = output_dir / filename

            # Create YAML frontmatter
            metadata = {
                'title': page_data['title'],
                'url': page_data.get('url'),
                'published': page_data.get('published', False),
                'front_page': page_data.get('front_page', False),
                'canvas_id': page_data['page_id']
            }

            # Get body content
            body = page_data.get('body', '')

            # Write markdown file
            with open(filepath, 'w') as f:
                f.write('---\n')
                yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
                f.write('---\n\n')
                f.write(body)

            print(f"  ✓ {page_data['title']}")

        print(f"✓ Saved {len(pages)} pages to {output_dir}")

    def download_files_metadata(self, output_file: Path) -> None:
        """Download file metadata (not the actual files, just references)."""
        print("Downloading file metadata...")
        url = f"{self.base_url}/courses/{self.course_id}/files"
        files = self._get_paginated(url)

        files_data = []
        for file_obj in files:
            files_data.append({
                'name': file_obj['display_name'],
                'filename': file_obj['filename'],
                'size': file_obj['size'],
                'content_type': file_obj['content-type'],
                'url': file_obj['url'],
                'folder': file_obj.get('folder_id'),
                'canvas_id': file_obj['id']
            })

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            yaml.dump({'files': files_data}, f, default_flow_style=False, sort_keys=False)

        print(f"✓ Saved metadata for {len(files)} files to {output_file}")

    def download_course_info(self, output_file: Path) -> None:
        """Download basic course information."""
        print("Downloading course information...")
        url = f"{self.base_url}/courses/{self.course_id}"
        response = self.session.get(url)
        response.raise_for_status()
        course = response.json()

        course_info = {
            'name': course['name'],
            'course_code': course.get('course_code', ''),
            'start_at': course.get('start_at'),
            'end_at': course.get('end_at'),
            'time_zone': course.get('time_zone', 'America/Chicago'),
            'canvas_id': course['id']
        }

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            yaml.dump(course_info, f, default_flow_style=False, sort_keys=False)

        print(f"✓ Saved course info to {output_file}")

    @staticmethod
    def _map_item_type(canvas_type: str) -> str:
        """Map Canvas module item types to template types."""
        mapping = {
            'Assignment': 'assignment',
            'Quiz': 'quiz',
            'ExternalUrl': 'link',
            'ExternalTool': 'link',
            'File': 'file',
            'Page': 'content',
            'SubHeader': 'label'
        }
        return mapping.get(canvas_type, 'content')

    @staticmethod
    def _sanitize_filename(name: str) -> str:
        """Convert a name to a valid filename."""
        # Replace spaces with underscores
        name = name.replace(' ', '_')
        # Remove or replace invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            name = name.replace(char, '')
        # Lowercase and limit length
        name = name.lower()[:100]
        return name


def main():
    parser = argparse.ArgumentParser(
        description='Download content from Canvas course for templating'
    )
    parser.add_argument(
        '--course-id',
        required=True,
        help='Canvas course ID'
    )
    parser.add_argument(
        '--output-dir',
        default='.',
        help='Output directory for downloaded content (default: current directory)'
    )
    parser.add_argument(
        '--modules-only',
        action='store_true',
        help='Only download module structure'
    )
    parser.add_argument(
        '--assignments-only',
        action='store_true',
        help='Only download assignments'
    )
    parser.add_argument(
        '--quizzes-only',
        action='store_true',
        help='Only download quizzes'
    )
    parser.add_argument(
        '--pages-only',
        action='store_true',
        help='Only download pages'
    )

    args = parser.parse_args()

    # Get API credentials from environment
    api_token = os.environ.get('CANVAS_API_TOKEN')
    instance_url = os.environ.get('CANVAS_INSTANCE_URL')

    if not api_token:
        print("Error: CANVAS_API_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    if not instance_url:
        print("Error: CANVAS_INSTANCE_URL environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Initialize downloader
    downloader = CanvasDownloader(instance_url, api_token, args.course_id)

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nDownloading content from Canvas course {args.course_id}")
    print(f"Output directory: {output_dir.absolute()}\n")

    try:
        # Determine what to download
        download_all = not any([
            args.modules_only,
            args.assignments_only,
            args.quizzes_only,
            args.pages_only
        ])

        if download_all or args.modules_only:
            downloader.download_modules(output_dir / 'modules.yaml')

        if download_all:
            downloader.download_course_info(output_dir / 'course_info.yaml')

        if download_all or args.assignments_only:
            downloader.download_assignments(output_dir / 'assignments')

        if download_all or args.quizzes_only:
            downloader.download_quizzes(output_dir / 'quizzes')

        if download_all or args.pages_only:
            downloader.download_pages(output_dir / 'content')

        if download_all:
            downloader.download_files_metadata(output_dir / 'files_metadata.yaml')

        print("\n✓ Download complete!")

    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error downloading from Canvas: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
