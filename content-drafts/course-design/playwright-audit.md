# Playwright Visual Audit — Week 1: The Late Diagnosis Disruption
**Date:** 19 June 2026  
**Audited by:** Claude Code via Playwright MCP  
**Files inspected:** `week-1.html`, `week-1-experience-prototype.html`  
**Screenshots:** `content-drafts/course-design/browser-audit/`

---

## TASK 1 — Visual Inspection of Current Page (`week-1.html`)

### Visual hierarchy

The page has a clear typographic scale — serif headline, body copy, labelled cards — but no single dominant moment. Everything competes at similar visual weight. The sidebar exists and is functionally useful but creates a split-attention layout from the very first scroll. On desktop, the learner's eye has no place to land. There is a large-title heading ("The Late Diagnosis Disruption") and a wall of copy before anything else happens visually.

The accordion labels ("LEARN 01", "LEARN 02") function as navigation but read as bureaucratic tags, not emotional invitations. The workbook prompts (purple-bordered boxes) are the only distinct visual element, but by the third one they have become wallpaper.

### First impression

The opening viewport on desktop is: nav bar, eyebrow label, serif headline, a "Start here" card, a video placeholder with a play button floating in a dark rectangle, and a sidebar full of checkboxes and a timer. It reads as a well-designed admin panel for a course, not the opening of an emotional or intellectually significant learning experience. The first thing a learner sees after reading the title is a paragraph explaining they do not need to complete everything today. That is a necessary caveat but it is not an opening.

There is no sense of arrival. Nothing signals that what follows is worth the learner's attention or money.

### Content density

Very high throughout. The full page is approximately 14,400px tall on desktop. Six accordion sections each contain three to five paragraphs. The Reframe section contains three subsections of prose separated by horizontal rules. The Life Review Map contains five stepped prompts. The resource area repeats content already shown in context. The Quick Reference Card adds another full block. The evidence note, milestone, scope block, and week navigation all follow.

The page contains enough content for a short book chapter. The problem is not that the content is wrong — the writing is good — but that the page makes no editorial decision about what matters most.

### Section rhythm

The rhythm is: card → video → mode strip → six accordions → card → card → card → accordion → card → card → card → card → card → card → navigation. Every section uses the same card or accordion container. There is no visual rhythm variation, no moment of quiet, no section that looks or feels meaningfully different from any other. The learner cannot orient themselves by feel — everything has the same texture.

### Scanability

Poor. On first pass, a learner skimming this page cannot identify: what they are supposed to do, in what order, what will take time and what is optional, or what the single most important thing on this page is. The card labels ("Start here", "Recognise", "Reframe", "Apply", "Integrate", "Finish") are the closest thing to a learning path but they are visually identical to every other card label and easy to miss when scanning vertically.

### Proportion of text to interaction

Approximately 85% dense prose and 15% interactive elements. The interactive elements present (accordion open/close, milestone tick, focus timer, format switch, transcript toggle) are either decorative or peripheral to the learning. None of them produce learner-generated output that matters. The workbook prompts look interactive but are not — they display a question with no writing surface. The learner is being asked to mentally engage with content they cannot act on within the page.

### Dead space

Almost none on desktop, which is itself a problem. The page is relentlessly dense. On mobile, the experience is even more compressed with no visual breathing room. Where the page could have used space to signal transition or weight, it instead stacks another card.

### Repetitive visual patterns

The purple workbook prompt box (border-left: 3px solid var(--purple), slightly tinted background) appears at least 10 times across the page. By the fourth or fifth occurrence it has lost all signal value. The learner no longer knows why this visual treatment is being used — it was originally signalling a question worth pausing on, but by the second card it means "more text in a box."

Similarly, the section label pattern (small uppercase lilac text, icon, text) appears on approximately 18 separate elements on the page. The icon set (info circle, magnifying glass, rotate, map, checkered flag, vault, bookmark, flag, pen) adds variety but the label treatment reads the same regardless of icon.

### Whether the learner knows where they are

