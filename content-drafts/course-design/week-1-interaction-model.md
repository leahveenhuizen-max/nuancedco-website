# Week 1 Interaction Model
**Date:** 19 June 2026  
**Purpose:** Define every interaction state, data shape, localStorage schema, and accessibility behaviour for Week 1  
**Scope:** Beta build (no backend required; all state in localStorage)  
**Constraint:** No sensitive data collected externally. No PII transmitted.

---

## localStorage key schema

All keys prefixed `tul-w1-`. All values JSON-serialised.

| Key | Type | Scene | Description |
|---|---|---|---|
| `tul-w1-route` | `"full" \| "lowcap" \| "speedread"` | 1 | Chosen route |
| `tul-w1-current-scene` | `string` | Global | Last active scene slug |
| `tul-w1-scene2-response` | `string` | 2 | Free text: what feels different |
| `tul-w1-labels-selected` | `string[]` | 3 | All label cards selected |
| `tul-w1-label-focus` | `string` | 3 | Single label chosen for deep look |
| `tul-w1-label-interpretation` | `string` | 3 | Learner's own reinterpretation |
| `tul-w1-support-then` | `string` | 3 | Support that may have helped |
| `tul-w1-ef-areas` | `string[]` | 4 | EF areas checked |
| `tul-w1-emotions` | `string[]` | 5 | Emotion chips selected |
| `tul-w1-paused` | `boolean` | 5 | Whether learner paused at Scene 5 |
| `tul-w1-life-area` | `string` | 6 | Chosen life area for LRM |
| `tul-w1-lrm-1` | `string` | 6 | LRM Step 1 response |
| `tul-w1-lrm-2` | `string` | 6 | LRM Step 2 response |
| `tul-w1-lrm-3` | `string` | 6 | LRM Step 3 response |
| `tul-w1-lrm-4` | `string` | 6 | LRM Step 4 response |
| `tul-w1-lrm-5` | `string` | 6 | LRM Step 5 response |
| `tul-w1-snapshot-label` | `string` | 6 | Snapshot Field 1 (editable) |
| `tul-w1-snapshot-underneath` | `string` | 6 | Snapshot Field 2 (editable) |
| `tul-w1-snapshot-support-then` | `string` | 6 | Snapshot Field 3 (editable) |
| `tul-w1-snapshot-support-now` | `string` | 6 | Snapshot Field 4 (editable) |
| `tul-w1-snapshot-sentence` | `string` | 6 | Snapshot Field 5 (new text) |
| `tul-w1-milestone` | `boolean` | 6 | Milestone ticked |
| `tul-w1-lowcap` | `boolean` | Global | Low-capacity mode active |
| `tul-w1-last-saved` | `number` | Global | Unix timestamp of last auto-save |
| `tul-w1-additional-areas` | `object[]` | 6 | Array of additional LRM areas [{area, lrm-1..5}] |

---

## Interaction 1: Route Selector (Scene 1)

**Purpose:** Let the learner choose how they want to engage with Week 1.

| State | Behaviour |
|---|---|
| Default | Three route cards visible. None selected. No CTA visible. |
| Hovered/focused | Card border highlights. Route name and duration visible. |
| Selected | Card gets selected state (border, background shift). CTA "Continue →" appears below. |
| Completed | Route saved to localStorage. Scene 1 marked as visited. |

**Data collected:** `tul-w1-route`  
**Default state:** None selected  
**Selected state:** One route card highlighted, CTA visible  
**Completed state:** Route saved, scene advances  
**Edit behaviour:** Learner can tap another route before continuing — selection updates  
**Reset behaviour:** Clearing localStorage resets to default; "Start from beginning" CTA clears all  
**Mobile:** Full-width stacked cards, 56px tall minimum tap targets  
**Keyboard:** Tab between cards, Space/Enter to select, Tab to CTA  
**Screen reader:** `role="radiogroup"`, `role="radio"`, `aria-checked`, group labelled "How would you like to work through this week?"  
**Appears in Snapshot:** No

---

## Interaction 2: Resume Block (Scene 1)

**Purpose:** On return visits, offer to resume from last active scene rather than starting over.

