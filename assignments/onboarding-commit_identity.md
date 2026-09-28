---
title: 'Onboarding: Commit Identity'
points_possible: 0
due_at: '2026-09-30T21:00:00Z'
submission_types:
- online_text_entry
published: false
assignment_group: "Assignments"
grading_type: pass_fail
---

**Target Sprint:** 3

**Focus:** Attribution and Team Records

# Overview

Git records a name and email address on every commit. GitHub shows that commit as yours only if the address is registered to your account. If it is not, the work stays in the repository but attaches to no account at all.

You have two jobs here. The first is your own identity, which every developer on the course is doing as well. The second is your team's attribution record, which is yours alone. Nobody else is positioned to notice that a teammate has been committing under an address that belongs to nothing.

## Why this lands on the Tech Lead

The sprint summary counts commits per developer. A developer whose commits attribute to no account looks inactive in that summary no matter how much they shipped. You are the person who sees both the team's actual work and the report that describes it, so you are the one who can catch the gap between them.

It is also easier to fix early. Attribution can usually be repaired later by adding the old address to a GitHub account, but that only works if the address was real. An address git invented from a hostname cannot be claimed by anyone, ever.

# Activity

## Part 1: Your own identity

Complete the developer version of this activity, **Onboarding: Commit Identity** in your Capstone course. It walks through checking your current configuration, choosing an address, configuring git, and verifying a commit attributes correctly. It also covers the background on how git and GitHub relate, the tradeoffs between your noreply address and your SLU address, and how to repair earlier commits.

Do that first. The rest of this assignment assumes you have done it.

## Part 2: Audit your team

Open your team's repository on GitHub and look at the commit history for this semester.

**1. Check each contributor.**

The contributors view and the commit list both work. For each person who has committed, confirm their avatar appears and their username links to a profile. A plain name with no link means those commits are attached to no account.

You can also read the addresses directly:

```
git log --format='%an <%ae>' | sort -u
```

Any address ending in `.local` was invented by git from a machine hostname and belongs to no account.

**2. Note anyone whose commits are not attributing.**

You are looking for two cases. Someone whose commits attach to no account, and someone committing under more than one identity, which usually means a second machine that was never configured.

**3. Tell them, and help them fix it.**

Point them at the developer assignment. For an address that is real but unregistered, adding it to their GitHub account repairs the history retroactively and they do not need access to that mailbox. For an address that is not real, the history cannot be repaired and we will record the work directly instead.

This is a normal thing to raise, not a criticism. Most people have never been told any of this.

**4. Check your repository credits contributors at all.**

If your team has no `CONTRIBUTORS.md`, create one and seed it with the people who have worked on the project. Developers are being asked to add themselves to it as their verification commit, so having the file in place helps them.

# Requirements

* Your own git identity is configured to an address registered to your GitHub account, verified against a real commit.
* Every current contributor to your team's repository has been checked.
* Anyone whose commits are not attributing has been contacted, with a specific next step.
* Your repository has a `CONTRIBUTORS.md`.

# Deliverables

Submit your own three lines first, in this format, since it is read by tooling.

```
Commit: <URL of the commit you verified>
Email: <the address you configured>
Machines: <how many machines you commit from>
```

Then a short table covering everyone who has committed to your team's repository this semester.

```
| Contributor | Attributing? | Action taken |
| --- | --- | --- |
| jdoe | yes | none needed |
| asmith | no, .local address | messaged Sep 29, history cannot be repaired, needs manual credit |
| bjones | partial, second machine | messaged Sep 29, configuring laptop |
```

Close with two or three sentences on what you found, and whether anything needs the instructor's help.

# Evaluation

Required, not graded. There is no rubric. What matters is that the audit actually happened and that anyone affected knows about it.

# About the Deadline

*This is a target deadline.* Part 2 depends on teammates responding to you, which you do not control. Submit the audit with whatever state each person is in and note what is still outstanding. Missing the date because you are waiting on a teammate is fine as long as you say so.

# Submission

Submit your three lines, the contributor table, and your closing notes as a text entry.