They know they are on "Week 1 of 4" from the eyebrow and the sidebar. They do not know where they are *within* the week, because the page is a single vertical scroll with no persistent stage indicator. The accordion section "LEARN 01 through 06" implies a sequence but the closed accordions obscure whether the learner has engaged with them or not.

### Whether the learner knows what to do next

No. After reading the Start Here card and watching/ignoring the video, the accordion section opens automatically on "Learn 01". The learner reads it. It closes when they open "Learn 02". By "Learn 03" the pattern is clear but by "Learn 04" it is fatiguing. After Learn 06 closes, there is no clear signal that the learning mode has shifted — a new card labelled "Recognise" appears, but it looks identical to the previous content cards. The pace and direction of the page is not visible to the learner.

### Where attention is likely to drop

1. Immediately after the "Start here" card — the video placeholder with no content is a dead end. There is nothing to watch. The format switch (Video / Speed-read / Audio) signals three options but one is a dark rectangle and two are hidden.
2. After "Learn 03 — Identity disruption". By this point the learner has read significant emotional content and the accordion texture has become uniform.
3. The "Recognise" card — three stacked workbook prompt boxes with no writing surface, following six accordions of reading. This is peak passive density.
4. The "Apply: Life Review Map" section — the stepped prompts are well structured but the workbook-prompt visual treatment (with no actual textarea) makes them look the same as everything that came before.

### Whether the page feels premium

No. It is polished — the typography is beautiful, the colour system is coherent, the dark background is appropriate. But polish is not premium. Premium is the feeling that someone designed this specifically for you, that the pace was considered, that what is shown first was chosen deliberately. This page feels like a well-formatted knowledge dump. It is dense in the way a good Notion document is dense: well-organised information, not a designed experience.

### Whether it feels like a course, article, email or digital workbook

It reads most like a long-form article or a Notion page formatted as a course. The accordion sections are the closest thing to "course structure" but they are also just a common way of organising long-form web content. It does not feel like a course because there is no sense of progression, no designed moment where the learner does something that matters, and no output at the end that represents the learner's own thinking.

### Desktop vs tablet vs mobile differences

**Desktop (1280px):** Two-column layout (main content + sidebar). The sidebar contains milestones, a Pomodoro timer, display controls, and a "Hit a wall?" card. These are genuinely useful but they fragment the learner's attention. The sidebar follows the scroll and is always visible, which means the learner is always aware of the timer and the unchecked milestone boxes — both can induce anxiety in neurodivergent learners.

**Tablet (768px):** Single-column, sidebar stacks below. This is better for focus but the sidebar content (timer, milestones) is now buried at the bottom of a ~14,000px page. A learner on tablet would never find the timer unless they scrolled to the end.

**Mobile (390px):** The hamburger menu replaces the nav. The page is a single column with aggressive density — the card/accordion cards stack with very little spacing variation. The mobile page is approximately 18,000–20,000px tall when fully loaded. There is no mobile-specific simplification. A learner in a neurodivergent moment of low capacity opening this page on mobile would see the same density they would see on desktop, just narrower. This is a significant accessibility failure for the stated audience.

### Whether mobile is too long or too repetitive

Yes, on both counts. The page length on mobile is excessive for a learner who may have low attention stamina. The visual pattern repetition is worse on mobile because the sidebar visual variety (timer, milestones as separate components) is no longer breaking up the text. On mobile the page is: card, video, buttons, six accordions, five more cards, one more accordion, six more cards. The workbook prompt box — the same purple-tinted bordered element — appears more than ten times in this single-column flow.

### Whether current interactions support learning or decorate content

They decorate content. The interactions present are:
- **Accordion open/close:** Organises reading, creates no output.
- **Format switch (Video/Speed-read/Audio):** Useful concept, but in practice switches to content that is identical in tone and length. Speed-read is just prose without accordion structure.
- **Transcript toggle:** No transcript exists yet.
- **Focus timer (Pomodoro):** Genuinely useful tool, but it is a generic timer with no relation to the content. It could appear on any page.
- **Milestone tick:** Decorative at this stage — the single Week 1 milestone is not connected to anything the learner has done on the page.
- **Workbook prompts:** Display questions only. No writing surface. The learner is asked to reflect with no way to capture the reflection.
- **Display toggles (focus mode, reduce motion):** Useful accessibility controls, but buried in the sidebar.