| State | Behaviour |
|---|---|
| Default | Block hidden if no prior `tul-w1-current-scene` in localStorage |
| Shown | Appears above route cards when `tul-w1-current-scene` exists. Shows scene name. |
| Resume tapped | Smooth scroll to last scene. Scene strip updates to active dot. |
| Start over tapped | Confirmation prompt: "This will clear your saved progress. Are you sure?" → if confirmed, clear all `tul-w1-*` keys, scroll to top of Scene 1 |

**Data collected:** Reads `tul-w1-current-scene`  
**Mobile:** Full-width card, two stacked buttons  
**Screen reader:** `aria-live="polite"` on conditional reveal; resume described clearly  
**Appears in Snapshot:** No

---

## Interaction 3: Something Changed Textarea (Scene 2)

**Purpose:** Capture the learner's first personal observation — what feels different now that they know.

| State | Behaviour |
|---|---|
| Default | Textarea empty. "Save to My Snapshot" button active. |
| Typing | Auto-save on blur. "Last saved: just now" appears. |
| Saved | Button label changes to "✓ Saved". Confirmation note visible. Content persists on return. |
| Skip (low-cap) | "Skip for now" link saves an empty string with a skip flag. Snapshot field shows "[To be completed]" placeholder. |
| Completed | Textarea retains value. Edit inline on return. |

**Data collected:** `tul-w1-scene2-response`  
**localStorage key:** `tul-w1-scene2-response`  
**Default:** Empty string  
**Selected/active:** Cursor in textarea, typing  
**Completed:** Non-empty string saved, confirmation shown  
**Edit behaviour:** Learner can return and edit; auto-saves on blur; Snapshot field updates dynamically  
**Reset:** "Clear and start again" link below textarea (small, not prominent)  
**Mobile:** Full-width textarea, 80px min-height, auto-expand; save button full-width below  
**Keyboard:** Tab to textarea, normal text input, Tab to save button, Enter on button to save  
**Screen reader:** `aria-label="What feels different now that you know?"`, save confirmation `aria-live="assertive"`  
**Appears in Snapshot:** No (feeds context for Snapshot Field 2 framing; not directly mapped to a Snapshot field in the MVP)

---

## Interaction 4: Label Selector Grid (Scene 3)

**Purpose:** Allow learner to recognise which labels were applied to them before diagnosis.

| State | Behaviour |
|---|---|
| Default | 8 label cards, none selected. Step 2 hidden. |
| Card tapped | Card gets selected state. Counter updates: "N of 8 selected." Step 2 appears if N ≥ 1. |
| Card tapped again | Deselected. Counter decrements. |
| Completed | Selected labels saved. Step 2 becomes available. |

**Data collected:** `tul-w1-labels-selected` (array)  
**Default:** `[]`  
**Selected:** Card border highlighted, dot indicator visible  
**Completed:** Array saved, Step 2 visible  
**Edit:** Learner can deselect/reselect at any time  
**Reset:** Tapping a selected card deselects it  
**Mobile:** 2-column grid, full-width tap targets, 60px min-height  
**Keyboard:** `role="checkbox"` in `role="group"`, Tab to navigate, Space to select/deselect  
**Screen reader:** Group labelled "Which of these labels sound familiar?". Each card announces its label and checked state. Counter `aria-live="polite"`.  
**Appears in Snapshot:** `tul-w1-labels-selected` used to display Snapshot Field 1 (the focused label from Interaction 5)

---

## Interaction 5: Label Focus Selector (Scene 3)

**Purpose:** From selected labels, learner picks one to look at more closely this week.

| State | Behaviour |
|---|---|
| Default | Hidden until at least one label is selected in Interaction 4 |
| Visible | Shows only the selected labels as tappable chips |
| Chip tapped | Reveal panel appears with content for that label. Other chips dim. |
| Changed | Tapping a different chip changes the reveal panel content |
| Completed | Focus label saved, reveal panel persistent |

