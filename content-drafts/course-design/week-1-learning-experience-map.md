# Week 1 Learning Experience Map
## The Unmasked Life — Nuanced Co.

**Status:** Session 2 audit output — for Leah review before implementation
**File context:** Companion to `week-1-experience-prototype.html`
**Audit date:** June 2026
**Do not implement directly:** This is a design planning document. The prototype file demonstrates the recommended direction.

---

## Audit Findings: Current week-1.html

### What the current page does well
- All content is present and accurate
- Scope and evidence notes are correctly positioned
- Resource disambiguation (Life Review Map, Late Diagnosis Life Review, Companion Guide) is clear
- Sidebar milestone system works correctly
- Reduce-motion and keyboard navigation are supported
- The 14-section structure covers the right ground

### What is not working as a learning experience

**1. Accordions are the primary delivery mechanism**
Six "Learn" accordions hide all of the week's teaching content. A learner opening the page sees six identical grey boxes labelled "Learn 01" through "Learn 06" with chevrons. There is no way to scan what the lesson covers, no sense of the intellectual journey, and no visual relief. The content is good. It is just invisible until clicked.

**2. All elements carry the same visual weight**
Cards, accordions, workbook prompts, the QR card, the resource section, the evidence note, and the milestone all use the same visual density and treatment. There are no visual landmarks, no moments of emphasis, and no rhythm changes. The learner cannot tell which part of the page matters most.

**3. There is no sense of "where am I in this lesson?"**
The page has 14 logical sections, but no in-page navigation, no progress indicator visible in the content flow, and no visual separation that signals section transitions. A learner who pauses mid-lesson has no easy way to orient on return.

**4. Workbook prompts are passive**
The `.workbook-prompt` component is a styled box containing a question. Learners are expected to write elsewhere (paper, another device, a note app). There is no in-page writing surface. This is a low-friction expectation for a paid course that is partly designed as a workbook experience.

**5. The Recognise section is structurally invisible**
The "Recognise" section (Section 4) is three workbook prompts inside a card. It does not function as a recognition experience. It reads as more prompts after the accordion content. The learner has no way to select patterns that resonate, see their responses reflected back, or feel the recognition land.

**6. The Reframe section is three sub-headings inside one card**
Three reframe concepts (grief + relief co-exist, grief vs self-pity, missing support) are packed into a single card with horizontal rules separating them. They do not breathe. The emotional content deserves more visual space.

**7. Integration options are visually identical to other cards**
The three integration options (A, B, C) are styled identically to other content. A learner cannot quickly identify the call to action. The section does not feel like a decision point.

**8. The QR card, resources, evidence note, and milestone appear consecutively at the bottom**
After the main content ends, the learner encounters: QR card, resources card, evidence note, milestone card, scope block, and week navigation in sequence. This is a dead zone with no sense of closing or transition. The milestone (the most meaningful moment of the week) is buried fifth from the bottom.

**9. No visual rest between teaching and reflection**
The page moves from accordion (teaching) directly to card (recognition) directly to card (reframe) without a visual break or transition. Neurodivergent learners benefit from visible pacing signals. There are none.

**10. Mobile scroll length**
The current page, at 940 lines, produces an estimated 6,000-8,000px of scroll on mobile. The navigation sidebar collapses at 1100px. On mobile, there is no progress reference at all.

---

## Design Principles for the Rebuild

These are the principles the prototype is built around. They should govern all subsequent week rebuilds.

1. **Teaching flows as readable prose, not as hidden accordion content.** Accordions are reserved for: optional deeper dives, transcripts, supplementary references, extra examples, support resources.

2. **Visual rhythm must vary.** Teaching text, pull quotes, visual diagrams, recognition interactions, and workbook surfaces alternate. No two consecutive elements of the same type.

3. **Every section must be visible from scroll position.** Section titles, section numbers, and a top-level lesson map must be visible so a learner can orient at any point.

