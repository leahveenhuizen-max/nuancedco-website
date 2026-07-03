# Week 1 Mobile Flow
**Date:** 19 June 2026  
**Purpose:** Define the mobile-specific experience for Week 1 — not a compressed desktop, but a designed mobile journey  
**Primary viewport:** 390px wide (iPhone 14 baseline)  
**Secondary viewports:** 375px (SE), 414px (Plus), 430px (Pro Max)  
**Target:** Single scene per visible screen area, no 20,000px scroll

---

## The core mobile problem with the current page

The current `week-1.html` on mobile is a single vertical scroll of approximately 18,000–20,000px. The learner opens it, sees a wall of text, and has no sense of how much is left, what matters most, or when they are done. For a learner with ADHD and potentially low cognitive capacity at the moment of opening, this is hostile.

The solution is not to cut content. It is to change the scrolling model: **each scene fills one mobile viewport** and contains **one primary action**. The learner scrolls within a scene but not across the full week in one continuous scroll.

---

## Mobile scrolling model

**Within a scene:** Normal vertical scroll. Each scene is designed to fit comfortably within 1.5–3 viewport heights (1,266px–2,532px). Some scenes have more content (Scene 6 LRM) but the progressive unlock model means the learner never sees it all at once.

**Between scenes:** Scene transition is a full-screen slide or fade (CSS), not a continuous scroll. The learner knows they have moved to something new.

**Result:** The page total scroll length on mobile is distributed across six scene transitions. No single scene exceeds ~3 scroll lengths. The learner always knows where they are.

---

## Mobile navigation pattern

### Sticky minimal nav bar (top)
```
┌─────────────────────────────────────────────────────────┐
│  [Logo — small]   Week 1: The Late Diagnosis Disruption  │
│                        ⚑ Need support                   │
└─────────────────────────────────────────────────────────┘
```
- Height: 48px
- Logo: text only, links to course-dashboard.html
- "Need support" link: always visible, right-aligned, small
- No hamburger menu during lesson — full nav unnecessary on lesson page
- Safe area: `env(safe-area-inset-top)` padding on iOS

### Progress strip (below nav, sticky)
```
┌─────────────────────────────────────────────────────────┐
│  ●  ○  ○  ○  ○  ○                                      │
│  Arrive                                                  │
└─────────────────────────────────────────────────────────┘
```
- 6 dots, 8px diameter, 12px gap
- Active dot filled; completed dots filled (different style); future dots hollow
- Scene name shown only for active dot, below the strip
- Strip height: 36px total
- Tapping a completed dot: scrolls to that scene top (or shows that scene in scene-based model)

### Bottom sticky CTA (visible in each scene)
```
┌─────────────────────────────────────────────────────────┐
│  [Continue to [Next Scene Name] →]                      │
│  — or —                                                  │
│  [Save and pause]  [Continue →]   (Scene 5 only)        │
└─────────────────────────────────────────────────────────┘
```
- Appears after the learner has completed the primary action in the scene
- Before completion: CTA is visible but shows "Complete the activity above to continue" (not disabled — still tapable, which shows a gentle "Finish this section first" prompt)
- Height: 56px tap target
- Safe area: `env(safe-area-inset-bottom)` padding
- Semi-transparent blur background so content scrolling behind it remains readable

---

## Screen sequence

### Screen 1: Arrive — opening (top of Scene 1)

**Content visible in first viewport:**
- Sticky nav (48px)
- Progress strip (36px)
- Week tag: "Week 1 of 4 — The Unmasked Life™"
- H1: "The Late Diagnosis Disruption" (large, ~2.4rem)
- Lead paragraph (3 lines)
- Time estimate
- Bottom: Video placeholder starts

**Content below fold (scroll within Scene 1):**
- Video placeholder full width
- Three route cards stacked
- Resume block (if returning)
- Permission note
- Support link

**Bottom CTA:** "Choose a route to continue" → appears after a route is selected → "Continue to Something Changed →"

**Approximate scene height:** 1,800px

---

### Screen 2: Arrive — route choice

**This is not a separate screen** — it is below the fold on Screen 1. On low-cap mode, route choice can be surfaced as the *first* visible element after the title.

