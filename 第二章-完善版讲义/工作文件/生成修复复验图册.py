from pathlib import Path
P=Path(__file__).resolve().parents[1];s=(P/'第二章-质点组力学讲义-完善版.tex').read_text();head=s[:s.index(r'\begin{document}')]
keys=['ex03','ex06','ex12','ex26','ex25','ex35','ex50','ex51'];body=r'\begin{document}\pagestyle{empty}'+'\n'
for k in keys:
 for folder in ['题图','解答图']:
  body+=r'\noindent\textbf{'+folder+':'+k+r'}\par\smallskip\noindent\begin{minipage}{\linewidth}\centering\sbox{\QuestionDrawing}{\input{'+folder+'/'+k+'.tex}}'+ '\n'
  body+=r'\sbox{\SolutionScaled}{\resizebox{.90\linewidth}{!}{\usebox{\QuestionDrawing}}}\ifdim\ht\SolutionScaled>7.4cm\resizebox{!}{7.4cm}{\usebox{\QuestionDrawing}}\else\usebox{\SolutionScaled}\fi\end{minipage}\par\vfill'+'\n'
 body+=r'\clearpage'+'\n'
body+=r'\end{document}';(P/'工作文件/修复复验.tex').write_text(head+body)
