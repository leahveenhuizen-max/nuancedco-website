/* Grief After Diagnosis course. Phase 1: progress, notes and settings are saved in this browser only (localStorage). */
(function () {
  var P = 'gc:';
  var LESSONS = {1: ['1.1', '1.2', '1.3'], 2: ['2.1', '2.2', '2.3'], 3: ['3.1', '3.2', '3.3'], 4: ['4.1', '4.2', '4.3', '4.4'], 5: ['5.1', '5.2', '5.3']};
  var TOTAL = 16;
  function get(k, d) { try { var v = localStorage.getItem(P + k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(P + k, JSON.stringify(v)); return true; } catch (e) { return false; } }

  var root = document.documentElement;
  var SIZES = [0.9, 1, 1.15, 1.3];
  var prefs = get('prefs', {});
  var sysReduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function applyPrefs() {
    var s = typeof prefs.size === 'number' ? prefs.size : 1;
    root.style.fontSize = (18 * SIZES[s]) + 'px';
    root.setAttribute('data-motion', prefs.motion ? prefs.motion : (sysReduce ? 'reduce' : 'full'));
    root.setAttribute('data-font', prefs.font || 'standard');
    var m = document.querySelector('[data-gc="motion"]');
    if (m) m.setAttribute('aria-pressed', String(root.getAttribute('data-motion') === 'reduce'));
    var f = document.querySelector('[data-gc="font"]');
    if (f) f.setAttribute('aria-pressed', String(prefs.font === 'readable'));
  }
  applyPrefs(); // runs in <head> so there is no flash of the wrong size

  function done() { return get('lessons', {}); }
  function modCount(n, d) { return LESSONS[n].filter(function (id) { return d[id]; }).length; }

  function render() {
    var d = done(), visited = get('visited', {}), total = 0;
    Array.prototype.forEach.call(document.querySelectorAll('[data-lstatus]'), function (el) {
      var id = el.getAttribute('data-lstatus');
      var st = d[id] ? 'complete' : visited[id] ? 'visited' : 'new';
      el.textContent = st === 'complete' ? 'Complete' : st === 'visited' ? 'In progress' : 'Not started';
      el.setAttribute('data-state', st);
    });
    for (var n = 1; n <= 5; n++) {
      var c = modCount(n, d); total += c;
      var len = LESSONS[n].length;
      Array.prototype.forEach.call(document.querySelectorAll('[data-module-progress="' + n + '"]'), function (el) {
        el.textContent = c + ' of ' + len + ' lessons complete';
        el.setAttribute('data-state', c === len ? 'complete' : 'new');
      });
      var btn = document.querySelector('[data-start="' + n + '"]');
      if (btn) btn.textContent = (c === len ? 'Review' : c > 0 ? 'Continue' : 'Start') + ' module ' + n;
    }
    var t = document.getElementById('gc-progress-text');
    if (t) t.textContent = total + ' of ' + TOTAL + ' lessons complete';
    var bar = document.querySelector('.gc-progress');
    if (bar) { bar.setAttribute('aria-valuenow', total); bar.firstElementChild.style.width = (total / TOTAL * 100) + '%'; }
    var lb = document.querySelector('[data-gc="lesson-complete"]');
    if (lb) {
      var on = !!d[lb.getAttribute('data-lesson')];
      lb.setAttribute('aria-pressed', String(on));
      lb.textContent = on ? 'Lesson complete. Mark as not complete' : 'Mark lesson as complete';
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    applyPrefs();
    var lp = document.querySelector('[data-lesson-page]');
    if (lp) { var v = get('visited', {}); v[lp.getAttribute('data-lesson-page')] = true; set('visited', v); }
    render();

    // Reflection notes
    Array.prototype.forEach.call(document.querySelectorAll('textarea[data-note]'), function (ta) {
      var key = ta.getAttribute('data-note');
      var msg = document.getElementById(ta.getAttribute('aria-describedby'));
      var notes = get('notes', {});
      if (notes[key]) ta.value = notes[key];
      var timer;
      ta.addEventListener('input', function () {
        clearTimeout(timer);
        timer = setTimeout(function () {
          var all = get('notes', {}); all[key] = ta.value;
          var ok = set('notes', all);
          if (msg) msg.textContent = ok ? 'Saved on this device' : 'This browser could not save your note. Copy it somewhere safe.';
        }, 500);
      });
    });

    var dlg = document.getElementById('gc-crisis');
    var opener = null;

    document.addEventListener('click', function (e) {
      var b = e.target.closest('[data-gc]');
      if (!b) return;
      var a = b.getAttribute('data-gc');
      var s = typeof prefs.size === 'number' ? prefs.size : 1;
      if (a === 'size-down') { prefs.size = Math.max(0, s - 1); }
      else if (a === 'size-up') { prefs.size = Math.min(SIZES.length - 1, s + 1); }
      else if (a === 'size-reset') { prefs.size = 1; }
      else if (a === 'font') { prefs.font = prefs.font === 'readable' ? 'standard' : 'readable'; }
      else if (a === 'motion') { prefs.motion = root.getAttribute('data-motion') === 'reduce' ? 'full' : 'reduce'; }
      else if (a === 'captions') {
        var on = b.getAttribute('aria-pressed') !== 'true';
        b.setAttribute('aria-pressed', String(on));
        b.textContent = on ? 'Captions on' : 'Captions off';
        var cm = document.querySelector('[data-captions-msg]');
        if (cm) cm.textContent = on ? 'Captions will show on the video once it is recorded.' : '';
        var vid = document.querySelector('.gc-video video');
        if (vid && vid.textTracks && vid.textTracks[0]) vid.textTracks[0].mode = on ? 'showing' : 'hidden';
        return;
      }
      else if (a === 'transcript') {
        var panel = document.getElementById(b.getAttribute('aria-controls'));
        var open = b.getAttribute('aria-expanded') !== 'true';
        b.setAttribute('aria-expanded', String(open));
        b.textContent = open ? 'Hide transcript' : 'Show transcript';
        if (panel) panel.hidden = !open;
        return;
      }
      else if (a === 'print') {
        Array.prototype.forEach.call(document.querySelectorAll('details.gc-section'), function (d) { d.open = true; });
        window.print();
        return;
      }
      else if (a === 'toggle-all') {
        var op = b.getAttribute('aria-pressed') !== 'true';
        Array.prototype.forEach.call(document.querySelectorAll('details.gc-section'), function (d) { d.open = op; });
        b.setAttribute('aria-pressed', String(op));
        b.textContent = op ? 'Collapse all sections' : 'Expand all sections';
        return;
      }
      else if (a === 'lesson-complete') {
        var id = b.getAttribute('data-lesson'), d = done();
        if (d[id]) delete d[id]; else d[id] = true;
        var ok = set('lessons', d);
        render();
        var m = document.querySelector('[data-complete-msg]');
        if (m) m.textContent = ok ? (d[id] ? 'Nice work. Saved on this device.' : 'Marked as not complete.') : 'This browser could not save your progress.';
        return;
      }
      else if (a === 'reset') {
        if (b.getAttribute('data-armed') !== '1') {
          b.setAttribute('data-armed', '1');
          b.textContent = 'Are you sure? Select again to clear everything on this device';
          return;
        }
        try { ['lessons', 'visited', 'notes', 'progress'].forEach(function (k) { localStorage.removeItem(P + k); }); } catch (err) {}
        b.removeAttribute('data-armed');
        b.textContent = 'Cleared. Your progress and notes have been removed from this device.';
        render();
        return;
      }
      else if (a === 'crisis-open') {
        if (dlg && typeof dlg.showModal === 'function') { opener = b; dlg.showModal(); dlg.querySelector('.gc-close').focus(); }
        else { window.location.href = 'support.html#crisis'; }
        return;
      }
      else if (a === 'crisis-close') { if (dlg) dlg.close(); return; }
      else return;
      set('prefs', prefs);
      applyPrefs();
    });

    if (dlg) dlg.addEventListener('close', function () { if (opener) opener.focus(); });
  });
})();