**Three route cards (stacked, full width):**
```
┌─────────────────────────────────────────────────────────┐
│  Full journey                                           │
│  All six scenes · ~45 min                              │
│  [→]                                                    │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│  Low-capacity route                                     │
│  One scene at a time · under 10 min each               │
│  [→]                                                    │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│  Speed-read                                             │
│  Core concepts only · 5 min                            │
│  [→]                                                    │
└─────────────────────────────────────────────────────────┘
```
- Tap target height: 72px minimum per card
- Selected card: highlighted border, tick in top-right corner
- After selection: sticky CTA transitions from "Choose a route" to "Continue to Something Changed →"

---

### Screen 3: Something Changed

**Content:**
- Scene separator strip at top: "○●○○○○ Something Changed"
- H2: "What late diagnosis actually does"
- Teaching prose: 3 short paragraphs (~300 words total)
- Timeline visual: horizontal scrollable if needed, or vertical list on narrow viewports
- Prose continuation: 1–2 paragraphs
- Textarea interaction: "What feels different now that you know?"
- Save button
- Save confirmation
- Pull quote (after save)

**Key mobile decisions:**
- Teaching prose: max-width 100%, font-size 1rem, line-height 1.75
- Timeline visual: if horizontal scroll needed, show "scroll →" hint; alternative is a simple vertical list with arrows
- Textarea: `min-height: 96px`, auto-expand
- Save button: full-width, 48px tall

**Bottom CTA:** "Continue to The Old Story →" (appears after save; also visible immediately as "skip" fallback)

**Approximate scene height:** 2,200px

---

### Screen 4: The Old Story

**Sequence of reveal on mobile (progressive, not all-visible at once):**

**Step 1: Label grid**
- Header + teaching prose (2 short paragraphs)
- 2-column grid of 8 label cards
- Counter: "N of 8 selected"
- "Step 2" button: appears after ≥ 1 selected

```
┌──────────────────┐ ┌──────────────────┐
│  lazy            │ │  inconsistent    │
└──────────────────┘ └──────────────────┘
┌──────────────────┐ ┌──────────────────┐
│  careless        │ │  too sensitive   │
└──────────────────┘ └──────────────────┘
[etc. × 8]
```
Card height: 56px. Tap target entire card. Selected state: border highlight.

**Step 2: Focus selector**
- "Which one do you want to look at this week?"
- Chips showing only selected labels (smaller than the Step 1 grid, row of chips)
- After tap: Step 3 reveals below

**Step 3: Reveal panel**
- Full-width card with three sections:
  - WHAT PEOPLE MAY HAVE SEEN
  - WHAT MAY HAVE BEEN HAPPENING UNDERNEATH
  - SUPPORT THAT MAY HAVE HELPED
- Each section: label (small caps) + 2–3 sentences

**Step 4: Learner's own words (two textareas)**
- Textarea 1: "How do you understand this label now?"
- Textarea 2: "What support might have helped?"
- Save button (full-width)

**Bottom CTA:** "Continue to How the Brain Manages Life →"

**Approximate scene height (all steps):** 3,200px (but progressive — learner never sees all 3,200px at once)

---

### Screen 5: Executive Function (Mobile)

**Decision:** Cards are **single column, full width** on mobile. No grid.

```
┌─────────────────────────────────────────────────────────┐
│  TASK INITIATION                                        │
│  Getting started on things you intend to do.            │
│  For example: writing the email you've had open         │
│  for two days.                                          │
│  [☐] Does this show up for you?                         │
└─────────────────────────────────────────────────────────┘
[... × 6 cards]
```

- Card height on mobile: ~100px per card
- Checkbox: visible at bottom of card, right-aligned, 44×44px tap area
- After any checkbox tapped: counter appears below last card: "N areas recognised"
- Research note accordion: below all cards, collapsed

**Bottom CTA:** "Continue to Relief, Grief and Anger →"

**Approximate scene height:** 1,800px (all 6 cards + prose + response)

---

### Screen 6: Relief, Grief and Anger (Mobile)

**Emotion chips on mobile:** 2 per row, each chip full-half-width (~185px), 44px tall

```
[Relief]        [Grief]
[Anger]         [Numbness]
[Confusion]     [Gratitude]
[Exhaustion]    [Sadness]
[Hope]          [Nothing yet]
[Something I don't have a word for]  ← full width
```

- Dynamic response: appears as a card below the chip grid after first selection
- Pause block: below dynamic response, always visible
- Companion Guide callout: below pause block, labelled "Optional"
- Support link: below callout

