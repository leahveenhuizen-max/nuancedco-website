# Week 1 Visual Concept Comparison

**Date:** 19 June 2026
**Purpose:** Compare three visual directions for the Week 1 redesign of The Unmasked Life, ahead of choosing one to carry into production HTML.
**Inputs:** `_concept-a-quiet-editorial.html`, `_concept-b-guided-journey.html`, `_concept-c-warm-studio.html` — inspected live via local server + Playwright at desktop (1280×900) and mobile (390×844) widths. Screenshots in `adobe-express-concepts/`.

---

## Important clarification on method

**Adobe Express MCP was not used to produce these three boards.** The original brief asked for "Adobe Express visual concept boards." What was actually built is three static, fixed-canvas HTML documents, each containing 4–5 desktop slides and 1–2 mobile slides, styled with the brand's actual Adobe Fonts kit (Cormorant Garamond + Atkinson Hyperlegible Next) and real Week 1 content.

Why HTML instead of Express:
- Express's own design surface is built around single-canvas, drag-and-drop layout. Producing three genuinely different *interactive, responsive, multi-breakpoint* concepts — with hover/selected states, accordions, a 6-scene progress track, SVG-based visual teaching elements, and mobile-specific layouts — is something HTML/CSS expresses far more accurately than a static design tool, where this would have to be faked as flat artwork.
- Each concept needed to demonstrate *behaviour* (chip selection states, route cards, low-capacity toggle, accordion reveal) — not just colour and layout. That is a coding problem, not an Express layout problem.
- These HTML files were exportable to Adobe Express via `export_html_to_express` (the tool was loaded and ready), but exporting was paused — see recommendation below.

These three HTML files should be treated as **visual concept boards**, not production prototypes. They are deliberately disposable scaffolding to make a design decision, not code intended to ship. None of `week-1.html`, `nc-course.css`, or any production file was touched to build them.

**Should an Adobe Express export still happen?** Marginal value only. Express would flatten these into static slides, losing the interactive states that are part of what's being evaluated (chip selection, card hover, accordion reveal). An export is useful only if Leah specifically wants an Express file to comment on or share with someone outside the coding environment — it adds no design information beyond what the screenshots already show. Recommend skipping unless there's a specific external-sharing reason.

---

## How the three concepts differ structurally

This is not a colour/font/border-radius exercise — each concept makes different decisions about layout, hierarchy, navigation, and interaction model:

| Dimension | A — Quiet Editorial | B — Guided Visual Journey | C — Warm Interactive Studio |
|---|---|---|---|
| Background | `#0D0A08` — coldest, almost black | `#2A1F1A` — standard warm ink | `#1A1512` — warmest, most saturated brown |
| Typography texture | Cormorant Garamond everywhere — one voice throughout | Cormorant for H1/H2 only; Atkinson for everything else — two voices | Atkinson leads almost everywhere; Cormorant reserved for H1 + Snapshot text only |
| Structural device | Hairline rules only — no card surfaces anywhere | Horizontal 6-node journey track, persistent under nav | Two-column "workspace" with Snapshot panel visible from Scene 1 |
| Interaction surface | Text-only options separated by rules, no boxes | Card surfaces with backgrounds + borders, selected state = lilac fill | Card surfaces + Gold-framed Snapshot document, Purple-tinted interactive zones |
| Visual teaching | Single-line SVG timeline, dot markers only | Multi-track SVG timeline (time × life areas) + 6 SVG EF pictograms | Border-draw selection treatment on Old Story labels + live-building Snapshot panel |
| Navigation model | Dot progress strip only, resume via text link | Persistent journey track with named nodes, Resume/Start Over buttons | Progress dots + always-visible Snapshot status ("Field 1 saved · 4 fields remaining") |
| Mobile treatment | Single column, video collapses above text, routes stack as text list | Condensed track at top, 2-col card grid preserved from desktop | Same 2-col card grid as B, but Snapshot status bar pinned near bottom |
| Emotional tone | Austere, literary, slow — almost gallery-like | Reassuring, wayfinding-led — "you can see where you are" | Personal and tactile — "you are building something as you go" |

---

## Assessment by concept

### Concept A — Quiet Editorial

- **Visual distinctiveness:** Very high. The coldest palette and complete absence of card surfaces make it instantly recognisable against the other two.
- **Emotional fit:** Strong for the *reflective* register of Week 1 content (disruption, identity), but risks feeling distant or under-warm for an audience that may already feel alienated.
- **Premium feel:** High — reads like a considered editorial product, not a course platform.
- **Learning clarity:** Good for linear reading; weaker for showing *progress* or *state* since there's no visual feedback for selections beyond colour change on text.
- **Visual teaching quality:** Lowest of the three — the single-line timeline and lack of EF pictograms mean most teaching is still carried by prose.
- **Learner-generated output strength:** Present but visually minimal — the Snapshot is a quiet hairline-bordered block, consistent with the aesthetic but less satisfying as a "thing you made."
- **Mobile suitability:** Excellent — the minimal aesthetic translates cleanly to a single column with no compromise.
- **Accessibility:** Strong contrast (cream on near-black), but text-only selection states may be harder to scan for low-capacity or visually-fatigued users — no shape/colour redundancy beyond underline.
- **Cognitive load:** Lowest — very little on screen at once.
- **Implementation complexity:** Lowest — mostly typography and rules, few component states to build.
- **Scalability across Weeks 2–4:** Easy to extend, but the lack of structural variety could make four weeks feel monotonous without deliberate content-level variation.
- **Risk of feeling like an article:** Highest of the three. This is the concept most likely to be perceived as "just reading," despite the interactions technically being there.
- **Suitability for founding beta:** Good but risky — elegant, but doesn't visually signal "paid course product" as strongly as B or C.

