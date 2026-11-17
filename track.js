/* Nuanced Co. click tracking for Google Analytics (G-0ZMMJLTMJD). */
(function () {
  function send(name, params) {
    if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
  }
  var TIERS = {
    '4gMcN7eIX4rKgla0cq1RC04': 'Full course ($397)',
    '4gM14p7gv9M4fh68IW1RC05': 'Lessons only ($197)'
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a, button');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var text = (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    var where = location.pathname;
    if (a.dataset && a.dataset.track) {
      send(a.dataset.track, { link_text: text, page_path: where });
    }
    if (href.indexOf('buy.stripe.com') > -1) {
      var id = href.split('/').pop();
      send('enrol_click', { tier: TIERS[id] || id, link_text: text, page_path: where });
      return;
    }
    if (/grief-course\/?(index\.html)?$|grief-course\/?#/.test(href) || href === 'index.html#enrol' || href === '#enrol') {
      send('course_click', { link_text: text, page_path: where });
      return;
    }
    if (/login(\.html)?$/.test(href)) {
      send('course_login_click', { page_path: where });
      return;
    }
    if (/(^|\/)book(\.html)?$/.test(href)) {
      send('book_call_click', { link_text: text, page_path: where });
      return;
    }
    if (/\.pdf$/i.test(href)) {
      send('guide_download', { file_name: href.split('/').pop(), page_path: where });
    }
  }, true);
  if (/\/enrolled(\.html)?$/.test(location.pathname)) send('course_purchase', {});
})();