4. **Interactive elements must be rewarding.** Recognition cards are selectable. The Life Review Map has in-page text inputs. Integration options are radio-selectable. These are small interactions that signal "this is for you, not at you."

5. **The milestone is the emotional close of the lesson.** It belongs at the end of the main teaching sequence, not buried beneath resources and QR cards. Resources and supplementary content follow, but the milestone should close the learning arc.

6. **Low-capacity mode is a first-class option.** A persistent banner lets learners switch to a simplified view: teaching prose only, prompts hidden, video + speed-read + milestone only visible. This is not a separate page. It is a CSS class applied to the existing page.

7. **The Companion Guide is a contextual callout within the reframe section.** It should appear where the emotional content is densest, not in a resource card at the bottom of the page.

8. **Premium means breathing room.** Section padding should be generous (not tight). Pull quotes should have their own line. The page should feel like a well-designed book, not a LMS template.

---

## Learner Journey Map

The following table maps each stage of the learner's experience through Week 1.

### Stage 1: Arrive and Orient

| | |
|---|---|
| **Learner goal** | Know what this week is about and feel welcome to begin |
| **Core content** | Week title, brief paragraph framing the week, lesson map showing all sections |
| **Interaction** | Format chooser (video / speed-read / audio-only) |
| **Visual component** | Lesson map: horizontal strip or numbered list of all 8 learning stages, visible at the top |
| **Approximate time** | 1-2 minutes |
| **Essential?** | Yes |
| **Emotional load** | Low — orientation only |
| **Low-capacity alternative** | None needed — this is the entry point |
| **Mobile behaviour** | Lesson map collapses to compact icon strip |
| **Progress signal** | Stage 1 of 8 highlighted |
| **Output / takeaway** | Learner knows what is coming |

### Stage 2: Watch (or read / listen)

| | |
|---|---|
| **Learner goal** | Receive the week's introduction through their preferred format |
| **Core content** | Video embed with caption toggle, speed-read summary, audio-only note |
| **Interaction** | Format switch (Video / Speed-read / Audio-only) |
| **Visual component** | Video player with visible captions indicator |
| **Approximate time** | 10-15 min video; 4-5 min speed-read |
| **Essential?** | Yes (one format) |
| **Emotional load** | Low to moderate |
| **Low-capacity alternative** | Speed-read is the low-capacity format; 4-minute read |
| **Mobile behaviour** | Video is full-width; speed-read panel fills viewport |
| **Progress signal** | Stage 2 of 8 |
| **Output / takeaway** | Introduction to week themes; curiosity activated |

### Stage 3: Understand (teaching)

| | |
|---|---|
| **Learner goal** | Understand the six core concepts of the week |
| **Core content** | Six teaching sections as prose: (1) What late diagnosis does, (2) The retroactive review, (3) Identity disruption, (4) Emotional landscape, (5) Executive function, (6) Explanation vs excuse |
| **Interaction** | Pull quotes as full-width emphasis breaks; one in-line workbook prompt per section |
| **Visual component** | Section separators with section number; pull quote at large serif type; visual diagram of executive function (HTML/CSS only) |
| **Approximate time** | 20-30 minutes |
| **Essential?** | Yes |
| **Emotional load** | Moderate to high in sections 3 and 4 |
| **Low-capacity alternative** | Low-capacity mode shows a collapsed summary of each section rather than full prose |
| **Mobile behaviour** | Single-column, max-width constrained, large leading |
| **Progress signal** | Stage 3 of 8; sub-progress within teaching (concept 1/6 through 6/6) |
| **Output / takeaway** | Named understanding of late diagnosis disruption, retroactive review, identity shift, emotional response, executive function, explanation vs excuse |

### Stage 4: Recognise

