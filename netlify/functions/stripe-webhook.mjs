// Stripe -> MailerLite: when someone pays for the grief course, add them to the right
// MailerLite group. A MailerLite automation on each group sends the welcome email.
// Netlify environment variables needed: STRIPE_WEBHOOK_SECRET, MAILERLITE_API_KEY
import crypto from 'node:crypto';

const GROUPS = {
  plink_1UcHsgS8QGR6JGvqaDyLkeyL: 'Grief course - full',
  plink_1UcHsiS8QGR6JGvqoUKcrUnT: 'Grief course - lessons only',
};
const ML = 'https://connect.mailerlite.com/api';

function validSignature(payload, header, secret) {
  if (!header || !secret) return false;
  const parts = Object.fromEntries(header.split(',').map((p) => p.split('=')));
  const t = parts.t;
  const sigs = header.split(',').filter((p) => p.startsWith('v1=')).map((p) => p.slice(3));
  if (!t || !sigs.length || Math.abs(Date.now() / 1000 - Number(t)) > 600) return false;
  const expected = crypto.createHmac('sha256', secret).update(`${t}.${payload}`).digest('hex');
  return sigs.some((s) => s.length === expected.length && crypto.timingSafeEqual(Buffer.from(s), Buffer.from(expected)));
}

async function ml(path, opts = {}) {
  const res = await fetch(ML + path, {
    ...opts,
    headers: { Authorization: `Bearer ${process.env.MAILERLITE_API_KEY}`, 'Content-Type': 'application/json', Accept: 'application/json', ...(opts.headers || {}) },
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(`MailerLite ${path} ${res.status}: ${JSON.stringify(body)}`);
  return body;
}

async function groupId(name) {
  const found = await ml(`/groups?filter[name]=${encodeURIComponent(name)}&limit=25`);
  const g = (found.data || []).find((x) => x.name === name);
  if (g) return g.id;
  return (await ml('/groups', { method: 'POST', body: JSON.stringify({ name }) })).data.id;
}

export default async (req) => {
  if (req.method !== 'POST') return new Response('Method not allowed', { status: 405 });
  const payload = await req.text();
  if (!validSignature(payload, req.headers.get('stripe-signature'), process.env.STRIPE_WEBHOOK_SECRET)) {
    return new Response('Invalid signature', { status: 400 });
  }
  const event = JSON.parse(payload);
  if (event.type !== 'checkout.session.completed') return new Response('Ignored', { status: 200 });

  const s = event.data.object;
  const group = GROUPS[s.payment_link];
  const email = s.customer_details && s.customer_details.email;
  if (!group || !email) return new Response('Not a course purchase', { status: 200 });

  const name = (s.customer_details.name || '').trim();
  const heard = ((s.custom_fields || []).find((f) => f.key === 'heard') || {}).text;
  try {
    const id = await groupId(group);
    await ml('/subscribers', {
      method: 'POST',
      body: JSON.stringify({
        email,
        fields: { name: name.split(' ')[0] || '', last_name: name.split(' ').slice(1).join(' ') },
        groups: [id],
        status: 'active',
      }),
    });
    console.log('Added', email, 'to', group, heard ? `(heard: ${heard.value})` : '');
    return new Response('OK', { status: 200 });
  } catch (err) {
    console.error(err);
    return new Response('MailerLite error', { status: 500 }); // Stripe will retry
  }
};

export const config = { path: '/api/stripe-webhook' };
