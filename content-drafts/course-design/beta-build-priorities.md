# Week 1 Beta Build Priorities
**Date:** 19 June 2026  
**Purpose:** Define what must be built for the founding beta cohort vs what can wait  
**Constraint:** No backend. localStorage only. Mobile-first.

---

## P1 — Essential for founding beta

These features are required for the beta cohort to experience this as a paid course.

| # | Feature | Scene | Why essential |
|---|---|---|---|
| 1 | Route choice (Full / Low-cap / Speed-read) | 1 | Without this, every learner gets the same experience regardless of capacity |
| 2 | Resume previous progress | 1 | Beta learners will not complete in one sitting. Without resume, they start over every time. |
| 3 | Video placeholder with chapter labels | 1 | Architecture must be ready before the video is filmed |
| 4 | Transcript accordion (empty/placeholder) | 1 | Must be in place structurally from day one |
| 5 | Six-scene progress strip (sticky, mobile) | Global | Learner must always know where they are |
| 6 | Minimal sticky nav (no sidebar) | Global | Sidebar removed; nav must work on all viewports |
| 7 | Low-capacity mode toggle (global) | Global | Core accessibility feature for the stated audience |
| 8 | Auto-save on blur + 30s interval | Global | All inputs save silently without requiring explicit action |
| 9 | Scene 2 textarea + save | 2 | First learner output; must work |
| 10 | Label selector grid (8 labels, Scene 3) | 3 | Core recognition interaction |
| 11 | Label focus selector + reveal panel (8 content blocks) | 3 | Primary reframe mechanism |
| 12 | Label interpretation textarea | 3 | Snapshot Field 2 source |
| 13 | Support-then textarea | 3 | Snapshot Field 3 source |
| 14 | EF checkboxes (6 areas, Scene 4) | 4 | Snapshot Field 4 source |
| 15 | Emotion chips (11 options, Scene 5) | 5 | Normalisation interaction |
| 16 | Dynamic emotional response (minimum: 4 text variants) | 5 | Core emotional support mechanism |
| 17 | Pause button + save-and-exit | 5 | Critical safety feature for this audience |
| 18 | Support link (always visible, Scene 5 and global) | 5 / Global | Non-negotiable for psychoeducation content |
| 19 | Life area selector (7 areas, Scene 6) | 6 | LRM entry point |
| 20 | Life Review Map — 5 steps, progressive unlock | 6 | Primary learning output mechanism |
| 21 | My Week 1 Snapshot — assembled display | 6 | The deliverable |
| 22 | Snapshot fields editable inline | 6 | Learner must be able to correct auto-populated text |
| 23 | Snapshot Field 5 (one sentence) — new textarea | 6 | The one field that must be written from scratch |
| 24 | Copy to clipboard | 6 | Learner needs a way to keep the Snapshot outside the browser |
| 25 | Print / save as PDF | 6 | Companion to copy; important for learners who use paper |
| 26 | Milestone tick | 6 | Meaningful close |
| 27 | Week 1 complete message | 6 | Learner must know they finished something |
| 28 | Beta session panel (static, placeholder date/link) | 6 | Connects the async and live experience |
| 29 | Week 2 preview + link | 6 | Continuity |
| 30 | Scope note (educational, not therapy) | 6 | Legal and ethical requirement |
| 31 | Mobile scene-based navigation (scene transitions, not full-page scroll) | Global | Without this, mobile is unusable for this audience |
| 32 | 44px minimum tap targets throughout | Global | WCAG + accessibility for ND learners |
| 33 | Font size 16px minimum in all inputs | Global | Prevents iOS auto-zoom |
| 34 | Keyboard navigation for all interactions | Global | Accessibility requirement |
| 35 | `aria-live` on all save confirmations and dynamic content | Global | Screen reader support |
| 36 | `prefers-reduced-motion` respected | Global | Mandatory for this audience |
| 37 | Companion Guide callout (placeholder, no live link yet) | 5 | Must indicate the guide exists even if PDF not yet supplied |

---

## P2 — Important, can follow after first participant testing

These features improve the experience meaningfully but do not block the beta from launching.