| | |
|---|---|
| **Learner goal** | See themselves in the content; feel seen |
| **Core content** | "Does this sound like you?" — 8-10 pattern cards |
| **Interaction** | Cards are tappable / clickable to select; selection is saved in localStorage; count shown ("You selected 4 of 10") |
| **Visual component** | 2-column card grid on desktop; single column on mobile; selected cards show subtle glow/border change |
| **Approximate time** | 3-5 minutes |
| **Essential?** | Yes — recognition is a core psychoeducational function of the week |
| **Emotional load** | Moderate — recognition can be both relief and grief |
| **Low-capacity alternative** | Cards still visible; selection still works; no prompt to reflect aloud |
| **Mobile behaviour** | Single column, cards tappable |
| **Progress signal** | Stage 4 of 8 |
| **Output / takeaway** | Named self-recognition; groundwork for the reframe |

### Stage 5: Reframe

| | |
|---|---|
| **Learner goal** | Shift from old-story labels to more accurate understanding |
| **Core content** | Three reframe concepts, each with prose + a paired before/after visual |
| **Interaction** | Old story / new understanding pairing — two boxes side by side; Companion Guide callout in context |
| **Visual component** | Before/after pair: left box "What you were told" (subtle dimmer treatment); right box "What is more accurate" (slight warm border); Companion Guide callout card in purple |
| **Approximate time** | 5-8 minutes |
| **Essential?** | Yes |
| **Emotional load** | High for some learners (grief concepts) |
| **Low-capacity alternative** | Prose only; before/after boxes still visible but compact |
| **Mobile behaviour** | Before/after pair stacks vertically |
| **Progress signal** | Stage 5 of 8 |
| **Output / takeaway** | At least one reframe named; grief vs self-pity distinction understood |

### Stage 6: Apply (The Life Review Map)

| | |
|---|---|
| **Learner goal** | Apply the week's understanding to a specific moment in their own life |
| **Core content** | The Life Review Map (5 steps) |
| **Interaction** | Each step has a visible prompt and a textarea for in-page writing (saved to localStorage); "Save responses" button; "Print my responses" option |
| **Visual component** | Stepped form: step counter (1 of 5) with progress line; each step on its own visual block; completion checkmark per step |
| **Approximate time** | 10-20 minutes |
| **Essential?** | No — clearly marked as "take as long as you need; one step is enough to begin" |
| **Emotional load** | Moderate to high — applying the life review to real memories |
| **Low-capacity alternative** | "Start with Step 1 only" option visible; remaining steps collapsed by default in low-capacity mode |
| **Mobile behaviour** | Single column; textareas full-width |
| **Progress signal** | Stage 6 of 8 |
| **Output / takeaway** | At least one past pattern named with old and new explanation |

### Stage 7: Integrate

| | |
|---|---|
| **Learner goal** | Choose one action to take this week |
| **Core content** | Three integration options (A, B, C) |
| **Interaction** | Radio-select (choose one); selection saves to localStorage; brief confirmation ("You chose Option B") |
| **Visual component** | Three option cards, visually distinct from teaching cards; selected option highlights |
| **Approximate time** | 1-2 minutes |
| **Essential?** | Yes — this is the "what I am doing with this" close |
| **Emotional load** | Low — this is a decision, not an emotional stretch |
| **Low-capacity alternative** | Options still visible; selection still works |
| **Mobile behaviour** | Single column; full-width |
| **Progress signal** | Stage 7 of 8 |
| **Output / takeaway** | Named intention for the week |

### Stage 8: Complete (Milestone + Closing)

| | |
|---|---|
| **Learner goal** | Acknowledge what has been done; feel the lesson close |
| **Core content** | Week 1 summary (what was covered), milestone text and tick, closing sentence from Leah, link to Week 2 |
| **Interaction** | Milestone tick (localStorage-synced with sidebar); "What I am taking with me" short-answer field (optional, localStorage) |
| **Visual component** | Milestone section with generous white space above it; summary list in a lighter style; "What is next" teaser |
| **Approximate time** | 2-3 minutes |
| **Essential?** | Yes — the milestone is the emotional close |
| **Emotional load** | Low — this is a completion moment |
| **Low-capacity alternative** | Same — milestone is always visible |
| **Mobile behaviour** | Full-width; large milestone text |
| **Progress signal** | Stage 8 of 8 — complete |
| **Output / takeaway** | Milestone ticked (if true); personal note saved; Week 2 previewed |

