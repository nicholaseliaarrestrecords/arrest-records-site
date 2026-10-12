import re
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=os.path.join(ROOT,'src','blocks')
os.chdir(os.path.join(ROOT,'public'))
def frag(n):
    t=open(f'{S}/{n}.html',encoding='utf8').read()
    t=re.sub(r'^<script>window\.onmessage.*?</script>','',t,flags=re.S)
    t=re.sub(r"<body style='margin: 0'>",'',t).replace('</body>','')
    t=t.replace('target="_top"','target="_blank" rel="noopener"')
    return t
NAV=[('/','MAINFRAME','index'),('/case-files','CASE FILES','case-files'),('/the-art','THE ART','the-art'),('/public-records-1','PUBLIC RECORDS','public-records-1')]
TITLES={'index':'MAINFRAME','case-files':'CASE FILES','the-art':'THE ART','public-records-1':'PUBLIC RECORDS'}
DESC='Arrest Records: 100% Clean. 100% Hard. Static & Gold by Nicholas Elia, South Florida.'
BANNER={'case-files':('banner-case-files.jpg','center'),'the-art':('banner-the-art.jpg','50% 22%'),'public-records-1':('banner-public-records.jpg','center')}
def page(slug,src,hero):
    nav=''.join(f'<li><a href="{h}"{" class=active" if s==slug else ""}>{l}</a></li>' for h,l,s in NAV)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLES[slug]}</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="Arrest Records — {TITLES[slug].title()}"><meta property="og:description" content="{DESC}">
<meta property="og:image" content="https://arrest-records.com/images/logo.png"><meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Source+Sans+Pro:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head><body>
<header class="nav"><ul>{nav}</ul></header>
<main class="wrap">
{hero}
{frag(src+'-0')}
{frag(src+'-1')}
{frag(src+'-2')}
</main>
<div id="cookie" class="cookie" hidden><h4>Signal Detected.</h4><p>Optimizing connection... We use cookies to analyze the data stream and improve the build. By accepting, your input is aggregated to help us cut through the noise.</p><div><button data-v="declined">Decline</button><button data-v="accepted">Accept</button></div></div>
<script src="/site.js"></script>
</body></html>'''
home='''<section class="hero"><div class="frame"><img src="/images/logo.png" alt="Arrest Records logo" width="900" height="900"></div></section>
<section class="intro"><h1>Static &amp; Gold: Nicholas Elia</h1><p>100% Clean. 100% Hard. High-octane fuel for your workout, your commute, and your spirit.</p></section>'''
def ban(slug):
    f,pos=BANNER[slug]
    return f'<section class="banner"><img src="/images/{f}" alt="" style="object-position:{pos}"></section>'
for slug,src in [('index','index'),('case-files','case-files'),('the-art','the-art'),('public-records-1','public-records-1')]:
    open(f'{slug}.html','w',encoding='utf8').write(page(slug,src,home if slug=='index' else ban(slug)))
open('mainframe.html','w',encoding='utf8').write(open('index.html',encoding='utf8').read().replace('<title>MAINFRAME','<title>MAINFRAME'))
