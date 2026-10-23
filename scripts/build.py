#!/usr/bin/env python3
"""Build the public privacy + support pages from content/<app>.json.

  python3 scripts/build.py          # writes ../ (repo root: index.html, assets/, <app>/privacy/, <app>/support/)

Plain static HTML + one stylesheet. No JavaScript, no analytics, no third-party requests (the page's own CSP says so).
Every piece of text is HTML-escaped here. Text comes only from content/*.json, which a person reviews before it is published.
"""
import datetime
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT
CONTENT = ROOT / "content"
ISSUES = "https://github.com/purple-daddy/apps/issues/new/choose"
SITE = "https://purple-daddy.github.io/apps"

REQUIRED = ["slug", "name", "tagline", "platforms", "status", "updated", "about", "collects", "not_collected", "third_parties",
            "permissions", "usage_data", "retention", "children", "support_what", "support_steps", "support_faq"]


def e(s):
    return html.escape(str(s), quote=True)


def para(s):
    return "".join(f"<p>{e(p)}</p>" for p in str(s).split("\n\n") if p.strip())


def bullets(items):
    return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>" if items else "<p>None.</p>"


def table(rows, cols):
    head = "".join(f"<th>{e(c)}</th>" for c in cols)
    body = "".join("<tr>" + "".join(f"<td>{e(r.get(k, ''))}</td>" for k in keys) + "</tr>" for r in rows for keys in [KEYS[tuple(cols)]])
    return f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


KEYS = {("Data", "Where it lives", "Who receives it", "Why"): ["what", "where", "shared", "why"],
        ("Who", "What they receive"): ["who", "what"],
        ("Permission", "Why the app asks"): ["name", "why"]}

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="no-referrer">
<link rel="stylesheet" href="{base}assets/style.css">
</head><body>
<header><a class="home" href="{base}">Apps</a>{nav}</header>
<main>
{body}
</main>
<footer><p>Questions or problems: <a href="{issues}" rel="noopener noreferrer">open an issue on GitHub</a> (public: please don't post private information){tf}.</p></footer>
</body></html>
"""


def page(path, title, desc, body, nav="", tf=False):
    depth = len(Path(path).parts) - 1
    base = "../" * depth
    out = OUT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PAGE.format(title=e(title), desc=e(desc), body=body, nav=nav, base=base, issues=ISSUES,
                                tf=" or send feedback from TestFlight if you are in the beta" if tf else ""))


def validate(a, name):
    miss = [k for k in REQUIRED if k not in a or a[k] in (None, "")]
    if miss:
        sys.exit(f"{name}: missing {miss}")
    if not re.fullmatch(r"[a-z0-9-]{2,30}", a["slug"]):
        sys.exit(f"{name}: bad slug")
    datetime.date.fromisoformat(a["updated"])
    for k in ("collects", "third_parties", "permissions"):
        if not isinstance(a[k], list):
            sys.exit(f"{name}: {k} must be a list")
    for k in ("collects",):
        for r in a[k]:
            if not all(r.get(x) for x in ("what", "where", "shared", "why")):
                sys.exit(f"{name}: a 'collects' row needs what/where/shared/why")
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", json.dumps(a)):
        sys.exit(f"{name}: contains an email address; pages use no email")
    if re.search(r"(?i)(password|secret|token|api[_ -]?key)\s*[:=]\s*\S{8,}", json.dumps(a)):
        sys.exit(f"{name}: looks like it contains a secret")


def build():
    apps = []
    for f in sorted(CONTENT.glob("*.json")):
        a = json.loads(f.read_text())
        validate(a, f.name)
        apps.append(a)
    for a in apps:
        slug = a["slug"]
        nav = f'<nav><a href="../privacy/">Privacy</a><a href="../support/">Support</a></nav>'
        priv = f"""<h1>{e(a['name'])} privacy policy</h1>
<p class="meta">{e(a['platforms'])} · {e(a['status'])} · Last updated {e(a['updated'])}</p>
<p class="lead">{e(a['tagline'])}</p>
<h2>What this app is</h2>{para(a['about'])}
<h2>What it collects or handles</h2>{table(a['collects'], ['Data', 'Where it lives', 'Who receives it', 'Why'])}
<h2>Diagnostic and usage data</h2>{para(a['usage_data'])}
<h2>What it does not collect</h2>{bullets(a['not_collected'])}
<h2>Other companies that receive data</h2>{table(a['third_parties'], ['Who', 'What they receive']) if a['third_parties'] else '<p>None.</p>'}
<h2>Permissions it asks for</h2>{table(a['permissions'], ['Permission', 'Why the app asks']) if a['permissions'] else '<p>None.</p>'}
<h2>How long it keeps data, and how to delete it</h2>{para(a['retention'])}
<h2>Children</h2>{para(a['children'])}
<h2>Changes and contact</h2><p>If this policy changes, the date above changes. To ask about your data, <a href="{ISSUES}" rel="noopener noreferrer">open an issue</a> (don't include private information){' or use TestFlight feedback' if 'TestFlight' in a['status'] else ''}.</p>"""
        page(f"{slug}/privacy/index.html", f"{a['name']} privacy policy", f"What {a['name']} does with your data.", priv,
             nav.replace('href="../privacy/"', 'href="./" aria-current="page"'), tf="TestFlight" in a["status"])
        faq = "".join(f"<h3>{e(q['q'])}</h3>{para(q['a'])}" for q in a["support_faq"])
        sup = f"""<h1>{e(a['name'])} support</h1>
<p class="meta">{e(a['platforms'])} · {e(a['status'])}</p>
<h2>What it is</h2>{para(a['support_what'])}
<h2>Getting started</h2><ol>{''.join(f'<li>{e(s)}</li>' for s in a['support_steps'])}</ol>
<h2>Common questions</h2>{faq}
<h2>Still stuck?</h2><p>If the app has a Help screen, it runs self-checks first. If that doesn't fix it, <a href="{ISSUES}" rel="noopener noreferrer">open an issue on GitHub</a> (public: leave out private information){', or send feedback from TestFlight if you are in the beta' if 'TestFlight' in a['status'] else ''}.</p>
<p>Your data: see the <a href="../privacy/">privacy policy</a>.</p>"""
        page(f"{slug}/support/index.html", f"{a['name']} support", f"Help for {a['name']}.", sup,
             nav.replace('href="../support/"', 'href="./" aria-current="page"'), tf="TestFlight" in a["status"])
    cards = "".join(f'<li><b>{e(a["name"])}</b> <span class="meta">{e(a["platforms"])}</span><br>{e(a["tagline"])}<br>'
                    f'<a href="{a["slug"]}/privacy/">Privacy</a> · <a href="{a["slug"]}/support/">Support</a></li>' for a in apps)
    page("index.html", "Apps: privacy and support", "Privacy policies and support pages for Jay's apps.",
         f"<h1>Apps</h1><p class=\"lead\">Privacy policies and support pages for each app.</p><ul class=\"cards\">{cards}</ul>")
    (OUT / ".nojekyll").write_text("")
    print(f"built {len(apps)} apps: " + ", ".join(a["slug"] for a in apps))


if __name__ == "__main__":
    build()
