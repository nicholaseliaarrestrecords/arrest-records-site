import re, os, json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=os.path.join(ROOT,'src','blocks')
os.chdir(os.path.join(ROOT,'public'))
SITE='https://arrest-records.com'
LOGO=SITE+'/images/logo.jpg'
COVER=SITE+'/images/arrested-cover.jpg'
LASTMOD='2026-10-12'
def frag(n):
    t=open(f'{S}/{n}.html',encoding='utf8').read()
    t=re.sub(r'^<script>window\.onmessage.*?</script>','',t,flags=re.S)
    t=re.sub(r"<body style='margin: 0'>",'',t).replace('</body>','')
    t=t.replace('target="_top"','target="_blank" rel="noopener"')
    return t

# slug -> (path, nav label, title, description)
PAGES={
 'index':('/','MAINFRAME','Nicholas Elia | Arrest Records - Official Site, Music & Videos',
   'Official site of Nicholas Elia and Arrest Records. 100% clean, 100% hard. Watch Static & Gold and preview the new album ARRESTED, coming 1st quarter 2027.'),
 'case-files':('/case-files','CASE FILES','Case Files | Nicholas Elia - Arrest Records',
   'The Case Files: the story, lyrics and lore behind every Static & Gold track by Nicholas Elia on Arrest Records.'),
 'the-art':('/the-art','THE ART','The Art | Nicholas Elia - Arrest Records',
   'The art, mission and sound of Nicholas Elia and Arrest Records: clean, hard-hitting hip-hop and electronic music from South Florida.'),
 'public-records-1':('/public-records-1','PUBLIC RECORDS','Public Records & Booking | Nicholas Elia - Arrest Records',
   'Press, metrics and booking for Nicholas Elia and Arrest Records. Inquiries: NicholasEliaArrestRecords@gmail.com.'),
 'arrested':('/arrested','ARRESTED','ARRESTED - New Album by Nicholas Elia | Coming 1st Quarter 2027',
   'ARRESTED, the new album by Nicholas Elia on Arrest Records, arrives 1st quarter 2027. 100% clean, 100% hard hip-hop and electronic music from South Florida.'),
}
ORDER=['index','case-files','the-art','public-records-1','arrested']
BANNER={'case-files':('banner-case-files.jpg','center'),'the-art':('banner-the-art.jpg','50% 22%'),'public-records-1':('banner-public-records.jpg','center')}
DIMS={"banner-case-files.jpg": [1600, 873], "banner-public-records.jpg": [1600, 892], "banner-the-art.jpg": [1200, 1219]}
ALTS={'case-files':'Arrest Records access-granted ID card glowing against digital code, Case Files banner',
      'the-art':'Nicholas Elia as a neon-lit cyberpunk figure in a city skyline, The Art banner',
      'public-records-1':'Ancient stone tablets and glowing holographic scrolls, Public Records banner'}
SAMEAS=['https://www.youtube.com/@ArrestRecords','https://open.spotify.com/artist/7iNOGW9wT6PSKnPOhkGwwY','https://music.amazon.com/artists/B001XGL392/nicholas-elia']
PERSON={'@type':'Person','@id':SITE+'/#nicholas-elia','name':'Nicholas Elia','url':SITE+'/',
  'jobTitle':'Recording artist, director and producer',
  'description':'Nicholas Elia is a hip-hop and electronic recording artist, director and producer based in South Florida, founder of Arrest Records.',
  'image':LOGO,'sameAs':SAMEAS,'worksFor':{'@id':SITE+'/#arrest-records'}}
LABEL={'@type':['Organization','MusicGroup'],'@id':SITE+'/#arrest-records','name':'Arrest Records','url':SITE+'/','logo':LOGO,'sameAs':SAMEAS,'founder':{'@id':SITE+'/#nicholas-elia'}}
def jsonld(slug):
    g=[PERSON,LABEL,{'@type':'WebSite','@id':SITE+'/#website','url':SITE+'/','name':'Arrest Records - Nicholas Elia','publisher':{'@id':SITE+'/#arrest-records'}}]
    path,label,title,desc=PAGES[slug]
    g.append({'@type':'WebPage','@id':SITE+path+'#webpage','url':SITE+path,'name':title,'description':desc,'isPartOf':{'@id':SITE+'/#website'},'about':{'@id':SITE+'/#nicholas-elia'}})
    if slug=='arrested':
        g.append({'@type':'MusicAlbum','name':'ARRESTED','url':SITE+'/arrested','byArtist':{'@id':SITE+'/#nicholas-elia'},
          'recordLabel':{'@id':SITE+'/#arrest-records'},'genre':['Hip-Hop','Electronic'],
          'description':'ARRESTED is the new album by Nicholas Elia on Arrest Records, coming 1st quarter 2027.','image':COVER})
    if slug!='index':
        g.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Arrest Records','item':SITE+'/'},{'@type':'ListItem','position':2,'name':label.title(),'item':SITE+path}]})
    return json.dumps({'@context':'https://schema.org','@graph':g},ensure_ascii=False)
