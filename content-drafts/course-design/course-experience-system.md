# The Unmasked Life — Course Experience System

The shared design and engineering specification for all four week pages, derived from the Week 1 production candidate (`week-1-production-candidate.html`). This is the reference document for building Weeks 2, 3 and 4 so the course feels like one designed experience rather than four separately built pages.

---

## What stays consistent across all four weeks

- **Six-scene shape:** opening/route-selection scene, two-to-three teaching/interaction scenes, one feelings/emotional-response scene, one closing/output-assembly scene.
- **Three routes per week:** Full Journey (all scenes, ~45 minutes), Low-Capacity (one scene at a time, simplified framing, under 10 minutes each), Speed-Read (core concepts only, ~5 minutes). Route choice is remembered but can be changed mid-week without losing saved progress.
- **Resume behaviour:** on reload, the learner lands on the opening scene with a "Continue where you left off" prompt naming the scene they were last in, plus a "Start over" option that clears that week's data with a confirmation step.
- **The "Leah moment" pattern:** an icon, "A note from Leah" label, one or two sentences of context, and an honest placeholder state ("Audio placeholder — not yet recorded") until the real media exists. Never silently omit this pattern — show the placeholder rather than nothing.
- **The output/Snapshot pattern:** five fields, always visible via a lightweight indicator, auto-populated from scene interactions where possible, manually editable (overrides win over auto-computed values), copyable to clipboard, printable via a dedicated print stylesheet.
- **The milestone:** one honest, non-performative completion marker per week, phrased as recognition ("I have identified...") rather than achievement ("I have completed...").
- **The weekly catch-up panel:** consistent structure (what to bring, sharing is optional language, date/link fields, scope note linking to `support.html`).
- **The "Coming in Week N+1" preview block** at the end of each week, linking to the next week's page.
- **The footer disclaimer:** "educational... not clinical advice, diagnosis, or treatment" framing, present on every week page.
- **The evidence/scope note pattern:** every week states plainly that this is "educational content delivered by a neurodivergent consultant and registered nurse," never therapy or clinical advice, with a link to `support.html`.

## What changes by week

- **Content, labels, and reflection prompts** — entirely week-specific.
- **Visual metaphor** — Week 1: the map. Week 2: the mask. Weeks 3 and 4: to be defined when those weeks are planned (suggested direction: Week 3 could use a toolkit/environment metaphor; Week 4 could use a compass/foundation metaphor, but this is not yet confirmed).
- **Colour accent** — see below.
- **Emotion set in the feelings scene** — tuned to that week's themes (Week 1: relief/grief/anger/numbness around diagnosis; Week 2: shame/disorientation/relief/grief around unmasking; Weeks 3-4 TBD).
- **Output/Snapshot title and fields** — see learner outputs below.
- **The interaction types in the teaching scenes** — reuse the same *patterns* (selectable cards with reveal panels, checklist-style toggles with running summaries, progressive-unlock multi-step worksheets) but with week-specific content.

### Weekly learner outputs

| Week | Output name |
|---|---|
| 1 | My Week 1 Snapshot |
| 2 | My Masking and Self-Blame Map |
| 3 | My Support Needs Map |
| 4 | My Self-Trust and Next Steps Plan |

Each output keeps the same five-field, indicator/sheet/inline pattern established in Week 1, with field labels and count text (e.g. "X of 5") adjusted to the week's content.

---

## Shared navigation pattern

- Sticky top nav: logo, "Week N of 4" label, "Need support" link to `support.html`. Identical across all weeks except the week number.
- Journey track immediately below nav: a horizontal row of dot-and-label nodes, one per scene, with done/active states. Tapping a label jumps directly to that scene (this works in Week 1 regardless of route, and should remain available in all weeks rather than gated behind "Full Journey only").
- Scene-level "Continue" / "← Back" buttons at the bottom of every scene, plus a final scene that ends in "Back to dashboard" rather than "Continue."

## Shared Snapshot/output pattern

- A fixed pill indicator ("My Snapshot — X of 5" or week-appropriate label), top-right on desktop (under the nav, not overlapping it), fixed bottom pill on mobile (≤760px).
- Clicking the indicator opens a slide-in sheet (right edge on desktop, bottom sheet on mobile) containing all five fields, a Copy button, and a Print button. The sheet is not a permanent side panel — it must be dismissible and closed by default.
- The same five fields are also editable inline in the closing scene, with overrides written to distinct `localStorage` keys so manual edits are never silently overwritten by auto-computed values.

## Weekly colour accent guidance

Each week should have a distinct primary accent within the existing ink/cream/gold/purple/sage/rose palette, so the four weeks feel like a connected set rather than identical pages:

- **Week 1:** lilac/purple (`--lilac` / `--purple`) — already established for "the map," diagnosis, recognition.
- **Week 2:** rose (`--rose`) — already present in the palette for emotional/shame-adjacent content; recommended as Week 2's primary accent given the masking/self-blame theme, replacing lilac as the *primary* interactive colour for that week (lilac can remain for shared chrome like the journey track).
- **Week 3:** sage (`--sage`) — already used for "done" states and support-oriented language; fits a practical, support-and-environment theme.
- **Week 4:** gold (`--gold`) — already used for premium/Companion Guide framing; fits a closing, "what you're keeping forward" theme.

