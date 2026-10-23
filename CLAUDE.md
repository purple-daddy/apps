# App pages (privacy + support)

Public GitHub Pages site `https://purple-daddy.github.io/apps/` with `<app>/privacy/` and `<app>/support/` for each of Jay's apps
(App Store Connect needs both URLs). Static HTML, no JavaScript, no third-party requests.

Read `coordination/STATUS.md` first.

## Layout
```
content/<slug>.json     THE text for one app (schema: content/_SCHEMA.md). Reviewed before it is published.
scripts/build.py        validates content (rejects emails/secret-looking text), writes <slug>/privacy|support/index.html + index.html
assets/style.css        the one stylesheet (dark mode via prefers-color-scheme)
coordination/           project docs (kept out of the served pages by not being linked; the repo itself is public)
```
## Rules
- PUBLIC repo: nothing private, no hostnames/IPs/keys/paths, no customer or staff names, no personal email. Say "the developer's own server".
- Policies must be TRUE: change the app's data handling -> change its content JSON the same day (`updated` date too), rebuild, push.
- Each page was written from a fact sheet that cites the app's code (kept in the developer's private workspace).
- After editing content: `python3 scripts/build.py`, commit, push `main`; Pages republishes in ~1 minute.
