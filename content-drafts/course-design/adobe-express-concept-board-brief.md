# Adobe Express Concept Board Brief
**Date:** 19 June 2026  
**Stage:** Visual direction (Stage 2 — after wireframe review)  
**Tool:** Adobe Express  
**Purpose:** Three visually distinct concept boards to define the visual language for the Week 1 redesign before any production HTML is written  
**Constraint:** Do not create these until wireframes are reviewed and approved. This document is the brief, not the output.

---

## Ground rules for all three concepts

- Each concept must be visually distinct. Not recoloured versions of one layout.
- Each board shows the same three moments: Week 1 opening, the recognition interaction, and the Snapshot closing.
- Greyscale structural wireframes are separate (already completed). These boards are for visual direction, not layout specification.
- Adobe Express is used for visual direction only — not to simulate a full responsive interface.
- The Nuanced Co. design tokens (cream, ink-deep, purple, lilac, sage, rose, serif/sans-serif) may be used in all three, but may be applied differently.

---

## What each concept board should contain

Three screens per concept (nine boards total):

**Board A:** Week 1 opening — first impression, route choice visual  
**Board B:** The Old Story interaction — label cards, reveal panel, reframe  
**Board C:** The Snapshot — assembled output, milestone close, beta session panel

Each board should be sized at 1280×900px (desktop first) with a 390×844px mobile detail inset.

---

## Concept 1: Quiet Editorial

**Character:**
Restrained, literary, unhurried. Modelled on long-form editorial design — a thoughtful magazine or essay-form digital publication. The experience feels handcrafted and considered.

**Typography character:**
- Cormorant Garamond leads. Body text is generous. Serif headlines are large and have breathing room.
- Body text line-height: 1.8–2.0 — longer than typical web
- No uppercase tracking on headings — sentence case everywhere
- Pull quotes use italic Cormorant at large scale, nearly full-column width
- Section markers: hairline rules and small numerals, nothing more