**Data collected:** `tul-w1-label-focus`  
**Content model:** 8 label content objects, each with: `{ seen: string, underneath: string, support: string }`  
**Mobile:** Chips wrap, each 44px tall  
**Keyboard:** Tab between chips, Space/Enter to select  
**Screen reader:** `role="radiogroup"`, announces selected chip and updates reveal panel with `aria-live="polite"`  
**Appears in Snapshot:** Yes — focused label becomes Snapshot Field 1

---

## Interaction 6: Label Interpretation Textarea (Scene 3)

**Purpose:** Learner writes their own understanding of the label in careful language.

| State | Behaviour |
|---|---|
| Default | Hidden until label focus is selected |
| Active | Textarea visible with placeholder: "What may have been happening was..." |
| Typing | Auto-save on blur |
| Completed | Saves to `tul-w1-label-interpretation`, feeds Snapshot Field 2 |

**Data collected:** `tul-w1-label-interpretation`  
**Appears in Snapshot:** Yes — Snapshot Field 2

---

## Interaction 7: Support Then Textarea (Scene 3)

**Purpose:** Learner names support that may have helped before diagnosis.

| State | Behaviour |
|---|---|
| Default | Below label interpretation textarea, same reveal sequence |
| Active | Placeholder: "Support that may have helped..." |
| Completed | Saves to `tul-w1-support-then`, feeds Snapshot Field 3 |

**Data collected:** `tul-w1-support-then`  
**Appears in Snapshot:** Yes — Snapshot Field 3

---

## Interaction 8: Executive Function Checkboxes (Scene 4)

**Purpose:** Learner selects which EF areas show up for them.

| State | Behaviour |
|---|---|
| Default | 6 cards with unchecked checkboxes |
| Checkbox tapped | Checked state, card highlighted, counter updates |
| Unchecked | Returns to default state |
| Completed | Checked areas saved, selection response appears |

**Data collected:** `tul-w1-ef-areas` (array of area slugs: `["task-initiation", "working-memory", "time-awareness", "shifting-attention", "planning", "emotional-regulation"]`)  
**Default:** `[]`  
**Completed:** Non-empty array saved  
**Edit:** Check/uncheck at any time; Snapshot updates dynamically  
**Low-cap alternative:** Single `role="radio"` group, one EF area selection  
**Mobile:** Single-column cards, checkbox at bottom right of each card, 44px minimum tap area  
**Keyboard:** Tab to each checkbox, Space to check/uncheck  
**Screen reader:** Each checkbox labelled with EF area name. Selection response `aria-live="polite"`.  
**Appears in Snapshot:** Yes — informs Snapshot Field 4 ("Support I may need now")  
Snapshot Field 4 text is auto-generated: "Areas where support may help: [comma-separated list of selected areas]"

---

## Interaction 9: Emotional Check-In Chips (Scene 5)

**Purpose:** Learner identifies current emotional state. No minimum or maximum selection required.

| State | Behaviour |
|---|---|
| Default | 11 chips, none selected. Dynamic response hidden. |
| Chip tapped | Selected state. Dynamic response area generates appropriate text. |
| Multiple selected | Response updates to reflect combination (priority logic: if Grief + Relief → "both can be true" response; if Nothing yet selected alone → different response) |
| Deselected | Chip returns to default. Response updates. |
| Completed | Selections saved. Pause option visible regardless of state. |

**Data collected:** `tul-w1-emotions`  
**Response logic (simplified priority):**
- Contains "grief" → includes grief response text
- Contains "relief" AND "grief" → co-existence text
- Contains "anger" → anger response text
- Contains "nothing-yet" → "not feeling anything yet" text
- Contains "exhaustion" OR "numbness" → gentler tone text
- Else → general "all of these are valid" text

**Mobile:** 2-per-row chip layout, 44px height, full-width on very narrow viewports  
**Keyboard:** Tab between chips, Space to select/deselect  
**Screen reader:** `role="group"` labelled "What's present for you right now?". Each chip `role="checkbox"`. Response `aria-live="polite"`.  
**Appears in Snapshot:** No (informs emotional tone only; not a Snapshot field)

---

## Interaction 10: Pause Button (Scene 5)

**Purpose:** Explicit exit for learners who need to stop.

