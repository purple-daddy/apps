# App pages — status
Updated: 2026-10-23 04:31 by Standby 09 ("2 weeks · own public URL")
- 14 apps have privacy + support pages (reviewed three ways: leaks/HTML, truthfulness against code, then corrected). Repo `purple-daddy/apps` is created and pushed (PUBLIC).
- NOT LIVE YET: enabling GitHub Pages for the repo was refused by the safety check ("Create Public Surface"), so the URLs `https://purple-daddy.github.io/apps/<app>/privacy/` and `/support/` do not answer yet. Needs Jay's/the Coordinator's go; then: `gh api -X POST repos/purple-daddy/apps/pages -f 'source[branch]=main' -f 'source[path]=/'`.
- Contact on every page: GitHub Issues + TestFlight feedback (only for apps that are on TestFlight). No email, no form.
