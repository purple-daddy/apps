# App pages — log (newest at the top)
## 2026-10-23 21:28 — Standby 09 (Precinct 2008)
- Added Precinct 2008 (privacy + support) from a code-verified fact sheet, reviewed (4 corrections). Then updated for the app's commit d074c70: optional Face ID/passcode lock (off by default), Remove from roster now really deletes (8 s undo; older backups still hold the person), no school contact in the bundle, privacy manifest. Note: d074c70 was local in the app repo when I wrote this; if it is not in the TestFlight build, re-check the page against what actually ships.

## 2026-10-23 04:17 — Standby 09
- Built the generator and 14 apps' content from fact sheets (subagents read each app's code; sheets in _workspace/app-privacy-facts/). Content leak-grep clean.
