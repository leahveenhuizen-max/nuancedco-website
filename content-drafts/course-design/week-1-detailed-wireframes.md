# Week 1 Detailed Wireframes — The Unmasked Life™
**Date:** 19 June 2026  
**Stage:** Design wireframes (pre-production)  
**Method:** Mobile-first, scene-based structure  
**Output:** Six scenes replacing fourteen equal-weight sections  
**Files do not touch:** `week-1.html`, `nc-course.css`

---

## Structural overview

Six scenes replace fourteen equal-weight card sections. Each scene has a single purpose, a primary learner action, and a defined output that feeds My Week 1 Snapshot.

| Scene | Name | Primary purpose | Learner action | Feeds Snapshot |
|---|---|---|---|---|
| 1 | Arrive | Orient and reduce uncertainty | Choose route | — |
| 2 | Something Changed | Explain why late diagnosis rewrites the past | Name one shift in how you see something | Field 2 |
| 3 | The Old Story | Reconsider old labels with careful language | Select one label + interpretation | Fields 1, 2, 3 |
| 4 | How the Brain Manages Life | Introduce executive function plainly | Mark which areas show up | Field 4 |
| 5 | Relief, Grief and Anger | Normalise mixed emotional responses | Emotional check-in | Context for Field 5 |
| 6 | Build Your Snapshot | Turn learning into a usable personal output | Complete Life Review Map + review Snapshot | All 5 fields |

---

## SCENE 1: ARRIVE

### Purpose
Orient the learner, reduce uncertainty about what is ahead, and offer three clear routes so no learner is trapped in a format that does not suit their current capacity.

### Desktop structure

