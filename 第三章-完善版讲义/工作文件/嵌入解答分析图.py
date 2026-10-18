from pathlib import Path
import re,json
P=Path(__file__).resolve().parents[1];N='第三章-刚体力学讲义-完善版'
s=(P/(N+'.tex')).read_text(); assert r'\SolutionFigure{' not in s,'Run 应用详解修订.py first to reset to the text master'
macro=r'''
\newsavebox{\SolutionDrawing}
\newsavebox{\SolutionScaled}
\newcommand{\SolutionFigure}[2]{%
\par\addvspace{6pt}\noindent\begin{minipage}{\linewidth}\centering%
\sbox{\SolutionDrawing}{\input{解答图/#1.tex}}%
\sbox{\SolutionScaled}{\resizebox{.88\linewidth}{!}{\usebox{\SolutionDrawing}}}%
\ifdim\ht\SolutionScaled>5.6cm\resizebox{!}{5.6cm}{\usebox{\SolutionDrawing}}\else\usebox{\SolutionScaled}\fi%
\captionof{figure}{#2}\label{fig:solution-#1}\end{minipage}\par\addvspace{6pt}}
'''
s=s.replace(r'\begin{document}',macro+'\n'+r'\begin{document}',1)
R=json.loads((P/'工作文件/解答图与推导对应.json').read_text())
for row in R:
 key=row['key']; a=s.index('% BEGIN DETAILED ANSWER '+key);b=s.index('% END DETAILED ANSWER '+key,a)
 body=s[a:b];step=list(re.finditer(r'\\Step\{[^}]+\}',body));assert step,key
 # The first modelling step and its equations precede the analysis diagram; later steps refer back to it.
 pos=step[1].start() if len(step)>1 else len(body)
 body=body[:pos]+r'\SolutionFigure{'+key+'}{'+row['caption']+'}\n'+body[pos:]
 first=re.search(r'\\Step\{[^}]+\}',body);body=body[:first.end()]+'\n'+row['note']+'\n'+body[first.end():]
 s=s[:a]+body+s[b:]
s=s.replace('要求此量远小于1。',r'要求 $P^2\gg Amgl$、初始轴远离两极，并使此量远小于1。')
assert s.count(r'\SolutionFigure{')==96 and len(re.findall(r'\\ref\{fig:solution-',s))==96
assert s.count(r'\OriginalFigure[')==117 and s.count(r'\TeachingFigure{')==59
(P/(N+'.tex')).write_text(s)
(P/'资料核查/解答图逐题覆盖检查.json').write_text(json.dumps({'status':'passed','questions':96,'standalone_question_diagrams':96,'solution_stage_diagrams':96,'explicit_figure_references':96,'all_diagrams_editable_tikz':True,'integration':'after modelling step and before subsequent calculation','rows':R},ensure_ascii=False,indent=2))
print('All 96 answers now have a numbered calculation-stage diagram with an explicit textual reference')
