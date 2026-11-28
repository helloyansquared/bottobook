import fs from 'fs';
const html = fs.readFileSync(new URL('../src/index.html', import.meta.url), 'utf8');
const core = html.split('/*CORE-START*/')[1].split('/*CORE-END*/')[0];
const CORE = new Function(core + '; return CORE;')();
const assert = (c, m) => { if (!c) { console.error('FAIL', m); process.exitCode = 1; } else console.log('ok', m); };

// 1. official-style export: array, no roles, all chats mixed
const sample = JSON.parse(html.split('<script id="sample" type="application/json">')[1].split('</script>')[0]);
let p = CORE.parseExport([{ name: 'message.json', text: JSON.stringify(sample) }]);
assert(p.chats.length === 2, '2 chats from sample');
assert(p.chats[0].messages.length === 7 && p.chats[0].offset === 0, 'lighthouse 7 msgs, offset 0');
assert(CORE.roleAt(p.chats[0], 0) === 'char' && CORE.roleAt(p.chats[0], 1) === 'user', 'alternation');
// shuffled order sorted by time
const sh = [...sample].reverse();
p = CORE.parseExport([{ name: 'message.json', text: JSON.stringify(sh) }]);
assert(p.chats[0].messages[0].text.startsWith('*The lamp room'), 'sorted by time');
// JSON lines
p = CORE.parseExport([{ name: 'message.jsonl', text: sample.map(x => JSON.stringify(x)).join('\n') }]);
assert(p.chats.length === 2, 'jsonl');
// wrapped in object
p = CORE.parseExport([{ name: 'message.json', text: JSON.stringify({ messages: sample }) }, { name: 'user.json', text: JSON.stringify({ first_name: 'Alex', email: 'a@b.c', date_joined: '2023-01-01' }) }, { name: 'character.json', text: JSON.stringify([{ name: 'Wren', greeting: 'Hi', definition: 'x', external_id: 'abc' }]) }]);
assert(p.userName === 'Alex' && p.characters.includes('Wren'), 'user + characters');
// offset guess when first message is the user's (user wrote first; character replies fast)
const t0 = Date.parse('2026-01-01T10:00:00Z');
const msgs = []; let t = t0;
for (let i = 0; i < 20; i++) { t += (i % 2 === 0 ? 60000 + i * 1000 : 4000); msgs.push({ chat_id: 'x', raw_content: 'm' + i, create_time: new Date(t).toISOString().replace('T', ' ').replace('Z', '000+00:00') }); }
p = CORE.parseExport([{ name: 'm.json', text: JSON.stringify(msgs) }]);
assert(p.chats[0].offset === 1, 'guess offset 1 when user speaks first');
// timeOf formats
assert(CORE.timeOf('2026-11-01 09:00:00.123456+00:00') === Date.parse('2026-11-01T09:00:00.123Z'), 'microsecond time');
assert(CORE.timeOf('2026-11-01 09:00:00') === Date.parse('2026-11-01T09:00:00Z'), 'no-zone time as UTC');
assert(CORE.timeOf(1730451600) === 1730451600000, 'unix seconds');
// SillyTavern / CAI Tools Tavern JSONL with roles
const st = [{ user_name: 'Me', character_name: 'Nova', create_date: '2024-1-1' }, { name: 'Nova', is_user: false, mes: 'Hello traveller', send_date: '2024-1-1 @10h 00m 00s 000ms' }, { name: 'Me', is_user: true, mes: 'Hi!', send_date: '2024-1-1 @10h 01m 00s 000ms' }];
p = CORE.parseExport([{ name: 'nova.jsonl', text: st.map(x => JSON.stringify(x)).join('\n') }]);
assert(p.chats.length === 1 && p.chats[0].known && p.chats[0].charName === 'Nova' && p.chats[0].userName === 'Me', 'sillytavern roles + names');
assert(CORE.roleAt(p.chats[0], 1) === 'user', 'known role used');
// conversations shape
p = CORE.parseExport([{ name: 'c.json', text: JSON.stringify({ conversations: [{ id: 'a', character_name: 'Quill', messages: [{ author: { name: 'Quill', is_human: false }, text: 'Morning', created_at: '2026-10-20T08:00:00Z' }, { author: { name: 'Sam', is_human: true }, text: 'Hi', created_at: '2026-10-20T08:01:00Z' }] }] }) }]);
assert(p.chats.length === 1 && p.chats[0].charName === 'Quill' && p.chats[0].known, 'conversations shape');
// markdown
const md = CORE.mdParas('*waves* hello **there** <b>x</b>\nline2\n\npara 2 2*3*4');
assert(md[0] === '<em>waves</em> hello <strong>there</strong> &lt;b&gt;x&lt;/b&gt;<br/>line2' && md[1] === 'para 2 2*3*4', 'markdown ' + JSON.stringify(md));
// EPUB
p = CORE.parseExport([{ name: 'message.json', text: JSON.stringify(sample) }]);
p.chats[0].charName = 'Wren';
const big = { ...p.chats[1], messages: Array.from({ length: 800 }, (_, i) => ({ text: 'Message ' + i + ' 😀 中文 <&>', role: '', name: '', at: t0 + i * 3600e3 })) };
const epub = CORE.buildEpub({ title: 'Test & Book', author: 'Sam', lang: 'en', cover: null, chats: [p.chats[0], big], opt: { times: true, days: true, lang: 'en', defUser: 'Sam' } });
fs.writeFileSync('/tmp/test.epub', epub);
assert(epub.length > 1000, 'epub built ' + epub.length);
const pr = CORE.printHtml({ title: 'T', chats: p.chats, opt: { days: true, defUser: 'Sam' }, size: 'paperback' });
fs.writeFileSync('/tmp/print.html', pr);
fs.writeFileSync('/tmp/read.html', CORE.readHtml({ title: 'T', chats: p.chats, opt: { days: true, defUser: 'Sam' } }));
assert(pr.includes('Conversations with Character') || pr.includes('Conversations with'), 'print html');
console.log(CORE.txtOf(p.chats[0], 'Sam').slice(0, 300));

