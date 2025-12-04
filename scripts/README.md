# Course Automation Scripts

This directory contains automation scripts for managing the Developing Open Source Software Products course. These scripts interact with Canvas, GitHub, and Slack to streamline course setup and management.

## Overview

The automation scripts help you:

1. **Download existing content** from Canvas to create templates
2. **Setup new course instances** in Canvas from templates
3. **Create GitHub repositories and projects** for course tracking
4. **Setup Slack channels** for course communication

## Prerequisites

### Python Environment

All scripts require Python 3.8 or higher. It's recommended to use a virtual environment:

```bash
cd scripts
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### API Tokens

You'll need to set up API tokens for the services you want to use:

#### Canvas API Token

1. Log into your Canvas instance
2. Go to Account → Settings → Approved Integrations
3. Click "+ New Access Token"
4. Set the token as an environment variable:

```bash
export CANVAS_API_TOKEN="your-token-here"
export CANVAS_INSTANCE_URL="https://yourschool.instructure.com"
```

#### GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token with these scopes:
   - `repo` (Full control of private repositories)
   - `project` (Full control of projects)
3. Set the token as an environment variable:

```bash
export GITHUB_TOKEN="your-token-here"
```

#### Slack Token

1. Create a Slack app at https://api.slack.com/apps
2. Add these OAuth scopes:
   - `channels:manage`
   - `channels:write`
   - `groups:write`
   - `users:read`
   - `users:read.email`
3. Install the app to your workspace
4. Set the token as an environment variable:

```bash
export SLACK_TOKEN="xoxb-your-token-here"
```

## Configuration

Before using any scripts, you need to configure [course-info.yaml](../course-info.yaml). This file contains all course-specific settings.

### Required Fields

At minimum, fill in these required fields:

```yaml
course:
  course_number: "CSCI-5930"
  section: "02"
  semester: "262"  # Spring 2026
  crn: "12345"
  academic_year: "2025-2026"
  start_date: "2026-01-15"
  end_date: "2026-05-15"
  instructor:
    name: "Your Name"
    email: "you@university.edu"

canvas:
  instance_url: "https://yourschool.instructure.com"
  course_id: "123456"

github:
  organization: "your-org"
```

See the [course-info.yaml](../course-info.yaml) file for all available configuration options.

## Scripts

### 1. Download Canvas Content

Downloads existing content from a Canvas course to use as templates for future courses.

**Usage:**

```bash
python download_canvas_content.py --course-id COURSE_ID [options]
```

**Options:**

- `--course-id COURSE_ID` (required): Canvas course ID to download from
- `--output-dir DIR`: Output directory (default: current directory)
- `--modules-only`: Only download module structure
- `--assignments-only`: Only download assignments
- `--quizzes-only`: Only download quizzes
- `--pages-only`: Only download pages

**Examples:**

```bash
# Download everything from a course
python download_canvas_content.py --course-id 123456 --output-dir ../templates

# Download only assignments
python download_canvas_content.py --course-id 123456 --assignments-only

