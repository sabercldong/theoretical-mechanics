from pathlib import Path
P=Path(__file__).resolve().parents[1];s=(P/'第二章-质点组力学讲义-完善版.tex').read_text();head=s[:s.index(r'\begin{document}')]
keys=[f'ex{n:02}' for n in range(1,67)]+[f'tr{n:02}' for n in range(1,25)]
for kind,folder,per,w,h in [('题图总览','题图',6,'.91', '3.25cm'),('解答图总览','解答图',4,'.94','4.5cm')]:
 body=r'\begin{document}\pagestyle{empty}'+'\n'
 for i,k in enumerate(keys):
  body+=r'\noindent\begin{minipage}{\linewidth}\centering\textbf{'+k+'}\\[2pt]\n'+r'\sbox{\QuestionDrawing}{\input{'+folder+'/'+k+'.tex}}'+ '\n'+r'\includegraphics[width='+w+r'\linewidth,height='+h+r',keepaspectratio]{example-image}' if False else ''
  # Both dimension bounds are applied to the saved picture.
  body+=r'\noindent\begin{minipage}{\linewidth}\centering\textbf{'+k+r'}\par\smallskip\sbox{\QuestionDrawing}{\input{'+folder+'/'+k+'.tex}}'+ '\n'
  body+=r'\sbox{\SolutionScaled}{\resizebox{'+w+r'\linewidth}{!}{\usebox{\QuestionDrawing}}}\ifdim\ht\SolutionScaled>'+h+r'\resizebox{!}{'+h+r'}{\usebox{\QuestionDrawing}}\else\usebox{\SolutionScaled}\fi\end{minipage}\par\vfill'+'\n'
  if (i+1)%per==0:body+=r'\clearpage'+'\n'
 body+=r'\end{document}'
 (P/'工作文件'/(kind+'.tex')).write_text(head+body)