| # | Feature | Scene | Why P2 |
|---|---|---|---|
| 1 | Video player (once video is recorded and uploaded) | 1 | Can't build it without the video; architecture is in place |
| 2 | Transcript content (once video transcript exists) | 1 | Same dependency as video |
| 3 | Audio-only mode | 1 | Deferred until recording exists |
| 4 | Dynamic Snapshot Field 4 generation from EF + LRM-5 | 6 | Can use a simpler concatenation for beta |
| 5 | Snapshot field validation (prompt if Field 5 empty) | 6 | Nice-to-have before save |
| 6 | Additional life areas in LRM (add a second area) | 6 | P1 covers one area; second is optional |
| 7 | Low-cap mode: full scene-specific simplification per scene | Global | P1 covers the global toggle; per-scene simplification can follow |
| 8 | Dynamic emotional response (all combinations, not minimum 4 variants) | 5 | Beta can use simplified logic |
| 9 | Research note accordions (evidence base per scene) | 2–4 | Content needs to be written; accordion is built in P1 |
| 10 | Speed-read route (full text version) | 1 | Can use the Scene 2–5 prose directly as speed-read content for beta |
| 11 | Live date/join link in beta session panel | 6 | Add when confirmed |
| 12 | Companion Guide live link (PDF download) | 5 | Add when PDF is supplied |
| 13 | Snapshot "last edited" timestamp display | 6 | Minor UX improvement |
| 14 | Scene-level back navigation (not just dot-tap) | Global | Dot-tap resume covers most cases for beta |
| 15 | Scroll-anchoring within scene (smooth scroll to interaction) | Global | Helpful but not blocking |

---

## P3 — Future enhancement (post-beta)

These are meaningful improvements for the production course but are out of scope for founding beta.

| # | Feature | Notes |
|---|---|---|
| 1 | Snapshot persists cross-device (requires backend or account system) | localStorage is device-specific; cross-device needs a backend |
| 2 | Scrollytelling visual moment for core concept | Requires design + front-end implementation time |
| 3 | Recognition selections feeding forward to Week 2 | Requires Week 2 redesign to reference Week 1 localStorage |
| 4 | Personalised opening based on intake question | Requires intake mechanism and routing logic |
| 5 | EF selections generating personalised Snapshot Field 4 text | Can be more sophisticated than beta concatenation |
| 6 | Mobile Share API for Snapshot (native share sheet) | Browser support improving; add post-beta |
| 7 | Custom pictograms or illustrations for EF section | Requires illustration production |
| 8 | Scene slide animation (Option A: scene-based DOM architecture) | Option B (simple reveal) for beta; Option A post-beta |
| 9 | Week 2–4 back-references to Week 1 Snapshot | Requires all weeks to be redesigned |
| 10 | Progress visible on course dashboard | Requires dashboard to read `tul-w1-*` localStorage |
| 11 | Adobe Express concept boards → production visual design | Stage 2 of this design process |
| 12 | Chaptered video player with timestamp navigation | Requires the video to be produced and chaptered |

---

## Build sequence recommendation for P1

If building sequentially (one developer, single sprint):

1. **Global structure first:** Minimal nav, progress strip, scene container model, localStorage utility functions, auto-save scaffolding, `prefers-reduced-motion` CSS
2. **Scene 1:** Route choice, resume block, video placeholder, transition to Scene 2
3. **Scenes 2–5:** In order (each scene depends on the previous scene's data model)
4. **Scene 6:** LRM first (most complex), then Snapshot assembly, then milestone + closing
5. **Mobile QA:** Test every scene at 390px before declaring P1 complete
6. **Accessibility pass:** Keyboard + screen reader test at end of each scene build

---

## What is not in scope at any priority level

- Database or account system (all state in localStorage for beta and production until explicitly decided otherwise)
- AI-generated content or personalisation via API
- Push notifications or email reminders
- Community features (comments, sharing, social proof)
- Gamification (streaks, points, badges, leaderboards)
- Any feature requiring external data collection

---

*Build priorities defined. P1 is the founding beta. P2 follows first participant session feedback.*
