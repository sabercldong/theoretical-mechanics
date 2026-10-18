from pathlib import Path
import json,re,runpy,hashlib
from 题目解析 import commands,boundary
P=Path(__file__).resolve().parents[1];N='第二章-质点组力学讲义-完善版'
s=(P/'工作文件/题干修订后主稿.tex').read_text();baseline=s
D=runpy.run_path(str(P/'工作文件/详解扩展数据.py'));E,T=D['E'],D['T']
F={r['key']:r for r in json.loads((P/'工作文件/解答图与推导对应.json').read_text())}
records=[];spans=[]
for kind,data in [('example',E),('exercise',T)]:
 for n,_,end,title in commands(s,kind):
  a=s.index(r'\solution',end);b=boundary(s,a);old=s[a:b];body=old.removeprefix(r'\solution').strip()
  key=('ex' if kind=='example' else 'tr')+f'{n:02}';pre,post=data[n];f=F[key]
  body=re.sub(r'\\paragraph\{([^}]+)\}',lambda m:r'\Step{'+m[1]+'}',body)
  new=r'\solution \Step{明确系统、坐标与约束} '+pre+'\n\n'+f['note']+'\n'+r'\SolutionFigure{'+key+'}{'+f['caption']+'}\n\n'+r'\Step{列出方程并求解} '+body+'\n\n'+post+'\n\n'
  marked=f'% BEGIN DETAILED ANSWER {key}\n'+new+f'% END DETAILED ANSWER {key}\n'
  assert re.findall(r'\\label\{[^}]+\}',old)==re.findall(r'\\label\{[^}]+\}',new)
  spans.append((a,b,marked,old));records.append(dict(kind=kind,number=n,key=key,title=title,old_characters=len(old),new_characters=len(new),steps=new.count(r'\Step{'),old_solution_preserved=body in new,solution_figure=key))
for a,b,new,_ in sorted(spans,reverse=True):s=s[:a]+new+s[b:]
restored=s
for _,_,new,old in spans:restored=restored.replace(new,old,1)
assert restored==baseline,'Unexpected change outside answer regions'
s=s.replace(r'\renewcommand*\l@section',r'\renewcommand\@pnumwidth{2.5em}\renewcommand*\l@section',1)
s=re.sub(r'([A-Za-z])\\prime',lambda m:m[1]+r'^{\prime}',s)
s=s.replace('证明径向转向点仍有角向运动',r'证明 $\rho>0$ 时径向转向点仍有角向运动，并说明 $\rho=0$ 的区别')
s=s.replace(r'$m\prime$',r'$m^{\prime}$').replace(r'$s\prime$',r'$s^{\prime}$').replace(r'$a\prime$',r'$a^{\prime}$')
for pat,n in [(r'\OriginalFigure{',31),(r'\OriginalPanel{',12),(r'\TeachingFigure{',22),(r'\SolutionFigure{',90)]:assert s.count(pat)==n,(pat,s.count(pat))
assert len(records)==90
assert all(v not in s for v in ['课件原图来源索引','补充绘制',r'\boxed{',r'\colorbox{'])
(P/(N+'.tex')).write_text(s)
report=dict(answers=90,examples=66,training=24,old_solution_characters=sum(x['old_characters'] for x in records),new_solution_characters=sum(x['new_characters'] for x in records),steps=sum(x['steps'] for x in records),outside_answer_blocks_preserved=True,records=records,tex_sha256=hashlib.sha256(s.encode()).hexdigest())
(P/'资料核查/第二章详解修订记录.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print({k:v for k,v in report.items() if k!='records'})