**Critical mobile design:** Pause button must be large and unambiguous. "Save and pause for now" — full width, 52px tall, clearly distinct from Continue.

**Bottom CTA:** "Continue to Build Your Snapshot →" | "Save and pause"

**Approximate scene height:** 2,000px

---

### Screens 7–8: Build Your Snapshot and Milestone (Mobile)

**This scene is the most complex on mobile. The solution is strict progressive disclosure.**

**Step A: Life area selector**
```
[School]    [Work]      [Relationships]
[Home]      [Health]    [Money]
[Identity]
```
- 3 chips per row where space allows, else 2
- After tap: LRM Step 1 appears below

**Step B: LRM Step 1 only**
Full-width textarea, "Save and go to Step 2" button. Steps 2–5 hidden.

**Step C: LRM Steps 2–5**
Each step appears as learner saves the previous. Only one step visible at a time. "Step 2 of 5" label above each textarea.

Back navigation: "← Step 1" link above current step.

**Step D: My Week 1 Snapshot**
Appears after Step 1 minimum is completed.

```
┌─────────────────────────────────────────────────────────┐
│  MY WEEK 1 SNAPSHOT                                     │
│  The Unmasked Life™ · Week 1                           │
│                                                         │
│  OLD LABEL                                              │
│  [Content or placeholder]           [Edit]              │
│                                                         │
│  WHAT MAY HAVE BEEN HAPPENING                           │
│  [Content or placeholder]           [Edit]              │
│                                                         │
│  SUPPORT THEN                                           │
│  [Content or placeholder]           [Edit]              │
│                                                         │
│  SUPPORT NOW                                            │
│  [Content or placeholder]           [Edit]              │
│                                                         │
│  ONE SENTENCE I WANT TO KEEP                            │
│  [Textarea — write here]                                │
│                                                         │
│  [Save Snapshot]                                        │
│  [Copy to clipboard]                                    │
│  [Print / save as PDF]                                  │
└─────────────────────────────────────────────────────────┘
```

**Milestone block:**
```
┌─────────────────────────────────────────────────────────┐
│  ◯  I have identified at least one pattern from my past │
│     that I am now seeing differently.                   │
│  Tick when it feels true. There is no deadline.         │
└─────────────────────────────────────────────────────────┘
```
Large tap target, centred.

**Beta session panel:** Full-width card below milestone.

**Week 2 preview:** Minimal card, small text, link to week-2.html.

**Approximate scene height (full LRM + Snapshot + closing):** 4,800px (but distributed across multiple progressive reveals — learner never sees it all at once)

---

## Progress display on mobile

The 6-dot strip is always visible. Behaviour:

| Scene | Dot state |
|---|---|
| Before visiting | Hollow (○) |
| Currently active | Filled/highlighted (●) |
| Completed (any save made) | Filled with completion indicator (✓ or different fill) |
| Milestone ticked | All 6 dots show completed state |

Dot label below active dot only. Prevents the strip from feeling crowded.

---

## Back and next behaviour

**Next ("Continue →"):**
- Sticky bottom CTA
- Smooth transition to next scene (CSS slide or fade)
- Updates `tul-w1-current-scene` in localStorage

**Back:**
- Tap any completed dot in the progress strip → returns to that scene
- In LRM step sequence: "← Step N" link above current step (not a full scene transition — just step navigation within Scene 6)
- Back to previous scene: arrow or link below the scene header — visible but not prominent (learner should rarely need to go back)

**No browser back button dependency:** Learner should be able to navigate entirely within the page without using the browser's back button.

---

## Resume behaviour

On page load:
1. Check `tul-w1-current-scene`
2. If it exists: show Resume block at the top of Scene 1 (scroll to it, or show as an interstitial) — "You were working on [Scene Name]. Resume?"
3. If not: begin at Scene 1 as normal

On resume:
- Scroll/transition to saved scene
- Restore all field values from localStorage
- Show "Last saved: [relative time]" near any textarea

---

## Low-capacity behaviour

When `tul-w1-lowcap: true`:

