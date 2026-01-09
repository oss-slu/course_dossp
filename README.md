# Developing Open Source Software Products Course Materials

## Overview

This repo contains the templates for automatically spinning up new instances of the Developing Open Source Software Products Course, along with resources and documents used during the course, and automation scripts that interact with Canvas, GitHub (especially GitHub Projects), and Slack.

## Directory structure

- assignments: Markdown files with yaml metadata that describes each assignment posted in Canvas.
- content: More detailed course content like long-form descriptions, lists of resources, videos and various other documetns. Where possible, original documents are written in Markdown and rendered to either HTML or PDF. Video and other media files are typically only final output versions.
- issues: A set of GitHub Issues that can be added to a private course Kanban board to ensure course materials are covered. This includes required readings, course discussion topics, and instructor deliverables (e.g. performance evaluations). Student deliverables are tracked in individual assignments.
- quizzes: Markdown files with yaml metadata that describes each quiz posted in Canvas.
- scripts: Automation scripts that set up a new instance of the course. The scripts can create a course archive in a private GitHub repository, create Issues with proper labels in GitHub Projects, update Canvas with templated materials, retrieve materials from Canvas and store them either locally or in the course archive, and create course related channels in Slack.

## Using this repository

If you are a student you may have followed a link to course content and found yourself here. Feel free to submit a pull request for any course materials you think could be improved

## Administering a course

> **Note:** As of January 2026, the Python scripts in `scripts/` for Canvas operations have been superseded by MosTidy's `canvas extract` and `canvas insert` commands. See the [MosTidy Canvas Course Templates documentation](../../__program/MosTidy/docs/canvas-course-templates.md) for current usage. The Python scripts are preserved for historical reference.

To create a new course, create a branch of this repo named with the course number, section number, semester code, and CRN delimted by hyphens. It should look like `csci-5930-02-262-26314`. Update the course-info.yaml with any fields labeled `required`. When you push your branch to GitHub and open a Pull Request, it will trigger a GitHub Action that will initiate a new course.

### Quick Start (MosTidy - Recommended)

```bash
# Extract templates from an existing course
mostidy canvas extract <source_course_id> -o ./

# Preview what will be created
mostidy canvas insert . --course <new_course_id> --config course-info.yaml --dry-run

# Create content in new course
mostidy canvas insert . --course <new_course_id> --config course-info.yaml
```

### Quick Start (Legacy Python Scripts)

1. **Setup Python virtual environment and install dependencies:**

   ```bash
   cd scripts
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**

   ```bash
   cp .env.example .env
   # Edit .env and add your API tokens
   ```

3. **Update course configuration:**

   ```bash
   # Edit course-info.yaml and fill in required fields
   vim course-info.yaml
   ```

4. **Run setup:**

   ```bash
   cd scripts

   # Dry run to preview changes
   python setup_canvas_course.py --config ../course-info.yaml --dry-run

   # Run full setup
   python setup_canvas_course.py --config ../course-info.yaml
   ```

For detailed documentation on the automation scripts, see [scripts/README.md](scripts/README.md).
