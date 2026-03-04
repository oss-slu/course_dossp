---
title: "Week 4 Discussion Prompts: Products"
url: week-4-discussion-prompts-products
published: true
front_page: false
---

# Week 4 Discussion Prompts: Products (Tech Leads)

## Overview

These prompts synthesize three readings that triangulate on the question of what it means to build a *product* rather than just write code:

| Author            | Work                                            | Core Lens                                                                 |
| ----------------- | ----------------------------------------------- | ------------------------------------------------------------------------- |
| **Dave Farley**   | "Engineering for Software in 8 Minutes" (video) | Engineering as applied science: optimize for learning, manage complexity  |
| **Teresa Torres** | *Continuous Discovery Habits*, Intro + Part 1   | Product as discovery challenge: find the right outcome, test assumptions  |
| **Payal Arora**   | *From Pessimism to Promise*, p. ix-62           | Product as justice challenge: whose needs get centered, whose get ignored |

Every prompt is addressed directly to the Tech Lead role. The arc moves from identity ("what are you building?") through epistemology ("how do you know what to build?") to practice ("how do you lead a team that learns?").

---

## Prompts

### 1. Product or codebase?

This week's theme is "Products." Farley says "our job isn't writing code -- it's solving problems for people with software." Torres structures continuous discovery around understanding customer needs. Arora challenges assumptions about who "people" are and what they actually need. As a tech lead, you're the person most likely to set the frame your team operates in. What distinguishes a product from a codebase -- and which one is your team actually building right now?

### 2. Whose problems?

As a tech lead for an open source product, you decide whose problems the team focuses on. But Arora shows that technology designed in one context rarely transfers cleanly to another, and Torres warns against jumping to solutions before understanding the problem. Who are your intended users? What are you assuming about their context -- connectivity, devices, language, ability, prior experience? Have you validated any of those assumptions, or are you building for a user that exists only in your head?

### 3. Experts at being wrong

Farley says to start by assuming you're probably wrong. Torres advocates continuous discovery over upfront requirements. Arora demonstrates just how deeply wrong assumptions about technology users can be -- entire fields of research built on misreading how people in the Global South engage with technology. What does it actually look like to build a product culture that embraces being wrong? And when your telemetry says a feature is being used "wrong," do you fix the user's behavior or support it?

### 4. Closing the discovery gap

Torres's framework assumes a product team with regular access to customers -- weekly interviews, prototype testing. Your open source project probably doesn't have that. Meanwhile, Arora shows that open source tools get repurposed by users far from the original designers' imagination. As tech lead, this is your problem to solve. What are you doing to ensure your team hears from real users -- including users you never anticipated? If the answer is "nothing yet," what's one realistic step you could take this semester?

### 5. Architecture as strategy

Farley argues that good engineering manages complexity through modularity, separation of concerns, and abstraction. Torres argues that discovery never stops -- what you learn next month may reshape your direction. As the person making architectural decisions, are you building a system that can absorb new learning, or one that locks in today's assumptions? Point to a specific decision in your codebase. Will it help or hurt when the direction shifts?

### 6. Outcomes, not outputs

Torres distinguishes between outputs (features shipped) and outcomes (measurable impact on users). Farley might define quality as the ability to change the code. Arora might ask: quality for whom, measured by whose standards? As the person defining "done" for your team, how do you decide whether a sprint was successful? If your team shipped every ticket on the board this semester but nobody's life got better, would you consider that a success?

### 7. Speed, quality, and context

Farley argues that speed and quality reinforce each other -- they're not a trade-off. Torres argues that shipping quickly without discovery is just "building faster in the wrong direction." Arora shows that communities in the Global South often adopt and adapt technology faster than expected -- but that building trust requires patience, not velocity. As tech lead, you navigate this tension daily. When your team feels pressure to ship, what do you protect and what do you sacrifice? Has that instinct served you well?

### 8. The tech lead as learner-in-chief

Farley says we need to become "experts at learning." Torres structures learning through discovery habits. Arora reveals the blind spots that emerge when builders don't examine their own assumptions. All three readings converge here: the tech lead's primary job isn't deciding what to build -- it's creating the conditions for a team to learn what to build. What are you doing to create those conditions? What's the hardest part?

---

## Facilitation Notes

### Session Design

