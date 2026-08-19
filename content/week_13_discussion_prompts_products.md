---
title: "Week 13 Discussion Prompts: Products"
url: week-13-discussion-prompts-products
published: true
front_page: false
---

# Week 13 Discussion Prompts: Products (Tech Leads)

## Overview

These prompts synthesize three readings that triangulate on the question of where a product ends and how a team sustains the discipline of building one:

| Author            | Work                                          | Core Lens                                                                  |
| ----------------- | --------------------------------------------- | -------------------------------------------------------------------------- |
| **Eric Evans**    | "Bounded Contexts" (video, 35min)             | Products are shaped by language: draw explicit boundaries around models    |
| **Tony Fadell**   | *Build*, p. xi-86                             | Products are shaped by conviction: know why you're building, make it real  |
| **Teresa Torres** | *Continuous Discovery Habits*, Ch 11-15       | Products are shaped by discipline: sustain discovery, avoid anti-patterns  |

Every prompt is addressed directly to the Tech Lead role. The arc moves from boundaries ("what is your product, and what isn't it?") through language ("how do the words you use shape what you build?") to practice ("did you sustain the habits that matter?").

This is the final Products week. In Week 4, we asked whether you were building a product or a codebase. In Week 9, we asked whether your architecture could absorb new learning. Now the question is: after a full semester of product work, what have you actually learned about building products?

---

## Prompts

### 1. Drawing the line

Evans argues that every model has a boundary. Beyond that boundary the model breaks down, and pretending otherwise causes more damage than having two separate models. Fadell opens *Build* with stories about products that failed because they tried to be everything. Torres warns against anti-patterns where teams lose focus by chasing every opportunity. Your product has boundaries too, even if you never drew them explicitly. Where does your product end? What have you deliberately left out this semester, and what crept in that probably shouldn't have?

### 2. The language you inherited

Evans says that within a bounded context, every term has one precise meaning. When the same word means different things to different people, you don't have a shared model. You inherited a codebase, a backlog, maybe a README. What language did you inherit with it? Are there terms your team uses that your client understands differently? Terms your developers interpret differently from each other? Have those misalignments cost you anything this semester?

### 3. Conviction and evidence

Fadell argues that great products come from strong conviction. He describes leaders who knew what they wanted to build and fought for it. Torres argues the opposite: great products come from disciplined discovery, not conviction. In her framework, strong opinions are hypotheses to be tested, not truths to be defended. You've spent a semester navigating this tension. When did conviction serve you well? When did it lead you astray? And did you have a reliable way to tell the difference in the moment?

### 4. Making it real

Fadell insists that you have to make the intangible tangible. Prototypes, stories, physical artifacts. He describes building foam models and storyboards long before writing code. Torres structures this as assumption testing and experimentation. Evans, meanwhile, insists on precise language as the foundation of shared understanding. All three are saying: don't let important ideas stay abstract. This semester, what was the most effective thing you did to make your product vision concrete for your team or your client? What stayed too abstract for too long?

### 5. The map between contexts

Evans introduces context maps as a way to describe the relationships between bounded contexts. Two teams working on different parts of a system need to understand how their models translate at the boundaries. Your product sits at the intersection of at least three contexts: your development team, your client, and your users. Each group has a different model of what the product is and what it should do. How have you managed translation between those contexts? Where has something gotten lost in translation?

### 6. Discovery at the end

Torres's final chapters address sustaining discovery, measuring impact, and recognizing anti-patterns. She assumes a team that has been doing discovery work and needs to keep doing it. As your semester ends, be honest. Did you sustain any discovery practices? Did you talk to users, test assumptions, measure outcomes? Or did delivery pressure collapse everything into "build what's on the board"? If you're handing this product to a future team, what discovery debt are you leaving behind?

### 7. What mentors taught you

Fadell dedicates significant space to the role of mentors in building great products. He credits specific people who shaped how he thinks about design, engineering, and leadership. Evans's bounded contexts framework is itself a tool passed down through a community of practice. Torres's habits are designed to be taught and spread across organizations. Who or what taught you the most about product thinking this semester? It could be a person, a reading, a failure, a conversation. Name it specifically.

### 8. The product leader you became

In Week 4, we asked whether you were building a product or a codebase. Thirteen weeks later, answer that question again. But this time, don't just name which one. Describe what changed, what you tried, what you'd do differently. Evans says that models evolve as understanding deepens. Fadell says you learn the most from the products that fail. Torres says the goal is not to be right but to be less wrong over time. What do you understand about building products now that you didn't understand in January?

