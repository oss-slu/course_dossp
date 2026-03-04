# Administering the DOSSP Course

This document covers how to create and configure new instances of the Developing Open Source Software Products course.

## Directory Structure

- `assignments/` — Markdown files with YAML metadata describing each assignment posted in Canvas
- `content/` — Detailed course content (long-form descriptions, resource lists, videos, documents). Originals are in Markdown, rendered to HTML or PDF where needed. Media files are typically final output versions only.
- `files/` — Static files (PDFs, images) distributed through Canvas
- `issues/` — GitHub Issues for a private course Kanban board covering required readings, discussion topics, and instructor deliverables. Student deliverables are tracked in individual assignments.
- `quizzes/` — Markdown files with YAML metadata describing each quiz posted in Canvas
- `modules.yaml` — Defines the Canvas module structure and item ordering
- `course-info.yaml` — Per-instance course configuration (section, semester, CRN, etc.)

## Creating a New Course Instance

To create a new course, create a branch of this repo named with the course number, section number, semester code, and CRN delimited by hyphens. It should look like `csci-5930-02-262-26314`. Update `course-info.yaml` with any fields labeled `required`. When you push your branch to GitHub and open a Pull Request, it will trigger a GitHub Action that will initiate a new course.

### Quick Start (MosTidy)

Course provisioning uses MosTidy's Canvas commands. See the [MosTidy Canvas Course Templates documentation](../../__program/MosTidy/docs/canvas-course-templates.md) for full details.

```bash
# Extract templates from an existing course
mostidy canvas extract <source_course_id> -o ./

# Preview what will be created
mostidy canvas insert . --course <new_course_id> --config course-info.yaml --dry-run

# Create content in new course
mostidy canvas insert . --course <new_course_id> --config course-info.yaml
```

> **Note:** Prior to January 2026, Canvas operations were handled by Python scripts in a `scripts/` directory. Those scripts have been removed; MosTidy is the sole supported tool for course provisioning.
