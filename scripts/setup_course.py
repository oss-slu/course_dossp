#!/usr/bin/env python3
"""
Master Course Setup Script

This script orchestrates the complete setup of a new course instance by running
all the individual setup scripts in the correct order.

Usage:
    python setup_course.py --config ../course-info.yaml [options]

Requirements:
    - All required environment variables must be set (see .env.example)
    - course-info.yaml must be properly configured
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Dict, List
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class CourseSetup:
    """Orchestrate complete course setup."""

    def __init__(self, config_path: Path, scripts_dir: Path):
        self.config_path = config_path
        self.scripts_dir = scripts_dir
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load course configuration."""
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def run_setup(self, steps: List[str], dry_run: bool = False) -> None:
        """Run the specified setup steps."""
        print("=" * 70)
        print("COURSE SETUP")
        print("=" * 70)
        print(f"\nCourse: {self.config['course']['title']}")
        print(f"Section: {self.config['course']['section']}")
        print(f"Semester: {self.config['course']['semester']}")
        print(f"Instructor: {self.config['course']['instructor']['name']}")
        print()

        if dry_run:
            print("DRY RUN MODE - No changes will be made\n")

        # Check environment variables
        self._check_environment(steps)

        # Run each step
        if 'canvas' in steps:
            self._setup_canvas(dry_run)

        if 'github' in steps:
            self._setup_github(dry_run)

        if 'slack' in steps:
            self._setup_slack(dry_run)

        print("\n" + "=" * 70)
        print("SETUP COMPLETE!")
        print("=" * 70)

    def _check_environment(self, steps: List[str]) -> None:
        """Check that required environment variables are set."""
        print("Checking environment variables...")

        required_vars = []

        if 'canvas' in steps:
            required_vars.extend(['CANVAS_API_TOKEN', 'CANVAS_INSTANCE_URL'])

        if 'github' in steps:
            required_vars.append('GITHUB_TOKEN')

        if 'slack' in steps:
            if self.config['slack'].get('create_channels', False):
                required_vars.append('SLACK_TOKEN')

        missing_vars = [var for var in required_vars if not os.environ.get(var)]

        if missing_vars:
            print("\n✗ Missing required environment variables:")
            for var in missing_vars:
                print(f"  - {var}")
            print("\nPlease set these environment variables before running setup.")
            print("See .env.example for details.\n")
            sys.exit(1)

        print("✓ All required environment variables are set\n")

    def _setup_canvas(self, dry_run: bool) -> None:
        """Run Canvas setup."""
        print("-" * 70)
        print("CANVAS SETUP")
        print("-" * 70)

        script = self.scripts_dir / 'setup_canvas_course.py'
        cmd = [
            sys.executable,
            str(script),
            '--config', str(self.config_path)
        ]

        if dry_run:
            cmd.append('--dry-run')
        elif self.config.get('canvas', {}).get('publish_on_create', False):
            cmd.append('--publish')

        self._run_command(cmd)

    def _setup_github(self, dry_run: bool) -> None:
        """Run GitHub setup."""
        print("\n" + "-" * 70)
        print("GITHUB SETUP")
        print("-" * 70)

        script = self.scripts_dir / 'setup_github_project.py'
        cmd = [
            sys.executable,
            str(script),
            '--config', str(self.config_path)
        ]

        if dry_run:
            cmd.append('--dry-run')

        self._run_command(cmd)

    def _setup_slack(self, dry_run: bool) -> None:
        """Run Slack setup."""
        if not self.config['slack'].get('create_channels', False):
            print("\nSlack setup disabled in configuration (skipping)")
            return

        print("\n" + "-" * 70)
        print("SLACK SETUP")
        print("-" * 70)

        script = self.scripts_dir / 'setup_slack_channels.py'
        cmd = [
            sys.executable,
            str(script),
            '--config', str(self.config_path)
        ]

        if dry_run:
            cmd.append('--dry-run')

        self._run_command(cmd)

    def _run_command(self, cmd: List[str]) -> None:
        """Run a command and handle errors."""
        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=False,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"\n✗ Error running command: {' '.join(cmd)}")
            print(f"Exit code: {e.returncode}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"\n✗ Script not found: {cmd[1]}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Complete course setup automation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full setup (Canvas, GitHub, Slack)
  python setup_course.py --config ../course-info.yaml

  # Only Canvas setup
  python setup_course.py --config ../course-info.yaml --canvas-only

  # Only GitHub setup
  python setup_course.py --config ../course-info.yaml --github-only

  # Dry run to preview changes
  python setup_course.py --config ../course-info.yaml --dry-run

  # Setup Canvas and GitHub, skip Slack
  python setup_course.py --config ../course-info.yaml --skip-slack
        """
    )

    parser.add_argument(
        '--config',
        required=True,
        type=Path,
        help='Path to course-info.yaml configuration file'
    )

    # Step selection
    parser.add_argument(
        '--canvas-only',
        action='store_true',
        help='Only run Canvas setup'
    )
    parser.add_argument(
        '--github-only',
        action='store_true',
        help='Only run GitHub setup'
    )
    parser.add_argument(
        '--slack-only',
        action='store_true',
        help='Only run Slack setup'
    )
    parser.add_argument(
        '--skip-canvas',
        action='store_true',
        help='Skip Canvas setup'
    )
    parser.add_argument(
        '--skip-github',
        action='store_true',
        help='Skip GitHub setup'
    )
    parser.add_argument(
        '--skip-slack',
        action='store_true',
        help='Skip Slack setup'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without making them'
    )

    args = parser.parse_args()

    # Validate config file exists
    if not args.config.exists():
        print(f"Error: Config file not found: {args.config}", file=sys.stderr)
        sys.exit(1)

    # Determine which steps to run
    steps = []

    if args.canvas_only:
        steps = ['canvas']
    elif args.github_only:
        steps = ['github']
    elif args.slack_only:
        steps = ['slack']
    else:
        # Run all by default, unless explicitly skipped
        if not args.skip_canvas:
            steps.append('canvas')
        if not args.skip_github:
            steps.append('github')
        if not args.skip_slack:
            steps.append('slack')

    if not steps:
        print("Error: No setup steps selected. Use --help for usage information.", file=sys.stderr)
        sys.exit(1)

    # Get scripts directory
    scripts_dir = Path(__file__).parent

    # Run setup
    try:
        setup = CourseSetup(args.config, scripts_dir)
        setup.run_setup(steps, dry_run=args.dry_run)
    except KeyboardInterrupt:
        print("\n\nSetup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error during setup: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