```
┌─ NAV (minimal: logo | Week 1 of 4 | Support link) ──────────────────────────────────────┐
│  No sidebar. No timer. No full course nav on the lesson page.                             │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ JOURNEY MAP STRIP (sticky below nav) ─────────────────────────────────────────────────────┐
│  ● Arrive  ○ Something Changed  ○ Old Story  ○ Brain  ○ Feelings  ○ Snapshot               │
│  [Active dot highlighted. Non-active dots grey. No labels on mobile — dots only]            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ MAIN COLUMN (max-width 720px, centred) ───────────────────────────────────────────────────┐
│                                                                                              │
│  [WEEK TAG]  Week 1 of 4 — The Unmasked Life™                                              │
│                                                                                              │
│  [H1 — LARGE SERIF]  The Late Diagnosis Disruption                                         │
│                                                                                              │
│  [LEAD]  A late ADHD diagnosis does not just add a label. It arrives inside a life already  │
│  built, and it changes what you can see. This week is about what happens next.              │
│                                                                                              │
│  [ESTIMATED TIME]  ⏱ About 30–45 minutes in full · 10 minutes on low-capacity route       │
│                                                                                              │
│  [VIDEO PLACEHOLDER — 16:9 aspect ratio]                                                   │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐   │
│  │                          ▶  Week 1 Lesson Video                                     │   │
│  │                    Direct to camera · 10–15 min · Chaptered                         │   │
│  │  [Chapter 1] What diagnosis does  [Chapter 2] The review  [Chapter 3] What's next  │   │
│  └─────────────────────────────────────────────────────────────────────────────────────┘   │
│  [Caption / Transcript toggle — collapsed by default]                                       │
│                                                                                              │
│  ─── How would you like to work through this week? ─────────────────────────────────────   │
│                                                                                              │
│  [ROUTE A]  Full journey                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐   │
│  │  All six scenes · video + reading + interactions · ~45 min                          │   │
│  │  [Select Full Journey →]                                                            │   │
│  └─────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                              │
│  [ROUTE B]  Low-capacity route                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐   │
│  │  One scene at a time · no required reflection · under 10 min each                   │   │
│  │  [Start low-capacity →]                                                             │   │
│  └─────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                              │
│  [ROUTE C]  Speed-read                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐   │
│  │  Core concepts only · no interactions · 5 min                                       │   │
│  │  [Speed-read →]                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                              │
│  [RESUME BLOCK — shown only if prior progress exists in localStorage]                       │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐   │
│  │  ↩  You were working on Scene 3: The Old Story. Resume where you left off?         │   │
│  │  [Resume] [Start from the beginning]                                                │   │
│  └─────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                              │
│  [QUIET NOTE]  You do not need to finish this today. There is no deadline.                  │
│                                                                                              │
│  [SUPPORT NOTE — small, bottom of scene]                                                    │
│  If this week brings up something that needs immediate support: [support link]              │
│                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile structure
- Nav: logo left, "Week 1 of 4" centred, hamburger right — minimal
- Journey map: sticky strip showing dots only (6 dots, active highlighted), scene name shown in a small label below active dot only
- H1: full width, large, top-of-page impact
- Video: full-width 16:9 placeholder
- Route choice: three stacked full-width tap targets (not a grid)
- Resume block: conditional, appears as a card above the route choice
- "You do not need to finish this today": displayed prominently, not buried in a footnote
- No sidebar, no timer, no milestone tracker in the arrive scene

### Content hierarchy
1. Title + lead (what this week is)
2. Time estimate
3. Video
4. Route choice (the one required decision at this scene)
5. Resume (conditional)
6. Quiet permission note
7. Support link

### Interaction
- Route selection: tap/click one of three options → sets route preference in localStorage → advances to Scene 2 (in full or low-cap mode) or replaces content with speed-read
- Video chapters: clicking a chapter label seeks to that timestamp (deferred until video exists)
- Transcript: accordion, collapsed by default
- Resume: tap → jump to saved scene; or "Start from beginning" → clear progress and begin

### Learner action
Choose a route. No reflection required at this scene.

### Data saved
`tul-w1-route`: "full" | "lowcap" | "speedread"  
`tul-w1-current-scene`: "arrive" → "something-changed" on continue

### Progress signal
Dot 1 active in journey strip.

### Emotional intensity
**Low.** This scene should feel welcoming and calm. No heavy content. No reflection prompts.

### Low-capacity alternative
Route B is the low-capacity mode. On this route: scenes are displayed one at a time with reduced optional content. Each scene ends with "That's enough. Come back for the next part when you're ready."

### Accessibility requirements
- Route cards: keyboard navigable, `role="radio"` group with named group label
- Video placeholder: `role="img"` with descriptive aria-label
- Journey map: `role="navigation"` with `aria-label="Lesson progress"`
- Resume block: `aria-live="polite"` on conditional reveal
- All tap targets minimum 44×44px

### Empty state
No prior progress: resume block hidden. Route choice is the primary action.

### Completed state
Route chosen: selected route card highlighted, "Continue to Something Changed →" CTA appears.

### Transition to Scene 2
Smooth scroll to Scene 2 top, or in low-cap mode, fade/slide to Scene 2 only.

---

## SCENE 2: SOMETHING CHANGED

### Purpose
Explain why a late diagnosis can alter how the past is understood, and invite the learner to name one shift they have noticed.

### Desktop structure

```
┌─ SCENE SEPARATOR ──────────────────────────────────────────────────────────────────────────┐
│  ○●○○○○  Scene 2: Something Changed                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ MAIN COLUMN (max-width 720px, centred) ───────────────────────────────────────────────────┐
│                                                                                              │
│  [H2 — SERIF]  What late diagnosis actually does                                            │
│                                                                                              │
│  [TEACHING PROSE — no accordion]                                                            │
│  A late ADHD diagnosis is not simply receiving new information. It is information arriving  │
│  inside a life that was already built around explanations that were wrong, incomplete,      │
│  or missing entirely.                                                                       │
│                                                                                              │
│  When that information arrives, it does not stay in the present. It travels backwards.     │
│  Across your life. Through your past.                                                       │
│                                                                                              │
│  ┌─ VISUAL: DIAGNOSIS → LIFE REVIEW TIMELINE ─────────────────────────────────────────┐   │
│  │                                                                                      │   │
│  │  [Past]────────────────────────[Diagnosis]────────────────►[Now]                   │   │
│  │    ↑ School  ↑ Work  ↑ Relationships  ↑ Health                                     │   │
│  │    │                                                                                 │   │
│  │    └── New understanding flows backward                                             │   │
│  │                                                                                      │   │
│  │  Label: When the diagnosis arrives, it changes how you see what came before it.    │   │
│  └──────────────────────────────────────────────────────────────────────────────────── ┘  │
│                                                                                              │
│  [TEACHING PROSE continues]                                                                  │
│  This retroactive review — the "was that ADHD too?" process — is recognised in the          │
│  research on late diagnosis in adults. You are not the first person to find this            │
│  disorienting, and you are not doing it wrong.                                              │
│                                                                                              │
│  ─── Your turn ─────────────────────────────────────────────────────────────────────────   │
│                                                                                              │
│  [INTERACTION — single text input]                                                           │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  What feels different now that you know?                                             │  │
│  │  [One area, one memory, one pattern — no pressure to be complete]                    │  │
│  │                                                                                      │  │
│  │  ┌────────────────────────────────────────────────────────────────────────────────┐ │  │
│  │  │ Textarea (3 rows min, auto-expand)                                             │ │  │
│  │  │ Placeholder: "Something I am seeing differently is..."                        │ │  │
│  │  └────────────────────────────────────────────────────────────────────────────────┘ │  │
│  │  [Save to My Snapshot]  · Saves to Scene 2 field · Does not submit anywhere         │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  [SAVE CONFIRMATION — appears after save]                                                    │
│  ✓ Saved to your Week 1 Snapshot.                                                           │
│                                                                                              │
│  [PULL QUOTE — after interaction]                                                            │
│  "The disruption that follows — to identity, to self-understanding, to the story you tell  │
│  about yourself — is a recognised part of what late diagnosis involves."                   │
│                                                                                              │
│  [CONTINUE]  Continue to The Old Story →                                                    │
│                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile structure
- H2 full width, strong visual weight
- Timeline visual: horizontal scrollable on mobile OR restructured as a vertical list with arrows if horizontal fails
- Teaching prose: standard reading width, good line-height
- Interaction block: full-width textarea, "Save to My Snapshot" as a full-width button below
- Pull quote: indented left border, not a boxed card
- Continue: sticky bottom CTA on mobile ("Continue →") that appears after first interaction or 30 seconds on page

