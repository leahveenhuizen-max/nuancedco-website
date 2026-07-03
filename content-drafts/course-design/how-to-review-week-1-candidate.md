# How to Review the Week 1 Production Candidate

Internal document. For Leah's review session only. This file is not linked anywhere on the public site.

---

## 1. Start a local server

The candidate uses relative links (to `support.html`, `week-2.html`, `course-dashboard.html`) so it needs to be served, not opened directly as a file.

Open Terminal, go to the project folder, and run:

```
cd /Users/leahveenhuizen/Desktop/Nuance/nuancedco-deploy
python3 -m http.server 8765
```

Leave that window open while you review. To stop the server later, click into that window and press `Ctrl+C`.

## 2. Open the candidate

In your browser, go to:

```
http://localhost:8765/week-1-production-candidate.html
```

Do not open the file directly from Finder (double-clicking it) — the links and some styling will not behave correctly without the server.

## 3. What to click first

1. Read the opening scene (Scene 1 — Week Opening) as a brand-new learner would.
2. Try each of the three routes once — see "Testing the routes" below.
3. Click through all six scenes in order at least once: Week Opening, Something Changed, The Old Story, How the Brain Manages Life, Relief Grief and Anger, Build Your Snapshot.
4. Open the "My Snapshot" pill (top-right on desktop, bottom pill on mobile) at least twice — once early (mostly empty) and once after completing Scene 6 (mostly full).

## 4. Testing the three routes

- **Full Journey** — click the "Full journey" card on Scene 1, then "Begin Week 1." This takes you through all six scenes in sequence using the "Continue" buttons at the bottom of each scene.
- **Low-Capacity Route** — click the "Low-capacity route" card, then toggle "Low-capacity mode" on using the switch beneath the route cards. This simplifies each scene's framing slightly; the destination content is unchanged, but the tone shifts.
- **Speed-Read** — click the "Speed-read" card. This route is intended for participants who want the core ideas without full engagement. Confirm the experience still feels respectful at speed (not a quiz, not skippable to nothing).

You do not need to fully complete the Life Review Map (Scene 6) every time — one life area, one step, is enough to see how it behaves.

## 5. Resuming and starting over

- Close the browser tab (or just reload the page) partway through a scene. Reopen the URL — you should see a "Continue where you left off" prompt on Scene 1 naming the scene you were in. Click "Resume" to jump back there.
- To fully reset your test data, click "Start over" next to the resume prompt, or open your browser's developer console and run:

```js
Object.keys(localStorage).filter(k=>k.startsWith('tul-w1-')).forEach(k=>localStorage.removeItem(k));
```

Then reload the page. This clears only the Week 1 candidate's saved data — it does not touch anything else in your browser.

## 6. Testing on mobile

You do not need a phone. In your desktop browser:

- Chrome/Edge: open DevTools (`Cmd+Option+I`), click the device toolbar icon (or `Cmd+Shift+M`), and choose a phone size (e.g. iPhone 14) from the dropdown at the top.
- Safari: enable the Develop menu in Preferences > Advanced, then use Develop > Enter Responsive Design Mode.
- Or simply narrow your browser window manually to roughly 390px wide.

Check specifically: the "My Snapshot" pill should sit fixed at the bottom of the screen (not top-right), label and emotion grids should reflow to fewer columns, and there should be no sideways scrolling on any scene.

## 7. What to ignore for now

These are known, intentional placeholders — do not flag them as bugs:

- "Audio placeholder — not yet recorded" and "Video placeholder — not yet recorded" notes from Leah
- The "Video coming soon" badge and disabled play button on the lesson video frame
- Video chapter labels with no actual video behind them
- The Companion Guide card showing "Available in Resources" with no working link yet
- The weekly catch-up panel showing "[to be confirmed]" for date and join link
- The browser tab title saying "(Production Candidate)" — this will be removed if/when the file replaces `week-1.html`

## 8. What feedback to record

For each scene, useful feedback looks like:

- Does the tone feel right (warm, accurate, not clinical, not coach-y)?
- Does anything feel rushed, patronising, or too slow?
- Does the Snapshot feel like something you would actually want to keep?
- Anything that reads as a contradiction with brand rules (job title, course framing, claims of being free, em dashes, etc.)
- Anything broken: a button that does nothing, text that overlaps, a step that won't unlock.

A simple running list per scene (even just bullet points) is enough — there is no fixed feedback template required.
