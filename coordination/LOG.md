# App pages — log (newest at the top)
## 2026-10-29 21:27 — Standby 28 (App Store listings; Coordinator said fix and push)
- Updated six pages to the current builds, each re-read against the app's code by a subagent: mac-battery (now "PowerHouse – Battery & Notch"; Storage, Dictation, Convert, Lanes only in the direct-download Mac build), better-amazon ("Better Bezos"; logs stay on device without a tracker), shoppos ("Green Phoenix-ShopPOS"; amounts in optional admin push alerts go through Apple), shotlist (link fetch removed; coordinates go to Apple for the current city), precinct-2008 (build 5: Notable people, Notes, checkboxes), and new car-mode. Status stays "TestFlight beta" everywhere.
- Unverified (left as written): Erase All Data vs Files backup copies (Shotlist), Clementine converter network use (PowerHouse), tracker/ntfy server side (Better Bezos), live sale-alert server code (ShopPOS).
- When the App Store builds show the Developer tools row (house rule §9), each page's hidden-portal wording needs a re-check.
## 2026-10-23 21:28 — Standby 09 (Precinct 2008)
- Added Precinct 2008 (privacy + support) from a code-verified fact sheet, reviewed (4 corrections). Then updated for the app's commit d074c70: optional Face ID/passcode lock (off by default), Remove from roster now really deletes (8 s undo; older backups still hold the person), no school contact in the bundle, privacy manifest. Note: d074c70 was local in the app repo when I wrote this; if it is not in the TestFlight build, re-check the page against what actually ships.

## 2026-10-23 04:17 — Standby 09
- Built the generator and 14 apps' content from fact sheets (subagents read each app's code; sheets in _workspace/app-privacy-facts/). Content leak-grep clean.