| State | Behaviour |
|---|---|
| Default | Visible at all times in Scene 5 |
| Tapped | Sets `tul-w1-paused: true` and `tul-w1-current-scene: "feelings"`. Shows "Progress saved. Come back when you're ready." Scroll to top, no page reload. |
| Resumed | Resume block at Scene 1 shows "You were working on Scene 5: Relief, Grief and Anger." |

**Data collected:** `tul-w1-paused`, `tul-w1-current-scene`  
**Mobile:** Full-width button, prominent, labelled "Save and pause for now"  
**Keyboard:** Tab accessible, Enter to activate  
**Screen reader:** Announces "Your progress has been saved. You can close this page and return later."  
**Appears in Snapshot:** No

---

## Interaction 11: Life Area Selector (Scene 6)

**Purpose:** Learner selects one life area to explore in the Life Review Map.

| State | Behaviour |
|---|---|
| Default | 7 area pills, none selected. LRM hidden. |
| Area tapped | LRM Step 1 appears for that area. |
| Changed (before starting LRM) | Different area, LRM restarts for new area. Confirmation if LRM Step 1 has content: "You have started [area]. Switch to [new area]? Your [area] notes will be saved." |
| Completed | Area saved, LRM Steps 1–5 visible |

**Data collected:** `tul-w1-life-area`  
**Mobile:** Chips wrap 2–3 per row  
**Appears in Snapshot:** No (provides context only)

---

## Interaction 12: Life Review Map Steps 1–5 (Scene 6)

**Purpose:** Five-step guided reflection producing the deepest learner output of the week.

| Step | Question | Textarea placeholder | Saves to |
|---|---|---|---|
| 1 | What happened in this area that stands out? | "What was hard? What did others say at the time?" | `tul-w1-lrm-1` |
| 2 | What was the explanation at the time? | "What label was attached to it?" | `tul-w1-lrm-2` |
| 3 | What may have actually been happening? | "With my ADHD understanding..." | `tul-w1-lrm-3` → Snapshot Field 2 backup |
| 4 | What support might have helped? | "If someone had understood..." | `tul-w1-lrm-4` → Snapshot Field 3 |
| 5 | What might help now? | "Support that could work for my brain..." | `tul-w1-lrm-5` → Snapshot Field 4 |

**Progressive unlock:** Step 2 reveals only after Step 1 is saved (any non-empty content). Steps 3–5 similarly.  
**Low-cap:** Steps 1 only, no progressive unlock — all steps visible but clearly marked optional after Step 1.  
**Edit:** Return to any step and re-save; Snapshot updates.  
**Mobile:** One step visible at a time. "Next step →" button below each textarea. Back navigation ("← Step N") above.  
**Keyboard:** Tab to textarea, Tab to "Save and continue", Enter activates button  
**Screen reader:** Step number and question announced on reveal (`aria-live="polite"`). Save confirmation `aria-live="assertive"`.  
**Appears in Snapshot:** Steps 3/4/5 populate or supplement Snapshot Fields 2/3/4

---

## Interaction 13: My Week 1 Snapshot — Display and Edit (Scene 6)

**Purpose:** Show the assembled output and allow the learner to edit any field before saving.

| State | Behaviour |
|---|---|
| Empty | Placeholder text per field: "[Complete Scene 3 to fill this]" etc. |
| Populated | Field content shown from saved localStorage. |
| Edit tapped | Field becomes contenteditable OR a modal textarea appears with field content. |
| Edited | Content updates in Snapshot display and saves back to corresponding localStorage key. |
| Saved | "Snapshot saved — [timestamp]" confirmation. |

**Snapshot Field 1 (Old Label):** Pre-populated from `tul-w1-label-focus`  
**Snapshot Field 2 (Underneath):** Pre-populated from `tul-w1-label-interpretation` OR `tul-w1-lrm-3`  
**Snapshot Field 3 (Support Then):** Pre-populated from `tul-w1-support-then` OR `tul-w1-lrm-4`  
**Snapshot Field 4 (Support Now):** Generated from `tul-w1-ef-areas` + `tul-w1-lrm-5`  
**Snapshot Field 5 (One Sentence):** Empty — must be written by learner in this scene  

