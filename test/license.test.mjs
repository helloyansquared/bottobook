import fs from 'fs';
const src = fs.readFileSync(new URL('../functions/api/license.js', import.meta.url), 'utf8').replace('__PRODUCT_ID__', 'pdt_TEST');
const mod = await import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));
const cases = [
  [{ action: 'activate', license_key: 'K' }, 201, { id: 'lki_1', product: { product_id: 'pdt_TEST' }, customer: { email: 'x@y.z' } }, 200, true],
  [{ action: 'activate', license_key: 'K' }, 201, { id: 'lki_1', product: { product_id: 'pdt_OTHER' } }, 403, false],
  [{ action: 'activate', license_key: 'K' }, 422, {}, 422, false],
  [{ action: 'activate', license_key: 'K' }, 404, {}, 404, false],
  [{ action: 'validate', license_key: 'K', instance_id: 'lki_1' }, 200, { valid: true }, 200, true],
  [{ action: 'delete', license_key: 'K' }, 200, {}, 400, false],
];
for (const [input, st, body, wantStatus, wantOk] of cases) {
  let sent;
  globalThis.fetch = async (url, init) => { sent = { url, body: JSON.parse(init.body) }; return new Response(JSON.stringify(body), { status: st }); };
  const res = await mod.onRequestPost({ request: new Request('https://x/api/license', { method: 'POST', body: JSON.stringify(input) }) });
  const j = await res.json();
  const ok = res.status === wantStatus && j.ok === wantOk && !JSON.stringify(j).includes('@');
  console.log(ok ? 'ok' : 'FAIL', input.action, st, '->', res.status, JSON.stringify(j), sent && sent.url);
}
