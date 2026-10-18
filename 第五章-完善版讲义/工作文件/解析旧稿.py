from pathlib import Path
import re,json,hashlib,zipfile
P=Path(__file__).resolve().parents[1];B=P.parent
s=(P/'工作文件/旧版完整主稿.tex').read_text()
def group(s,a):
 assert s[a]=='{';b=a+1;d=1
 while d:
  if s[b]=='{' and s[b-1]!='\\':d+=1
  if s[b]=='}' and s[b-1]!='\\':d-=1
  b+=1
 return s[a+1:b-1],b

def commands(s,name):
 for n,m in enumerate(re.finditer(r'\\'+name+r'\{',s),1):
  title,b=group(s,m.end()-1);yield n,m.start(),b,title
# Detach all body TikZ figures, preserving their exact source and captions.
figures=[];spans=[]
for i,m in enumerate(re.finditer(r'\\figstart\b',s[s.index(r'\begin{document}'):]),1):
 a=s.index(r'\begin{document}')+m.start();t=s.index(r'\begin{tikzpicture}',a);u=s.index(r'\end{tikzpicture}',t)+len(r'\end{tikzpicture}');capstart=s.index(r'\figend{',u);cap,b=group(s,capstart+len(r'\figend'))
 # Adjacent material before the picture belongs to the body; standard figures have no prose here.
 assert not s[a+len(r'\figstart'):t].strip(),(i,s[a:t])
 key=f'c5-diagram-{i:02}';(P/'补充图'/(key+'.tex')).write_text(s[t:u]+'\n')
 figures.append(dict(key=key,caption=cap,old_start=a,sha256=hashlib.sha256(s[t:u].encode()).hexdigest()));spans.append((a,b,r'\TeachingFigure{'+key+'}{'+cap+'}'))
for a,b,new in reversed(spans):s=s[:a]+new+s[b:]
assert len(figures)==62
(P/'工作文件/正文图分离后主稿.tex').write_text(s)
R=[]
for kind in ['example','exercise']:
 for n,a,b,title in commands(s,kind):
  # Everything until the next topic heading or example is retained in this model record,
  # except figures, which are independently placed in the body.
  ends=[m.start()+b for m in re.finditer(r'\\(?:example\{|exercise\{|subsection\b|section\b|end\{document\})',s[b:])];c=min(ends or [len(s)])
  chunk=s[b:c];sol=chunk.find(r'\solution')
  R.append(dict(kind=kind,number=n,title=title,start=a,title_end=b,end=c,has_solution=sol>=0,stem=chunk[:sol] if sol>=0 else '',content=chunk,answer=chunk[sol:] if sol>=0 else chunk))
assert len(R)==106
(P/'工作文件/旧稿题目与解答.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
(P/'工作文件/正文图清单.json').write_text(json.dumps(figures,ensure_ascii=False,indent=2))
hashes=[]
for f in sorted(B.glob('理论力学-c5-*.pptx')):
 with zipfile.ZipFile(f) as z:n=len([a for a in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',a)])
 hashes.append(dict(file=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),slides=n))
(P/'资料核查/原课件校验.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2))
print('86 examples,20 exercises,62 body diagrams detached; source slides',sum(r['slides'] for r in hashes))
