---
title: Sprint Structure & Expectations
url: sprint_structure_expectations
published: true
front_page: false
---

This document explains how sprints work in Open Source with SLU and what's expected of you as a Tech Lead during each sprint cycle.

## Why Sprints?

Software development in the real world rarely happens in one big push. Professional teams break work into smaller, predictable cycles—delivering working software frequently rather than waiting until "everything is done."

Sprints create the rhythm that makes your leadership visible. Each sprint is a bounded commitment where your team picks up work, delivers it, and reflects. As the Tech Lead, you're responsible for making this cycle run smoothly:

- **Accountability**: Your team delivers concrete progress toward Milestones every two weeks because you've prepared the work and set clear expectations
- **Feedback loops**: Regular check-ins catch problems early, when they're easier to fix—and you're the one who needs to notice them first
- **Professional habits**: The ability to plan, communicate progress, and ship on a schedule is a career skill—and you're modeling it for your team

The sprint structure isn't arbitrary bureaucracy—it mirrors how software teams at companies large and small actually operate. Your role is to make that structure work for your specific team.

---

## The Two-Week Sprint Cycle

Each sprint runs for two weeks, Monday to Monday. The specific dates for each sprint are published in Canvas under the Work Cycle Schedule module.

Here's what a typical sprint looks like from your perspective:

### Before Sprint Start: Preparation

Your work starts before the sprint does. By the time the sprint begins, you need:

- **A pool of refined issues** ready for developers to pull from—enough work for each developer to complete multiple issues if they're working effectively
- **Clear acceptance criteria** so developers know what "done" looks like
- **Technical context** documented in issues so developers can start without needing to ask basic questions
- **Prioritization** that aligns with your iteration Milestone
- **Issue sizing** that allows developers to complete work and take on additional issues within the sprint

Issues must be ready by **6:00 PM Monday** at sprint start. If issues aren't prepared—or if there isn't enough work for productive developers to stay engaged—your team loses momentum.

### Week 1: Enable and Monitor

**Monday (Sprint Start)**
Developers should be able to pick up work immediately. Be available in Slack and during class time to answer questions and clarify requirements.

**Tuesday through Sunday**
Your developers are in heads-down development time. Your job is to:

- **Monitor progress**: Are developers pushing commits? Asking questions? Silent developers may be stuck
- **Unblock quickly**: When questions come up, respond promptly—within hours, not days
- **Stay ahead**: Start thinking about the next sprint's issues while this one is in progress
- **Review early**: If developers open draft PRs, look at them—don't wait for "ready for review"
- **Keep work flowing**: When developers finish early, have additional issues ready for them to pick up

**Monday (End of Week 1)**
Developers should have functional PRs raised by 4:10 PM. Strong developers may already be starting on additional issues. This is when your code review work intensifies.

### Week 2: Review, Refine, and Merge

**Tuesday through Friday**
This is your most active period. For every PR:

- **Acknowledge within 24 hours** of it being opened or updated
- **Complete meaningful review within 48 hours**—not just comments, but an actual GitHub review
- **Use "Request Changes"** when changes are required—a "Comment" leaves the PR showing "waiting for review"
- **Be constructive**: Follow good code review practices—focus on what matters, explain the "why"

If a PR needs revision, communicate clearly what needs to change and why. Push commits to the developer's branch if you need to provide guidance they can repeat elsewhere.

**By Wednesday of Week 2**
If an issue is too big to complete in the remaining time, you need to rescope:

- Reduce the active issue to something achievable
- Create a new issue for the removed work
- Consider feature flags if partial work needs to be merged
- The rescoped work should still merge by sprint end

**Monday (Sprint End)**
By 4:10 PM, all developer PRs should be either merged or closed. No PRs should carry over into the next sprint.

---

## Setting Developer Expectations

### The Baseline vs. The Goal

Developers are told that **one merged PR per sprint is the baseline**—the minimum to demonstrate they can participate in a professional development workflow. That baseline corresponds to C-level performance.

**Your job is to set expectations higher than the baseline.**

The goal isn't one PR per sprint. The goal is **meaningful progress toward your iteration Milestone**. For most developers on most sprints, that means:

- Multiple issues worked on and merged
- Sustained engagement throughout the two weeks
- Contributions that move the product forward, not just box-checking

When you prepare sprint work, prepare enough issues for developers to stay productive. When you discuss expectations with your team, frame the conversation around Milestones and product value—not minimum PR counts.

### Holding Developers Accountable

You are the first line of accountability for developer performance. This means:

- **Setting clear expectations** at sprint start about what progress looks like
- **Monitoring mid-sprint** to catch underperformance early
- **Having direct conversations** when developers aren't meeting expectations
- **Documenting patterns** of underperformance for performance evaluations

A developer who consistently delivers only one small PR per sprint while teammates deliver more is underperforming—even if they technically meet the baseline. Your feedback and expectations shape how developers understand their responsibilities.

---

## What's Expected of You

### The Baseline: Enabling Developer Success

At minimum, every sprint you must:

1. **Prepare sufficient work**: Issues refined and ready by Monday 6:00 PM—enough to keep your team productively engaged
2. **Review promptly**: Acknowledge PRs within 24 hours, complete reviews within 48 hours
3. **Merge thoughtfully**: Only merge functional code that meets standards and delivers value
4. **Close cleanly**: All PRs merged or closed before the next sprint starts