### Content hierarchy
1. Section heading
2. Teaching prose (concise — 3–4 paragraphs max)
3. Visual: timeline
4. Teaching prose continued (1–2 paragraphs)
5. The one required interaction
6. Save confirmation
7. Pull quote
8. Continue

### Interaction
Single textarea: "What feels different now that you know?" with save-to-Snapshot button. Auto-saves on blur also (backup).

### Learner action
Write one observation. Save it. Continue.

### Data saved
`tul-w1-scene2-response`: free text  
Written to Snapshot Field 2 preview

### Progress signal
Dot 2 active. Scene name visible in strip.

### Emotional intensity
**Medium.** The retroactive review concept can land as recognition or grief depending on the learner's state. The tone of the teaching must be warm and normalising, not clinical. The interaction is optional in low-capacity mode.

### Low-capacity alternative
Teaching prose only (condensed to 2 paragraphs). The interaction textarea is present but not required. "Skip for now" option saves an empty placeholder to the Snapshot.

### Accessibility
- Textarea: `aria-label="What feels different now that you know?"`, `aria-describedby` linked to placeholder text
- Save button: `aria-live="polite"` on confirmation message
- Timeline visual: full text alternative in a visually hidden description
- Pull quote: `<blockquote>` element

### Empty state
Textarea empty; save button visible but inactive OR active-with-skip-option.

### Completed state
Response saved; save confirmation visible; textarea retains content; "saved" indicator replaces button label.

### Transition to Scene 3
Smooth scroll OR explicit "Continue to The Old Story →" button.

---

## SCENE 3: THE OLD STORY

### Purpose
Help the learner reconsider old labels applied to them before diagnosis, without replacing one rigid story with another. Careful language throughout: "may," "might," "could have been." Yields the first two Snapshot fields.

### Desktop structure