### Concept B — Guided Visual Journey

- **Visual distinctiveness:** High — the persistent journey track is a structural signature no other concept has.
- **Emotional fit:** Strong — track + nodes give a constant, gentle sense of "you are somewhere, and that's fine," which suits an ADHD audience that benefits from external structure.
- **Premium feel:** High — card-based interactions and SVG pictograms read as deliberately designed software, not a document.
- **Learning clarity:** Best of the three — the multi-track timeline and EF pictograms do real explanatory work that prose alone wouldn't.
- **Visual teaching quality:** Highest — two distinct, well-executed visual teaching devices (timeline diagram, EF icon grid).
- **Learner-generated output strength:** Strong — the assembling Snapshot preview next to the Life Review Map step flow makes the output feel like it's being built in front of the learner.
- **Mobile suitability:** Strong — track condenses sensibly, 2-col grid holds up at 390px.
- **Accessibility:** Card surfaces give shape + colour + position redundancy for state (better than text-only). Track requires labels to remain legible at small sizes — confirmed legible in the mobile screenshot.
- **Cognitive load:** Medium — more visible structure than A, but organised, not cluttered.
- **Implementation complexity:** Highest of the three — track component, multi-track SVG, six pictograms, card state system all need building and maintaining.
- **Scalability across Weeks 2–4:** Very good — the track is designed to extend (more nodes/weeks), and the card system is reusable for any future selection-based interaction.
- **Risk of feeling like an article:** Lowest — the track and cards make it feel like a tool being used, not a page being read.
- **Suitability for founding beta:** Strongest single concept on paid-product feel and teaching clarity, at the cost of the most build time.

### Concept C — Warm Interactive Studio

- **Visual distinctiveness:** High — the two-column "workspace" with a live Snapshot panel is unique to this concept and not present in A or B's opening scene.
- **Emotional fit:** Strong, different register from B — feels personal and private ("your workspace") rather than guided ("your journey"). Likely to land well with learners who want agency rather than wayfinding.
- **Premium feel:** High — the Gold-framed Snapshot document gives the deliverable physical weight from the very first scene, which neither A nor B does.
- **Learning clarity:** Good — slightly less explicit visual teaching than B (no equivalent to the EF pictogram grid or multi-track timeline), relying more on the border-draw selection treatment and live Snapshot assembly.
- **Visual teaching quality:** Medium — strong in one place (Snapshot-building visualisation) but thinner elsewhere compared to B.
- **Learner-generated output strength:** Highest of the three — the Snapshot is visible and partially populated from Scene 1 onward, not just revealed at the end, so the sense of "building something" is present throughout, not just at the close.
- **Mobile suitability:** Strong — matches B's 2-col grid approach, adds a persistent Snapshot status bar that survives the move to mobile well.
- **Accessibility:** Similar profile to B (card-based, colour + position redundancy). Warmest background gives slightly lower contrast headroom than A or B — worth a contrast-ratio check before build.
- **Cognitive load:** Medium-high — the always-visible Snapshot panel is informative but is one more thing on screen than B's opening scene.
- **Implementation complexity:** Medium — fewer custom SVG diagrams than B, but the persistent live-updating Snapshot panel is its own non-trivial state-management problem.
- **Scalability across Weeks 2–4:** Good — the workspace metaphor and live Snapshot panel extend naturally if later weeks also produce a document-like output.
- **Risk of feeling like an article:** Low — the visible workspace and Snapshot panel keep it feeling like a tool.
- **Suitability for founding beta:** Strong, particularly because it makes the paid deliverable (the Snapshot) feel valuable from the first scene, which directly supports the "this is worth paying for" goal.

---

## Direct comparison table

| Criterion | A — Quiet Editorial | B — Guided Journey | C — Warm Studio |
|---|---|---|---|
| Visual distinctiveness | High | High | High |
| Emotional fit for audience | Medium-high (cool, literary) | High (structured, reassuring) | High (personal, agency-led) |
| Premium feel | High | High | High |
| Learning clarity | Medium | High | Medium-high |
| Visual teaching quality | Low | High | Medium |
| Learner-output strength | Medium | High | Highest |
| Mobile suitability | High | High | High |
| Accessibility | Medium-high | High | Medium-high |
| Cognitive load | Lowest | Medium | Medium-high |
| Implementation complexity | Lowest | Highest | Medium |
| Scalability Weeks 2–4 | Medium | High | High |
| Risk of feeling like an article | Highest | Lowest | Low |
| Founding-beta suitability | Good | Strongest on teaching | Strongest on deliverable value |

---

*Comparison complete. See recommendation in `beta-build-priorities.md` companion discussion and the final report delivered alongside this document.*
