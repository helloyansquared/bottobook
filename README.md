# BotToBook — Character.AI chats to PDF & EPUB

**Use it: https://bottobook.pages.dev/**

Open your Character.AI data export (the password-protected ZIP from the email, or `message.json`), read every chat,
and bind them into a PDF or EPUB book with chapters, names and a cover. Everything runs in the browser; the export is
never uploaded.

- Reads the official export (`message.json`, `character.json`, `user.json`), CAI Tools JSON / Tavern JSONL and SillyTavern `.jsonl`.
- The official export doesn't record who wrote each message, so sides are worked out from turn order and reply timing
  (and can be swapped with one click).
- EPUB 3 with an NCX table of contents; long chats are split into parts so e-readers stay fast.
- PDF via the browser's print engine (cover, contents, a chapter per chat, page numbers), so every script and emoji renders.

## Develop

```
python3 build.py https://bottobook.pages.dev/ pdt_XXXX   # writes public/ and fills in the Dodo product id
node test/core.test.mjs && node test/license.test.mjs
```

`public/` is the static site; `functions/api/license.js` is a Cloudflare Pages Function that checks Pro licence keys
against Dodo Payments' public licence endpoints (no API key needed) and only accepts keys for this product.

ZIP decryption uses [zip.js](https://github.com/gildas-lormeau/zip.js) (BSD-3-Clause, `public/vendor/`).

Not affiliated with Character Technologies, Inc. or Character.AI.