```
┌─ SCENE SEPARATOR ──────────────────────────────────────────────────────────────────────────┐
│  ○○●○○○  Scene 3: The Old Story                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ MAIN COLUMN ──────────────────────────────────────────────────────────────────────────────┐
│                                                                                              │
│  [H2 — SERIF]  The labels that didn't fit                                                  │
│                                                                                              │
│  [TEACHING PROSE — no accordion, 2–3 paragraphs]                                            │
│  Many adults received labels before their diagnosis arrived. Not ADHD labels. Other ones.  │
│  Lazy. Inconsistent. Too sensitive. Not trying hard enough. Wasted potential.               │
│                                                                                              │
│  These labels were often genuinely believed by the people who offered them. They were not  │
│  accurate explanations. They were guesses made without enough information.                   │
│                                                                                              │
│  This section is not about blaming the people who used them or discarding everything you    │
│  were told. It is about looking at some of those labels and asking: what might have        │
│  actually been happening?                                                                    │
│                                                                                              │
│  ─── Step 1: Which of these sound familiar? ───────────────────────────────────────────   │
│                                                                                              │
│  [LABEL SELECTOR GRID — 4 columns desktop, 2 columns tablet, 1 column mobile]               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                     │
│  │     lazy     │ │ inconsistent │ │   careless   │ │ too sensitive│                     │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘                     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                     │
│  │ not trying   │ │  difficult   │ │disorganised  │ │wasted        │                     │
│  │              │ │              │ │              │ │potential     │                     │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘                     │
│                                                                                              │
│  [SELECTION COUNT]  You have selected 0 labels. You can select more than one.              │
│                                                                                              │
│  ─── Step 2: Choose one to look at more closely ──────────────────────────────────────   │
│                                                                                              │
│  [SINGLE SELECT from selected labels — dropdown or tap-to-select among those chosen]        │
│  "Which one do you want to look at this week?"                                              │
│                                                                                              │
│  [REVEAL PANEL — appears after Step 2 selection]                                            │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  You chose: [LABEL]                                                                  │  │
│  │                                                                                      │  │
│  │  WHAT PEOPLE MAY HAVE SEEN                                                          │  │
│  │  [Short, non-judgmental description of what the behaviour looked like externally]   │  │
│  │                                                                                      │  │
│  │  WHAT MAY HAVE BEEN HAPPENING UNDERNEATH                                            │  │
│  │  [ADHD explanation using "may," "might," "could have been" — not certainty]        │  │
│  │                                                                                      │  │
│  │  SUPPORT THAT MAY HAVE HELPED                                                       │  │
│  │  [What a more accurate understanding might have enabled — 1–2 sentences]           │  │
│  │                                                                                      │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  ─── Step 3: In your own words ──────────────────────────────────────────────────────   │
│                                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  How do you understand this label now?                                               │  │
│  │  (Use "may" or "might." You do not need to be certain.)                             │  │
│  │  ┌────────────────────────────────────────────────────────────────────────────────┐ │  │
│  │  │ Textarea: "What may have been happening was..."                                │ │  │
│  │  └────────────────────────────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  ─── Step 4: What might have helped ─────────────────────────────────────────────────   │
│                                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  If someone had understood what was happening, what support might have made          │  │
│  │  a difference? (One word or one sentence is enough.)                                 │  │
│  │  ┌────────────────────────────────────────────────────────────────────────────────┐ │  │
│  │  │ Textarea: "Support that may have helped..."                                    │ │  │
│  │  └────────────────────────────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  [SAVE BLOCK]  [Save to My Snapshot]  — saves label + new understanding + support needed   │
│                                                                                              │
│  [REASSURANCE NOTE]  This is not a definitive rewrite. It is a beginning.                  │
│                                                                                              │
│  [CONTINUE]  Continue to How the Brain Manages Life →                                      │
│                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile structure
- Label selector: 2 columns of full-width tap cards (not 4 columns — too small on mobile)
- Step 2 single select: appears below the grid after any selection, as a clear "Pick one to explore" prompt
- Reveal panel: full-width card, readable font size
- Textareas: full width, good spacing between them
- Save button: full-width, prominent
- No step labels visible simultaneously — label each step as the learner arrives at it (progressive disclosure)

### Content hierarchy
1. Teaching prose (why labels, what they meant, what they weren't)
2. Label selector grid (all 8 options)
3. Single-label focus selector
4. Reveal panel (what was seen / what may have been happening / what may have helped)
5. Two short textareas (learner's own words)
6. Save to Snapshot
7. Reassurance note
8. Continue

### Interaction
- Multi-select label cards (all 8)
- Single select from chosen labels ("pick one to explore")
- Two textareas
- Reveal panel: JS reveals appropriate content per label (8 text blocks, one per label)
- Save button

### Learner action
Select labels, choose one, read the reveal, write their own interpretation, save it.

### Data saved
`tul-w1-labels-selected`: array of selected labels  
`tul-w1-label-focus`: single chosen label  
`tul-w1-label-interpretation`: free text (Snapshot Field 2)  
`tul-w1-support-then`: free text (Snapshot Field 3)

### Progress signal
Dot 3 active. Optional counter: "3 of 8 labels recognised."

### Emotional intensity
**Medium-high.** The label content is likely to resonate strongly. The reassurance note and "may"/"might" language are emotional safety mechanisms. The tone must not feel like therapy or diagnosis. "This is not a definitive rewrite" is essential.

### Low-capacity alternative
Show only the label selector grid and a single textarea: "What does one of these labels look like differently now?" No reveal panel. No four-step sequence. One save action.

### Accessibility
- Label cards: `role="checkbox"` in a `role="group"` with `aria-labelledby` pointing to "Which of these sound familiar?"
- Reveal panel: `aria-live="polite"` on reveal
- Textareas: individually labelled with `aria-label`
- Save confirmation: `aria-live="assertive"`

### Empty state
No labels selected: Step 2 and reveal panel hidden. "Select at least one label to continue" hint visible.

### Completed state
Labels selected, one focused, textareas completed, save confirmation visible. Content persists on return visit.

### Transition to Scene 4
"Continue to How the Brain Manages Life →"

---

## SCENE 4: HOW THE BRAIN MANAGES LIFE

### Purpose
Introduce executive function in plain language without a neuroscience lecture. Give the learner a set of named concepts they can use to understand their own patterns. Each item should feel recognisable, not clinical.

### Desktop structure

```
┌─ SCENE SEPARATOR ──────────────────────────────────────────────────────────────────────────┐
│  ○○○●○○  Scene 4: How the Brain Manages Life                                               │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ MAIN COLUMN ──────────────────────────────────────────────────────────────────────────────┐
│                                                                                              │
│  [H2 — SERIF]  Your brain's management system                                              │
│                                                                                              │
│  [TEACHING INTRO — 1 paragraph]                                                              │
│  ADHD affects what researchers call executive function — the set of processes that help     │
│  the brain manage getting started, keeping track, staying aware of time, handling           │
│  emotions, and following through. Week 3 covers this in depth. Here, the aim is to name    │
│  the areas so recognition can begin.                                                        │
│                                                                                              │
│  These are not character traits. They are neurological processes.                           │
│                                                                                              │
│  ─── Which of these shows up for you? ─────────────────────────────────────────────────   │
│                                                                                              │
│  [EXECUTIVE FUNCTION CARDS — 6 items, 2 columns, each card expandable]                      │
│                                                                                              │
│  ┌────────────────────────────────────────┐ ┌────────────────────────────────────────┐    │
│  │ TASK INITIATION                        │ │ WORKING MEMORY                         │    │
│  │ Getting started on things you intend   │ │ Holding information in mind while      │    │
│  │ to do, even when you know how.         │ │ you're using it.                       │    │
│  │                                        │ │                                        │    │
│  │ For example: writing the email you've  │ │ For example: losing your train of      │    │
│  │ had open for two days.                 │ │ thought mid-sentence.                  │    │
│  │                                        │ │                                        │    │
│  │ [  ] Does this show up for you?        │ │ [  ] Does this show up for you?        │    │
│  └────────────────────────────────────────┘ └────────────────────────────────────────┘    │
│                                                                                              │
│  ┌────────────────────────────────────────┐ ┌────────────────────────────────────────┐    │
│  │ TIME AWARENESS                         │ │ SHIFTING ATTENTION                     │    │
│  │ Tracking and estimating time           │ │ Moving between tasks without           │    │
│  │ accurately.                            │ │ losing what you were doing.            │    │
│  │                                        │ │                                        │    │
│  │ For example: two hours disappearing    │ │ For example: being interrupted and     │    │
│  │ without notice.                        │ │ not being able to return.              │    │
│  │                                        │ │                                        │    │
│  │ [  ] Does this show up for you?        │ │ [  ] Does this show up for you?        │    │
│  └────────────────────────────────────────┘ └────────────────────────────────────────┘    │
│                                                                                              │
│  ┌────────────────────────────────────────┐ ┌────────────────────────────────────────┐    │
│  │ PLANNING AND SEQUENCING                │ │ EMOTIONAL REGULATION                   │    │
│  │ Breaking tasks into steps and          │ │ Managing the speed and intensity        │    │
│  │ following through.                     │ │ of emotional responses.                │    │
│  │                                        │ │                                        │    │
│  │ For example: knowing what to do but    │ │ For example: frustration that feels    │    │
│  │ not knowing how to start.              │ │ disproportionate to the situation.     │    │
│  │                                        │ │                                        │    │
│  │ [  ] Does this show up for you?        │ │ [  ] Does this show up for you?        │    │
│  └────────────────────────────────────────┘ └────────────────────────────────────────┘    │
│                                                                                              │
│  [SELECTION RESPONSE — appears after any checkbox selected]                                  │
│  "You have identified [N] areas. These will appear in your Week 1 Snapshot as possible     │
│  present support needs."                                                                     │
│                                                                                              │
│  [RESEARCH NOTE — collapsed accordion, optional]                                             │
│  ▸ Where does this come from? (Research basis — expand to read)                             │
│                                                                                              │
│  [CONTINUE]  Continue to Relief, Grief and Anger →                                         │
│                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile structure
- Cards: single column, full width
- Each card: name (bold), real-life example (small text), checkbox at bottom
- Cards do NOT expand on mobile — all content visible at once to avoid tapping/expanding on small screen
- Selection response: inline below last card, updates live
- Research note: accordion, collapsed