**Format**: 75-minute Zoom session with ~25 Tech Leads. Full-class discussion doesn't scale at this size on Zoom -- use breakout rooms as the primary discussion space and plenary for framing, transitions, and harvest.

**Recommended structure**:

| Block            | Duration | Activity                                                                         |
| ---------------- | -------- | -------------------------------------------------------------------------------- |
| Frame            | 5 min    | Plenary: set context with three lenses on "product" (table above)                |
| Warm-up breakout | 10 min   | Breakout rooms (3-4 people): Prompt 1. No report-back -- just get people talking |
| Transition       | 3 min    | Plenary: deliver the transition line, introduce the core prompts                 |
| Core breakout    | 30 min   | Breakout rooms (4-5 people): 2-3 prompts, posted in chat before rooms open       |
| Harvest          | 15 min   | Plenary: one insight per room, then Prompt 8 as a closing reflection             |
| Close            | 5 min    | Chat waterfall: one sentence each -- what will you do differently this sprint?   |
|                  |          |                                                                                  |

**Breakout room logistics**:

- **Assign rooms manually** if you want cross-track mixing (Foundations + Advanced in every room). Otherwise, random assignment works for the warm-up.
- **Post prompts in chat** before opening rooms so leads have the text in front of them. Zoom breakout rooms don't carry main chat.
- **Broadcast a message** at the halfway mark of the core breakout ("~15 minutes left -- if you haven't gotten to the second prompt, shift now").
- **Don't over-harvest.** In plenary, ask for one highlight per room, not a full recap. The real work happened in the rooms.

**You will not use all 8 prompts in a single session.** Select based on where the cohort is and what emerged in prior weeks. The full set is available for async engagement, follow-up conversations, or written reflection.

### Prompt Selection Guide

Not every group needs the same prompts. Use this guide to select based on what you're observing in the cohort:

| If you're seeing...                                 | Prioritize                                                          | Why                                                     |
| --------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------- |
| Teams treating the project as a homework assignment | **1** (Product or codebase?)                                        | Forces the identity question directly                   |
| Leads making assumptions without user contact       | **2** (Whose problems?) + **4** (Discovery gap)                     | Challenges assumptions and demands a concrete next step |
| Teams afraid to experiment or change direction      | **3** (Experts at being wrong) + **5** (Architecture as strategy)   | Names the fear and connects it to technical decisions   |
| Feature-factory energy, shipping without direction  | **6** (Outcomes, not outputs) + **7** (Speed, quality, and context) | Reframes success metrics                                |
| Leads doing all the thinking, teams just executing  | **8** (Learner-in-chief)                                            | Shifts leadership from "deciding" to "enabling"         |

### Warm-Up Breakout: Prompt 1

Open breakout rooms of 3-4 people for 10 minutes on Prompt 1. This prompt is deliberately broad and non-threatening -- it asks about identity, not performance. It surfaces how each lead frames their own work, which sets up every subsequent prompt.

No formal report-back. When rooms close, deliver the transition line in plenary:

**Transition line**: "If your answer was closer to 'codebase,' the rest of today's conversation is about what it would take to move toward 'product.' If your answer was 'product,' the question becomes: how do you know?"

### Running the Core Breakout

**Pick 2-3 prompts** for the core breakout. Paste them into chat before opening rooms so every group has the text. Rooms of 4-5 people for 30 minutes.

**Before opening rooms**: Read the first prompt aloud and let it land for a beat. Tell groups to start there and move to the next prompt when they're ready. Not every group will cover every prompt -- that's fine.

**While rooms are open**:
- **Broadcast a halfway message**: "~15 minutes left -- if you haven't moved to the second prompt, shift now."
- **Drop into rooms briefly** if you want to gauge energy, but don't stay long enough to shift the dynamic. You're checking temperature, not facilitating.

**Facilitation moves for the harvest** (when rooms close):
- Ask one person per room to share a single insight or question that emerged -- not a summary of their whole conversation.
- **Redirect to specifics**: When answers stay abstract ("we should talk to users more"), push: "Who, specifically? When would you do it? What would you ask?"
- **Name the tension**: These prompts are built around tensions (speed vs. trust, modularity vs. holism, data vs. intuition). When the harvest settles on one side, name the other: "Farley would say X, but Arora would push back -- how do you hold both?"
- **Cross-pollinate across rooms**: "Did any other room land somewhere different on that question?"
- **Connect to their projects**: If discussion stays theoretical, bring it home: "How does this show up in your project this week?"

