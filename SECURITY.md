# Security

BotToBook runs in the browser and never uploads your Character.AI export. Apart from loading web fonts, the only network call it makes is the
licence-key check on the hosted site (`functions/api/license.js`), which sends the key and a random per-browser id, nothing from your export.

To report a security problem, email hello@yansquared.com with "security" in the subject. You'll get a reply within
a few days. Please don't open a public issue for it.