### Content hierarchy
1. Teaching intro (1 paragraph, non-clinical)
2. Key statement ("These are not character traits")
3. Six EF cards with real-life examples and checkboxes
4. Selection response (live update)
5. Optional research note (accordion)
6. Continue

### Interaction
- Checkbox per card (multi-select, no minimum required)
- Live selection counter
- Research note accordion (optional deeper reading)

### Learner action
Check which areas show up for them. No writing required.

### Data saved
`tul-w1-ef-areas`: array of checked EF areas  
Used to populate Snapshot Field 4 ("Support I may need now")

### Progress signal
Dot 4 active. Optional: "4 of 6 areas recognised."

### Emotional intensity
**Low-medium.** Recognition can be validating ("finally there's a word for this") or overwhelming. The tone must be matter-of-fact and normalising. No suggestion that these are deficits or problems — they are differences in how the management system works.

### Low-capacity alternative
Single question: "Which one area of executive function is most present for you right now?" — six single-select radio buttons. No grid, no cards.

### Accessibility
- Checkboxes: labelled individually, grouped with `fieldset`/`legend`
- Cards: not `role="button"` — checkboxes are the interaction element
- Selection response: `aria-live="polite"`

### Empty state
No boxes checked; selection response hidden; continue still available (no checkboxes required).

### Completed state
N checkboxes checked; selection response visible; data saved.

### Transition to Scene 5
"Continue to Relief, Grief and Anger →"

---

## SCENE 5: RELIEF, GRIEF AND ANGER

### Purpose
Normalise the range of emotional responses to late diagnosis without turning Week 1 into a grief module. Create space for the learner to identify their current emotional state and receive a short, appropriate response. Provide a bridge to the Companion Guide for those who need to go deeper.

### Desktop structure