esc=lambda x:x.replace('&','&amp;').replace('"','&quot;')
def page(slug,hero,robots='index,follow,max-image-preview:large,max-snippet:-1',canonical=True,title=None,desc=None,body=None):
    path,label,t,d=PAGES.get(slug,('','','',''))
    title=title or t; desc=desc or d
    nav=''.join(f'<li><a href="{PAGES[s][0]}"{" class=active" if s==slug else ""}>{PAGES[s][1]}</a></li>' for s in ORDER)
    img=COVER if slug=='arrested' else LOGO
    head_seo=''
    if canonical:
        c=SITE+path
        head_seo=f'''<link rel="canonical" href="{c}">
<meta property="og:site_name" content="Arrest Records"><meta property="og:type" content="website"><meta property="og:url" content="{c}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="1200"><meta property="og:image:alt" content="{esc(title)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{img}">
<script type="application/ld+json">{jsonld(slug)}</script>'''
    inner=body if body is not None else f'{hero}\n{frag(slug+"-0")}\n{frag(slug+"-1")}\n{frag(slug+"-2")}'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}"><meta name="author" content="Nicholas Elia"><meta name="theme-color" content="#111111">
{head_seo}
<link rel="icon" href="/images/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Source+Sans+Pro:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head><body>
<header class="nav"><nav aria-label="Main"><ul>{nav}</ul></nav></header>
<main class="wrap">
{inner}
</main>
<div id="cookie" class="cookie" hidden><h4>Signal Detected.</h4><p>Optimizing connection... We use cookies to analyze the data stream and improve the build. By accepting, your input is aggregated to help us cut through the noise.</p><div><button data-v="declined">Decline</button><button data-v="accepted">Accept</button></div></div>
<script src="/site.js"></script>
</body></html>'''

hero_logo='<section class="hero"><div class="frame"><img src="/images/logo.jpg" srcset="/images/logo-600.jpg 600w, /images/logo.jpg 1200w" sizes="(max-width:600px) 90vw, 500px" alt="Nicholas Elia and Arrest Records logo" width="1200" height="1200" fetchpriority="high"></div></section>'
hero_cover='<section class="hero"><div class="frame"><img src="/images/arrested-cover.jpg" srcset="/images/arrested-cover-600.jpg 600w, /images/arrested-cover.jpg 1200w" sizes="(max-width:600px) 90vw, 500px" alt="ARRESTED album cover by Nicholas Elia, coming 1st quarter 2027" width="1200" height="1200" fetchpriority="high"></div></section>'
ABOUT='''<section class="about"><h2>About Nicholas Elia</h2>
<p><strong>Nicholas Elia</strong> is a hip-hop and electronic recording artist, director and producer, and the founder of <strong>Arrest Records</strong>, an independent label based in South Florida. His music is 100% clean and 100% hard: radio-ready tracks with heavy 808 drive and a message of resilience, paired with cinematic 4K visuals he directs himself.</p>
<p>His latest project, <em>Static &amp; Gold</em>, is streaming on <a href="https://open.spotify.com/artist/7iNOGW9wT6PSKnPOhkGwwY" target="_blank" rel="noopener">Spotify</a>, <a href="https://music.apple.com/us/album/static-gold/1867552961" target="_blank" rel="noopener">Apple Music</a> and <a href="https://music.amazon.com/artists/B001XGL392/nicholas-elia" target="_blank" rel="noopener">Amazon Music</a>, and the full visual odyssey is on <a href="https://www.youtube.com/@ArrestRecords" target="_blank" rel="noopener">YouTube</a>. His next album, <a href="/arrested"><strong>ARRESTED</strong></a>, arrives 1st quarter 2027. Learn more on <a href="/the-art">The Art</a> and in the <a href="/case-files">Case Files</a>, or reach out through <a href="/public-records-1">Public Records &amp; Booking</a>.</p></section>'''
home=hero_logo+'''
<section class="intro"><h1>Static &amp; Gold: Nicholas Elia</h1><p>100% Clean. 100% Hard. High-octane fuel for your workout, your commute, and your spirit.</p><p class="cta"><a href="/arrested">New album <strong>ARRESTED</strong> by Nicholas Elia - coming 1st quarter 2027 &rarr;</a></p></section>'''
def ban(slug):
    f,pos=BANNER[slug]; W,H=DIMS[f]
    return f'<section class="banner"><img src="/images/{f}" alt="{ALTS[slug]}" width="{W}" height="{H}" fetchpriority="high" style="object-position:{pos}"></section>'

for slug in ORDER:
    hero=home if slug=='index' else hero_cover if slug=='arrested' else ban(slug)
    if slug=='index': hero=hero+ABOUT
    open(f'{slug}.html','w',encoding='utf8').write(page(slug,hero))
# 404 page (not indexed)
nf='<section class="intro"><h1>Signal Lost</h1><p>That page is not in the system. Head back to the <a href="/">Mainframe</a>, check the <a href="/case-files">Case Files</a>, or preview the new album <a href="/arrested">ARRESTED</a>.</p></section>'
open('404.html','w',encoding='utf8').write(page('404',None,robots='noindex,follow',canonical=False,title='Page Not Found | Nicholas Elia - Arrest Records',desc='Page not found.',body=nf))
# sitemap, robots, redirects
urls=''.join(f'<url><loc>{SITE}{PAGES[s][0]}</loc><lastmod>{LASTMOD}</lastmod></url>' for s in ORDER)
open('sitemap.xml','w',encoding='utf8').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open('robots.txt','w',encoding='utf8').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open('_redirects','w',encoding='utf8').write('/mainframe  /  301\n/mainframe.html  /  301\n/index.html  /  301\n')
if os.path.exists('mainframe.html'): os.remove('mainframe.html')
