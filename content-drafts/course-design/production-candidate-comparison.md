# Production Candidate Comparison — week-1.html vs week-1-production-candidate.html

**Date:** 19 June 2026
**Purpose:** Direct comparison of the current live Week 1 page against the production candidate, ahead of a decision to replace `week-1.html`.

---

## Page length

**week-1.html:** One continuous scrollable page. Fourteen stacked sections (Start Here, Watch, Learn accordion ×6, Recognise, Reframe, Apply, Integrate, Optional Deeper Dive, Finish, Quick-reference, Resources, Evidence note, Milestone, Scope/Support) plus a persistent two-column sidebar with a focus timer. Desktop scroll depth is roughly 6,000–7,000px; on mobile, considerably more once the sidebar collapses into the main flow.

**Candidate:** Six discrete scenes, only one visible at a time. Each scene is roughly 1–2 viewport heights. The learner never sees a single continuous wall of content — moving between scenes is a deliberate action (Continue button or journey-track tap), not a scroll.

**Verdict:** The candidate is structurally shorter per-screen and impossible to "doomscroll" past without engaging. This is the single biggest difference and the one most directly tied to the founding-beta brief's requirement that the page "must not be a long article."

---

## Interaction frequency

**week-1.html:** Interactive moments are: format switch (3 buttons), 6 accordion toggles, 1 milestone checkbox, a few workbook-prompt textareas (not wired to anything — they're static text blocks with no input field), a focus timer, and two toggles in the sidebar. Most of the page is read-only prose.

**Candidate:** Every scene has at least one structural interaction with saved state: route selection, label selection (8 toggles + focus chip + 2 textareas), EF checkboxes (6), emotion chips (11), Life Review Map (5 progressive steps), Snapshot sentence field, milestone, plus the always-available Snapshot sheet. Interaction density is roughly 4–5× higher, and — critically — interactions in the candidate actually persist to localStorage and feed a visible output; the "workbook prompts" in `week-1.html` are static text with no input at all.

**Verdict:** The candidate is a working tool. `week-1.html`'s "interactions" are mostly inert — the prompts read like exercises but nothing is actually saved anywhere in the current page.

---

## Learner-generated outputs

**week-1.html:** None are actually captured. The page contains a single milestone checkbox and a "Workbook prompt" pattern repeated many times, but none of those prompts have an input field — there is no textarea, no save function, no persisted output. The "Life Review Map" (Section 6) is five steps of static prose with prompt text, again with no actual input field.

**Candidate:** My Week 1 Snapshot — five real, separately-saved fields, auto-populated from earlier scene interactions where possible, editable, copyable, printable, and visible throughout the experience via the lightweight indicator. This is an actual artifact the learner leaves the week with.

**Verdict:** This is the most significant substantive gap between the two pages. The current live page has no mechanism for the learner to produce anything that persists. The candidate's entire structure exists to produce one.

---

## Mobile experience

**week-1.html:** Single column with the sidebar (focus timer, all-milestones, display toggles) pushed below the main content via CSS grid collapse. The page is still one continuous scroll — at 390px width this is a very long page, plausibly 8,000–10,000px of vertical scroll. The accordion helps somewhat by collapsing five of six Learn sections by default, but everything else (Recognise, Reframe, Apply, Integrate, Finish, Quick-reference, Resources) is fully expanded prose.

**Candidate:** Scene-based navigation means mobile is never longer than a single scene at a time — confirmed by Playwright at 390px with no horizontal overflow at any scene. Label grids go 2-column, EF cards stack single-column with icon left, emotion chips wrap, area pills wrap 3-per-row, LRM steps appear one at a time. The Snapshot indicator becomes a fixed bottom pill (not a full panel) consistent with the brief's "no large permanent side panel" instruction.

**Verdict:** The candidate's mobile experience is a different category of design — built for scene-based engagement rather than being a shrunk desktop page. This was the most consistent piece of feedback across the original Playwright audit of `week-1.html` and is directly addressed here.

---

## Visual rhythm

**week-1.html:** Visually monotonous — almost every section is the same `.card` component (cream-tinted rounded rectangle) repeated fourteen times. There is no diagrammatic content; the only visual variety comes from the quick-reference two-column list and the milestone checkbox styling.

**Candidate:** Distinct visual treatment per scene — a timeline SVG diagram in Scene 2, a label grid with reveal panel in Scene 3, six SVG pictograms in Scene 4, colour-coded emotion chips in Scene 5, and a gold-framed Snapshot document in Scene 6. Purple, sage, rose, and gold each carry distinct meaning (route/progress, completion, emotional content, the Snapshot/deliverable) rather than being used decoratively.

**Verdict:** The candidate fulfils the "diagrammatic teaching" and "stronger use of colour for meaning" requirements from the brief; `week-1.html` does not attempt this at all.

---

## Course value (does this look like something worth paying for)

**week-1.html:** Reads as a well-written educational article with a course-platform skin (nav, sidebar, milestone). The actual deliverable promised by the brand ("My Week 1 Snapshot") does not exist as a built artifact on this page — Section 6 ("Apply: The Life Review Map") and the Snapshot concept are described in prose but never actually constructed for the learner.

**Candidate:** Visibly building something throughout — the Snapshot indicator counts up live, the EF summary line updates as areas are checked, the Snapshot document itself is gold-framed and treated as a real document with copy/print actions. This is the structural difference that most directly answers "does this feel like a paid product."

**Verdict:** Strong advantage to the candidate. This was the explicit goal of the redesign.

---

## Cognitive load

**week-1.html:** High in aggregate (very long page) but low per-screen, since most of the page is plain reading with occasional accordions. No interaction-driven branching to track.

**Candidate:** Lower in aggregate (one scene visible at a time) but each scene asks slightly more of the learner — make a selection, write something, watch a count update. The low-capacity toggle, the route choice, and the explicit "you decide how many areas to complete" framing in Scene 6 are the load-management mechanisms built in.

**Verdict:** Roughly a wash, but the candidate's load is *purposeful* (interaction in service of the Snapshot) where the current page's load is *volume* (a lot of text to get through). The low-capacity mode in the candidate is a real toggle with a global effect; `week-1.html`'s "low-capacity" affordance is only the accordion default state.

---

## Emotional pacing

**week-1.html:** The grief/relief/anger content is folded into one accordion item ("Learn 04") alongside everything else, with no distinct emotional check-in moment. The Companion Guide is mentioned twice in passing.

**Candidate:** Scene 5 is a dedicated, distinct emotional beat — chip selection, a dynamic response that adapts to the combination selected (tested live: relief+grief → co-existence message), an explicit pause-and-exit option, and the Companion Guide presented as its own card with a clear inactive state. This matches the wireframe's intent of treating Scene 5 as its own emotional register, separate from the cognitive content of Scenes 2–4.

**Verdict:** Strong advantage to the candidate — this was flagged as a priority in the original wireframing stage and is now built.

---

## Accessibility

**week-1.html:** Decent baseline — `aria-expanded` on accordions, `aria-live` on some counters, keyboard support on milestones, focus-visible outline. No scene-based navigation to test since there are no scenes.

**Candidate:** `role="radiogroup"`/`role="radio"` on routes, `role="checkbox"` on labels/EF/milestone with keyboard handlers (Space/Enter), `aria-live="polite"` on the label counter and EF/emotion summaries, `aria-expanded` on transcript, focus-visible outline preserved, `prefers-reduced-motion` respected (`.reduce-motion` class disables transitions), 44px+ tap targets on chips/cards. Not yet screen-reader tested end-to-end with a real AT (see limitations below) — accessibility attributes are present and structurally correct but haven't been verified with VoiceOver/NVDA.

**Verdict:** Roughly equivalent in rigor; the candidate has more interactive surface area to cover but the same care has been applied. Both need a real screen-reader pass before shipping — this was simulated via DOM/ARIA inspection only, not a live AT session.

---

## Remaining weaknesses (direct)

1. **No real video.** Both pages use a placeholder. The candidate's placeholder is explicit ("Video coming soon") rather than implying the video is live — this is a deliberate improvement, but the gap itself remains until filming happens.
2. **Snapshot Field 2/3 depend on Scene 3 completion.** If a learner skips Scene 3 (e.g. via low-capacity route) and goes straight to Scene 6, Fields 2 and 3 stay empty unless they fill LRM Steps 3–4, which is correct per the interaction model but means the low-capacity route currently produces a thinner Snapshot. This is expected behaviour, not a bug, but worth flagging for beta testing.
3. **Reduced "explain it twice" redundancy is gone.** `week-1.html` has six full prose accordions plus a quick-reference card plus a Companion Guide blurb plus an Evidence note — a lot of restated content. The candidate compresses this considerably, which is the intended effect, but means some of the deeper educational prose from the original page (the full text of "Explanation versus excuse," the narrative-identity deeper dive, the detailed quick-reference card) is not carried over and would need a deliberate decision about where it lives (perhaps the Companion Guide PDF, or an optional "go deeper" link per scene).
4. **No live screen-reader test.** Verified via ARIA roles/attributes and accessibility tree snapshots only.
5. **No automated keyboard-only walkthrough end-to-end** — Tab-order was not exhaustively tested across all six scenes; spot-checked via the existing keyboard handlers in the code (Space/Enter on custom controls).
6. **Print/Copy tested functionally** (no console errors, clipboard API called) but the printed CSS (`@media print`) was not visually proofed against an actual printed page or PDF export.

---

## Direct comparison summary

| Dimension | week-1.html | Production candidate |
|---|---|---|
| Page length | Very long, single scroll | Six short scenes, one at a time |
| Interaction frequency | Low; mostly inert prompts | High; every scene saves state |
| Learner-generated output | None actually captured | Five-field Snapshot, live-building |
| Mobile experience | Long single-column scroll | Scene-based, no overflow, tested 390px |
| Visual rhythm | Repetitive card pattern | Distinct treatment per scene, SVG teaching |
| Course value / paid feel | Reads as an article | Reads as a tool producing a deliverable |
| Cognitive load | High aggregate, low per-screen | Lower aggregate, purposeful per-scene |
| Emotional pacing | Folded into one accordion item | Dedicated scene with dynamic response |
| Accessibility | Solid baseline | Equivalent rigor, larger surface, untested with real AT |
| Founding-beta readiness | Would ship as-is but underdelivers on the brief | Meets the redesign brief; needs video + AT testing before launch |

---

*Comparison complete. See final report for recommendation on next steps before this candidate replaces `week-1.html`.*
