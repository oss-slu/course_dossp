# Developing Open Source Software Products

A hands-on course where you join a real open source product team, contribute working software across a full semester lifecycle, and build professional skills in technical leadership, collaboration, and open source practices.

## Getting Started

The **Welcome** module is your starting point. It contains:

- **Syllabus** — course policies, grading structure, and expectations
- **Access Checklist** — everything you need set up before work begins (GitHub, Slack, development environment). Complete this early.
- **Required Readings & Reading Schedule** — the semester reading list with recommended pacing
- **Demonstrate Professional Leadership** — a semester-long assignment for students aiming for A-level performance, where you document leadership beyond your immediate project responsibilities. Start thinking about this early.

## Iteration Start

Before sprints begin, you'll orient to your product and team through the **Iteration Start** module:

- **BLA3DE** — a structured activity for learning about your assigned product's Background, Landscape, Architecture, Data, Dependencies, and Environment
- **Iteration Starters** — initial planning work to set your team up for productive sprints

## Work Cycle Schedule

The semester is organized into **two iterations** spanning **seven sprints** (Sprint 0 through Sprint 6), each roughly two weeks long.

**Iteration 1** (Sprints 0–3) focuses on onboarding, team formation, and establishing your development rhythm. It ends with Milestone 1 and an initial performance evaluation.

- Sprint 0 covers BLA3DE and developer onboarding
- Sprints 1–3 are full development sprints with sprint close reports
- Client Demo & Feedback 1 falls at the end of Sprint 2
- Sprint deadlines are firm — they follow the development lifecycle. Late work isn't penalized with "points," but factors into performance evaluations.

**Spring Break** falls between iterations.

**Iteration 2** (Sprints 4–6) builds on what you've established. It ends with Milestone 2, a second performance evaluation, and transitions into the Launch phase.

- Client Demo & Feedback 2 falls at the end of Sprint 4
- Sprint 5 includes preparation for the SSE Undergraduate Showcase poster presentation (developer responsibility)
- Sprint 6 is the final development sprint before Launch

## Good Practices

The **Good Practices** module contains recommended practices tied to key dates in the development lifecycle. The course uses the term "Good Practices" rather than "Best Practices" because there is no single, universal, context-free "best" — you adapt these practices to your specific context.

Completing good practices in a timely fashion is required for at least a B in the course. They include:

- **Milestones** — iteration-level goals that your team defines and works toward
- **Team OKRs** — Objectives and Key Results to guide your team's focus
- **Retrospective Facilitation** — leading your team through structured reflection
- **Team Metrics Reports** — periodic reports on team health and progress (three across the semester)

## Checkpoints

**Checkpoints** are structured deliverables where you engage with a specific dimension of open source product development. You'll complete a **Team Working Agreement**, a **Team Outing**, and **four Artifact Choices** selected from this catalog:

| Checkpoint         | Description                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| Community Building | Execute a community-building initiative and reflect on your project's community needs                           |
| User-Focused       | Conduct user research (interviews, usability testing, prototype testing) to validate your work helps real users |
| System Designs     | Create visual design artifacts — architecture diagrams, wireframes, data models, user flows                     |
| Strategy Draft     | Draft your Product Strategy and Community Strategy documents with feedback before finals                        |
| Threat Model       | Systematically identify security risks, assess impact and likelihood, and propose mitigations                   |
| Backlog Audit      | Audit and clean up your project backlog for future teams and external contributors                              |

Checkpoint due dates are recommendations, not hard deadlines — actual timing may vary based on team agreements and project needs.

## Launch & Reflection

The final phase of the course (after Sprint 6) shifts from development to delivery and reflection:

- **Launch Preparation Checklist** — ensure your product is ready for handoff
- **Team Presentation** — present your work to the class
- **Working Software Submission** — deliver functional, merged software
- **Product Strategy Final Document** — your polished product strategy
- **Community Strategy Document** — your plan for community engagement and growth
- **Performance Evaluation — Final Review** — a comprehensive reflection on your semester performance

## Additional Resources

The **Additional Resources** module provides supplementary materials available throughout the semester:

- **Handbooks & Guides** — [Tech Lead Handbook](https://github.com/oss-slu/handbook_tech_lead), [Developer Handbook](https://github.com/oss-slu/handbook_developer), [BOLT Handbook](https://github.com/oss-slu/handbook_bolt)
- **Supplemental Materials** — program overview, conference travel stipend information, related materials, Ideal Team Player model and self-assessment
- **Optional Resources** — recommendations for further reading

## Repository Structure

This repository holds the source materials used to build and deliver the course through Canvas. Students access course content through Canvas directly — this repo is the behind-the-scenes source.

```
assignments/    Assignment definitions (Markdown + YAML metadata)
content/        Long-form course content and page text
files/          Static files distributed through Canvas (PDFs, images)
issues/         GitHub Issues for instructor course management
quizzes/        Quiz definitions (Markdown + YAML metadata)
scripts/        Course setup automation
modules.yaml    Canvas module structure and ordering
course-info.yaml  Per-instance course configuration
```

If you spot an error or have a suggestion for improving course materials, feel free to submit a pull request.

For course administration (creating new instances, automation tooling), see [ADMINISTERING.md](ADMINISTERING.md).