---

## Facilitation Notes

### Session Design

**Format**: 75-minute Zoom session with ~25 Tech Leads. This is the final Products session. Expect a different energy than Week 4. Leads are tired, delivery-focused, and reflective. Lean into the reflective energy rather than fighting it.

**Recommended structure**:

| Block            | Duration | Activity                                                                           |
| ---------------- | -------- | ---------------------------------------------------------------------------------- |
| Frame            | 5 min    | Plenary: reconnect to Week 4 commitments, introduce the three lenses              |
| Warm-up breakout | 10 min   | Breakout rooms (3-4 people): Prompt 1. Quick, concrete, gets them talking          |
| Transition       | 3 min    | Plenary: deliver transition line, introduce core prompts                           |
| Core breakout    | 30 min   | Breakout rooms (4-5 people): 2-3 prompts, posted in chat before rooms open         |
| Harvest          | 15 min   | Plenary: one insight per room, then Prompt 8 as closing reflection                 |
| Close            | 10 min   | Written reflection or chat waterfall: the product leader you became                |

**Opening the session**:

If you captured Week 4 commitments (especially around Prompt 4, "closing the discovery gap"), open with them. Read a few back. Don't name names unless someone volunteers. The point isn't accountability. The point is: "We said these things 9 weeks ago. Let's see what happened."

If you don't have Week 4 records, open with: "In Week 4 we asked whether you were building a product or a codebase. Some of you said product. Some of you were honest and said codebase. Today we're asking: what happened between then and now?"

**Breakout room logistics**:

Same as Week 4. Post prompts in chat before opening rooms. Broadcast a halfway message. Don't over-harvest.

**Cross-track mixing is especially important this week.** Foundations leads read Fadell (conviction, mentorship, making it tangible). Advanced leads read Torres (sustaining discovery, measuring impact, anti-patterns). Evans is the shared anchor. Mix tracks in every room so conversations draw on all three sources.

### Prompt Selection Guide

| If you're seeing...                                    | Prioritize                                                      | Why                                                        |
| ------------------------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------- |
| Teams that shipped features but lost sight of direction | **1** (Drawing the line) + **6** (Discovery at the end)         | Forces them to name what got in and what fell out           |
| Miscommunication between team, client, and users       | **2** (Language you inherited) + **5** (Map between contexts)   | Names the translation failures they've been living with    |
| Teams that feel stuck between "just ship it" and "we need to learn more" | **3** (Conviction and evidence) + **4** (Making it real) | Surfaces the tension and asks how they navigated it        |
| Leads who grew significantly this semester              | **7** (Mentors) + **8** (Product leader you became)             | Gives them space to name what they learned and from whom   |
| End-of-semester fatigue, low energy                     | **4** (Making it real) + **7** (Mentors)                        | Concrete and personal. Doesn't require abstract thinking   |

### Warm-Up Breakout: Prompt 1

Open breakout rooms of 3-4 people for 10 minutes on Prompt 1. This prompt is concrete and bounded. Everyone can answer "what did you leave out?" without needing to have deeply engaged with Evans's theory. It surfaces product scope decisions they've already made, whether consciously or not.

No formal report-back. When rooms close, deliver the transition line:

**Transition line**: "Evans would say that every one of those boundaries you just described is a bounded context. You drew a line around a model. The question for the rest of today is: did you draw it in the right place, and did everyone on your team agree on where it was?"

### Running the Core Breakout

Pick 2-3 prompts for the core breakout. If the cohort has strong energy, lean toward the abstract prompts (2, 3, 5). If energy is low or reflective, lean toward the personal ones (4, 6, 7).

**While rooms are open**: Same protocol as Week 4. Halfway broadcast, brief drop-ins for temperature checks.

**Facilitation moves for the harvest**:
- **Reconnect to earlier weeks**: "How does that connect to what you said in Week 4?" or "Did your Week 9 architectural decisions hold up?"
- **Push past nostalgia**: End-of-semester reflections can drift into warm feelings. Push for specifics: "You said you learned a lot. What specifically? Name one thing you understand now that you didn't in January."
- **Cross-pollinate across tracks**: "For those who read Fadell, does that match what Torres would say? Where do they disagree?"
- **Name the Evans connection**: If conversations stay in Fadell/Torres territory, bridge to Evans: "What Evans adds here is that boundaries aren't just strategic choices. They're embedded in the language your team uses. Did your language match your boundaries?"