None of these create a learner output. None mark a moment of genuine engagement. None ask the learner to produce something they did not have when they arrived.

---

## THE VERDICT: WHY THIS PAGE STILL FEELS FLAT DESPITE BEING POLISHED

The fundamental problem is that the page treats good writing as sufficient experience design.

The content is genuinely good. The prose is clear, appropriately careful, emotionally attuned. The structure (understand → recognise → reframe → apply → integrate) is educationally sound. The accessibility features show real consideration.

But good writing arranged in cards is not a learning experience. It is a reading experience. And a reading experience that asks a learner to pay for it, to return to it across four weeks, to describe it as a course — that has a credibility problem.

**The page is flat because:**

1. **It has no designed moments.** Nothing on this page was built to stop the learner and say: *this is the moment that matters*. The pull quote in the prototype was a step toward this. The current page has no equivalent. Everything is equally weighted, which means nothing is weighted at all.

2. **It produces no learner output.** The workbook prompts are the right instinct but they present questions with no writing surface. The Life Review Map is structured beautifully but the "prompts" are non-interactive display elements. A learner who reads every word, opens every accordion, and reaches the milestone tick has nothing to show for it. No evidence of their own thinking. Nothing to carry forward.

3. **It has no emotional pacing.** This content deals with grief, identity disruption, and self-blame. These are not topics that should flow at the same tempo as an executive function explainer. The page does not vary its pace based on emotional weight. Heavy content and practical tools appear at identical volume.

4. **The sidebar creates a management mindset.** The Pomodoro timer and the unchecked milestone boxes signal to the learner that they are in an administrative task. They are tracking their progress through a module, not inhabiting an experience. This is the wrong feeling for this content.

5. **The visual system cannot carry the brand alone.** The dark background, serif font, purple system, and subtle gradients are beautiful. But they are applied consistently rather than purposefully. The visual system says "this is premium" in a generic sense — it says the same thing on every card, every prompt, every section label. A premium experience uses visual language to signal *this specific moment* matters, not just that the brand is sophisticated.

---

## TASK 3 — Comparison: Current Page vs Prototype

### What improved in the prototype

- **Opening.** The prototype's header is genuinely better. The title is large, alone, given space. The lead paragraph ("A late ADHD diagnosis does not just add a label. It arrives inside a life already built...") is visible above the fold without competing with a sidebar or video placeholder. First impression is more editorial, more considered.

- **Stage navigation.** The seven-dot lesson map (Watch → Understand → Recognise → Reframe → Apply → Integrate → Complete) gives the learner a sense of journey. It is small and could be made more prominent, but the concept is correct.

- **Teaching sections as flowing prose.** Removing the accordion in favour of continuous editorial headings makes the Understand section read like a considered essay rather than a FAQ. The learner is pulled through the thinking rather than choosing which boxes to open.

- **Recognition cards (selectable).** The 2×4 grid of selectable pattern cards is the single most important UX improvement in the prototype. It is the first moment on either page where the learner *does* something — they select patterns that feel familiar. This is low-effort, emotionally safe, and genuinely useful for self-understanding. It produces a micro-output (which cards are selected) and creates a sense of being seen.

- **Before/After Reframe pairs.** Visually showing "what you may have been told" alongside "a more accurate understanding" is cleaner and more emotionally direct than the prose-only reframe sections in the current page.

- **Life Review Map with textarea.** The prototype's LRM has actual textareas. The learner can type. The responses save to localStorage. This is not yet a meaningful output (it lives only in the browser) but it is the correct architectural decision.

- **Low-capacity mode toggle.** Correctly identifies that the neurodivergent learner audience needs a genuine simplification mode, not just a focus toggle that hides the sidebar.

- **Single-column editorial column.** Removing the sidebar entirely creates focus. The learner is reading, not managing.

- **Milestone takeaway input.** Asking "What am I taking with me from this week?" with a textarea at the close is a better ending than a tick-box alone. It asks the learner to produce a sentence.