// SillyTavern native .jsonl: header line + one message per line, roles follow the swap/offset, names from the chat
{
  const p2 = CORE.parseExport([{ name: 'message.json', text: JSON.stringify(sample) }]);
  const c = { ...p2.chats[0], charName: 'Wren', userName: 'Sam' };
  const out = CORE.stOf(c, '');
  const L = out.trim().split('\n').map(l => JSON.parse(l));
  assert(!out.startsWith('﻿') && out.endsWith('\n'), 'st: no BOM, trailing newline');
  assert(L[0].chat_metadata && L[0].user_name === 'unused' && L[0].character_name === 'unused' && !('mes' in L[0]), 'st: header line');
  assert(L.length === c.messages.length + 1, 'st: one line per message');
  assert(L[1].name === 'Wren' && L[1].is_user === false && L[2].name === 'Sam' && L[2].is_user === true, 'st: names and is_user');
  assert(L.slice(1).every(m => m.is_system === false && typeof m.mes === 'string' && m.extra && /^\d{4}-\d\d-\d\dT.*Z$/.test(m.send_date)), 'st: fields + ISO dates');
  assert(L[1].send_date === '2026-10-03T19:02:11.204Z', 'st: keeps original time');
  const sw = { ...c, offset: (c.offset + 1) % 2 };
  const L2 = CORE.stOf(sw, '').trim().split('\n').map(l => JSON.parse(l));
  assert(L2[1].is_user === true && L2[1].name === 'Sam', 'st: swap flips sides');
  // round trip through our own importer
  const back = CORE.parseExport([{ name: 'x.jsonl', text: out }]);
  assert(back.chats.length === 1 && back.chats[0].messages.length === c.messages.length && back.chats[0].messages[0].text === c.messages[0].text, 'st: round trip');
  assert(back.chats[0].charName !== 'unused' && back.chats[0].userName !== 'unused', 'st: header "unused" is not a name');
  assert(CORE.stName(c, '') === 'Wren - Oct 3, 2026 – Oct 4, 2026', 'st: file name = character + dates');
  const z = CORE.zip([{ name: 'a.jsonl', data: out }, { name: 'b.jsonl', data: out }]);
  assert(z[0] === 0x50 && z[1] === 0x4b, 'st: zip bytes');
}