This is a recommendation, not a locked decision — confirm with Leah before Week 2 build begins, since it affects every interactive element's colour in that week's CSS.

## Shared video placement

- One lesson video per week, placed in the opening scene, using the same `.video-frame` component (16:9, gradient overlay, play button, video pill, chapter labels, transcript toggle). Target length 10-15 minutes per the existing video scripts.
- One or two shorter "Leah moment" audio/video notes within the week, placed at emotionally significant transition points (Week 1 places these at the opening, before the feelings scene, and at the closing — this rhythm should repeat).

## Shared Companion Guide pattern

- One Companion Guide per week, introduced in the feelings scene (or wherever the week's heaviest content lands), framed as optional and deeper, explicitly "included in the full course, not free as a standalone." Card shows title, one-sentence description, and an availability state ("Available in Resources" once linked).

## Shared weekly catch-up panel

- Placed in the closing scene. Contains: a heading naming the week's catch-up question, 2-3 bulleted prompts to bring, a note that sharing is optional and listening-only participation is welcome, a date/join-link line (placeholder until confirmed), and the scope note linking to `support.html`.

## Shared evidence/scope note

Every week's closing scene includes: "This is educational content delivered by a neurodivergent consultant and registered nurse. It is not therapy or clinical advice." with a link to `support.html`. This exact phrasing (or a minimal week-specific variant) should not drift between weeks.

---

## localStorage naming conventions

Each week uses its own namespace prefix to avoid collisions and to make "start over" scoped correctly per week:

- Week 1: `tul-w1-*` (established in the candidate)
- Week 2: `tul-w2-*`
- Week 3: `tul-w3-*`
- Week 4: `tul-w4-*`

Within each namespace, keep the same key-naming pattern Week 1 established: `current-scene`, `visited-<scene>`, `route`, `lowcap`, `milestone`, `last-saved`, plus content-specific keys per scene, plus `<field>-override` keys for manually edited Snapshot/output fields. "Start over" should only ever clear keys matching that week's own prefix — never another week's data.

## Mobile-first rules

- No horizontal scroll at any viewport, tested down to 390px.
- Grids that are 3-4 columns on desktop collapse to 1-2 columns by 760px (label grids, EF rows already follow this in Week 1 and should be the template).
- The Snapshot/output indicator must convert from a floating top-right pill to a fixed bottom pill at ≤760px, and scenes must reserve bottom padding (~5.5rem) so the fixed pill never overlaps content.
- Sheets/panels that are side-anchored on desktop become bottom sheets on mobile, never full-screen takeovers that hide the close control.

## Accessibility rules

- All custom interactive elements (label cards, route cards, EF checkboxes, milestone row) must have appropriate ARIA roles (`role="radio"`, `role="checkbox"`, `radiogroup`, etc.), `aria-checked` state, and `tabindex="0"` plus `keydown` handlers for Space/Enter activation — confirmed working in Week 1 via direct keyboard testing.
- `:focus-visible` must remain visibly styled (Week 1 uses a 2px lilac outline) — do not remove focus rings for visual polish reasons.
- `prefers-reduced-motion` must be respected: when the OS setting is on, apply a `reduce-motion` class to `<body>` that disables all transitions/animations, including the smooth-scroll behaviour on scene change. This is implemented in Week 1 and should be copied verbatim into each week's script.
- Live regions (`aria-live="polite"` or `"assertive"`) should be used for dynamically updated text the learner needs to be told about without re-reading the whole scene (label counts, save confirmations, completion messages) — already the pattern in Week 1.

## What to avoid across all weeks

- Long, single-scroll pages with no interaction (the exact problem Week 1's rebuild solved) — every week must use the scene-based pattern, not a return to the old accordion-and-prose format.
- Static "workbook prompts" with no actual input field — every prompt that asks the learner something must have a real textarea or selectable control behind it.
- Permanent, large side panels — the Snapshot/output pattern must stay a dismissible sheet, not a persistent sidebar.
- Describing any week's substantive educational content (lessons, Companion Guides, Life Review-style maps) as free — Companion Guides remain $29 AUD paid items; the course as a whole has its own pricing/access model, which this experience layer does not change.
- Disallowed terms or framings: "ADHD coach," "psychologist," "psychology-led treatment," "counselling course," "therapy programme," "clinical course," or describing Leah as anything other than "Neurodivergent consultant, Registered nurse, Mental health educator."
- Em dashes and emojis in any learner-facing copy (the existing candidate correctly uses commas/parentheses instead of em dashes — keep this convention in new weeks).
- Diagnosing, re-diagnosing, or questioning a participant's diagnosis; recommending specific medications or treatments; or promising the course will "fix" anything — consistent with the video scripts' explicit scope notes.
