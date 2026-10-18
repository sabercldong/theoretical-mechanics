from pathlib import Path
import re,json
from 题设数据 import P,stems,exercises
from 图解数据 import rows,training
from 推导扩展 import extra_examples,extra_training
name='第五章-分析力学讲义-完善版'
s=(P/'工作文件/正文图分离后主稿.tex').read_text()
a=s.index(r'\begin{document}');head=s[:a];body=s[a:]
head=head.replace('单文件源文档，所有图为TikZ矢量图。','主文档与原图、题图及解答图共同组成可编辑工程。')
body=body.replace(r'\par\noindent\begin{minipage}{\linewidth}','').replace(r'\end{minipage}','')
body=re.sub(r'求解时依次检查：[^\n]+\n','',body)
body=body.replace('完整接触检验为','接触与摩擦条件为').replace('本章结构的回顾','分析力学的结构联系')
def group(s,a):
 d=1;b=a+1
 while d:
  if s[b]=='{' and s[b-1]!='\\':d+=1
  if s[b]=='}' and s[b-1]!='\\':d-=1
  b+=1
 return s[a+1:b-1],b
changes=[];counts={}
for kind,data,stemdata,extras,prefix in [('example',rows,stems,extra_examples,'ex'),('exercise',training,exercises,extra_training,'tr')]:
 for n,m in enumerate(re.finditer(r'\\'+kind+r'\{',body),1):
  title,b=group(body,m.end()-1);end=next((b+x.start() for x in re.finditer(r'\\(?:example\{|exercise\{|subsection\b|section\b|end\{document\})',body[b:])),len(body));old=body[b:end]
  explicit=old.find(r'\solution');answer=old[explicit+len(r'\solution'):] if explicit>=0 else old
  # Figures attached to the original question stay available in the worked solution too.
  if explicit>=0:
   figs=re.findall(r'\\TeachingFigure\{[^\n]+',old[:explicit])
   answer='\n'.join(figs)+'\n'+answer
  r=data[n];key=f'{prefix}{n:02}';label=f'ex:c5-{n}' if prefix=='ex' else f'tr:c5-{n}'
  if isinstance(r['fig'],int):
   answer=re.sub(r'\\TeachingFigure\{c5-diagram-'+f'{r["fig"]:02}'+r'\}\{[^\n]*\}\s*','',answer)
  if prefix=='ex' and n==19:
   answer=answer.replace(r'\mu',r'\mu_s').replace(r'\mu_s_s',r'\mu_s')
  if prefix=='ex' and n==23:answer=answer.replace('$P_1=m_1g,P_2=m_2g$','$P_1=m_1g,P_2=m_2g$')
  if prefix=='tr' and n==9:
   answer=answer.replace(r'各除以自身 $M$ 范数后得到归一模式，$Q_\pm=a_\pm^{\mathsf T}Mq$，再分别解谐振子。','质量归一化后的模式及运动展开如下。')
  if prefix=='ex' and n==46:
   answer=answer.replace('非凸函数可出现多支，需分别讨论反解区域。','一般非凸函数可能出现多支；本题 $a<0$ 的特殊二次函数仍可唯一反解，凸共轭另见下文。')
  if prefix=='ex' and n==1:answer=r'\[\dd x=R\cos\theta\,\dd\varphi,\qquad\dd y=R\sin\theta\,\dd\varphi.\]'+'\n'+answer
  if prefix=='ex' and n==76:answer=answer.replace(r'$u=A\sin(k_nx)\cos(\omega_nt+\delta)$',r'\[u=A\sin(k_nx)\cos(\omega_nt+\delta).\]')
  stem=stemdata[n]
  qmacro='LongQuestionStatement' if (prefix=='ex' and n in (66,68)) or r['fig'] in [3,4,13,40,42,'cyclic_three','four_models','atwood_pair','tangent_pair','cart_modes','geodesic_isoperimetric','two_osc','quantum_spread','elastic_waves'] else 'QuestionStatement'
  text='\n\\'+kind+'{'+title+'}\n\\label{'+label+'}\n\\'+qmacro+'{'+stem+'}{'+key+'}{'+('例' if prefix=='ex' else '训练题')+str(n)+'的条件与模型}\n'
  text+=r'\solution \Step{坐标、方向与模型关系}'+' 图~\\ref{fig:solution-'+key+'}~中，'+r['bridge']+'\n'
  text+=r'\SolutionFigure{'+key+'}{'+('例' if prefix=='ex' else '训练题')+str(n)+'的分析与计算过程}\n'
  text+=r'\Step{方程与推导}'+'\n'+(r'记两杆重量 $P_1=m_1g,P_2=m_2g$。' if prefix=='ex' and n==23 else '')+answer.strip()+'\n'
  if n in extras:
   heading,addition=extras[n];text+='\n'+r'\Step{'+heading+'} '+addition+'\n'
  if prefix=='tr' and n in (5,15,17):
   # Long calculational expressions belong on separate lines.
   def display_long(m):
    if len(m[1])<=(35 if n in (5,15) else 55):return m[0]
    punct={'，':',','。':'.','；':';','':''}[m[2]]
    return '\n\\['+m[1]+punct+'\\]\n'
   text=re.sub(r'\$([^$\n]+)\$([，。；]?)',display_long,text)
   text=text.replace(r'\]。两条水平边',r'\]两条水平边')
  changes.append((m.start(),end,text));counts[kind]=n
