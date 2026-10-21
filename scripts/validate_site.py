from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,parse_qs
import json,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent.parent/'docs'
origin='https://bygjun.github.io/albacheck-official'
class Audit(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.schema=[];self.in_schema=False;self.content=''
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t=='script' and dict(a).get('type')=='application/ld+json':self.in_schema=True;self.content=''
 def handle_data(self,t):
  if self.in_schema:self.content+=t
 def handle_endtag(self,t):
  if t=='script' and self.in_schema:self.schema.append(json.loads(self.content));self.in_schema=False
for file in root.rglob('index.html'):
 p=Audit();p.feed(file.read_text())
 handoff=file.relative_to(root).as_posix()=='ig/index.html'
 assert sum(t=='h1' for t,a in p.tags)==1,file
 canon=[a['href'] for t,a in p.tags if t=='link' and a.get('rel')=='canonical']
 assert len(canon)==1 and canon[0].startswith(origin)
 assert any(t=='meta' and a.get('name')=='description' and a.get('content') for t,a in p.tags)
 assert p.schema
 for t,a in p.tags:
  for key in ['src','href']:
   u=a.get(key,'');parsed=urlparse(u)
   if u.startswith('/') and not u.startswith('//'):
    assert parsed.path.startswith('/albacheck-official/'),(file,u);target=root/parsed.path.removeprefix('/albacheck-official/');assert target.exists(),(file,u)
   if u.startswith('https://play.google.com'):
    q=parse_qs(parsed.query);assert q['id']==['com.albacheck'];assert q['utm_source']==['ig' if handoff else 'website'];assert q.get('utm_medium') and q.get('utm_campaign');assert len(q.get('referrer', []))==1;ref=parse_qs(q['referrer'][0]);assert all(ref.get(k)==q[k] for k in ('utm_source','utm_medium','utm_campaign','utm_content') if k in q),(file,u);assert len(q['referrer'][0])<=512
  if t=='img':assert 'alt' in a,(file,a)
 if handoff:
  install=[a['href'] for t,a in p.tags if t=='a' and a.get('href','').startswith('https://play.google.com')]
  refresh=[a['content'] for t,a in p.tags if t=='meta' and a.get('http-equiv')=='refresh']
  assert len(install)==1 and refresh==['0;url='+install[0]]
  assert any(t=='meta' and a.get('name')=='robots' and a.get('content')=='noindex,follow' for t,a in p.tags)
  q=parse_qs(urlparse(install[0]).query);assert q['utm_medium']==['social'] and q['utm_campaign']==['albacheck_profile']
 print('PASS',file.relative_to(root))
ET.parse(root/'sitemap.xml');assert '/sitemap.xml' in (root/'robots.txt').read_text()
assert 'noindex' not in (root/'index.html').read_text()
print('PASS: HTML, semantic headings, canonical/descriptions, JSON-LD, links/assets, installation parameters, sitemap and robots')