| Scene | Low-cap behaviour |
|---|---|
| 1 | Route B selected automatically; time estimate shows 10 min/scene |
| 2 | Teaching prose condensed to 2 paragraphs; textarea optional; "Skip for now" visible |
| 3 | Label grid shown; single textarea only; reveal panel hidden unless learner taps "Tell me more" |
| 4 | Single EF radio button (pick one) instead of 6 checkboxes |
| 5 | 4 emotion options only; no dynamic response text (just an affirming sentence) |
| 6 | Life area pre-selected to "Identity"; LRM Step 1 only shown; Snapshot fields pre-labelled with placeholders the learner can ignore |

Low-cap mode is toggleable at any scene. State persists across sessions. Toggling off shows full content, but previously skipped content remains optional.

---

## Content length per scene (mobile)

These are design targets, not hard limits.

| Scene | Max words on screen at once | Total scene words |
|---|---|---|
| 1 (Arrive) | 80 words visible above fold | ~250 |
| 2 (Something Changed) | 120 words before interaction | ~350 |
| 3 (Old Story) | Teaching: 80 words; Reveal panel: 120 words | ~400 |
| 4 (Brain) | Per card: 40 words | ~280 total across 6 cards |
| 5 (Feelings) | Teaching: 80 words; Response: 60 words | ~200 |
| 6 (Snapshot) | LRM per step: 60 words | ~300 prose + learner text |

No scene should require the learner to read more than 400 words of prose. All prompts should be one question long.

---

## Interaction targets on mobile

All interactive elements:
- Minimum tap target: 44×44px (WCAG 2.5.5)
- Minimum tap target spacing: 8px gap between adjacent targets
- No tap targets in the bottom 20px of the screen (accidental home-gesture area on iOS)
- All textareas: minimum 96px tall, font-size 16px or larger (prevents iOS auto-zoom)
- Chip/card labels: readable at 14px minimum, prefer 16px

---

## Safe area spacing

- `padding-top: env(safe-area-inset-top)` on nav
- `padding-bottom: env(safe-area-inset-bottom)` on sticky bottom CTA
- `padding-left: env(safe-area-inset-left)` and `padding-right: env(safe-area-inset-right)` on full-width content
- Standard left/right content padding: 20px (inside safe areas)

---

## Print and save behaviour on mobile

**Copy to clipboard:**
- `navigator.clipboard.writeText()` with formatted Snapshot text
- Fallback: textarea with text pre-selected and "Long-press to copy" instruction
- iOS share sheet option: triggered by Web Share API if available (`navigator.share()`)

**Print / save as PDF:**
- `window.print()` with `@media print` CSS:
  - Hide nav, progress strip, bottom CTA, all buttons
  - Show only Snapshot content
  - Black text on white background
  - Font size 12pt minimum
  - Add "The Unmasked Life™ — Week 1 Snapshot" header to print output
- On iOS: Print triggers system print dialog which includes "Save to PDF" option
- On Android: Chrome print includes "Save to PDF" option

---

## How to avoid a 20,000-pixel page

The current page is long because all content exists in the DOM simultaneously. The mobile solution uses two techniques:

**Option A — Scene-based content loading (preferred for production):**
Only the active scene's content is in the DOM (or visible). Other scenes are hidden via `display: none` or rendered only on navigate. This dramatically reduces the effective scroll length.

Implementation:
```js
function navigateToScene(sceneId) {
  document.querySelectorAll('.scene').forEach(s => s.hidden = true);
  document.getElementById(sceneId).hidden = false;
  window.scrollTo(0, 0);
  updateProgressStrip(sceneId);
  saveCurrentScene(sceneId);
}
```

**Option B — Scroll anchoring with section reveals (simpler, acceptable for beta):**
All scenes in the DOM but subsequent scenes hidden until the previous one is completed. CSS transition on reveal. Scroll is anchored to the active scene. This is less clean than Option A but requires less JS architecture for the beta.

**Recommendation:** Option B for beta (simpler to implement, easier to test), Option A for production.

---

## What the mobile experience must never do

- Show the sidebar (there is no sidebar)
- Show the Pomodoro timer during lesson content
- Auto-advance to the next scene without learner input
- Present more than one required question at once
- Use a font size below 16px in inputs (causes iOS auto-zoom, which is disorienting for ND users)
- Require the learner to scroll past more than 3 viewport lengths before reaching the primary action
- Present the full 6-scene page as a single continuous scroll (the current failure mode)

---

*Mobile flow complete. All measurements are design targets for implementation.*
