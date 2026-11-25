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

## The Character.AI export format (checked November 2026)

| Item | What the official export contains |
|---|---|
| Delivery | An emailed link to a ZIP. Character.AI says 3–4 weeks; the link is valid for 7 days. |
| ZIP password | **The account's email address, in lowercase.** |
| Layout | A folder named after your username, with a data folder inside. |
| `user.json` | Your account profile. |
| `character.json` | Only characters you created: name, greeting, definition. |
| `message.json` | Every message from all your chats, in one list. |
| Fields per message | `chat_id`, `candidate_id`, `raw_content`, `create_time` (microsecond precision). |
| Not included | Who wrote each message, and the name of the character you chatted with. |

More: [what message.json contains](https://bottobook.pages.dev/character-ai-message-json/) ·
[the ZIP password](https://bottobook.pages.dev/character-ai-export-zip-password/) ·
[Character.AI chat to PDF](https://bottobook.pages.dev/character-ai-chat-to-pdf/) ·
[chats to Kindle (EPUB)](https://bottobook.pages.dev/character-ai-to-kindle/)

## Develop

```
python3 build.py https://bottobook.pages.dev/ pdt_XXXX   # writes public/ (home, guide pages, privacy, sitemap, robots, llms.txt)
node test/core.test.mjs && node test/license.test.mjs
```

Words live in `src/content.py` (FAQ answers feed both the visible FAQ and the FAQPage JSON-LD); `public/` is the static site; `functions/api/license.js` is a Cloudflare Pages Function that checks Pro licence keys
against Dodo Payments' public licence endpoints (no API key needed) and only accepts keys for this product.

## License

MIT — see [LICENSE](LICENSE). ZIP decryption uses [zip.js](https://github.com/gildas-lormeau/zip.js) (BSD-3-Clause, licence in `public/vendor/`).

The code is open; BotToBook Pro on the hosted site (PDF/EPUB/HTML books of your own export) is a $4.99 one-time unlock that supports the project.

Not affiliated with Character Technologies, Inc. or Character.AI.
