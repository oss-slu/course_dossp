#!/usr/bin/env python3
"""
Slack Channel Setup Script

This script creates Slack channels for a course instance based on the
configuration in course-info.yaml.

Usage:
    python setup_slack_channels.py --config ../course-info.yaml [options]

Requirements:
    - SLACK_TOKEN environment variable must be set with appropriate permissions
      (channels:manage, channels:write, groups:write)
    - course-info.yaml must be properly configured
"""

import os
import sys
import argparse
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class SlackSetup:
    """Setup Slack channels for course."""

    def __init__(self, token: str, config: Dict):
        self.token = token
        self.config = config
        self.base_url = "https://slack.com/api"
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        # Cache for created channels
        self.created_channels = {}

    def setup_channels(self) -> None:
        """Create all configured Slack channels."""
        if not self.config['slack'].get('create_channels', False):
            print("Slack channel creation disabled in config")
            return

        print("Setting up Slack channels...")

        channels_config = self.config['slack'].get('channels', [])
        if not channels_config:
            print("  No channels configured")
            return

        for channel_config in channels_config:
            self._create_channel(channel_config)

        print(f"\n✓ Created {len(self.created_channels)} Slack channels")

    def _create_channel(self, channel_config: Dict) -> None:
        """Create a single Slack channel."""
        # Substitute variables in channel name
        channel_name = self._substitute_variables(channel_config['name'])

        # Clean up channel name (Slack requirements)
        channel_name = self._sanitize_channel_name(channel_name)

        # Prepare description
        description = self._substitute_variables(channel_config.get('description', ''))

        # Check if channel already exists
        existing_channel = self._find_channel(channel_name)
        if existing_channel:
            print(f"  ✓ Channel already exists: #{channel_name}")
            self.created_channels[channel_name] = existing_channel['id']
            return

        # Determine if channel should be private
        is_private = channel_config.get('is_private', False)

        # Create channel
        if is_private:
            url = f"{self.base_url}/conversations.create"
            data = {
                'name': channel_name,
                'is_private': True
            }
        else:
            url = f"{self.base_url}/conversations.create"
            data = {
                'name': channel_name,
                'is_private': False
            }

        response = self.session.post(url, json=data)
        result = response.json()

        if result.get('ok'):
            channel_id = result['channel']['id']
            self.created_channels[channel_name] = channel_id
            print(f"  ✓ Created channel: #{channel_name} (ID: {channel_id})")

            # Set channel description/topic if provided
            if description:
                self._set_channel_topic(channel_id, description)

            # Set channel purpose if configured
            if 'purpose' in channel_config:
                purpose = self._substitute_variables(channel_config['purpose'])
                self._set_channel_purpose(channel_id, purpose)

        else:
            error = result.get('error', 'Unknown error')
            if error == 'name_taken':
                print(f"  ⚠ Channel name already taken: #{channel_name}")
            else:
                print(f"  ✗ Error creating channel #{channel_name}: {error}")

    def _find_channel(self, channel_name: str) -> Optional[Dict]:
        """Find a channel by name."""
        url = f"{self.base_url}/conversations.list"
        params = {
            'types': 'public_channel,private_channel',
            'exclude_archived': True,
            'limit': 1000
        }

        response = self.session.get(url, params=params)
        result = response.json()

        if result.get('ok'):
            for channel in result.get('channels', []):
                if channel['name'] == channel_name:
                    return channel

        return None

    def _set_channel_topic(self, channel_id: str, topic: str) -> None:
        """Set channel topic."""
        url = f"{self.base_url}/conversations.setTopic"
        data = {
            'channel': channel_id,
            'topic': topic
        }

        response = self.session.post(url, json=data)
        result = response.json()

        if result.get('ok'):
            print(f"    ✓ Set channel topic")
        else:
            print(f"    ⚠ Could not set topic: {result.get('error', 'Unknown error')}")

    def _set_channel_purpose(self, channel_id: str, purpose: str) -> None:
        """Set channel purpose."""
        url = f"{self.base_url}/conversations.setPurpose"
        data = {
            'channel': channel_id,
            'purpose': purpose
        }

        response = self.session.post(url, json=data)
        result = response.json()

        if result.get('ok'):
            print(f"    ✓ Set channel purpose")
        else:
            print(f"    ⚠ Could not set purpose: {result.get('error', 'Unknown error')}")

    def invite_users(self, channel_name: str, user_emails: List[str]) -> None:
        """Invite users to a channel by email."""
        if channel_name not in self.created_channels:
            print(f"  ⚠ Channel not found: #{channel_name}")
            return

        channel_id = self.created_channels[channel_name]

        # First, look up user IDs from emails
        user_ids = []
        for email in user_emails:
            user_id = self._lookup_user_by_email(email)
            if user_id:
                user_ids.append(user_id)
            else:
                print(f"    ⚠ User not found: {email}")

        # Invite users to channel
        if user_ids:
            url = f"{self.base_url}/conversations.invite"
            data = {
                'channel': channel_id,
                'users': ','.join(user_ids)
            }

            response = self.session.post(url, json=data)
            result = response.json()

            if result.get('ok'):
                print(f"  ✓ Invited {len(user_ids)} users to #{channel_name}")
            else:
                print(f"  ✗ Error inviting users: {result.get('error', 'Unknown error')}")

    def _lookup_user_by_email(self, email: str) -> Optional[str]:
        """Look up a user ID by email address."""
        url = f"{self.base_url}/users.lookupByEmail"
        params = {'email': email}

        response = self.session.get(url, params=params)
        result = response.json()

        if result.get('ok'):
            return result['user']['id']

        return None

    @staticmethod
    def _sanitize_channel_name(name: str) -> str:
        """
        Sanitize channel name to meet Slack requirements:
        - lowercase
        - no spaces (replace with hyphens)
        - only alphanumeric, hyphens, and underscores
        - max 80 characters
        """
        # Convert to lowercase
        name = name.lower()

        # Replace spaces with hyphens
        name = name.replace(' ', '-')

        # Remove invalid characters
        valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
        name = ''.join(c for c in name if c in valid_chars)

        # Remove consecutive hyphens
        while '--' in name:
            name = name.replace('--', '-')

        # Trim to 80 characters
        name = name[:80]

        # Remove leading/trailing hyphens
        name = name.strip('-')

        return name

    def _substitute_variables(self, text: str) -> str:
        """Substitute template variables with values from config."""
        if not text:
            return text

        import re

        # Handle special cases first
        text = text.replace('{prefix}', self.config['slack'].get('channel_prefix', 'course'))

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