```
┌─ SCENE SEPARATOR ──────────────────────────────────────────────────────────────────────────┐
│  ○○○○●○  Scene 5: Relief, Grief and Anger                                                  │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ MAIN COLUMN ──────────────────────────────────────────────────────────────────────────────┐
│                                                                                              │
│  [H2 — SERIF]  There is no correct response                                                │
│                                                                                              │
│  [TEACHING PROSE — 2 paragraphs, no accordion]                                               │
│  There is no correct emotional response to a late ADHD diagnosis. Some people feel relief  │
│  — a framework that finally fits. Some feel grief for the years that went differently.     │
│  Some feel anger. Some feel nothing yet. Many feel more than one thing at once.            │
│                                                                                              │
│  These responses can co-exist, alternate, and return. Relief and grief are not opposites.  │
│  You do not need to choose between them or arrive at one before you are allowed to feel    │
│  the other.                                                                                 │
│                                                                                              │
│  ─── What's present for you right now? ────────────────────────────────────────────────   │
│                                                                                              │
│  [EMOTIONAL CHECK-IN — multi-select chips, no grid]                                          │
│  [Relief]  [Grief]  [Anger]  [Numbness]  [Confusion]  [Gratitude]  [Exhaustion]           │
│  [Sadness]  [Hope]  [Nothing yet]  [Something I don't have a word for]                    │
│                                                                                              │
│  [DYNAMIC RESPONSE — appears after selection, changes based on selections]                   │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  [Response text: 2–3 sentences calibrated to selected emotions]                     │  │
│  │                                                                                      │  │
│  │  Examples:                                                                           │  │
│  │  – If Grief selected: "Grief after late diagnosis is a reasonable response to real  │  │
│  │    loss. It does not need a clinical category to be valid."                         │  │
│  │  – If Relief selected: "Relief and grief are not opposites. Both can be true."     │  │
│  │  – If Anger selected: "Anger at the systems that missed this is a reasonable       │  │
│  │    response. It does not need to be resolved right now."                           │  │
│  │  – If Nothing yet: "Not feeling anything yet is also a valid place to be."        │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  [PAUSE OPTION]                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  If this is landing heavily:                                                         │  │
│  │  You do not need to continue right now. Save your progress and come back.           │  │
│  │  [Save and pause] [Continue]                                                        │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  [COMPANION GUIDE CALLOUT — contained block, not a full-page interrupt]                      │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  Optional Week 1 Companion Guide                                                     │  │
│  │  Grieving the Life You Thought You Had                                               │  │
│  │                                                                                      │  │
│  │  A deeper research-informed guide to grief, anger, relief and the "what if I had    │  │
│  │  known sooner?" stage. If the grief side of this week is landing heavily,           │  │
│  │  this guide goes further than the course page can.                                  │  │
│  │                                                                                      │  │
│  │  Included in your course. Also available as a standalone resource.                  │  │
│  │  [Access in your resource vault →] ← placeholder, link not live until PDF supplied │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  [SUPPORT REMINDER — small, unobtrusive]                                                     │
│  If you need support right now: [support link]                                              │
│                                                                                              │
│  [CONTINUE]  Continue to Build Your Snapshot →                                             │
│                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile structure
- Emotion chips: wrapping row of full-width chips on mobile — 2 per row, 44px tall minimum
- Dynamic response: card below chips, appears on first selection, updates on additional selections
- Pause option: visible card with two clear buttons
- Companion Guide: full-width card, clearly marked "Optional"
- Support link: small but accessible, bottom of scene

### Content hierarchy
1. Teaching prose (non-clinical, 2 paragraphs)
2. Emotional check-in chips
3. Dynamic response
4. Pause option
5. Companion Guide callout (optional)
6. Support reminder
7. Continue

### Interaction
- Multi-select emotion chips
- Dynamic response text (JS selects appropriate response based on chip combinations)
- Pause / save-and-exit
- Companion Guide CTA (placeholder until PDF exists)

### Learner action
Select emotions. Read response. Decide whether to pause or continue.

### Data saved
`tul-w1-emotions`: array of selected emotion chips  
`tul-w1-paused`: boolean (used to show "Welcome back" on resume)  
Emotion selections not written directly to Snapshot — they inform tone of Scene 6 continue text

### Progress signal
Dot 5 active.

### Emotional intensity
**Potentially high.** This scene must be gentle. The pause option is always visible. The Companion Guide callout is never forced. The support link is always available. No interaction is required to continue.

### Low-capacity alternative
Single question: "Where are you right now?" with four options: "Relief," "Grief," "Somewhere in between," "I'm not sure yet." One-tap response, no chips, no dynamic text. Direct route to pause or continue.

### Accessibility
- Emotion chips: `role="checkbox"` in a `role="group"` with `aria-label="What's present for you right now?"`
- Dynamic response: `aria-live="polite"`
- Pause button: prominent, labelled "Save and pause for now"
- Companion Guide: not a modal interrupt, does not take focus unless clicked

### Empty state
No chips selected; dynamic response hidden; continue available without selection.

### Completed state
Chips selected; response shown; paused or continued.

### Transition to Scene 6
"Continue to Build Your Snapshot →"

---

## SCENE 6: BUILD YOUR SNAPSHOT

### Purpose
Turn the learning and interactions from Scenes 1–5 into one coherent, personally meaningful output: My Week 1 Snapshot. The Life Review Map feeds this output. The learner sees their own words assembled into something they can save, copy, or print.

### Desktop structure

```
┌─ SCENE SEPARATOR ──────────────────────────────────────────────────────────────────────────┐
│  ○○○○○●  Scene 6: Build Your Snapshot                                                     │
└────────────────────────────────────────────────────────────────────────────────────────────┘

