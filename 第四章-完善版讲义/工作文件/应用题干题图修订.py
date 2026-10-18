from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parents[1]
NAME='第四章-转动参考系讲义-完善版'
s=(P/'工作文件/题干题图修订前备份'/(NAME+'.tex')).read_text()
old=s
D=json.loads((P/'工作文件/完整题干.json').read_text())
def brace(text,i):
 assert text[i]=='{'
 d=1;j=i+1
 while d:
  if text[j]=='{' and text[j-1]!='\\':d+=1
  if text[j]=='}' and text[j-1]!='\\':d-=1
  j+=1
 return text[i+1:j-1],j
# Keep all existing original/model figures when a question statement is replaced.
changes=[]
for kind,prefix,data in [('example','ex',D['examples']),('exercise','tr',D['exercises'])]:
 spans=[]
 for n,m in enumerate(re.finditer(r'\\'+kind+r'\{',s),1):
  _,j=brace(s,m.end()-1)
  label=re.match(r'\\label\{[^}]+\}',s[j:]);assert label
  a=j+label.end();b=s.index(r'\solution',a)
  former=s[a:b]
  extras=re.findall(r'% BEGIN ORIGINAL FIGURES.*?% END ORIGINAL FIGURES',former,re.S)
  stem=data[str(n)]
  labeltext=('例' if kind=='example' else '训练题')+str(n)
  replacement='\n'+r'\QuestionStatement{'+stem+'}{'+prefix+f'{n:02}'+'}{'+labeltext+'题图}\n'
  # An original drawing already adjacent to this question stays after the compact model diagram.
  if extras:replacement+='\n'+'\n'.join(extras)+'\n'
  spans.append((a,b,replacement))
  changes.append({'kind':kind,'number':n,'former_statement':former.strip(),'new_statement':stem,'diagram':'题图/'+prefix+f'{n:02}.tex'})
 for a,b,r in reversed(spans):s=s[:a]+r+s[b:]
# Remove the three tinted callouts; retain the substantive sign reminder in plain text.
spans=[]
for m in re.finditer(r'\\important\{',s):
 body,j=brace(s,m.end()-1)
 keep=body if '加速度变换项' in body else ''
 spans.append((m.start(),j,keep))
for a,b,r in reversed(spans):s=s[:a]+r+s[b:]
s=s.replace(r'\newcommand{\important}[1]{\par\smallskip\noindent\colorbox{soft}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{#1}}\par\smallskip}',r'\newcommand{\important}[1]{\par\noindent #1\par}')
# Formula content remains unchanged; simple displayed equations do not need rectangular borders.
spans=[]
for m in re.finditer(r'\\boxed\{',s):
 body,j=brace(s,m.end()-1);spans.append((m.start(),j,body))