### Prompt-Specific Notes

**Prompt 2 (Whose problems?)** -- This one can get uncomfortable if leads realize they haven't thought about their users at all. That discomfort is productive. In a breakout room of 4-5 people, peers will hold each other accountable in ways plenary never could. If it comes up in the harvest, don't rescue them from it.

**Prompt 3 (Experts at being wrong)** -- The "telemetry" sub-question is deliberately provocative. It surfaces the difference between "the user is wrong" and "our model of the user is wrong." If the group hasn't read Arora deeply, you can offer a quick example: Arora documents how researchers assumed low-income users wanted "practical" tools but found them using phones for entertainment, romance, and social status -- the "wrong" use was actually the real use.

**Prompt 4 (Discovery gap)** -- This is the most actionable prompt. If it surfaces during harvest, push for concrete commitments: "What's one thing you could do in the next two weeks?" If someone says "I'd put a feedback form on our README," that's a real answer. Drop a note in chat asking each room to post their commitment -- this creates a written record you can revisit in Week 8.

**Prompt 5 (Architecture as strategy)** -- This prompt works best when leads can actually name a specific technical decision. If they struggle, offer examples: "Did you choose a database? A framework? A module boundary? An API shape? Those are all bets on the future. Which ones are easy to reverse, and which ones aren't?"

**Prompt 6 (Outcomes, not outputs)** -- The closing question ("If your team shipped every ticket but nobody's life got better") is intentionally stark. It may generate defensiveness ("but we're students, we can't measure real-world impact"). Valid -- but the question is about *orientation*, not measurement precision. Are they thinking about impact at all?

**Prompt 7 (Speed, quality, and context)** -- This prompt works well late in the session when breakout rooms have built trust. The "what do you sacrifice" question reveals real values. During harvest, listen for patterns across rooms.

### Closing: Prompt 8

Use Prompt 8 as the capstone during the harvest block. It synthesizes all three readings into a single claim: the tech lead's job is to create conditions for learning. Options:

- **Plenary discussion** (10-15 min) if harvest energy is high and people are unmuted and talking
- **Chat waterfall**: Post the prompt, give everyone 2 minutes to type, then everyone hits Enter at the same time. This gets 25 voices into the room simultaneously -- something plenary discussion can't do on Zoom.
- **Individual written reflection** (5 min of writing in a shared doc or DM to you) if the group needs a quieter close

**Closing commitment**: "In one sentence in the chat: what will you do differently this sprint?" Everyone posts. Screenshot the chat -- these are the commitments you revisit in Week 8.

### Connecting to the Semester Arc

This is the first "Products" week. The theme returns in Weeks 8 and 13:

- **Week 8**: Farley on software architecture + Arora p. 63-121 + Torres Ch 3-7. By then, leads should have acted on their Week 4 commitments. Open Week 8 by revisiting: "In Week 4, you said you'd do X. Did you? What happened?"
- **Week 13**: Eric Evans on Bounded Contexts + Arora or Torres conclusions. This is the most abstract Products week -- it assumes the leads have been *doing* product work for 9 weeks and can now reflect on it with theoretical language.

The Week 4 conversation plants seeds. Weeks 8 and 13 harvest them. Don't try to resolve every tension today -- name the tensions and let them sit.

### Reading Differentiation

All leads watched the Farley video (8 min). Foundations leads read Arora; Advanced leads read Torres. This means:

- **Cross-track breakout rooms** are especially valuable for Prompts 2, 3, and 6, where Arora and Torres offer complementary perspectives on the same question. If you manually assign rooms, mix Foundations and Advanced leads in each room for the core breakout.
- During harvest, if discussion skews toward one source, ask: "For those who read the other book -- what does it add here?"
- Don't assume everyone has read both. The prompts are written so each one is accessible from either track, but the *richest* answers draw on both.

### After the Session

- Share the full prompt set in the DOSSP channel for async engagement.
- If commitments were made (especially around Prompt 4), note them and plan to revisit in Week 8.
- If a particular prompt generated energy or conflict, consider building on it in a future week's warm-up.