┌─ MAIN COLUMN ──────────────────────────────────────────────────────────────────────────────┐
│                                                                                              │
│  [H2 — SERIF]  The Life Review Map                                                         │
│                                                                                              │
│  [INTRO PROSE]                                                                               │
│  The Life Review Map is this week's course exercise. It is not a diagnostic tool.          │
│  Choose one area of your life to look at. One area is enough to begin.                     │
│                                                                                              │
│  ─── Choose a life area ────────────────────────────────────────────────────────────────   │
│                                                                                              │
│  [LIFE AREA SELECTOR — pill buttons, single select]                                          │
│  [School]  [Work]  [Relationships]  [Home]  [Health]  [Money]  [Identity]                  │
│                                                                                              │
│  [LOW-CAPACITY OPTION — appears if low-cap mode active]                                     │
│  "Starting with just one area is the right amount. You can add more areas later."          │
│                                                                                              │
│  [LRM STEP SEQUENCE — reveals one step at a time, next step unlocks after current is saved]│
│                                                                                              │
│  ┌─ STEP 1 ────────────────────────────────────────────────────────────────────────────┐   │
│  │  What happened in this area that stands out?                                        │   │
│  │  [What was hard? What did others say about it at the time?]                         │   │
│  │  ┌──────────────────────────────────────────────────────────┐                       │   │
│  │  │ Textarea                                                  │                       │   │
│  │  └──────────────────────────────────────────────────────────┘                       │   │
│  │  [Save and continue to Step 2 →]                                                    │   │
│  └────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                              │
│  [STEPS 2–5 reveal progressively after each save]                                           │
│  Step 2: What was the explanation at the time?                                              │
│  Step 3: What may have actually been happening?                                             │
│  Step 4: What support might have helped?                                                    │
│  Step 5: What might help now?                                                               │
│                                                                                              │
│  ─── Add another area (optional) ──────────────────────────────────────────────────────   │
│  [Show life area selector again — same interaction, stacks new LRM below]                  │
│                                                                                              │
│  ═══════════════════════════════════════════════════════════════════════════════════════   │
│                                                                                              │
│  [MY WEEK 1 SNAPSHOT — appears after Step 1 is completed for at least one area]             │
│                                                                                              │
│  ┌─ MY WEEK 1 SNAPSHOT ───────────────────────────────────────────────────────────────┐   │
│  │  The Unmasked Life™ — Week 1                                                       │   │
│  │                                                                                    │   │
│  │  ONE OLD LABEL I AM RECONSIDERING                                                  │   │
│  │  [Pulled from Scene 3 label selection — editable]                                  │   │
│  │                                                                                    │   │
│  │  WHAT MAY HAVE BEEN HAPPENING UNDERNEATH                                           │   │
│  │  [Pulled from Scene 3 textarea — editable]                                         │   │
│  │                                                                                    │   │
│  │  SUPPORT THAT MAY HAVE HELPED THEN                                                 │   │
│  │  [Pulled from Scene 3 + Life Review Map — editable]                               │   │
│  │                                                                                    │   │
│  │  SUPPORT I MAY NEED NOW                                                            │   │
│  │  [Pulled from Scene 4 EF checkboxes + Life Review Map Step 5 — editable]         │   │
│  │                                                                                    │   │
│  │  ONE SENTENCE I WANT TO KEEP                                                       │   │
│  │  ┌────────────────────────────────────────────────────────────────────────────────┐│   │
│  │  ││ Textarea: "Write one sentence you want to carry forward from this week..."   ││   │
│  │  │└────────────────────────────────────────────────────────────────────────────────┘│   │
│  │                                                                                    │   │
│  │  [Edit any field]  [Save Snapshot]  [Copy to clipboard]  [Print / Download]       │   │
│  └─────────────────────────────────────────────────────────────────────────────────── ┘  │
│                                                                                              │
│  [MILESTONE]                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  ◯  I have identified at least one pattern from my past that I am now seeing         │  │
│  │     differently with my ADHD understanding.                                          │  │
│  │  Tick when it feels true. There is no deadline.                                      │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  [MILESTONE COMPLETION STATE — appears on tick]                                              │
│  ✓ Week 1 complete. Your snapshot has been saved to this browser.                          │
│                                                                                              │
│  ─── BRING THIS TO THE WEEKLY CATCH-UP ─────────────────────────────────────────────────  │
│                                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  Bring this to the weekly catch-up                                                   │  │
│  │                                                                                      │  │
│  │  [SESSION DATE PLACEHOLDER — not yet set]                                            │  │
│  │  [Join link placeholder — not yet set]                                               │  │
│  │                                                                                      │  │
│  │  Optional discussion prompts:                                                        │  │
│  │  1. Which label felt most familiar, and why?                                        │  │
│  │  2. What did the life review surface that surprised you?                             │  │
│  │  3. What are you still uncertain about after this week?                              │  │
│  │                                                                                      │  │
│  │  Sharing is optional. You are welcome to attend and listen.                         │  │
│  │  [Facilitator statement: this session is not therapy. It is a supported discussion.]│  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                              │
│  ─── Coming in Week 2 ─────────────────────────────────────────────────────────────────   │
│                                                                                              │
│  [WEEK 2 PREVIEW — small teaser, links to week-2.html]                                      │
│  Masking, Overcompensation and Self-Blame                                                   │
│  We go into the patterns many late-diagnosed adults have used to get through.               │
│  [Week 2 →]                                                                                 │
│                                                                                              │
│  [SCOPE NOTE — small, bottom of page]                                                        │
│  This course is educational content. It is not therapy, clinical advice, or a substitute   │
│  for professional mental health support. [Support resources]                                │
│                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile structure
- Life area selector: wrapping row of pill chips, 2 per row
- LRM steps: full width, one visible at a time on mobile
- "Add another area" button: below completed area, clearly secondary
- Snapshot: full-width card, each field on its own row
- Editable fields: tap to edit inline
- Action buttons: Save, Copy, Print — full width, stacked
- Milestone: large tap target, centred text
- Beta session panel: full-width card
- Week 2 preview: small card at bottom

