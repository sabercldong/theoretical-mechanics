from pathlib import Path
import re,json
P=Path(__file__).resolve().parents[1];N='第二章-质点组力学讲义-完善版'
def commands(s,kind):
 for n,m in enumerate(re.finditer(r'\\'+kind+r'\{',s),1):
  a=m.end();b=a;depth=1
  while depth:
   if s[b]=='{':depth+=1
   elif s[b]=='}':depth-=1
   b+=1
  yield n,m.start(),b,s[a:b-1]
def boundary(s,a):
 ends=[x for p in [r'\example{',r'\exercise{',r'\subsection',r'\section',r'\TeachingFigure{',r'\OriginalFigure{',r'\notice{',r'\subsubsection',r'\clearpage',r'\addtocontents',r'\begin{figure}'] if (x:=s.find(p,a+1))>=0];b=min(ends or [len(s)])
 panel=s.find(r'\OriginalPanel{',a,b)
 if panel>=0:
  start=s.rfind(r'\par\begin{center}\begin{minipage}',a,panel)
  assert start>=a,'paired original figure start missing';b=start
 return b
if __name__=='__main__':
 s=(P/'工作文件/详解修订前备份'/(N+'.tex')).read_text();R=[]
 for kind in ['example','exercise']:
  for n,a,b,title in commands(s,kind):
   c=s.index(r'\solution',b);d=boundary(s,c)
   R.append(dict(kind=kind,n=n,title=title,stem=s[b:c],answer=s[c:d],length=d-c))
 (P/'工作文件/详解修订前题目.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));print('90 question blocks parsed with balanced titles')