### Prompt-Specific Notes

**Prompt 2 (Language you inherited)** -- This prompt works best when leads can give concrete examples. If they struggle, offer one: "Does 'user' mean the same thing to your client as it does to your team? Does 'done' mean the same thing to your developers as it does to you?" Evans's ubiquitous language concept maps directly to product communication failures they've experienced.

**Prompt 3 (Conviction and evidence)** -- This is the most intellectually demanding prompt. Fadell and Torres genuinely disagree here. Fadell trusts the vision of a skilled builder. Torres trusts the process of structured learning. Neither is wrong. The interesting question is: which one served each lead better this semester, and why? If the group resolves the tension too quickly ("you need both"), push: "Sure, but when they conflicted, which one won? And was that the right call?"

**Prompt 5 (Map between contexts)** -- Evans's context maps describe formal patterns: Shared Kernel, Customer-Supplier, Conformist, Anti-Corruption Layer. You don't need to teach these patterns in the session. But if a lead describes a dynamic that maps to one, name it: "Evans would call that a Customer-Supplier relationship. Your client defines the model and you conform to it. Is that what you want?"

**Prompt 6 (Discovery at the end)** -- This prompt can surface guilt. Leads who know they should have done more discovery work may get defensive. The question about "discovery debt" reframes it: this isn't a moral failing, it's a practical inheritance. What does the next team need to know? This framing makes the conversation productive rather than confessional.

**Prompt 7 (Mentors)** -- Fadell's mentor stories are specific and personal. This prompt asks leads to be specific and personal too. If answers stay generic ("my team taught me a lot"), push: "Who? What did they teach you? What did you believe before that conversation that you don't believe now?"

### Closing: Prompt 8

This is the capstone for the entire Products arc, not just this session. Options:

- **Written reflection** (7-8 min): Give each lead a shared doc or private writing space. The prompt asks them to compare their Week 4 self to their Week 13 self. Written reflection captures this better than spoken discussion because it requires them to commit to specific words.
- **Chat waterfall**: Post Prompt 8, give everyone 3 minutes to type, then everyone hits Enter together. Read a few aloud. Don't comment on them. Let them land.
- **Plenary discussion** (10-15 min): Only if the group has strong energy and trust. This prompt is personal and some leads may not want to share publicly.

**Final closing**: "In one sentence in the chat: what's one thing you'll carry from this semester into whatever you build next?" Screenshot the chat. These are the sentences they'll remember.

### Connecting to the Semester Arc

This is the final Products week. The arc:

- **Week 4**: "Are you building a product or a codebase?" Identity question. Seeds planted.
- **Week 9**: "Can your architecture absorb new learning?" Practice question. Leads working in the middle of the semester.
- **Week 13**: "What have you learned about building products?" Reflection question. Harvest.

The transition from Week 4 to Week 13 should be visible in their answers. In Week 4, some leads couldn't distinguish product from codebase. By Week 13, they should be able to articulate what a product is, where its boundaries are, and what it takes to build one. If they can't, that's data too.

This session also connects forward to **Week 14** (Developing theme, final week of readings). The product leadership reflection here feeds into the broader leadership reflection next week. Consider seeding that connection: "Next week we'll talk about what healthy open source looks like. Today's question about product boundaries feeds directly into that."

### Reading Differentiation

All leads watched the Evans video (35 min). Foundations leads read Fadell; Advanced leads read Torres. This creates a productive tension:

- **Fadell's voice** is the passionate founder. Conviction, storytelling, mentorship, making it tangible. His lens is individual: what did YOU learn, what do YOU believe, who shaped YOUR thinking?
- **Torres's voice** is the disciplined practitioner. Habits, measurement, anti-patterns, sustainability. Her lens is systemic: what processes did your TEAM follow, what outcomes did you MEASURE, what traps did you AVOID?
- **Evans's voice** is the theorist. Boundaries, language, models, maps. His lens is structural: where are the BOUNDARIES, what LANGUAGE do you share, how do the MODELS translate?

All three are necessary. Mixed-track breakout rooms produce the richest conversations because each person brings a different lens to the same questions.

During harvest, if discussion skews toward one source: "For those who read the other book, what does it add here? Where would Fadell push back on Torres, or vice versa?"