def load_config(config_path: Path) -> Dict:
    """Load and validate course configuration."""
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Validate that slack section exists
    if 'slack' not in config:
        raise ValueError("Slack configuration section missing from config file")

    return config


def main():
    parser = argparse.ArgumentParser(
        description='Setup Slack channels for course'
    )
    parser.add_argument(
        '--config',
        required=True,
        type=Path,
        help='Path to course-info.yaml configuration file'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what channels would be created without making changes'
    )

    args = parser.parse_args()

    # Load configuration
    try:
        config = load_config(args.config)
    except Exception as e:
        print(f"Error loading configuration: {e}", file=sys.stderr)
        sys.exit(1)

    # Check if Slack setup is enabled
    if not config['slack'].get('create_channels', False):
        print("Slack channel creation is disabled in the configuration.")
        print("Set 'slack.create_channels' to true to enable.")
        sys.exit(0)

    # Get Slack token from environment
    slack_token = os.environ.get('SLACK_TOKEN')
    if not slack_token:
        print("Error: SLACK_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        print("DRY RUN MODE - No changes will be made\n")
        print("Would create the following Slack channels:")

        setup = SlackSetup(slack_token, config)
        for channel_config in config['slack'].get('channels', []):
            channel_name = setup._substitute_variables(channel_config['name'])
            channel_name = setup._sanitize_channel_name(channel_name)
            privacy = "Private" if channel_config.get('is_private', False) else "Public"
            print(f"  - #{channel_name} ({privacy})")

        sys.exit(0)

    # Initialize setup
    setup = SlackSetup(slack_token, config)

    try:
        # Create channels
        setup.setup_channels()

        # Print summary
        if setup.created_channels:
            print("\nCreated channels:")
            for name, channel_id in setup.created_channels.items():
                print(f"  - #{name} ({channel_id})")

    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error communicating with Slack: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
