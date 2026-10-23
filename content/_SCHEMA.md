# content/<slug>.json (one per app). Plain text only; paragraphs separated by a blank line (\n\n). No HTML, no markdown, no email addresses.
{
 "slug": "clementine",                      // lowercase, hyphens
 "name": "Clementine",
 "tagline": "one plain sentence",
 "platforms": "Mac",                         // e.g. "iPhone, iPad, Mac"
 "status": "Not on the App Store yet",       // or "TestFlight beta", "App Store"
 "updated": "2026-10-23",
 "about": "2-4 plain sentences: what it does and who uses it.",
 "collects": [ {"what": "...", "where": "on your device / on the developer's own server", "shared": "Nobody / the developer's own server / ...", "why": "..."} ],
 "usage_data": "TRUTHFUL paragraph about logs and diagnostics: what is recorded, where it stays, whether it is uploaded and to whom ('Usage Data'), how long kept, what is masked or left out.",
 "not_collected": ["only things verified NOT to happen, e.g. No advertising, No tracking across other apps, No analytics SDKs"],
 "third_parties": [ {"who": "Apple (push notifications)", "what": "..."} ],      // [] if none
 "permissions": [ {"name": "Camera", "why": "..."} ],                              // [] if none
 "retention": "how long data is kept and exactly how a person deletes it (e.g. Settings > Erase All Data on This Device and what that does NOT touch).",
 "children": "plain statement (not directed to children; no accounts / no data from children knowingly...) - only what is true.",
 "support_what": "1-2 paragraphs: what the app is for, in plain words.",
 "support_steps": ["3-6 getting-started steps"],
 "support_faq": [ {"q": "question", "a": "answer"} ]                              // 3-6 real questions from the docs
}