---

## Three Design Concepts

### Concept A: Editorial Journey

**Description:** The lesson flows as editorial long-form content, structured like a well-designed magazine or book chapter. Teaching sections flow as prose in a comfortable reading column. Key insights are pulled out as large-type pull quotes. Visual interest comes from typographic hierarchy and horizontal section breaks, not from components. Accordions are reserved for supplementary content only.

**Visual character:** Dark editorial. Serif headings at variable sizes. Cream on near-black. Section breaks as thin horizontal rules with a small section label above them. Pull quotes at ~1.6rem Cormorant Garamond, full reading width. Cards used only for contained, discrete items (quick-reference, resources, milestone).

**Interaction level:** Low to moderate. Recognition cards are selectable. Life Review Map has in-page textareas. Integration options are radio-selectable. No animations beyond subtle transitions.

**Build complexity:** Medium. Requires restructuring the HTML section by section; no new JS beyond what exists. New CSS components: pull-quote, section-separator, recognition-card (selected state), before/after pair, stepped form.

**Beta-essential?** Yes. This is the base level of what the course needs to feel like a paid course.

**Accessibility:** Strong. Prose-first, keyboard-navigable interactions, no animation dependencies. Reduce-motion fully compatible.

**Risk:** Requires significant HTML restructuring. The current week-1.html would be substantially rewritten (not altered — fully replaced with the new structure).

---

### Concept B: Guided Interactive Workbook

**Description:** The lesson is structured as a workbook the learner moves through step by step. Each stage has a visible number, a brief teaching intro, and an interactive element. Learners "check off" each stage (optional) before moving forward. The primary metaphor is a structured personal document they are building, not content they are consuming.

**Visual character:** Warmer, more tactile. Slight paper texture via CSS background pattern. Each workbook section has a subtle left border accent (colour-coded by section type). Handwriting-feel prompt labels.

**Interaction level:** High. Step completion tracking, in-page writing throughout, selectable options, Life Review Map fully embedded.

**Build complexity:** High. Requires new JS for step management, completion state, print-to-PDF styling.

**Beta-essential?** No. This is a phase-two enhancement.

**Accessibility:** Medium. Step-by-step navigation requires keyboard management. Skip-to-content patterns essential.

**Risk:** Higher complexity increases maintenance cost and testing overhead. More likely to break on edge-case browsers.

---

### Concept C: Modular Learning Studio

**Description:** The lesson is divided into modules. The left side shows a fixed module navigator. The main area shows one module at a time (not a long scroll, but a section-swap pattern). Each module fills the viewport. Navigation between modules is smooth.

**Visual character:** Modern course platform. More structured, less editorial. Closer to Notion or a custom LMS than a magazine.

**Interaction level:** High. Single-page application feel; section transitions; module completion tracked.

**Build complexity:** Very high. Requires a custom JS router, animated section transitions, persistent state. Closest to a framework application using vanilla JS.

**Beta-essential?** No. This is a phase-three concept that belongs post-funding.

**Accessibility:** Complex. Section transitions must be managed for screen readers. Focus management per-section required.

**Risk:** Very high for a static HTML platform. Cannot be implemented without significant JS refactoring across all week pages. Not appropriate for beta.

---

## Recommendation: Concept A — Editorial Journey

**Reasons:**

