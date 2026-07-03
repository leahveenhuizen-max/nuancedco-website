# Week 1 Production Candidate — Flatness Diagnosis

Reviewed at 1440px and 390px via Playwright, all six scenes, before any edits.

## Headline problem

Every scene uses the same visual unit: a dark ink-deep background, a thin-bordered
rounded box with the same corner radius, the same internal padding, and the same
two type sizes (serif title, body copy). Scene 2 (intellectual teaching), Scene 5
(grief/anger) and Scene 6 (artefact-building) all read as the same template with
different words swapped in. There is no change of background tone, spacing rhythm,
or surface treatment between scenes, so the page reads as one long dark page with
repeating cards rather than six distinct rooms in a guided journey.

## Scene-by-scene

**Scene 1 — Arrival.** Reasonably good bones (two-column layout, route cards,
video frame) but it does not feel premium. The route cards are three identical
boxes with no visual ranking — "Full journey" is the recommended default but
looks identical in weight to the other two. The video frame is a flat gradient
box; "video coming soon" sits in a generic pill. There is no felt sense of
beginning a four-week journey — no Week 1 of 4 marker beyond a small nav line.
No Old Map/New Map visual cue exists despite the text already using the
metaphor ("a map that was already there").

**Scene 2 — Something Changed.** The timeline SVG is the single best asset on
the page (a real diagram), but it sits inside the exact same vertical rhythm as
every other scene — teach-blocks (left-border list) → SVG → quote-block →
recognition-line → reflect-card. It does not feel like a "perspective shift";
it feels like a slightly longer Scene 1 column.

**Scene 3 — The Old Story.** The label grid is the strongest interaction
(distinct grid of words) but the "underneath" reveal is a flat purple-tinted
box, visually identical in family to every other panel on the page (snapshot
fields, companion card, milestone row, etc., all share the same rounded-box
language). There's no felt sense of "uncovering" — no overlay/peel metaphor,
just a panel that appears.

**Scene 4 — How the Brain Manages Life.** This is meant to be the
diagrammatic/explanatory scene but is the flattest of all six: six identical
horizontal rows (icon, copy, checkbox), no grouping, no visual system
explaining how the six EF areas relate to each other or to "managing life."
It is a checklist, not a diagram.

**Scene 5 — Relief, Grief and Anger.** Despite being the emotional core of the
week, it has no slower pacing, no increased whitespace, no softer palette
shift. The emotion chips, response box and companion card use identical
spacing/box treatment to Scene 2's intellectual content. Nothing in the visual
register signals "go slowly here."

**Scene 6 — Build Your Snapshot.** The Life Review Map steps and the Snapshot
document share the same box style as literally every preceding panel. The
Snapshot itself ("snapshot-doc") has a slightly different border colour (gold)
and a soft gradient fill, which is the single best differentiation on the
page — but it still uses plain `<textarea>` fields with no legend/map-key
framing, no sense that this is a finished, exportable artefact rather than
another form to fill in.

## Specific findings against the brief

- **Distinct visual role per scene:** No. All six scenes share one card
  language, one spacing rhythm, one type scale relationship.
- **Opening impact:** Weak. Calm but generic; no strong "Week 1" identity
  beyond text; video placeholder reads as an empty box with a play icon.
- **Scene transitions feel designed:** No. Going from Scene 4 to Scene 5
  (intellectual to emotional) and Scene 5 to 6 (emotional to artefact) produces
  no visual signal of a shift — same dark background, same box widths.
- **Old Map / New Map visible (not just textual):** No. The phrase appears in
  copy (`map-note`, `.snap-intro` "your updated map legend") but there is no
  visual motif anywhere — no path, no line, no marker, no layering of
  old-label vs new-understanding.
- **Visual teaching strength (Scene 4):** Weak. Six identical rows; the
  relationship between executive function areas and "managing life" is not
  shown, only listed.
- **Emotional weight in Scene 5:** Weak. Same box density as everywhere else;
  nothing visually slows the reader down.
- **Snapshot as artefact (Scene 6):** Partial. Gold border + soft gradient is
  a start, but it is still rendered as five identical textareas in a box, not
  as a legend/map-key style document with hierarchy.
- **Mobile vs "long beige scroll":** Confirmed at 390px — vertical stack of
  identical boxes, no scene-to-scene differentiation, snapshot indicator
  pinned at the bottom adds one more flat bar.
- **Card/box reliance:** Very high. Counted reusable rounded-box patterns:
  route-card, teach-block (border-only, not boxed — the one exception),
  reflect-card, reveal-panel, label-card, ef-row, emo-chip/response,
  companion-card, lrm-step, snapshot-doc, milestone-row, catchup-panel,
  week2-preview. At least 10 of these are visually interchangeable
  (`border:1px solid var(--rule2); border-radius:10px; padding:~1rem`).

## Concrete changes needed (used to drive the edit pass)

1. Give each scene a distinct background treatment (radial/linear gradient
   tint using existing palette vars only) so atmosphere shifts scene to scene
   without changing the dark base.
2. Introduce a thin inline-SVG "map line" motif used sparingly: in Scene 1 as
   a faint background path, in Scene 3 as an old-route line with a new marker
   added, in Scene 6 as a legend key style border treatment on the Snapshot.
3. Replace at least half of the repeated `.reflect-card`/`.teach-block` boxes
   in Scenes 2–5 with full-width dividers, inset notes, or borderless editorial
   bands so card density drops noticeably.
4. Restyle Scene 4's EF rows into a more diagrammatic split layout (label +
   short connecting line into explanation) instead of identical repeated rows.
5. Slow Scene 5 down: larger line-height, larger gaps, a single soft rose-tinted
   background wash, fewer simultaneous bordered boxes.
6. Rebuild the Snapshot in Scene 6 with a document/legend header treatment,
   numbered key-style rows, and print-specific polish so it reads as a kept
   artefact, not a form.
7. Improve Scene 1's route cards so "Full journey" reads as the calm default
   and the others as legitimate alternatives, not three equal buttons.
8. Tighten mobile rhythm: more breathing space between scene sections, visual
   scene-start markers, and make sure the fixed snap-indicator and sheet feel
   intentional rather than bolted on.
