# Week 1 Replacement Plan

How to replace `week-1.html` with the production candidate, when Leah decides to proceed. **This plan is documentation only — no replacement has been made.**

---

## Files that would change

| File | Change |
|---|---|
| `week-1.html` | Body replaced with the candidate's content and structure. This is the only public page that changes. |
| `week-1-production-candidate.html` | Deleted (or renamed to an internal archive name) once its content is merged in, so there is no duplicate live page lying around. |
| `nc-course.css` | Optionally updated if CSS is moved out of the candidate's inline `<style>` block (see below). |
| `week-2.html`, `week-3.html`, `week-4.html` | Not changed by this replacement, but see the Week 2 production plan for the next page in the sequence. |

No navigation file, redirect file, or other public page needs to change — nothing currently links to `week-1-production-candidate.html` (confirmed by repo-wide grep), so removing it breaks nothing.

---

## What moves from the candidate into week-1.html

Everything: the candidate is a complete, self-contained replacement, not a partial patch. Specifically:

- All six `<section class="scene">` blocks and their content
- The journey track, Snapshot indicator, and Snapshot sheet markup
- The full `<script>` block (scene logic, Snapshot assembly, LRM unlock logic, etc.)
- The print stylesheet block

Two things should **not** carry over verbatim:
- The page `<title>` and nav label both currently say "(Production Candidate)" — remove that suffix.
- The footer text "This is a production candidate for internal review" must be replaced with the real Week 1 footer copy (matching the footer pattern used elsewhere on the live site).

---

## CSS: inline or moved to nc-course.css?

**Recommendation: keep it inline in `week-1.html` for this replacement, do not merge into `nc-course.css` yet.**

Reasoning:
- The candidate's CSS is scene-specific (route cards, EF rows, emotion chips, Life Review Map steps, Snapshot sheet) and does not currently overlap with the variables or components in `nc-course.css` used by the other pages.
- Weeks 2-4 will need their own scene-specific variants of several of these components once rebuilt. Pulling shared, *stable* patterns (the Snapshot sheet, the journey track, the "Leah moment" block, the route-selection cards) into `nc-course.css` makes more sense **after** Week 2 is built, once it's clear which parts are genuinely shared across all four weeks versus specific to Week 1's content.
- Moving CSS prematurely risks breaking the other three (still-live) week pages, which currently rely on `nc-course.css` for their own layout.

Action: leave as-is now. Revisit consolidation into `nc-course.css` as part of the course experience system once Week 2's rebuild confirms which components repeat.

## JS: inline or separated?

**Recommendation: keep it inline in `week-1.html`, same reasoning as CSS.**

The script uses a `tul-w1-` localStorage namespace specific to Week 1. If/when Week 2-4 are rebuilt on the same pattern, each week's script will use its own namespace (e.g. `tul-w2-`) and most of the logic (scene navigation, resume, route selection) will be near-identical boilerplate. At that point it would be worth extracting the *shared* parts into a single `course-scene-engine.js` file referenced by all four week pages, with only the per-week content (label lists, EF lists, Snapshot field mapping) staying inline or in a small per-week config block. Doing this now, for one page, adds a build step for no real benefit yet.

---

## Screenshots to capture after replacement

Once `week-1.html` is replaced, capture (desktop 1440px and mobile 390px) for each of the six scenes, plus the open Snapshot sheet, for the record and for comparison if anything regresses later:

1. Scene 1 — Week Opening (route selection visible)
2. Scene 2 — Something Changed
3. Scene 3 — The Old Story (with a label selected and reveal panel open)
4. Scene 4 — How the Brain Manages Life (with at least one EF item checked)
5. Scene 5 — Relief, Grief and Anger (with emotion chips selected)
6. Scene 6 — Build Your Snapshot (with Life Review Map and Snapshot doc both populated)
7. Snapshot sheet open (the slide-in panel)

Save these to `content-drafts/course-design/post-replacement-review/` so there is a dated record distinct from the pre-replacement screenshots already in `production-candidate-review/`.

---

## How to test after replacement

1. Serve the site locally (`python3 -m http.server 8765` from the project root) and load `http://localhost:8765/week-1.html` directly — confirm the URL itself now serves the new content, not the old long-scroll page.
2. Re-run the full QA checklist from this review pass: all three routes, resume/start-over, all interactions, Snapshot copy/print, mobile viewport, console errors.
3. Confirm `week-2.html`'s "Coming in Week 2" link target and the dashboard's link to Week 1 both still resolve correctly to the new page.
4. Confirm no other page (`course-dashboard.html`, `course.html`, `downloads.html`) references content or anchors that only existed in the old long-scroll `week-1.html` (e.g. old section IDs used in deep links).
5. Have Leah do a manual read-through in a real browser (not just devtools) before calling it done.

---

## Rollback plan

Because this is a single-file replacement with no shared CSS/JS dependencies created elsewhere, rollback is simple:

1. `git diff week-1.html` to see the change, or `git show HEAD:week-1.html > week-1-rollback-backup.html` taken *before* the replacement, kept until the new page has been live and reviewed for at least a few days.
2. If something is wrong post-replacement: `git checkout -- week-1.html` (if uncommitted) or revert the specific commit that made the change (if committed) restores the prior long-scroll page immediately.
3. Keep `week-1-production-candidate.html` (or an archived copy of it) until the replacement has been confirmed stable, in case a partial rollback of just the new interactive layer is needed while keeping other site changes.

---

## Suggested commit message (when Leah is ready to commit)

```
Replace week-1.html with scene-based production candidate

Six-scene interactive structure replaces the long-scroll page.
Adds persistent Week 1 Snapshot, route selection (Full Journey /
Low-Capacity / Speed-Read), and resume support. Content and
interactions unchanged from the reviewed candidate; only the
"(Production Candidate)" labelling and footer copy were removed
for live use.
```

Do not commit until Leah has explicitly approved the replacement and reviewed the live page locally.
