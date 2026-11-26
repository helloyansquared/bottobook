# BotToBook — Character.AI chats to PDF & EPUB

**Use it: https://bottobook.yansquared.com/**

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

More: [what message.json contains](https://bottobook.yansquared.com/character-ai-message-json/) ·
[the ZIP password](https://bottobook.yansquared.com/character-ai-export-zip-password/) ·
[Character.AI chat to PDF](https://bottobook.yansquared.com/character-ai-chat-to-pdf/) ·
[chats to Kindle (EPUB)](https://bottobook.yansquared.com/character-ai-to-kindle/)

## Develop

```
python3 build.py https://bottobook.yansquared.com/ pdt_XXXX   # writes public/ (home, guide pages, privacy, sitemap, robots, llms.txt)
node test/core.test.mjs && node test/license.test.mjs
```

Words live in `src/content.py` (FAQ answers feed both the visible FAQ and the FAQPage JSON-LD); `public/` is the static site; `functions/api/license.js` is a Cloudflare Pages Function that checks Pro licence keys
against Dodo Payments' public licence endpoints (no API key needed) and only accepts keys for this product.

## Self-hosting

BotToBook is MIT-licensed and runs entirely in the browser. A self-hosted copy has every feature unlocked, including
full PDF, EPUB and HTML books: no licence key, no account, no server code.

```
git clone https://github.com/helloyansquared/bottobook
cd bottobook
python3 build.py http://localhost:8000/      # no product id = self-hosted build, everything unlocked
cd public && python3 -m http.server 8000
```

Then open http://localhost:8000/. (The `public/` folder committed here is the hosted build; rebuild it as above.)

## What the hosted site charges for

On https://bottobook.yansquared.com/ these are free: opening the export (including the password ZIP), reading every chat,
renaming and swapping speakers, downloading any chat as TXT, and a 30-message preview book. Full PDF/EPUB/HTML books
need a $4.99 one-time licence key, which pays for the hosted version and ongoing development. The key is only checked
when a Dodo Payments product id is passed to `build.py`; a self-hosted build doesn't do that.

## License

MIT — see [LICENSE](LICENSE). Third-party code: see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
The BotToBook name and logo are not covered by the MIT license.

Not affiliated with Character Technologies, Inc. or Character.AI.

## Also by YanSquared

- [FicToEpub](https://fictoepub.yansquared.com/) — AO3 HTML downloads to EPUB
- [FicWrapped](https://ficwrapped.pages.dev/) — your AO3 year in review