This is table stakes—the minimum to keep the sprint cycle functioning. Baseline performance corresponds to passing, but does not distinguish you as an effective leader.

### Beyond Baseline: What Distinguishes Stronger Performance

**Managing Team Dynamics (35% of your evaluation)**
- Facilitate productive retrospectives that drive actual improvement
- Build an inclusive culture where all team members contribute
- Handle conflicts constructively before they escalate
- Maintain strong client relationships and communication

**Software Engineering Quality (35% of your evaluation)**
- Make sound architectural decisions that balance immediate needs with long-term maintainability
- Establish and enforce code review culture that actually improves code quality
- Implement CI/CD and testing practices appropriate to your project
- Maintain technical documentation that helps future developers

**Product and Project Management (15% of your evaluation)**
- Articulate a clear product vision that aligns OSS requirements, client needs, and team inspiration
- Use project management tools effectively—not just for compliance, but for clarity
- Execute sprints smoothly with good checkpoint documentation

**Open Source Practices (15% of your evaluation)**
- Maintain proper licensing and documentation
- Build toward community governance and contributor-friendly processes
- Respond to issues and contributions as a maintainer would

### The Path to Excellence

An A in this course requires completing the Demonstrate Professional Leadership assignment—work that documents how you're building leadership capacity beyond your immediate project responsibilities.

Plan for this early. Leadership activities might include mentoring other Tech Leads, contributing to program-wide improvements, or building skills that benefit the broader OSS community.

---

## Merging Decisions

You control what gets merged. This is significant responsibility. Here are the principles:

**Only merge work worth merging**
- The work must fully resolve the issue being addressed
- The code must meet basic software engineering standards
- The work must improve the codebase, not just add to it

**Never merge just because the sprint is ending**
If code isn't ready, don't merge it. Your product's quality matters more than any individual sprint's velocity metrics.

**When work isn't complete by sprint end:**
- If the developer made significant effort but hit a technical wall beyond their ability, you may continue development yourself—the developer still gets credit for their contribution
- If the developer didn't put forth appropriate effort, they may have until Wednesday to finish for partial credit (70%)
- If work is almost done by Wednesday, you can finish small remaining pieces to merge on Thursday
- If work is genuinely valueless, close the PR without merging—the developer won't get credit

Document your rationale for these decisions. Your judgment is part of what's being evaluated.

---

## Sprint Close Visibility

Unlike developers, you don't submit a Sprint Close report. Instead, your sprint work is visible through:

- PRs reviewed and feedback provided
- Code merged into the main branch
- Issues closed and work completed
- Overall team velocity and progress toward Milestones

The instructor monitors this activity through GitHub. If there are concerns about code review activity, merge frequency, or team engagement, you'll receive direct feedback.

---

## When Things Don't Go as Planned

### "A developer is stuck and not making progress"

This is your problem to solve, not theirs alone. Resources available:

- Pair with them to understand the blocker
- Point them to teammates who've solved similar problems
- Connect them with office hours or other support
- Rescope the issue if it's genuinely too hard

If a developer suffers in silence for two weeks, you missed the warning signs.

### "An issue turned out to be bigger than expected"

Rescope by Wednesday of Week 2. This is a professional skill:

- Identify the achievable subset
- Create new issues for remaining work
- Use feature flags if needed
- Document what was learned about estimation

### "A developer isn't putting in appropriate effort"

Have a direct conversation early. Document it in the PR or Slack (no backchannels). If the pattern continues, escalate to the instructor. Your job is to lead, not to carry.

### "A developer finished early with nothing to do"

This is a preparation failure. You should have additional issues ready. In the moment, identify work they can pick up—even if it means creating issues on the fly. For future sprints, prepare more work than you think you'll need.

### "My team isn't communicating in the open"

Model the behavior you expect. Post updates in your project channel regularly—even brief ones. Ask questions publicly. Celebrate wins publicly. The tone and norms are yours to set.

---

## Key Deadlines Summary

| When | What |
|------|------|
| Monday 6:00 PM (Sprint Start) | Issues refined and ready for work |
| Monday 4:10 PM (Week 1) | Developer PRs should be raised |
| Within 24 hours of PR | Acknowledge PR with initial response |
| Within 48 hours of PR | Complete meaningful code review |
| Wednesday (Week 2) | Final opportunity to rescope if needed |
| Monday 4:10 PM (Week 2) | All PRs merged or closed |

All times are Central Time. Check Canvas for specific dates each sprint.

---

## Related Resources

- **[Tech Lead Handbook](https://github.com/oss-slu/handbook_tech_lead)**: Detailed guidance on technical leadership practices
- **Good Practices assignments**: Milestones, OKRs, retrospective facilitation, metrics reports
- **Checkpoint assignments**: Team working agreements, artifact choices
- **Performance Evaluations**: How sprint work factors into your grade (Team Dynamics, Software Quality, Product/Project Management, Open Source Practices)
- **Demonstrate Professional Leadership**: Requirements for A-level performance
- **Sprint 1 Transition**: Context on ownership expectations after onboarding