1. It solves the core problem (content hidden behind accordions, no visual pacing, flat hierarchy) without adding new technical dependencies.
2. It works on all browsers, all devices, with and without JS (graceful degradation).
3. It aligns with the brand's aesthetic (editorial, calm, adult, premium) more naturally than the workbook or studio concepts.
4. It is the fastest path from current state to a course that feels premium — structural HTML + CSS changes only, no new JS architecture.
5. It scales cleanly to Weeks 2, 3, and 4 using the same section template.
6. The interactive elements (recognition cards, Life Review form, integration options) are achievable as progressive enhancement in vanilla JS within the current architecture.
7. It is accessible by default.

**What it requires:**
- A new HTML section template (demonstrated in the prototype)
- Three new CSS component classes: `.pull-quote`, `.section-sep`, `.recognition-card`, `.before-after`, `.lrm-step`
- These new classes must be added to `nc-course.css` in a future session (the design system tokens remain locked; only new component classes are added)
- The week-1.html must be rebuilt from scratch using the new template (not edited patch-by-patch)

---

## Interactive Components: Build List

| Component | Description | Complexity | Beta-essential? |
|---|---|---|---|
| Section separator with label | `<div class="section-sep">` — horizontal rule with section number and title above | Low | Yes |
| Pull quote | `<blockquote class="pull-quote">` — large serif type, full reading width, generous vertical space | Low | Yes |
| Recognition card (selectable) | `.recognition-card` — tappable; `.selected` class applied on click; count displayed | Low | Yes |
| Before/after pair | `.before-after` — two divs side by side; "What you were told" + "What is more accurate" | Low | Yes |
| In-page Life Review Map | `<form>` with styled `<textarea>` inputs per step; step counter; save to localStorage | Medium | Yes |
| Integration option selector | Three `.option-card` elements with radio-select behaviour; localStorage | Low | Yes |
| Companion Guide callout in context | `.callout-companion` — styled callout card within the Reframe section | Low | Yes |
| Low-capacity mode toggle | Persistent banner: `body.low-capacity` CSS class; hides `.hide-low-cap` elements | Low | Yes |
| In-page lesson map | Strip of 8 numbered sections at the top; active section highlighted on scroll | Medium | No (Phase 2) |
| "Print my Life Review" | Print stylesheet for Life Review Map responses | Low | No (Phase 2) |
| Scroll-progress sub-indicator | Shows concept 1/6 through 6/6 within the teaching section | Medium | No (Phase 2) |
| Session-save banner | Notification that responses are saved to this browser session | Low | Yes |

---

## What the Prototype Demonstrates

The prototype (`week-1-experience-prototype.html`) demonstrates all beta-essential components in a working HTML file:

- Opening orientation with lesson map
- Format chooser (non-functional placeholder; demonstrates layout)
- Two teaching sections as editorial prose with section separators and pull quotes
- Executive function concept diagram (pure HTML/CSS)
- Recognition cards (selectable, count displayed)
- Before/after reframe pair
- Companion Guide callout in context
- Life Review Map Step 1 (functional textarea, saved to localStorage)
- Low-capacity mode toggle (functional)
- Integration option selector (functional)
- Closing milestone interaction (functional)
- Mobile layout (responsive)

The prototype does NOT include:
- Navigation (nav, sidebar, footer) from the current week-1.html
- The full six teaching concepts (demonstrates two, with structure for all six)
- All five Life Review Map steps (demonstrates Step 1)
- Transcript, speed-read panel, audio mode (demonstrates layout placeholder)
- Real video embed (placeholder)
- The QR card, resources section, or evidence note (documented but not prototyped)
- Scope block or week navigation links

---

## Files

| File | Purpose |
|---|---|
| `week-1-experience-prototype.html` | Working HTML prototype demonstrating Concept A |
| `content-drafts/course-design/week-1-learning-experience-map.md` | This document |
| `week-1.html` | Current production file — not altered in this session |
| `nc-course.css` | Current design system — not altered in this session |

---

*Document created Session 2, June 2026. For Leah review. Do not implement before reviewing the prototype and confirming the design direction.*