### Content hierarchy
1. Life area selector
2. LRM Step 1 (unlocks the sequence)
3. LRM Steps 2–5 (progressive)
4. Add another area (optional)
5. My Week 1 Snapshot (assembled, editable)
6. Milestone tick
7. Completion message
8. Beta session panel
9. Week 2 preview
10. Scope note

### Interaction
- Life area selector: single select, one area at a time
- LRM: five steps, each saves before unlocking next
- Snapshot fields: pre-populated from prior scenes, each editable inline
- "One sentence I want to keep": free textarea (the one field the learner writes from scratch in the Snapshot)
- Save / Copy / Print: localStorage save, clipboard API, window.print()
- Milestone: tap to tick, localStorage state
- Beta session panel: static content (no date yet)

### Learner action
Complete Life Review Map for one area. Review and edit Snapshot. Tick milestone. Optionally add more areas.

### Data saved
`tul-w1-life-area`: selected area  
`tul-w1-lrm-[1-5]`: five step responses  
`tul-w1-snapshot-label`: old label (from Scene 3)  
`tul-w1-snapshot-underneath`: interpretation (from Scene 3)  
`tul-w1-snapshot-support-then`: support then (from Scene 3 + LRM Step 4)  
`tul-w1-snapshot-support-now`: support now (from Scene 4 EF + LRM Step 5)  
`tul-w1-snapshot-sentence`: one sentence (new, written in Snapshot)  
`tul-w1-milestone`: boolean

### Progress signal
Dot 6 active. After milestone tick: all 6 dots turn to filled/completed state.

### Emotional intensity
**Medium-low.** This scene should feel productive and closing, not heavy. The learner is assembling something, not excavating something. The tone of the Snapshot display is calm and affirming.

### Low-capacity alternative
Life area pre-selected as "Identity" (the most likely single area for a Week 1 low-cap learner). LRM shows Step 1 only. Snapshot has a single field: "One thing I noticed." No multi-step sequence.

### Accessibility
- LRM steps: each step has explicit `aria-label`, `aria-describedby` for guidance text
- Snapshot fields: each has `contenteditable` or `textarea` with label
- Save confirmation: `aria-live="assertive"`
- Print: `window.print()` with print-specific CSS stripping nav and non-snapshot content
- Milestone: `role="checkbox"`, `aria-checked`, keyboard accessible

### Empty state
No LRM step completed: Snapshot shows placeholder text "Complete Step 1 of the Life Review Map to see your Snapshot."

### Completed state
Snapshot assembled, milestone ticked, completion message visible.

### Transition
No Scene 7 — this is the close of the week.

---

## Global: Persistent elements across all scenes

### Progress strip (sticky)
- Dot navigation: 6 dots, active dot labelled below (desktop), unlabelled on mobile
- On mobile: strip stays at top below minimal nav bar
- Dots become filled (green-equivalent in final visual) as scenes are completed
- Tapping a completed dot allows returning to that scene

### Minimal nav
- Logo left
- "Week 1 of 4" centred (or right on desktop)
- "Need support" link — always visible, never hidden
- No full course navigation visible during the lesson

### Low-capacity mode toggle
- Available globally at top of Scene 1 and persistently accessible via a small icon/button in the nav or progress strip
- When active: optional content hidden, single-question alternatives shown, each scene ends with "That's enough for now" before the continue button

### Auto-save
- All textarea and selection state auto-saves on blur and every 30 seconds
- "Last saved: just now" micro-text visible near inputs
- No data sent externally — localStorage only

---

*Wireframe specification complete. Visual wireframe screens follow in `wireframes/` directory.*
