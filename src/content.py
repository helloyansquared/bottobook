# Single source for the site's words: FAQ answers (visible text and FAQPage JSON-LD are generated
# from the same strings, so they can't drift), the export facts table, and the guide pages.
# Plain text in Q&A answers (no HTML) so the JSON-LD and the page say exactly the same thing.

LAST_UPDATED = "2026-11-25"      # visible "Last updated" + dateModified
PUBLISHED = "2026-11-25"
EMAIL = "hello@yansquared.com"
GITHUB = "https://github.com/helloyansquared/bottobook"

# ── Q&A bank ──────────────────────────────────────────────────────────────────
QA = {
 "can_export": ("Can Character AI chats be exported?",
  "Yes. Character.AI has an official Export Data option under Profile Settings → Account → Manage Account & Data on the web, and under Settings → Legal & Privacy in the app. It emails you a link to a password-protected ZIP of your messages. Character.AI says this can take 3–4 weeks, and the link works for 7 days."),
 "password": ("What is the password for the Character AI export ZIP?",
  "The password is the email address of your Character.AI account, typed in lowercase, for example alex.smith@gmail.com and not Alex.Smith@gmail.com. It is not your login password and it is not sent separately. If you signed in with Google or Apple, try the email address of that account."),
 "open": ("How do I open a Character AI export?",
  "Download the ZIP from Character.AI's email within 7 days. Unlock it with your account email in lowercase, or drop the ZIP on a browser viewer such as BotToBook, which decrypts it on your device. Your chats are inside message.json, a raw data file that needs a viewer before it reads like a conversation."),
 "not_working": ("Why is my Character AI export data not working?",
  "The usual causes are a ZIP password typed with capital letters (it must be your account email in lowercase), a download link that expired after 7 days, or opening message.json directly, which shows raw data with no names or speakers. A viewer such as BotToBook handles the password and rebuilds each chat for you."),
 "what_means": ("What does \"Export Data\" on Character AI mean?",
  "Export Data is Character.AI's official way to get a copy of what your account holds. You request it in settings, and Character.AI emails a link to a ZIP containing user.json (your profile), character.json (characters you created) and message.json (every message from all your chats). It is raw data, not a readable transcript."),
 "how_long": ("How long does it take for Character AI to export data?",
  "Character.AI says a data export can take 3 to 4 weeks to arrive. When it is ready you get an email with a download link that works for 7 days, so download the ZIP as soon as it arrives and keep a copy somewhere safe. Request it early if you are worried about losing access."),
 "pdf": ("How do I turn my Character AI chats into a PDF?",
  "Request your data export in Character.AI settings. When the email arrives, drop the ZIP on BotToBook and enter your account email in lowercase as the password. Pick the chats, type the character's name, press PDF book, then choose Save as PDF in the print dialog. Each chat becomes a chapter with page numbers."),
 "kindle": ("Can I read my Character AI chats on a Kindle?",
  "Yes. Turn your Character.AI export into an EPUB with BotToBook, then send the file to your Kindle with Amazon's Send to Kindle by email, the Kindle app or the web page. Kobo, Apple Books, Google Play Books, Boox and KOReader open the same EPUB directly, with one chapter for each chat."),
 "who_wrote": ("Why doesn't the Character AI export say who wrote each message?",
  "Character.AI's official export lists each message's text, chat ID and time, but not whether you or the character wrote it, and not the character's name. BotToBook works out the sides from turn order and reply timing, since characters answer within seconds, and you can swap the sides or type the names yourself."),
 "safe": ("Is it safe to open my Character AI export in BotToBook?",
  "BotToBook opens the ZIP and builds the book with JavaScript running in your own browser, so your chats are never uploaded to a server. The page has no ads and no trackers. The only thing sent anywhere is a Pro license key, when you activate one, so the payment provider can confirm it."),
 "transfer": ("Can I move Character AI chats to another account or app?",
  "As far as we know, Character.AI offers no way to import an export into another account or back into the app. What you can do is keep the chats readable: open the export in a viewer and save them as a PDF, EPUB or text file you control. Some other chat apps also accept SillyTavern-style files."),
 "free": ("Is BotToBook free?",
  "Opening your Character.AI export, reading every chat, setting names and downloading any chat as a text file are free, and you can preview a short book from your own chats. Full PDF, EPUB and HTML books cost $4.99 once, with no subscription, on up to three devices. A sample export is loaded so you can try every button first."),
 "shutdown": ("Is Character.AI shutting down?",
  "As of late November 2026, Character.AI is in a Chapter 11 sale process that it expects to finish in late November or early December, and it has said the platform could be wound down if no suitable buyer is found. Check Character.AI's own announcements for the latest, and request your export now either way."),
 "files": ("What files does BotToBook open?",
  "The official Character.AI export (the ZIP, or message.json, character.json and user.json from inside it), CAI Tools exports (JSON and Tavern JSONL), SillyTavern .jsonl chats, and most JSON files that hold a list of messages. When a file does record who spoke, BotToBook uses that instead of guessing."),
 "pro": ("What do I get with BotToBook Pro?",
  "One payment of $4.99 unlocks full PDF, EPUB and HTML books for every chat you open, as many as you like, on up to three devices, with no subscription. Your license key appears when you return from checkout and is emailed to you, so you can enter it again any time. Questions or refunds: hello@yansquared.com."),
 "pw_capitals": ("Why doesn't my email work as the Character AI ZIP password?",
  "It is almost always capital letters: phones often capitalize the first letter, so type the address in lowercase. Also check for a trailing space, and make sure it is the email your Character.AI account uses, which can differ from the one you check most. BotToBook trims spaces and retries in lowercase for you."),
 "pw_unzip": ("Why won't my computer open the Character AI ZIP even with the right password?",
  "The export ZIP is encrypted, and the unzip tools built into Windows, macOS and phones often refuse encrypted ZIPs or reject a correct password. You don't need to unzip it at all: drop the ZIP on BotToBook, type your account email in lowercase, and it is opened in your browser without uploading anything."),
 "pdf_phone": ("Can I save Character AI chats as a PDF on my phone?",
  "Yes. Open BotToBook in your phone's browser, drop the export ZIP, and press PDF book. On iPhone tap Share, then Print, then Share again and Save to Files. On Android choose Print and then Save as PDF. The book keeps its cover, chapters and page breaks."),
 "pdf_noexport": ("Can I save a Character AI chat as a PDF without the export?",
  "You can scroll a chat to the top and use your browser's Print and Save as PDF, or copy the text into a document, but long chats load in pieces and the layout is rough. The official export contains every message, so it is the more complete way to keep a chat."),
 "epub_long": ("Will a very long Character AI chat work on an e-reader?",
  "Yes. BotToBook splits long chats into parts of about 350 messages inside the EPUB, each listed in the table of contents, so pages turn quickly even on older Kindles and Kobos. A chat with thousands of messages becomes one chapter with several parts rather than one huge file."),
 "json_open": ("How do I read message.json from a Character AI export?",
  "Open it in a viewer rather than a text editor. message.json holds every message from all your chats in one list, so a viewer has to group messages by chat_id, sort them by create_time and work out who spoke. Drop the file on BotToBook to see each conversation in order."),
 "json_fields": ("What fields are in Character AI message.json?",
  "Each entry in message.json has a chat_id that groups it into a conversation, a candidate_id for the reply, raw_content with the message text, and create_time, a timestamp with microsecond precision. There is no field for who wrote the message and no character name, so those have to be inferred or typed in."),
}