### What remained fundamentally unchanged

- **The content volume.** The prototype is still extremely long. It explicitly notes in its prototype annotations that concepts 4–6 are not shown to keep the page readable — which means the production version would be even longer.

- **The absence of designed moments.** The recognition cards are the closest thing to a designed moment in the prototype, but the executive function diagram (a flex-wrap of labelled boxes) is not a visual teaching tool — it is a list formatted as a diagram. There is still no moment where the page does something the learner did not expect.

- **The pull quote pattern.** The prototype uses pull quotes, which are the right instinct, but the quotes are from the course content itself rather than from research sources, real experiences, or named voices. They read as self-referential.

- **No video.** Both pages are built around a video that does not exist. The entire content architecture assumes a video lesson as the primary consumption mode but neither page has one. The design cannot be fairly evaluated without knowing the video's role, length, or tone.

- **No learner identity or personalisation.** Both pages begin with the same content for every learner regardless of where they are in their diagnosis journey, what emotional state they are in, or what they have said they need.

### Where the prototype still relies on cards, panels and article-style scrolling

The prototype's recognition section uses cards. The callout companion block uses a card. The Life Review Map uses bordered step panels. The option cards for integration use bordered selectable elements. The milestone uses a bordered container. The "Coming in Week 2" block uses a bordered panel. The prototype replaced the accordion with prose — that is an improvement — but it replaced cards with slightly lighter-weight cards. The fundamental language is still: text in boxes, stacked vertically, read by scrolling down.

The prototype is editorial in its text sections and card-grid in its interactive sections. This creates a visual inconsistency — you are reading a long-form essay and then suddenly presented with a UX pattern. This is not wrong, but it is not resolved.

### Whether the interactions create meaningful learner outputs

**Recognition cards:** Yes, marginally. The learner selects items, sees a count, and the selections are saved. But the selections are not referenced again — they don't feed into the Life Review Map, they don't generate a personalised reflection, they don't create anything the learner can reference later or share.

**Life Review Map textarea:** Yes, but only if the learner actually types. The textarea is there. The save-to-localStorage behaviour is correct. But there is no prompt to export, print, or use this output — it lives only in the current browser and disappears if the browser data is cleared.

**Integration option cards:** No. Selecting Option A, B, or C produces a "Option A chosen" confirmation. This is not an output.

**Milestone takeaway textarea:** Yes, the best output on either page. A single sentence or paragraph that the learner writes about what they are taking with them. This is the most correct instinct in the prototype.

**Overall:** The prototype produces two meaningful outputs — the recognition card selections and the takeaway text. The current page produces zero. The prototype wins on this dimension, but neither page produces an output substantial enough to justify calling this a course.

### Whether the visual system is memorable

The colour system is distinctive. Dark background, cream, purple, lilac, sage — this is unusual for the healthcare-adjacent psychoeducation space, which is typically light, pastel, or clinical. The serif/sans-serif combination is elegant. The system is memorable in the sense that you would recognise it as "the Nuanced Co. aesthetic."

But the visual system is not *expressive*. It does not do different things in different moments. It does not get quieter when the content is heavy or bolder when a concept needs emphasis. It applies the same treatment to a grief prompt and a resource download link. The aesthetic is distinctive; the visual communication is not.

### Whether the learner experience justifies a paid course

**Current page:** No. The content justifies a paid course. The experience does not. The current page is an excellently written web article with accordion navigation and a sidebar timer. A learner who paid for this would feel they had received good information — they would not feel they had received a course.

**Prototype:** Getting closer but not yet. The recognition cards and the narrative prose sections represent genuine experience improvements. The Life Review Map with textareas represents the right architecture. But the prototype is still a reading experience with some interaction layered in. It does not yet feel like it was designed specifically for a late-diagnosed ADHD adult navigating emotionally significant content. It feels like it was designed for an intelligent reader who prefers good editorial design — which is different.

**What is still missing in both:** Designed emotional moments. Pacing variation. Genuine learner output that has value beyond the page. A reason to come back. The sense that this week has changed something specific, not just informed something general.

---

*Audit complete. No files modified.*
