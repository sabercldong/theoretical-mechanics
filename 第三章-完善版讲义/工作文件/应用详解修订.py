from pathlib import Path
import json,re,runpy,hashlib
P=Path(__file__).resolve().parents[1];N='第三章-刚体力学讲义-完善版'
s=(P/'工作文件/题干题图修订后主稿.tex').read_text(); baseline=s
E=runpy.run_path(str(P/'工作文件/详解扩展数据.py'))['E']
Q=runpy.run_path(str(P/'工作文件/训练详解补全.py'));X,A,H=Q['X'],Q['A'],Q['H']
notes={
3:r'\Step{给出速率} 由 $v^2=75$，速率为 $5\sqrt3\simeq8.66025\,\mathrm{m\,s^{-1}}$。三个分量的符号描述运动方向，取模时不能把分量代数相加。',
7:r'\Step{检验初始位置与单一转动极限} 题设 $AB$ 还须取向 $+\vect e_2$，才与上述有向相位一致。若 $\omega_2=0$，两点只随杆绕铰轴转动；若 $\omega_1=0$，圆心静止，两点速度大小均为 $a|\omega_2|$。两项的方向与初值均由同一个右手轴组确定。',
8:r'\Step{明确轴向分量的含义} 本体轴向分量是 $\Omega\cos\theta_0+\omega$，欧拉角自转率为 $\omega$，差值来自进动在本体轴上的投影。只有 $\Omega\cos\theta_0=0$ 时两者才相同。',
11:r'\Step{检查滚动轴与量纲} 接触母线上任一点的位置平行于 $\vect\omega$，因此其速度严格为零；最高圆周材料点的速度则垂直接触母线。$h|\omega|\sin2\alpha$ 的量纲为长度除时间，与速度一致。',
48:r'\Step{说明能量求导与初始静止的相容性} 能量式在 $\dot x\ne0$ 的运动段求导后得到加速度；再由运动方程的连续性延伸至释放瞬间，避免在 $t=0$ 直接除以零。实心圆柱由静止开始还有 $x(t)=g\sin\beta\,t^2/3$，与常加速度 $2g\sin\beta/3$ 一致。',
52:r'\Step{应用小振动初值并检查接触} 线性近似给出 $\varphi(t)\simeq\varphi_0\cos(\sqrt{2g/(3q)}\,t)$。释放端 $N=mg\cos\varphi_0>0$，运动中 $\cos\varphi\ge\cos\varphi_0$，故接触持续受压。最大摩擦比在端点取得，保证全程纯滚动的条件须在释放前核查。'}
# Divide preserved proofs only at complete displayed-equation boundaries, never inside an environment.
def organize(body,first='明确模型与计算依据',second='逐项计算与求解',third='回代与物理检验'):
 body=body.strip(); cuts=[]
 for m in re.finditer(r'\\\]\s*\n|\\end\{(?:align\*?|equation\*?)\}\s*\n',body):
  if .19*len(body)<m.end()<.84*len(body):cuts.append(m.end())
 # Existing titled paragraphs are already logical steps. Retain their wording.
 if r'\paragraph{' in body:
  return r'\Step{'+first+'} '+re.sub(r'\\paragraph\{([^}]+)\}',lambda m:r'\Step{'+m[1].rstrip('。')+'}',body)
 chosen=[]
 for frac in [.38,.72]:
  available=[c for c in cuts if c not in chosen]
  if available:chosen.append(min(available,key=lambda c:abs(c-frac*len(body))))
 for c,title in sorted(zip(sorted(chosen),[second,third][:len(chosen)]),reverse=True):body=body[:c]+'\n\\Step{'+title+'}\n'+body[c:]
 return r'\Step{'+first+'} '+body
