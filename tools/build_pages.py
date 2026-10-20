"""Copy index.html into one folder per page so each page has its own address
(www.iyerlab.ca/research/ and so on), and point old addresses at the new ones.
Run after any change to index.html:  python3 tools/build_pages.py"""
import os, re

SITE = "https://www.iyerlab.ca"
PAGES = {  # folder: (title, description)
    "research": ("Research · Iyer Lab", "Research in the Iyer Lab: chalcogenide crystals for infrared nonlinear optics, water remediation and two-dimensional magnetism, guided by machine learning."),
    "team": ("Team · Iyer Lab", "Meet Abishek Iyer and the students and researchers of the Iyer Lab, Department of Chemistry, University of Manitoba."),
    "publications": ("Publications · Iyer Lab", "Publications from Abishek Iyer and the Iyer Lab on chalcogenide, nonlinear optical and quantum materials."),
    "news": ("News · Iyer Lab", "News, talks, features and interviews from the Iyer Lab at the University of Manitoba."),
    "join-us": ("Join us · Iyer Lab", "Graduate, undergraduate and postdoctoral openings in the Iyer Lab, Department of Chemistry, University of Manitoba."),
    "resources": ("Resources · Iyer Lab", "Useful links for crystallography, databases, software and lab resources, collected by the Iyer Lab."),
}
OLD = {  # old Google Sites style addresses -> new page
    "home": "/", "openings": "/join-us/", "useful-links": "/resources/", "people": "/team/", "contact": "/join-us/",
}
REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Iyer Lab</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{site}{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace("{to}");</script>
</head><body><p>This page has moved to <a href="{to}">{site}{to}</a>.</p></body></html>
"""

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
src = open(os.path.join(root, "index.html"), encoding="utf-8").read()

for folder, (title, desc) in PAGES.items():
    url = f"{SITE}/{folder}/"
    html = src.replace("<title>Iyer Lab</title>", f"<title>{title}</title>", 1)
    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', html, count=1)
    os.makedirs(os.path.join(root, folder), exist_ok=True)
    open(os.path.join(root, folder, "index.html"), "w", encoding="utf-8").write(html)

for folder, to in OLD.items():
    os.makedirs(os.path.join(root, folder), exist_ok=True)
    open(os.path.join(root, folder, "index.html"), "w", encoding="utf-8").write(REDIRECT.format(site=SITE, to=to))

urls = [f"{SITE}/"] + [f"{SITE}/{f}/" for f in PAGES]
open(os.path.join(root, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built", len(PAGES), "pages and", len(OLD), "redirects")