for a,b,t in sorted(changes,reverse=True):body=body[:a]+t+body[b:]
# Keep physical validity conditions, but remove advisory checklists and study paragraphs.
body=body.replace('若连接物只能受拉，应逐时检查 $s\ge a$。','若连接物只能受拉，解仅在 $s\ge a$ 的绷紧阶段有效。')
body=body.replace('原课件','课件').replace('所有“驻值”条件','一阶“驻值”条件')
head=head.replace('amsmath,amssymb,bm,mathtools,xcolor,tikz,booktabs,array,tabularx,longtable','amsmath,amssymb,bm,mathtools,xcolor,tikz,booktabs,array,tabularx,longtable,graphicx,adjustbox')
head=head.replace(r'\newcommand{\solution}{\par\nopagebreak[4]\noindent\textbf{解}\quad}',r'\newcommand{\solution}{\par\setcounter{solutionstep}{0}\Needspace{6\baselineskip}\noindent\textbf{解}\quad}')
head=head.replace(r'\subsubsection*{例\theexample\quad #1}',r'\Needspace{8\baselineskip}\subsubsection*{例\theexample\quad #1}').replace(r'\subsubsection*{训练题\theexercise\quad #1}',r'\Needspace{8\baselineskip}\subsubsection*{训练题\theexercise\quad #1}')
macros=r'''
\makeatletter
\newcommand{\Needspace}[1]{\par\if@nobreak\else\penalty0\begingroup\dimen0=#1\relax\dimen2=\pagegoal\advance\dimen2 by-\pagetotal\ifdim\dimen0>\dimen2\newpage\fi\endgroup\fi}
\makeatother
\newcounter{solutionstep}
\newcommand{\Step}[1]{\ifnum\value{solutionstep}>0\par\smallskip\noindent\fi\stepcounter{solutionstep}\textbf{（\arabic{solutionstep}）#1}\quad}
\newsavebox{\LessonDrawing}
\newcommand{\TeachingFigure}[2]{\par\addvspace{6pt}\noindent\begin{minipage}{\linewidth}\centering\sbox{\LessonDrawing}{\input{补充图/#1.tex}}\adjustbox{max width=.97\linewidth,max height=7cm}{\usebox{\LessonDrawing}}\captionof{figure}{#2}\label{fig:lesson-#1}\end{minipage}\par\addvspace{6pt}}
\newcommand{\OriginalFigure}[2]{\par\addvspace{5pt}\noindent\begin{minipage}{\linewidth}\centering\includegraphics[width=.77\linewidth,height=5.5cm,keepaspectratio]{原图/#1.pdf}\captionof{figure}{#2}\label{fig:original-#1}\end{minipage}\par\addvspace{5pt}}
\newsavebox{\QuestionDrawing}
\newcommand{\QuestionStatement}[3]{\par\noindent\begin{minipage}{\linewidth}\begin{minipage}[t]{.60\linewidth}\vspace{0pt}\raggedright\setlength{\parindent}{0pt}#1\end{minipage}\hfill\begin{minipage}[t]{.37\linewidth}\vspace{2pt}\centering\sbox{\QuestionDrawing}{\input{题图/#2.tex}}\adjustbox{max width=.99\linewidth,max height=5.5cm}{\usebox{\QuestionDrawing}}\captionof{figure}{#3}\label{fig:question-#2}\end{minipage}\end{minipage}\par\smallskip}
\newcommand{\LongQuestionStatement}[3]{\par #1\par\smallskip\noindent\begin{minipage}{\linewidth}\centering\sbox{\QuestionDrawing}{\input{题图/#2.tex}}\adjustbox{max width=.82\linewidth,max height=4.5cm}{\usebox{\QuestionDrawing}}\captionof{figure}{#3}\label{fig:question-#2}\end{minipage}\par\smallskip}
\newsavebox{\SolutionDrawing}
\newcommand{\SolutionFigure}[2]{\par\addvspace{5pt}\noindent\begin{minipage}{\linewidth}\centering\sbox{\SolutionDrawing}{\input{解答图/#1.tex}}\adjustbox{max width=.98\linewidth,max height=6cm}{\usebox{\SolutionDrawing}}\captionof{figure}{#2}\label{fig:solution-#1}\end{minipage}\par\addvspace{5pt}}
'''
# Do not repeat diagram labels when the original body illustration appears twice.
macros=macros.replace(r'\label{fig:lesson-#1}','')
main=head+macros+body
# Keep sentence punctuation attached to the preceding displayed equation.
main=re.sub(r'\\\]\s*([，。；])',lambda m: {'，':',','。':'.','；':';'}[m[1]]+r'\]',main)

(P/(name+'.tex')).write_text(main)
(P/'资料核查/重排记录.json').write_text(json.dumps({'counts':counts,'retained_body_diagrams':62,'question_drawings':106,'solution_drawings':106,'source_derivations':'old derivations retained; explicit-stem conditions restated independently','new_detail_blocks':len(extra_examples)+len(extra_training)},ensure_ascii=False,indent=2))
print(name,counts,len(main))
