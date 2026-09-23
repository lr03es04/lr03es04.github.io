"""Generate the static homepage from the editable JSON files (Python 3, no dependencies)."""
import json
from pathlib import Path
from html import escape
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent
e = lambda value: escape(str(value), quote=True)
members = json.loads((ROOT / 'data/members.json').read_text(encoding='utf-8'))
content = json.loads((ROOT / 'data/content.json').read_text(encoding='utf-8'))
groups = OrderedDict()
for batch in members:
    for name in batch['names']:
        groups.setdefault(batch['group'], []).append((name, batch['rank']))
directory = []
for i, (group, rows) in enumerate(groups.items()):
    entries = []
    for name, rank in rows:
        email = content['emails'].get(name, '')
        if email and ('@' not in email or any(c.isspace() for c in email)):
            raise ValueError(f'Invalid email for {name}')
        contact = f'<a href="mailto:{e(email)}">{e(email)}</a>' if email else '<span class="missing">Not provided</span>'
        director = '<span class="role">Laboratory director</span>' if name == 'Slim Tayachi' else ''
        entries.append(f'<tr><td>{e(name)}{director}</td><td data-label="Rank" lang="fr">{e(rank)}</td><td data-label="Email">{contact}</td></tr>')
    directory.append(f'''<details class="group" {'open' if i == 0 else ''}><summary>{e(group)}<span class="count">{len(rows)}</span></summary><div class="table-wrap"><table aria-label="{e(group)}"><thead><tr><th scope="col">Full name</th><th scope="col">Rank</th><th scope="col">Email</th></tr></thead><tbody>{''.join(entries)}</tbody></table></div></details>''')
talks = []
for talk in content['talks']:
    talks.append(f'''<article class="talk"><h3>{e(talk['title'])}</h3><p>{e(talk['speaker'])}</p><p class="meta">{e(talk['date'])} · {e(talk['time'])}<br>{e(talk['location'])}</p><details><summary>Read abstract</summary><p class="abstract">{e(talk['abstract'])}</p></details></article>''')
talk_html = ''.join(talks) or '<div class="empty"><strong>Programme to be announced</strong><p>Talk titles, speakers, and abstracts will be published here when confirmed.</p></div>'
announcements = ''.join(f'<article class="announcement"><h3>{e(a["title"])}</h3><p>{e(a["text"])}</p></article>' for a in content['announcements']) or '<div class="empty"><strong>No announcements yet</strong><p>Seminar news and programme updates will appear here.</p></div>'
next_talk = content['talks'][0] if content['talks'] else {}
date = next_talk.get('date') or 'To be announced'
time = next_talk.get('time') or 'To be announced'
location = next_talk.get('location') or 'To be announced'
status = 'Scheduled' if next_talk else 'Programme forthcoming'
title = 'Seminar of FST-PDEs Laboratory LR03ES04'
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="Seminar announcements, talk abstracts, dates, location, and members of the FST-PDEs Laboratory LR03ES04, directed by Professor Slim Tayachi."><meta name="theme-color" content="#142d40"><link rel="stylesheet" href="styles.css"><link rel="icon" href="favicon.svg" type="image/svg+xml"></head>
<body><a class="skip" href="#main">Skip to content</a><header><div class="wrap topbar"><a class="identity" href="./" aria-label="FST-PDEs Laboratory home"><span class="mark" aria-hidden="true">∂</span><span>FST-PDEs Laboratory<small>LR03ES04</small></span></a><nav aria-label="Main navigation"><a href="#talks">Talks &amp; abstracts</a><a href="#announcements">Announcements</a><a href="#members">Members</a></nav></div></header>
<main id="main" class="wrap"><div class="intro"><div><p class="eyebrow">Partial differential equations</p><h1>Seminar of <span>FST-PDEs Laboratory</span><span class="code">LR03ES04</span></h1><p class="subline">Faculty of Sciences of Tunis · University of Tunis El Manar</p></div><aside class="director" aria-label="Laboratory director"><span>Laboratory director</span><strong>Professor Slim Tayachi</strong></aside></div>
<section class="seminar" aria-labelledby="next-heading"><div class="seminar-top"><h2 id="next-heading">Next seminar</h2><span class="status">{status}</span></div><dl class="facts"><div><dt>Date</dt><dd>{e(date)}</dd></div><div><dt>Time</dt><dd>{e(time)}</dd></div><div><dt>Location</dt><dd>{e(location)}</dd></div></dl></section>
<div class="programme"><section id="talks"><div class="section-heading"><h2>Talks &amp; abstracts</h2></div>{talk_html}</section><section id="announcements"><div class="section-heading"><h2>Announcements</h2></div>{announcements}</section></div>
<section id="members" class="members"><div class="section-heading"><h2>Laboratory members</h2><span>{sum(map(len,groups.values()))} members · 2025 directory</span></div><p class="members-note">Names and ranks from the laboratory’s 2025 activity report. Rank titles are retained in French. Unavailable email addresses are marked “Not provided”.</p>{''.join(directory)}</section></main>
<footer><div class="wrap footer-inner"><p>FST-PDEs Laboratory · LR03ES04<br>Faculty of Sciences of Tunis · University of Tunis El Manar</p><p>Seminar of FST-PDEs Laboratory<br>Director: Professor Slim Tayachi</p></div></footer></body></html>'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
print(f'Built index.html: {sum(map(len, groups.values()))} members, {len(talks)} talks.')