**Colour balance:**
- Ink-deep (#0F0C0A) background throughout
- Cream (#F6F1E9) for body text
- Lilac (#9668A4) used sparingly — only for active interactions and pull-quote accents
- No purple background boxes — colour is used as text/border accent only
- No filled card backgrounds — all content areas are differentiated by whitespace, not boxes

**Visual teaching style:**
- Timeline and diagrams: drawn in a single-line style (SVG paths), no filled shapes
- No icons — text labels only
- Label cards: text-only, minimal border, no background
- Recognition interaction: clean text with single underline on selection, no box highlight

**Chapter-transition style:**
- A horizontal hairline rule + small chapter number in grey
- Scene name appears in italic serif, fades in
- No slide or animation — content appears on scroll in the editorial column

**Icon or illustration approach:**
- No decorative icons
- System icons (Font Awesome) replaced with text labels where possible
- Where icons must appear (support link, save indicator): thin-line, no fill

**Motion approach:**
- Minimal. Fade-in on section reveal only.
- No parallax, no sliding elements
- `prefers-reduced-motion` respected: static display with no fallback needed

**Emotional tone:**
Quiet, respectful, like a considered letter written specifically to you. Nothing is trying to be engaging — it simply is. The learner feels their intelligence is respected.

**What to avoid:**
- Purple-tinted card boxes
- Any gamification visual (progress bars with colour fills, achievement badges)
- Animated illustrations
- Gradient backgrounds
- Compact grid layouts that reduce whitespace

**How it would scale across Weeks 2–4:**
Each week uses a slightly different accent — Week 2 uses rose (#C07A8A) where Week 1 used lilac. Week 3 uses sage. Week 4 uses gold. The typographic system and whitespace remain constant. A learner who returns to a different week recognises the system immediately.

---

## Concept 2: Guided Visual Journey

**Character:**
Warmer and more structured than Concept 1. The experience feels like being walked through something by someone who has considered the pace carefully. There are visible stages, clear visual markers of progress, and moments where the page does something more than display text.

**Typography character:**
- Cormorant Garamond for H1 and H2 only. Atkinson Hyperlegible for all body and interactive text.
- Headings: medium weight (500), not light — slightly more assertive than Concept 1
- Body text: 1rem, 1.7 line-height
- Stage labels: small caps in lilac, stronger tracking than Concept 1
- Action prompts: bold body text in cream, clear visual distinction from explanatory prose

**Colour balance:**
- Ink-deep background
- Cream text
- Lilac used for active states, progress dots, and interaction highlights
- Purple-dim used for interactive card backgrounds (not all cards — only interactive elements)
- Sage used for save confirmations and completed states
- Rose used for the Scene 5 emotional content only

**Visual teaching style:**
- Timeline: a horizontal track with labelled points — visually shows the progression of time and how diagnosis sits within it
- Executive function cards: each card has a small pictogram (simple, custom, not Font Awesome) representing the function — e.g., a clock face for time awareness, a stack of papers for task initiation
- Before/After frames: two panels with visible left/right arrows between them
- Label cards: text with a soft background, selected state uses a visible highlight

**Chapter-transition style:**
- Full-width scene separator: a thin horizontal rule with scene number on the left and scene name on the right
- Below the rule: a short contextual sentence explaining what is happening in this scene ("Here you will name an old label and start to see it differently")
- Transition is not animated — it is spatial and visible

**Icon or illustration approach:**
- Simple geometric pictograms for the executive function section (not Font Awesome — custom SVG or Noun Project style)
- Pictograms: monochrome (cream on dark or lilac on dark), no filled colour
- No decorative illustration — all visuals are functional

**Motion approach:**
- Scene reveals: fade-in on scroll (very subtle, 200ms)
- Interactive state changes: 150ms transition on card background and border
- Progress dot: smooth fill on scene completion
- No auto-playing animation

**Emotional tone:**
Guided and steady. The learner feels that the path ahead is clear and that someone has thought about it carefully. Engaging without being cheerful.

**What to avoid:**
- Gamification (streaks, points, colour-filled progress bars)
- Dense card grids
- Any element that looks like a corporate LMS (e.g., blue-and-white progress bars, checkbox-heavy layouts)
- Bright or cheerful colour accents — the content is emotionally serious

**How it would scale across Weeks 2–4:**
The journey structure (stage labels, scene transitions, progress strip) remains constant. The pictogram set expands in each week — Week 2 adds mask/face shapes for the masking content, Week 3 adds brain/environment shapes for executive function depth. The course develops a consistent pictogram language across all four weeks.

---

## Concept 3: Warm Interactive Studio

**Character:**
The most interactive of the three. The page feels like a workspace that has been designed for the learner — not clinical, not cold, but purposeful and personal. There is more texture, more visual warmth, and more explicit acknowledgement that the learner is making something.

**Typography character:**
- Atkinson Hyperlegible leads (more accessible for extended reading and interaction)
- Cormorant Garamond reserved for the H1 title and Snapshot display text only
- Interactive labels: slightly larger than Concepts 1 and 2 — 1.1rem for interaction headings
- "Workspace" feel: labels look like hand-applied elements, not rigid system components
- Prompts are framed as invitations ("Here's what you noticed →") rather than instructions

**Colour balance:**
- Not pure ink-deep — slightly warmer dark background (#1A1512 range) — less harsh contrast
- Cream text with slightly warmer white (#FBF7F0)
- Purple used more generously as surface colour (not just accents) — interaction areas have a distinct purple-warm tint
- Sage used for anything related to saving, completing, or accomplishing
- Rose used for the emotional content scenes and for the Snapshot border
- Gold accent: used for the Snapshot document itself — feels like something of value

**Visual teaching style:**
- Timeline: a warm, slightly imperfect horizontal track — not perfectly rendered, feels drawn
- Executive function cards: cards with handwritten-style labels (not literally handwritten but in a typeface that suggests it, e.g., a slightly irregular weight) — or normal type with a visible card texture
- Label cards: full-card tap state with a visible border-fill animation (border draws around the card on selection)
- Snapshot: displayed as a document with a visible frame — looks like an artefact the learner has made

**Chapter-transition style:**
- A warm-tinted banner appears at scene transition: "You're moving into [Scene Name]" with a small icon
- 1-second transition: current scene fades slightly, new scene slides in from right
- On mobile: scene slides left on "Continue →" tap

**Icon or illustration approach:**
- Warm-tinted Font Awesome icons (already in use) — recolouring them to cream on a slightly tinted background
- Optionally: one custom illustration per scene (Week 1 budget: 6 simple SVG illustrations representing each scene's theme) — only if illustration production is feasible
- Snapshot: an illustration of a folded page or document as the Snapshot container

**Motion approach:**
- More motion than Concepts 1 and 2, but all motion is meaningful
- Card selection: border draws, background fills — 150ms, satisfying
- Snapshot assembly: each field "drops in" as the learner completes the corresponding scene
- Milestone tick: a small animation on completion (circle fills, content shifts slightly)
- All motion respects `prefers-reduced-motion`: static state changes without animation

**Emotional tone:**
Warm, productive, and human. The learner feels like they are making something real. The experience has a workshop quality — there is visible craft in the design, and the learner's work is treated as valuable.

**What to avoid:**
- Anything that looks like an app rather than an experience (bottom tab bars, floating action buttons)
- Confetti or celebration animations — wrong tone for grief content
- Pastel colours (too clinical-wellness)
- Over-designed Snapshot (it should look crafted, not like a certificate)
- Excessive motion — two or three animations per scene maximum

**How it would scale across Weeks 2–4:**
Each week's workspace has the same warm feel but a different visual anchor element. Week 1: the Snapshot document. Week 2: a "mask" reveal (something hidden becoming visible). Week 3: a brain/environment diagram that builds across the scenes. Week 4: a self-trust inventory that grows across the four scenes. The learner's outputs from Week 1 are referenced in the Week 2 opening — "Last week you identified [label]. This week we look at what that label was protecting."

---

## What the three concepts must not share

| Element | Concept 1 | Concept 2 | Concept 3 |
|---|---|---|---|
| Card boxes for interactive content | ✗ none | ✓ subtle | ✓ warm-tinted |
| Custom pictograms | ✗ | ✓ geometric | ✓ or illustrations |
| Scene transitions | Static, text-only | Rule + label | Slide animation |
| Snapshot visual style | Clean text, no container | Structured document | Artisan document |
| Warmth of background | Cold ink-deep | Standard ink-deep | Warmer ink tone |
| Typography lead | Cormorant | Mixed | Atkinson |
| Motion | Near-zero | Minimal | Present, controlled |

---

## Production notes for Adobe Express

When creating the concept boards:

1. **Use the Nuanced Co. fonts:** Cormorant Garamond and Atkinson Hyperlegible are available via Google Fonts. Add them as custom fonts in Adobe Express if not available by default.
2. **Size each board at 1280×900px** for the desktop view. Create a separate artboard at 390×844px for the mobile inset.
3. **Do not design a full responsive interface.** Three boards per concept (9 total). Each board is a visual impression, not a spec.
4. **Use actual (or near-actual) copy.** The visual impression depends on real text length. Do not use Lorem Ipsum.
5. **Label each board clearly:** Concept 1 / Quiet Editorial / Board A: Opening.
6. **Export at 2× (144dpi minimum)** for clear reading in review.
7. **Do not include working interactions.** Static boards only. Interaction states shown as "Default" and "Selected" side by side if needed.

---

## Timing

Do not begin Adobe Express concept boards until:
- [ ] Wireframe document reviewed by Leah
- [ ] Mobile flow reviewed by Leah
- [ ] Visual direction choice confirmed (all three to be created, or one direction prioritised?)
- [ ] Illustration approach confirmed (SVG, Font Awesome, or none?)
- [ ] Any brand updates to the token set confirmed

---

*This document is the brief for Stage 2. No Adobe Express work has been started.*