**Copy behaviour:** `navigator.clipboard.writeText()` with formatted text content. Fallback: textarea with content for manual copy.  
**Print behaviour:** `window.print()` with `@media print` CSS isolating Snapshot element only.  
**Mobile:** Each field on separate row. "Edit" icon tappable. Save/Copy/Print as three stacked full-width buttons.  
**Keyboard:** Tab between fields, Tab to edit icon, Enter on edit opens editor  
**Screen reader:** Snapshot announced as a region. Each field labelled. Edit icon has `aria-label="Edit [field name]"`.  
**Appears in Snapshot:** This IS the Snapshot

---

## Interaction 14: Milestone (Scene 6)

**Purpose:** One clear closing action that marks Week 1 as done in a meaningful way.

| State | Behaviour |
|---|---|
| Default | Circular checkbox, unchecked. Statement visible. |
| Tapped | Checked state (filled circle). Completion message appears. Milestone saved. |
| Untapped | Can be unticked. Returns to default state. No penalty. |
| Completed | `tul-w1-milestone: true`. Journey strip dots all show completed state. |

**Completion message:** "Week 1 complete. Your snapshot has been saved to this browser."  
**Note:** No "✨ dopamine" emoji in the wireframe — visual language decision for Stage 2.  
**Mobile:** Large tap target (min 44px), centred  
**Keyboard:** `role="checkbox"`, Space to toggle  
**Screen reader:** Announces "Week 1 milestone: checked. Week 1 complete." on check.  
**Appears in Snapshot:** No (controls completion UI state only)

---

## Interaction 15: Beta Session Panel (Scene 6)

**Purpose:** Prepare the learner for the live beta session. Static display; no interaction beyond links.

| State | Behaviour |
|---|---|
| Default | Panel visible. Date field shows "[Date to be confirmed]". Join link shows "[Join link to be added]". |
| Date set | Replace placeholder with actual date/time. |
| Link set | Replace placeholder with actual join URL. |
| Discussion prompts | Static list, no interaction required. |

**Data collected:** None  
**Mobile:** Full-width card  
**Accessibility:** Linked text must be descriptive ("Join the Week 1 beta session", not "click here")  
**Appears in Snapshot:** No

---

## Auto-save behaviour (global)

- Auto-save fires on:
  - `blur` event on any textarea
  - 30-second interval if textarea is focused and has content
  - "Save" button press
- "Last saved: just now" appears near any active input after save
- If localStorage is unavailable (private browsing, quota exceeded): show one-time warning "Your browser cannot save progress. Copy your notes before closing."
- All saves silent by default; only explicit "Save to Snapshot" triggers visible confirmation

---

## Reset behaviour (global)

- "Start from beginning" in resume block → confirms with learner → clears all `tul-w1-*` keys → returns to Scene 1 top
- Individual field "Clear" links → clears that field's key only → Snapshot updates to show placeholder
- No global "delete all" button visible outside the resume block confirmation flow

---

## Data flow to My Week 1 Snapshot

```
Scene 3 label focus    ──────────────────────────► Snapshot Field 1 (Old Label)
Scene 3 interpretation textarea ─────────────────► Snapshot Field 2 (Underneath)
Scene 6 LRM Step 3     ──────────────────────────┘ (backup/supplement)

Scene 3 support-then textarea ───────────────────► Snapshot Field 3 (Support Then)
Scene 6 LRM Step 4     ──────────────────────────┘ (backup/supplement)

Scene 4 EF checkboxes  ──────────────────────────► Snapshot Field 4 (Support Now)
Scene 6 LRM Step 5     ──────────────────────────┘ (supplement)

Snapshot scene textarea (new) ───────────────────► Snapshot Field 5 (One Sentence)
```

If a learner completes Scene 3 thoroughly, Fields 1–4 are pre-populated from prior interactions. If they skipped Scene 3 (low-cap route), they may fill Fields 1–4 directly in the Snapshot editor.

---

*Interaction model complete. All state is browser-local. No data leaves the device.*
