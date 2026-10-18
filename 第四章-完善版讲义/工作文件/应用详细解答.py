from pathlib import Path
import re,json,runpy,hashlib
P=Path(__file__).resolve().parents[1];N='第四章-转动参考系讲义-完善版'
s=(P/'工作文件/详解扩充前备份'/(N+'.tex')).read_text();baseline=s
E={}
for name in ['详解数据_例题前半.py','详解数据_例题后半.py']:E.update(runpy.run_path(str(P/'工作文件'/name))['E'])
T=runpy.run_path(str(P/'工作文件/详解数据_训练.py'))['T']
original=json.loads((P/'工作文件/详解扩充前各题解答.json').read_text())
# Two already extensive derivations are retained and made explicit at the skipped steps.
for n in [16,26]:
 body=next(r['solution'] for r in original if r['kind']=='example' and r['number']==n)
 body=body.removeprefix(r'\solution').strip()
 body=re.sub(r'\s*% BEGIN ORIGINAL FIGURES\s*$','',body)
 if n==16:
  body=r'\Step{选用随地球转动的框架} '+body
  body=body.replace('地球角速度分解为',r'''\Step{说明相对加速度中的球面曲率}
由沿经线南行有 $\dot\lambda=-u/R$，而局部北向基矢满足 $\partial\vect e_N/\partial\lambda=-\vect e_U$，因此
\[
\left(\frac{\dd\vect e_N}{\dd t}\right)_{\text{地球}}=\frac uR\vect e_U,
\quad\vect a'=-u\left(\frac{\dd\vect e_N}{\dd t}\right)_{\text{地球}}=-\frac{u^2}{R}\vect e_U.
\]
\Step{计算框架转动引起的各项}
地球角速度分解为''')
  body=body.replace('最终',r'\Step{合成绝对运动} 最终')
  body=body.replace('速度模为',r'\Step{速率与极限检验} 速度模为')
  body+=r' 当 $\Omega_E\to0$ 时，速度只剩南向 $u$，加速度只剩向地心的 $u^2/R$；当 $u=0$ 时，则恢复静止地面点随地球转动的速度和向轴加速度。'
 else:
  body=r'\Step{建立逐质元的力矩模型} '+body
  old=r'积分 $\int s\dd m=ML/2$、$\int s^2\dd m=ML^2/3$，有'
  new=r'''\Step{明确质量分布并进行积分}
均匀杆有 $\dd m=(M/L)\dd s$，所以
\[
\int_0^L s\dd m=\frac ML\int_0^Ls\dd s=\frac{ML}{2},\qquad
\int_0^Ls^2\dd m=\frac ML\int_0^Ls^2\dd s=\frac{ML^2}{3}.
\]
第二个积分同时给出关于铰轴的转动惯量。代入力矩方程，有'''
  assert old in body;body=body.replace(old,new)
  body=body.replace('令 $\\alpha=3g/(2L)$',r'\Step{在平衡附近逐项线性化} 令 $\alpha=3g/(2L)$')
  body=body.replace('令 $\\Omega_c=\\sqrt{3g/(2L)}$。',r'\Step{给出不同转速区间的周期} 令 $\Omega_c=\sqrt{3g/(2L)}$。')
  body=body.replace('杆上离心力随距铰点',r'\Step{用等效合力检查力矩积分} 杆上离心力随距铰点')
 E[n]=body
assert set(E)==set(range(1,48));assert set(T)==set(range(1,25))
spans=[];records=[]
for kind,data,prefix in [('example',E,'ex'),('exercise',T,'tr')]:
 for n,m in enumerate(re.finditer(r'\\'+kind+r'\{([^}]+)\}',s),1):
  a=s.index(r'\solution',m.end())
  ends=[x for pat in [r'\example{',r'\exercise{',r'\subsection',r'\section',r'\TeachingFigure{',r'\OriginalFigure[',r'\notice{',r'\subsubsection'] if (x:=s.find(pat,a+1))>=0]
  b=min(ends or [len(s)])
  marker=re.search(r'\s*% BEGIN ORIGINAL FIGURES\s*$',s[a:b])
  if marker:b=a+marker.start()
  old=s[a:b];new=r'\solution '+data[n].strip()+'\n\n'
  oldlabels=re.findall(r'\\label\{([^}]+)\}',old);newlabels=re.findall(r'\\label\{([^}]+)\}',new)
  assert oldlabels==newlabels,(kind,n,oldlabels,newlabels)
  key=prefix+f'{n:02}'
  marked=f'% BEGIN EXPANDED SOLUTION {key}\n'+new+f'% END EXPANDED SOLUTION {key}\n'
  spans.append((a,b,marked,old,key))
  records.append({'kind':kind,'number':n,'title':m[1],'previous_source_characters':len(old),'current_source_characters':len(new),'steps':new.count(r'\Step{'),'labels_preserved':oldlabels})
for a,b,new,old,key in sorted(spans,reverse=True):s=s[:a]+new+s[b:]
# Prove that theory, statements, diagrams and appendix outside the solution regions were preserved exactly.
restored=s
for a,b,new,old,key in spans:
 assert restored.count(new)==1,key
 restored=restored.replace(new,old,1)
assert restored==baseline
stepmacro=r'''
\newcounter{solutionstep}
\newcommand{\Step}[1]{\ifnum\value{solutionstep}>0\par\smallskip\noindent\fi\stepcounter{solutionstep}\textbf{（\arabic{solutionstep}）#1}\quad}
'''
s=s.replace(r'\newcommand{\solution}{',stepmacro+'\n'+r'\newcommand{\solution}{\setcounter{solutionstep}{0}',1)
assert s.count(r'\QuestionStatement{')==71
assert s.count(r'\TeachingFigure{')==47 and s.count(r'\OriginalFigure[')==47
assert s.count(r'\solution ')==71
assert set(re.findall(r'\\label\{([^}]+)\}',s))==set(re.findall(r'\\label\{([^}]+)\}',baseline))
assert all(x not in s for x in ['课件原图来源索引',r'\colorbox{',r'\boxed{','补充绘制'])
(P/(N+'.tex')).write_text(s)
report={'status':'passed','examples':47,'training_questions':24,'all_solution_regions_updated':71,'all_material_outside_answers_preserved_exactly':True,
 'all_equation_and_figure_labels_preserved':True,'original_figures':47,'explanatory_figures':47,'question_figures':71,
 'steps':sum(r['steps'] for r in records),'previous_solution_source_characters':sum(r['previous_source_characters'] for r in records),
 'current_solution_source_characters':sum(r['current_source_characters'] for r in records),'records':records,
 'baseline_tex_sha256':hashlib.sha256(baseline.encode()).hexdigest(),'current_tex_sha256':hashlib.sha256(s.encode()).hexdigest()}
(P/'资料核查/解答逐题完善记录.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='records'},ensure_ascii=False))