HOME_FAQ = ["password", "can_export", "open", "how_long", "pdf", "kindle", "who_wrote", "safe", "free", "shutdown", "files", "pro"]

# ── Facts table (home + message.json page) ────────────────────────────────────
FACTS_ROWS = [
 ("Delivery", "An emailed link to a ZIP. Character.AI says 3–4 weeks; the link is valid for 7 days."),
 ("ZIP password", "The account's email address, in lowercase."),
 ("Layout", "A folder named after your username, with a data folder inside."),
 ("<code>user.json</code>", "Your account profile."),
 ("<code>character.json</code>", "Only characters you created: name, greeting, definition."),
 ("<code>message.json</code>", "Every message from all your chats, in one list."),
 ("Fields per message", "<code>chat_id</code>, <code>candidate_id</code>, <code>raw_content</code>, <code>create_time</code> (microsecond precision)."),
 ("Not included", "Who wrote each message, and the name of the character you chatted with."),
]
def facts_table():
    rows = "".join(f"<tr><th scope=\"row\">{a}</th><td>{b}</td></tr>" for a, b in FACTS_ROWS)
    return f"<table class=\"facts\"><caption>What the official Character.AI export contains (checked November 2026)</caption><tbody>{rows}</tbody></table>"

# ── Guide pages ───────────────────────────────────────────────────────────────
# body: HTML after the direct answer and the CTA. {FACTS} is replaced by the facts table.
PAGES = [
 {
  "slug": "character-ai-export-zip-password",
  "crumb": "Character.AI export ZIP password",
  "title": "Character.AI Export ZIP Password: It's Your Email, Lowercase",
  "description": "The Character.AI export ZIP password is your account's email address in lowercase. Why it fails, and how to open the ZIP in your browser without an unzip app.",
  "h1": "What is the password for the Character.AI export ZIP?",
  "answer": "The password for a Character.AI export ZIP is the email address of your Character.AI account, typed in lowercase, for example alex.smith@gmail.com rather than Alex.Smith@gmail.com. It is not your login password and it does not arrive in a separate email. If it fails, the cause is nearly always capital letters or the wrong address.",
  "body": """
<h2>If the password doesn't work</h2>
<ul>
<li><b>Capital letters.</b> Phones capitalize the first letter of a field. Type the whole address in lowercase.</li>
<li><b>A trailing space.</b> Pasting often adds one at the end.</li>
<li><b>The wrong address.</b> Use the email your Character.AI account is registered with — the one the export email was sent to. If you signed in with Google or Apple, try that account's address.</li>
<li><b>Your unzip app.</b> The ZIP is encrypted, and the tools built into Windows, macOS and phones often refuse it even with the right password.</li>
</ul>
<h2>Open the ZIP without an unzip app</h2>
<p>You don't need to unzip it. Drop the ZIP on <a href="/">BotToBook</a> and type your email when it asks for the password. The ZIP is decrypted in your browser — nothing is uploaded — and BotToBook trims spaces and retries in lowercase automatically. Every chat then appears in a list, longest first, ready to read.</p>
<h2>What's inside once it opens</h2>
<p>A folder named after your username with <code>user.json</code>, <code>character.json</code> and <code>message.json</code>. Your chats are all in <code>message.json</code>, as raw data without names. See <a href="/character-ai-message-json/">what message.json contains</a>.</p>
""",
  "faq": ["password", "pw_capitals", "pw_unzip", "open"],
  "links": ["how-to-open-character-ai-export", "character-ai-message-json"],
 },
 {
  "slug": "how-to-open-character-ai-export",
  "crumb": "How to open a Character.AI export",
  "title": "How to Open a Character.AI Export (ZIP or message.json)",
  "description": "Step by step: request your Character.AI export, unlock the ZIP with your email in lowercase, and read message.json as real conversations in a browser viewer.",
  "h1": "How to open your Character.AI export",
  "answer": "To open a Character.AI export, download the ZIP from the email within 7 days and unlock it with your account email in lowercase. Your chats are in message.json, a raw data file with no names, so load the ZIP or that file into a browser viewer such as BotToBook to read them as conversations.",
  "body": """
<h2>Step 1: request the export</h2>
<p>On character.ai go to <em>Profile Settings → Account → Manage Account &amp; Data → Export Data</em>. In the app it's <em>Settings → Legal &amp; Privacy → Export Data</em>. Character.AI says the export can take 3–4 weeks; the email's download link works for 7 days, so save the ZIP as soon as it arrives.</p>
<h2>Step 2: unlock the ZIP</h2>
<p>The ZIP is password-protected. The password is your account email in lowercase — <a href="/character-ai-export-zip-password/">more on the password</a>. Built-in unzip tools often refuse it; a browser viewer can open it directly.</p>
<h2>Step 3: read the chats in a viewer</h2>
<p>Drop the ZIP (or <code>message.json</code>) on <a href="/">BotToBook</a>. It groups messages into conversations, puts them in order, works out who said what, and lets you type the character's name for each chat. Reading and text downloads are free.</p>
<h2>Why the export looks broken</h2>
<p>Opened in a text editor, <code>message.json</code> is one long list of every message from every chat, with no sender and no character name. That's how Character.AI's export is built, not a damaged file.</p>
{FACTS}
<h2>Other free viewers</h2>
<p>Several free tools also open the export in the browser, including the open-source viewer by anima-universe on GitHub, Amavie, Yanmate, Neon Bay and chatbotbackup.com. BotToBook's focus is turning the chats into a proper book — a typeset PDF and an EPUB for e-readers.</p>
""",
  "faq": ["can_export", "open", "not_working", "what_means", "how_long", "transfer"],
  "links": ["character-ai-export-zip-password", "character-ai-chat-to-pdf", "character-ai-message-json"],
 },
 {
  "slug": "character-ai-chat-to-pdf",
  "crumb": "Character.AI chat to PDF",
  "title": "Character.AI Chat to PDF: Save Your Chats as a Book",
  "description": "Save Character.AI chats as a PDF book with a cover, contents, a chapter per chat and page numbers. Works from the official export, in your browser, on phone or computer.",
  "h1": "How to save Character.AI chats as a PDF",
  "answer": "To save Character.AI chats as a PDF, request your data export in Character.AI settings, then drop the emailed ZIP on BotToBook. Pick the chats, type the character's name, press PDF book and choose Save as PDF in the print dialog. You get a cover, a chapter per chat and page numbers.",
  "body": """
<h2>Steps</h2>
<ol class="steps">
<li><b>Request your export</b> in Character.AI (Profile Settings → Account → Manage Account &amp; Data → Export Data).</li>
<li><b>Drop the ZIP on <a href="/">BotToBook</a></b> and type your account email in lowercase as the password.</li>
<li><b>Name each chat:</b> type the character's name, and press <em>Swap who said what</em> if a chat comes out backwards.</li>
<li><b>Pick the chats</b> to include and a page size: paperback 5.5 × 8.5 in, US Letter, A4 or A5.</li>
<li><b>Press PDF book</b> and choose <em>Save as PDF</em> in the print dialog.</li>
</ol>
<h2>What the PDF looks like</h2>
<figure><img src="/img/sample-book.png" width="1200" height="464" alt="Four pages of a sample BotToBook PDF: a cover, a contents page, and chapter pages with speaker names and date headings" loading="lazy"><figcaption>Pages from the sample book: cover, contents, and chat pages with names and dates.</figcaption></figure>
<p>A cover with the title and the characters' names, a contents page when there's more than one chat, then each chat as a chapter with date headings and page numbers. Your browser does the typesetting, so every language and emoji comes out right.</p>
<h2>On iPhone and Android</h2>
<p>Press <em>PDF book</em>, then on iPhone tap Share → Print, and Share again → Save to Files. On Android choose Print → Save as PDF.</p>
<h2>Free vs Pro</h2>
<p>Reading every chat, text downloads and a short preview book from your own chats are free. The full PDF, EPUB and HTML books are $4.99 once — a typeset book, not a printout.</p>
""",
  "faq": ["pdf", "pdf_phone", "pdf_noexport", "free"],
  "links": ["how-to-open-character-ai-export", "character-ai-to-kindle"],
 },
 {
  "slug": "character-ai-to-kindle",
  "crumb": "Character.AI chats to Kindle",
  "title": "Character.AI Chats to Kindle: Export to EPUB",
  "description": "Read your Character.AI chats on a Kindle, Kobo or Apple Books: turn the official export into an EPUB with a chapter per chat, then send it with Send to Kindle.",
  "h1": "How to read your Character.AI chats on a Kindle",
  "answer": "To read Character.AI chats on a Kindle, turn your data export into an EPUB and send it with Amazon's Send to Kindle. BotToBook builds the EPUB in your browser from the export ZIP, one chapter per chat with a table of contents. Kobo, Apple Books and Google Play Books open the same file directly.",
  "body": """
<h2>Make the EPUB</h2>
<p>Drop your Character.AI export ZIP on <a href="/">BotToBook</a> (the password is your account email in lowercase), type the character's name for each chat, tick the chats you want, and press <em>EPUB</em>. You get one EPUB 3 file with a cover, a title page and a chapter per chat.</p>
<h2>Send it to your Kindle</h2>
<ul>
<li><b>Email:</b> attach the EPUB and send it to your Kindle's Send-to-Kindle address (shown in your Amazon device settings).</li>
<li><b>Kindle app:</b> share the file to the Kindle app on your phone or computer.</li>
<li><b>Web:</b> upload it on Amazon's Send to Kindle page.</li>
</ul>
<p>Amazon converts the EPUB for your Kindle; it then syncs to every Kindle device and app on your account.</p>
<h2>Kobo, Apple Books, Boox, KOReader</h2>
<p>These open EPUB directly: copy it to the device, add it to Apple Books, or upload it to Google Play Books.</p>
<h2>Long chats</h2>
<p>Very long chats are split into parts inside the book, each listed in the table of contents, so pages turn quickly even on older e-readers.</p>
""",
  "faq": ["kindle", "epub_long", "free"],
  "links": ["character-ai-chat-to-pdf", "how-to-open-character-ai-export"],
 },
 {
  "slug": "character-ai-message-json",
  "crumb": "Character.AI message.json format",
  "title": "Character.AI message.json Explained: Export File Format",
  "description": "What's inside a Character.AI data export: user.json, character.json and message.json, the fields in each message, what's missing, and how viewers rebuild your chats.",
  "h1": "What is message.json in a Character.AI export?",
  "answer": "message.json is the file in a Character.AI data export that holds your chats. It is one list of every message from all conversations, each with a chat_id, candidate_id, raw_content and create_time. It does not record who wrote a message or the character's name, which is why it needs a viewer.",
  "body": """
<h2>Files in the export ZIP</h2>
{FACTS}
<h2>Fields in message.json</h2>
<p>An entry looks like this (values made up):</p>
<pre><code>{
  "chat_id": "a1b2c3d4-…",
  "candidate_id": "e5f6…",
  "raw_content": "*She sets down the lantern.* You came back.",
  "create_time": "2026-10-03 19:02:11.204188+00:00"
}</code></pre>
<p><code>chat_id</code> ties the message to a conversation. <code>raw_content</code> is the text, with Character.AI's Markdown (<code>*actions*</code>, <code>**bold**</code>) left in. <code>create_time</code> has microsecond precision. Some exports are a single JSON array; others put one message per line.</p>
<h2>What the export leaves out</h2>
<p>There is no field for whether you or the character wrote a message, and no character name — not even for the characters you talked to. <code>character.json</code> only lists characters you created yourself.</p>
<h2>How viewers rebuild your conversations</h2>
<ol>
<li>Group messages by <code>chat_id</code>.</li>
<li>Sort each group by <code>create_time</code>.</li>
<li>Work out who spoke. Turns alternate, and the character's replies arrive within seconds while yours take longer, so the gaps between messages show which side is which. <a href="/">BotToBook</a> does this and lets you swap the sides with one click.</li>
<li>Name the speakers: you type the character's name once per chat.</li>
</ol>
<h2>character.json and user.json</h2>
<p><code>character.json</code> holds the characters you made — name, greeting and the long definition. <code>user.json</code> holds your profile, such as your first name and the date you joined.</p>
""",
  "faq": ["json_open", "json_fields", "who_wrote", "what_means"],
  "links": ["how-to-open-character-ai-export", "character-ai-export-zip-password"],
 },
]
