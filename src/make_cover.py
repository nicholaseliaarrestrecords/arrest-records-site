# Adds the title/artist lettering to the Nano Banana artwork. Run with plain `python3` (needs Pillow).
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART=os.path.join(os.path.dirname(ROOT),'Arrested','Artwork')
BASE=os.path.join(ART,'ARRESTED-cover-base-no-text.jpeg')
FONT='/System/Library/Fonts/Supplemental/Copperplate.ttc'
N=2048
img=Image.open(BASE).convert('RGB').resize((N,N),Image.LANCZOS)
# gentle darkening of the lower band so lettering stays legible
band=Image.new('L',(N,N),0); bd=ImageDraw.Draw(band)
for y in range(int(N*.62),N):
    bd.line([(0,y),(N,y)],fill=int(150*(max(0,(y-N*.62))/(N*.38))**1.4))
img=Image.composite(Image.new('RGB',(N,N),(0,0,0)),img,band)

def tracked(text,font,track):
    w=sum(font.getlength(c) for c in text)+track*(len(text)-1)
    return w
def text_mask(text,font,track,size):
    m=Image.new('L',size,0); d=ImageDraw.Draw(m)
    w=tracked(text,font,track); x=(size[0]-w)/2
    asc,desc=font.getmetrics(); y=(size[1]-(asc+desc))/2
    for c in text:
        d.text((x,y),c,font=font,fill=255); x+=font.getlength(c)+track
    return m
def gold_layer(mask,top,bot):
    g=Image.new('RGB',mask.size); gd=ImageDraw.Draw(g)
    bbox=mask.getbbox(); y0,y1=bbox[1],bbox[3]
    for y in range(mask.size[1]):
        t=min(max((y-y0)/max(1,y1-y0),0),1)
        gd.line([(0,y),(mask.size[0],y)],fill=tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3)))
    return g

# Title
title='ARRESTED'
fsize=330
while True:
    f=ImageFont.truetype(FONT,fsize,index=2)
    if tracked(title,f,fsize*0.10)<=N*0.80: break
    fsize-=4
f=ImageFont.truetype(FONT,fsize,index=2); track=fsize*0.10
tm=text_mask(title,f,track,(N,420))
# place the title block
ty=int(N*0.755)
glow=tm.filter(ImageFilter.GaussianBlur(28)); 
glow_rgb=Image.new('RGB',tm.size,(212,175,55))
img.paste(glow_rgb,(0,ty),glow.point(lambda v:int(v*0.55)))
shadow=tm.filter(ImageFilter.GaussianBlur(6)); 
img.paste(Image.new('RGB',tm.size,(0,0,0)),(4,ty+8),shadow)
gold=gold_layer(tm,(255,236,150),(176,128,26))
img.paste(gold,(0,ty),tm)
# thin gold highlight edge
edge=ImageChops.subtract(tm,tm.filter(ImageFilter.MinFilter(5)))
img.paste(Image.new('RGB',tm.size,(255,246,200)),(0,ty),edge.point(lambda v:int(v*0.7)))

# Artist line
af=ImageFont.truetype(FONT,92,index=2); atrack=92*0.42
am=text_mask('NICHOLAS ELIA',af,atrack,(N,160))
ay=int(N*0.915)
img.paste(Image.new('RGB',am.size,(0,0,0)),(2,ay+4),am.filter(ImageFilter.GaussianBlur(5)))
img.paste(Image.new('RGB',am.size,(245,240,225)),(0,ay),am)
# label line, small, top
lf=ImageFont.truetype(FONT,44,index=1); lm=text_mask('ARREST RECORDS',lf,44*0.5,(N,90))
img.paste(Image.new('RGB',lm.size,(212,175,55)),(0,int(N*0.032)),lm.point(lambda v:int(v*0.9)))

os.makedirs(ART,exist_ok=True)
img.save(os.path.join(ART,'ARRESTED-cover-2048.png'),optimize=True)
site=img.resize((1200,1200),Image.LANCZOS)
site.save(os.path.join(ROOT,'public','images','arrested-cover.jpg'),quality=88,optimize=True,progressive=True)
site.resize((600,600),Image.LANCZOS).save(os.path.join(ROOT,'public','images','arrested-cover-600.jpg'),quality=86,optimize=True,progressive=True)
print('ok',fsize)