for a,b,r in reversed(spans):s=s[:a]+r+s[b:]
# Do not print image provenance at the end of the handout.
a=s.index(r'\section*{课件原图来源索引}')
s=s[:a]+'\n\\end{document}\n'
s=s.replace('综合自测与详细解答','综合训练与详细解答').replace('自测\\theexercise','训练题\\theexercise').replace('讲义中的例题和自测','讲义中的例题和训练题')
s=s.replace(r'\newcommand{\solution}{\par\nopagebreak[4]\noindent\textbf{解}\quad}',r'\newcommand{\solution}{\par\nopagebreak[4]\smallskip\nopagebreak[4]\noindent\textbf{解答}\quad}')
# Make every stem and its diagram a single unframed unit.
macro=r'''
\newsavebox{\QuestionDrawing}
\newcommand{\QuestionStatement}[3]{%
\par\noindent\begin{minipage}{\linewidth}%
\begin{minipage}[t]{.63\linewidth}\vspace{0pt}\setlength{\parindent}{0pt}#1\end{minipage}\hfill%
\begin{minipage}[t]{.34\linewidth}\vspace{2pt}\centering%
\sbox{\QuestionDrawing}{\input{题图/#2.tex}}%
\resizebox{.98\linewidth}{!}{\usebox{\QuestionDrawing}}\par\vspace{3pt}{\small #3}%
\end{minipage}\end{minipage}\par\smallskip}
'''
s=s.replace(r'\begin{document}',macro+'\n'+r'\begin{document}',1)
# Explicitly answer new requests that were previously only implicit in surrounding discussion.
s=s.replace('极点速率约 $15.041^\\circ/\\mathrm h$。','极点速率约 $15.041^\\circ/\\mathrm h$，完整进动周期等于恒星日 $23.9345\\,\\mathrm h$。三处都位于北半球，俯视主轴均顺时针进动。')
oldanswer='\\solution 保守力可有显式时间变化的势。'
newanswer=r'''\solution 坐标变换给出 $X=x\cos\Omega t-y\sin\Omega t$，因此
\[
U'(x,y,t)=-F_0(x\cos\Omega t-y\sin\Omega t),
\quad\frac{\partial U'}{\partial t}=F_0\Omega(x\sin\Omega t+y\cos\Omega t).
\]
虽然惯性系中的力恒定且保守，动系势却一般显含时间，所以 $\dot J=\partial U'/\partial t$ 一般不为零。保守力也可有显式时间变化的势。'''
assert s.count(oldanswer)==1;s=s.replace(oldanswer,newanswer)
# Split long solution lines without changing their mathematical content.
s=s.replace(r'\solution $\Omega_E^2R\approx0.03388\,\mathrm{m/s^2}$。赤道有效重力减少此值；',r'\solution $\Omega_E^2R\approx0.03388\,\mathrm{m/s^2}$。'+'\n\n'+r'赤道有效重力减少此值；')
s=s.replace(r'\solution 绕铰点转动惯量 $I=ML^2/3$，重力矩 $-MgL\sin\varphi/2$，离心力矩 $M\Omega^2L^2\sin\varphi\cos\varphi/3$。相除得到',r'''\solution 绕铰点的转动惯量、重力矩和离心力矩分别为
\[
I=\frac{ML^2}{3},\qquad
\tau_g=-\frac{MgL}{2}\sin\varphi,\qquad
\tau_{\rm cf}=\frac{M\Omega^2L^2}{3}\sin\varphi\cos\varphi.
\]
由 $I\ddot\varphi=\tau_g+\tau_{\rm cf}$ 得到''')
assert s.count(r'\QuestionStatement{')==71
assert s.count(r'\example{')==47 and s.count(r'\exercise{')==24
assert s.count(r'\TeachingFigure{')==47 and s.count(r'\OriginalFigure[')==47
assert 'colorbox{' not in s and '课件原图来源索引' not in s
(P/(NAME+'.tex')).write_text(s)
(P/'资料核查/题干与题图修订记录.json').write_text(json.dumps({'examples':47,'training_questions':24,'question_diagrams':71,'original_figures_preserved':47,'explanatory_figures_preserved':47,'removed_tinted_callouts':3,'source_index_removed':True,'changes':changes},ensure_ascii=False,indent=2))
# Compact atlas permits inspecting every new diagram without rereading unchanged theory pages.
preamble=s[:s.index(r'\begin{document}')]
atlas=preamble+r'\begin{document}\pagestyle{empty}'+'\n'
for row in changes:
 n=row['number'];kind=row['kind'];title=('例' if kind=='example' else '训练题')+str(n)
 atlas+=r'\noindent\begin{minipage}[t][6cm][t]{.32\linewidth}\centering\textbf{'+title+'}\\par\\vspace{4mm}\\resizebox{.92\\linewidth}{!}{\\input{'+row['diagram']+'}}\\end{minipage}\\hfill\n'
 if (changes.index(row)+1)%3==0:atlas+='\\par\\vspace{5mm}\n'
 if (changes.index(row)+1)%9==0:atlas+='\\clearpage\n'
atlas+=r'\end{document}'
(P/'工作文件/题图校样.tex').write_text(atlas)
print('71 complete problem blocks; 47 original and 47 explanatory figures retained; source appendix removed')
