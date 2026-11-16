// Password gate for the Grief After Diagnosis course area.
// The password is set in Netlify: Site configuration > Environment variables > COURSE_PASSWORD
const COOKIE = 'gc_access';

async function token(pw) {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode('nuancedco-gc:' + pw));
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

export default async (request, context) => {
  const pw = Netlify.env.get('COURSE_PASSWORD');
  const url = new URL(request.url);
  if (!pw) return Response.redirect(new URL('/grief-course/', url), 302);
  const good = await token(pw);

  if (url.pathname === '/grief-course/login') {
    if (request.method !== 'POST') return Response.redirect(new URL('/grief-course/login.html', url), 302);
    const form = await request.formData();
    const next = String(form.get('next') || '');
    const safe = /^\/grief-course\/[a-z0-9-]+(\.html)?$/.test(next) ? next : '/grief-course/home.html';
    if (String(form.get('password') || '').trim() === pw.trim()) {
      return new Response(null, {
        status: 303,
        headers: {
          Location: safe,
          'Set-Cookie': `${COOKIE}=${good}; Path=/grief-course; Max-Age=31536000; HttpOnly; Secure; SameSite=Lax`,
        },
      });
    }
    return Response.redirect(new URL('/grief-course/login.html?error=1&next=' + encodeURIComponent(safe), url), 303);
  }

  if (context.cookies.get(COOKIE) === good) return;
  return Response.redirect(new URL('/grief-course/login.html?next=' + encodeURIComponent(url.pathname), url), 302);
};

export const config = {
  path: [
    '/grief-course/login',
    '/grief-course/home',
    '/grief-course/home.html',
    '/grief-course/live-sessions',
    '/grief-course/live-sessions.html',
    '/grief-course/module-*',
    '/grief-course/lesson-*',
  ],
};
