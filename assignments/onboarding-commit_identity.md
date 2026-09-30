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

Do this first. Your own commits need to attribute before you can credibly ask a teammate to fix theirs. It takes about ten minutes.

**1. See what git is set to right now.**

```
git config user.name
git config user.email
```

An address ending in `.local` was invented by git from your computer's hostname and belongs to no account anywhere.

**2. Choose your address.**

The recommended choice is your GitHub noreply address. Find it at [github.com/settings/emails](https://github.com/settings/emails), under "Keep my email addresses private." It looks like `12345678+yourusername@users.noreply.github.com`, and it attributes by definition because it belongs to your account.

Your SLU address or a personal address also work, but you have to add the address to your GitHub account on that same page first. It then appears in every commit permanently. A commit address is not retractable, so consider what you are willing to have public for good.

**3. Configure git.**

```
git config --global user.name "Your Name"
git config --global user.email "your-chosen-address"
```

The name is whatever you want associated with your professional work. It does not need to match your GitHub username and has no effect on attribution. Only the address does.

**4. Verify against a real commit.**

Make a commit that is worth having. Adding yourself to your repository's `CONTRIBUTORS.md` is a good one, since Part 2 asks you to make sure that file exists anyway. Push it, find the commit on GitHub, and confirm your avatar appears and your username links to your profile. If it does not, the address in the commit is not registered to your account.

**5. Repeat on every machine you commit from.**

Git reads the configuration fresh on every commit. A lab computer, a personal laptop, and a desktop at home are three separate configurations, as is any machine you start using later in the term.

The developer version of this activity covers the same ground in more depth, along with how git and GitHub actually relate, the full tradeoffs between address options, how to repair earlier commits, and a bonus section on profile polish and commit signing. It is public, so you can read it whether or not you are enrolled in Capstone: [checkpoint-commit_identity.md](https://github.com/oss-slu/course_capstone/blob/main/assignments/checkpoint-commit_identity.md). You do not need it to finish this assignment, but it is what your developers are working from.

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

Point them at the [developer assignment](https://github.com/oss-slu/course_capstone/blob/main/assignments/checkpoint-commit_identity.md), or walk them through the steps in Part 1. For an address that is real but unregistered, adding it to their GitHub account repairs the history retroactively and they do not need access to that mailbox. For an address that is not real, the history cannot be repaired and we will record the work directly instead.

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