# Download to current directory
python download_canvas_content.py --course-id 123456
```

**Output:**

The script creates:
- `modules.yaml`: Course module structure
- `assignments/*.md`: Assignment files with YAML frontmatter
- `quizzes/*.md`: Quiz files with YAML frontmatter
- `content/*.md`: Course page content
- `files_metadata.yaml`: File references
- `course_info.yaml`: Basic course information

### 2. Setup Canvas Course

Creates a new Canvas course instance from templates.

**Usage:**

```bash
python setup_canvas_course.py --config ../course-info.yaml [options]
```

**Options:**

- `--config FILE` (required): Path to course-info.yaml
- `--templates-dir DIR`: Directory with templates (default: config file parent)
- `--publish`: Publish modules after creation
- `--dry-run`: Show what would be done without making changes

**Examples:**

```bash
# Setup course from templates
python setup_canvas_course.py --config ../course-info.yaml

# Dry run to see what would happen
python setup_canvas_course.py --config ../course-info.yaml --dry-run

# Setup and publish modules
python setup_canvas_course.py --config ../course-info.yaml --publish
```

**What it does:**

1. Uploads all assignments from `assignments/` directory
2. Uploads all quizzes from `quizzes/` directory
3. Uploads all pages from `content/` directory
4. Creates course modules based on `modules.yaml`
5. Links modules to the created content

**Variable Substitution:**

The script substitutes variables in templates using values from `course-info.yaml`:

- `{course.instructor.name}` → Instructor name
- `{sprint_1.weekly_video_1.title}` → Sprint 1 video 1 title
- `{sprint_1_dates}` → Formatted sprint dates
- `{launch_dates}` → Launch period dates

### 3. Setup GitHub Project

Creates a GitHub repository and project board for course tracking.

**Usage:**

```bash
python setup_github_project.py --config ../course-info.yaml [options]
```

**Options:**

- `--config FILE` (required): Path to course-info.yaml
- `--issues-dir DIR`: Directory with issue templates (default: ../issues)
- `--skip-repo`: Skip repository creation
- `--skip-issues`: Skip issue creation
- `--skip-project`: Skip project creation
- `--dry-run`: Show what would be done without making changes

**Examples:**

```bash
# Full setup
python setup_github_project.py --config ../course-info.yaml

# Only create issues (repo already exists)
python setup_github_project.py --config ../course-info.yaml --skip-repo --skip-project

# Dry run
python setup_github_project.py --config ../course-info.yaml --dry-run
```

**What it does:**

1. Creates a private repository in the specified organization
2. Sets up issue labels (reading, discussion, deliverable, etc.)
3. Creates issues from template files in `issues/` directory
4. Creates a project board with To Do/In Progress/Done columns

**Issue Templates:**

Create issue templates as markdown files with YAML frontmatter:

```markdown
---
title: "Week 1 Reading: Open Source Basics"
labels: ["reading"]
---

Read the following materials before our next class:

- Article 1
- Article 2
```

### 4. Setup Slack Channels

Creates Slack channels for course communication.

**Usage:**

```bash
python setup_slack_channels.py --config ../course-info.yaml [options]
```

**Options:**

- `--config FILE` (required): Path to course-info.yaml
- `--dry-run`: Show what channels would be created

**Examples:**

```bash
# Create channels
python setup_slack_channels.py --config ../course-info.yaml

# Dry run to preview
python setup_slack_channels.py --config ../course-info.yaml --dry-run
```

**What it does:**

1. Creates channels defined in `slack.channels` section of config
2. Sets channel descriptions and topics
3. Handles both public and private channels

**Channel Naming:**

Channel names are automatically sanitized to meet Slack requirements:
- Converted to lowercase
- Spaces replaced with hyphens
- Only alphanumeric, hyphens, and underscores allowed
- Maximum 80 characters

## Complete Workflow

Here's a complete workflow for setting up a new course instance:

### 1. Download Templates (One-time)

If you don't have templates yet, download from an existing course:

```bash
# Set Canvas credentials
export CANVAS_API_TOKEN="your-token"
export CANVAS_INSTANCE_URL="https://yourschool.instructure.com"

# Download from existing course
python download_canvas_content.py --course-id 123456 --output-dir ../
```

### 2. Configure New Course

Create a branch for your new course and update `course-info.yaml`:

```bash
# Create course branch
git checkout -b csci-5930-02-262-26314

# Edit configuration
vim ../course-info.yaml
# Fill in required fields
```

### 3. Setup Canvas Course

```bash
# Set Canvas credentials (if not already set)
export CANVAS_API_TOKEN="your-token"
export CANVAS_INSTANCE_URL="https://yourschool.instructure.com"

# Dry run first to verify
python setup_canvas_course.py --config ../course-info.yaml --dry-run

# Run actual setup
python setup_canvas_course.py --config ../course-info.yaml

# Or setup and publish immediately
python setup_canvas_course.py --config ../course-info.yaml --publish
```

### 4. Setup GitHub Project

```bash
# Set GitHub credentials
export GITHUB_TOKEN="your-token"

# Run setup
python setup_github_project.py --config ../course-info.yaml
```

### 5. Setup Slack Channels (Optional)

```bash
# Set Slack credentials
export SLACK_TOKEN="xoxb-your-token"

# Enable in config first
# Edit course-info.yaml and set slack.create_channels: true

# Run setup
python setup_slack_channels.py --config ../course-info.yaml
```

## Tips and Best Practices

### Security

- **Never commit API tokens** to version control
- Store tokens in environment variables or a secure credential manager
- Use `.gitignore` to exclude any files with credentials
- Rotate tokens periodically

### Testing

- Always run with `--dry-run` first to preview changes
- Test with a sandbox Canvas course before using on production
- Keep a backup of your Canvas course before running automation

### Template Maintenance

- Review downloaded templates for institution-specific content
- Replace absolute URLs with template variables
- Document any manual steps required after automation
- Keep templates updated as Canvas features change

### Customization

- Modify scripts to match your institution's requirements
- Add custom validation in `load_config()` functions
- Extend variable substitution for your use cases
- Add logging for better troubleshooting

## Troubleshooting

### Canvas API Issues

**Problem:** "401 Unauthorized" error

**Solution:** Check that your `CANVAS_API_TOKEN` is set correctly and hasn't expired.

**Problem:** "Course not found" error

**Solution:** Verify the course ID is correct. You can find it in the Canvas URL: `https://canvas.school.edu/courses/123456`

### GitHub API Issues

**Problem:** "Resource not accessible by integration"

**Solution:** Ensure your GitHub token has the required scopes (`repo`, `project`).

**Problem:** "Repository already exists"

**Solution:** The script will skip creation if the repo exists. Use `--skip-repo` if you only want to create issues/projects.

### Slack API Issues

**Problem:** "Invalid token"

**Solution:** Make sure you're using a Bot User OAuth Token (starts with `xoxb-`), not a User OAuth Token.

**Problem:** "Channel name already taken"

**Solution:** The script will detect existing channels and skip creation. Check your Slack workspace for naming conflicts.

### Variable Substitution Issues

**Problem:** Variables not being replaced (showing as `{variable}`)

**Solution:** Check that:
1. The variable exists in `course-info.yaml`
2. The path is correct (use dot notation: `course.semester`)
3. The value is not empty in the config

## Contributing

If you improve these scripts or add new features:

1. Test thoroughly with a sandbox course
2. Update this README with new options/features
3. Add error handling for edge cases
4. Submit a pull request with a clear description

## Support

For issues or questions:

1. Check this README first
2. Review the script source code for detailed comments
3. Test with `--dry-run` to diagnose issues
4. Check API documentation:
   - [Canvas API](https://canvas.instructure.com/doc/api/)
   - [GitHub API](https://docs.github.com/en/rest)
   - [Slack API](https://api.slack.com/methods)
