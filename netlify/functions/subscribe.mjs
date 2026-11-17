// Website newsletter signup -> MailerLite "Newsletter" group.
// Uses the MAILERLITE_API_KEY Netlify environment variable.
const ML = 'https://connect.mailerlite.com/api';
const GROUP = 'Newsletter';

async function ml(path, opts = {}) {
  const res = await fetch(ML + path, {
    ...opts,
    headers: { Authorization: `Bearer ${process.env.MAILERLITE_API_KEY}`, 'Content-Type': 'application/json', Accept: 'application/json' },
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(`MailerLite ${path} ${res.status}: ${JSON.stringify(body)}`);
  return body;
}

function back(url, to) {
  return new Response(null, { status: 303, headers: { Location: new URL(to, url).toString() } });
}

export default async (req) => {
  if (req.method !== 'POST') return new Response('Method not allowed', { status: 405 });
  const form = await req.formData();
  const ret = String(form.get('return') || '/');
  const safeRet = /^\/[a-z0-9\-/.]*$/i.test(ret) ? ret : '/';
  if (form.get('website')) return back(req.url, '/subscribed.html'); // honeypot: quietly ignore bots
  const email = String(form.get('email') || '').trim();
  const name = String(form.get('name') || '').trim().slice(0, 80);
  const consent = form.get('consent');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || !consent) {
    return back(req.url, safeRet + (safeRet.includes('?') ? '&' : '?') + 'signup=error#newsletter');
  }
  try {
    const groups = await ml(`/groups?filter[name]=${encodeURIComponent(GROUP)}&limit=25`);
    const g = (groups.data || []).find((x) => x.name === GROUP);
    const gid = g ? g.id : (await ml('/groups', { method: 'POST', body: JSON.stringify({ name: GROUP }) })).data.id;
    await ml('/subscribers', {
      method: 'POST',
      body: JSON.stringify({ email, fields: name ? { name } : {}, groups: [gid], status: 'active' }),
    });
    const next = String(form.get('next') || '');
    return back(req.url, next === '/free-guides.html' ? '/free-guides.html' : '/subscribed.html');
  } catch (err) {
    console.error(err);
    return back(req.url, safeRet + (safeRet.includes('?') ? '&' : '?') + 'signup=error#newsletter');
  }
};

export const config = { path: '/api/subscribe' };