spans=[];records=[]
for kind in ['example','exercise']:
 for n,m in enumerate(re.finditer(r'\\'+kind+r'\{([^}]+)\}',s),1):
  a=s.index(r'\solution',m.end());ends=[x for pat in [r'\example{',r'\exercise{',r'\subsection',r'\section',r'\TeachingFigure{',r'\OriginalFigure[',r'\notice{',r'\subsubsection',r'\clearpage',r'\addtocontents'] if (x:=s.find(pat,a+1))>=0];b=min(ends or [len(s)])
  marker=re.search(r'\s*% BEGIN ORIGINAL FIGURES\s*$',s[a:b])
  if marker:b=a+marker.start()
  old=s[a:b];body=old.removeprefix(r'\solution').strip()
  if kind=='example':
   if n in E:newbody=E[n]
   else:newbody=organize(body)+('\n'+notes[n] if n in notes else '')
  else:
   h1,h2,h3=H[n];newbody=r'\Step{'+h1+'} '+body
   found=[]
   for anchor,title in zip(A[n],[h2,h3]):
    if anchor in newbody:
     newbody=newbody.replace(anchor,r'\Step{'+title+'} '+anchor,1);found.append(anchor)
   if len(found)<2:
    # A missing literal anchor is resolved through complete math-block boundaries.
    newbody=organize(body,h1,h2,h3)
   newbody+='\n'+X[n]
  new=r'\solution '+newbody.strip()+'\n\n';key=('ex' if kind=='example' else 'tr')+f'{n:02}'
  labs=lambda t:re.findall(r'\\label\{([^}]+)\}',t)
  assert labs(old)==labs(new),(kind,n,labs(old),labs(new))
  marked=f'% BEGIN DETAILED ANSWER {key}\n'+new+f'% END DETAILED ANSWER {key}\n'
  spans.append((a,b,marked,old));records.append({'kind':kind,'number':n,'title':m[1],'old_characters':len(old),'new_characters':len(new),'steps':new.count(r'\Step{'),'rewritten':kind=='example' and n in E})
for a,b,new,old in sorted(spans,reverse=True):s=s[:a]+new+s[b:]
restored=s
for a,b,new,old in spans:restored=restored.replace(new,old,1)
assert restored==baseline,'Unintended alteration outside answer regions'
# Correct standalone statements found during derivation and align examples with declared vector conventions.
s=s.replace('其中位置矢量均在空间系表达。',r'题给 $\vect\rho$ 均为本体坐标中的常矢量，以 $\mathsf R$ 将其转换为空间分量。')
s=s.replace('半径 $AB$ 垂直铰轴并在水平面内。',r'半径 $AB$ 垂直铰轴并在水平面内，初始沿 $\vect e_2=\vect e_3\times\vect e_1$，其中 $\vect e_1$ 沿杆向下、$\vect e_3$ 沿铰轴正向。')
# The numerical test is part of the question, rather than an unannounced choice in the answer.
needle='给定 $\\gamma$ 的单位为 $\\mathrm{rad\\,s^{-1}\\,T^{-1}}$，'
# Preserve the actual existing stem and append its numerical input before the diagram key.
start=s.index(r'\exercise{共振角频率与普通频率的换算}');end=s.index(r'\solution',start)
part=s[start:end]
if '2\\pi\\times10^7' not in part:
 part=part.replace('}{tr28}',r'并以 $|\gamma|=2\pi\times10^7\,\mathrm{rad\,s^{-1}\,T^{-1}}$、$B_0=2\,\mathrm T$ 为给定数值，求频率和周期。}{tr28}')
 s=s[:start]+part+s[end:]
# Preserve complete prose in the three legacy one-line notices.
s=re.sub(r'(?m)^\\notice (.+)$',lambda m:r'\notice{'+re.sub(r'\\Step\{[^}]+\}\s*','',m[1])+'}',s)
s=s.replace(r'\vspace{0pt}\setlength{\parindent}{0pt}#1',r'\vspace{0pt}\raggedright\setlength{\parindent}{0pt}#1')
s=s.replace(r'$|a_B|\cos30^\circ=R\Omega^2\cos75^\circ+(\sqrt2/3)R\Omega^2$，与分量法一致。',r'\[|a_B|\cos30^\circ=R\Omega^2\cos75^\circ+\frac{\sqrt2}{3}R\Omega^2,\]与分量法一致。')
s=s.replace(r'连杆角加速度逆时针，滑块加速度向左，大小约为 $0.8431895R\Omega^2$。',r'连杆角加速度逆时针，滑块加速度向左。其大小为\[|a_B|\simeq0.8431895R\Omega^2.\]')
s=s.replace(r'\Step{直接求角速度导数验证反例}',r'\Step{检验角速度导数}')
s=s.replace('章末自测','章末训练题').replace('自测与详解','训练题与详解')
assert s.count(r'\OriginalFigure[')==117 and s.count(r'\TeachingFigure{')==59
assert len(records)==96 and s.count('% BEGIN DETAILED ANSWER ')==96
assert all(x not in s for x in ['课件原图来源索引','补充绘制',r'\colorbox{',r'\boxed{'])
(P/(N+'.tex')).write_text(s)
report={'answers':96,'main_answers_rewritten':len(E),'all_original_solution_explanations_outside_answer_blocks_preserved':True,'original_figures':117,'body_figures':59,'question_figures':96,'steps':sum(r['steps'] for r in records),'old_characters':sum(r['old_characters'] for r in records),'new_characters':sum(r['new_characters'] for r in records),'records':records,'tex_sha256':hashlib.sha256(s.encode()).hexdigest()}
(P/'资料核查/第三章详解修订记录.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='records'},ensure_ascii=False))
