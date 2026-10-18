from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1]; N='第三章-刚体力学讲义-完善版'
s=(P/'工作文件/详解修订前备份'/(N+'.tex')).read_text(); baseline=s
R=json.loads((P/'工作文件/详解修订前题目.json').read_text())
asks={
1:r'取圆心为固定原点，$t=0$ 时中心位于 $+x$ 轴。写出任意材料点的速度、加速度，并判断运动类型。',
2:r'其中位置矢量均在空间系表达。分别以 $C$、$O$ 为基点写出 $A$ 的位置与速度，并说明换基点是否改变姿态矩阵。',
3:r'同时计算速率，并检验速度与角速度、位置矢量的正交关系。',
4:r'求圆盘的绝对角速度及其大小、绝对角加速度，并解释恒定分转速为何仍可有角加速度。',
5:r'同时求总角速率大小与角加速度，说明进动对轴向角速度的贡献。',
6:r'这里的两种 $\omega$ 均相对于支架测量。求各机构的绝对角速度及大小，比较 $\beta=0$ 时的结果。',
7:r'两转速均取恒定有向值。给出任意时刻两点的速度，并写出 $t=0$ 时的结果以检验符号。',
8:r'说明 $\omega_z$ 与欧拉角自转率 $\dot\psi$ 是否相同。',
9:r'采用本章 $z$--$x$--$z$ 欧拉角约定，设初始自转角为 $\psi_0$。求三个欧拉角和总角速度，说明年周公转是否须计入姿态自转。',
10:r'设轨道半径为 $R$，$t=0$ 时卫星位于 $+X$ 轴，标记体轴 $\vect e_1$ 指向中心天体。求惯性系中的姿态、角速度及周期，并说明“始终同面”与自转的关系。',
11:r'采用本章的 $z$--$x$--$z$ 约定，初始本体 $x$ 轴取竖直方向在垂直于对称轴平面内的投影。',
12:r'取 $B$ 位于 $A$ 上方的装配支路，初始 $BA$ 向下，连杆转角 $\psi\in(-\pi/2,\pi/2)$。',
13:r'采用主动转动、列矢量和 $R=R_z(\varphi)R_x(\theta)R_z(\psi)$ 约定；解释反解的象限选择和奇异姿态。',
14:r'均指作用于列矢量的主动转动，$x,y,z$ 是固定空间右手轴。写出两个合成矩阵，跟踪初始 $\vect e_z$，并比较总转角与小转动极限。',
15:r'讨论合力为零和两力反向的特殊情况，说明什么条件下可化为单一合力。',
16:r'求主矢、关于任意点的主矩，以及移动取矩点后的变化。',
17:r'从力矩与合力的内积证明结论，并给出力系简化后的最简表示。',
18:r'设 $0<\varphi<\pi/2$，所有接触仅能受压。除临界等式外，还须写出接触与静摩擦可行条件。',
19:r'同时给出铰反力，判断所得平衡姿态的稳定性。',
20:r'求平衡倾角及墙面、棱边的反力，并筛选接触力非负的几何分支。',
21:r'同时求两处反力，列出满足杆有碗外部分且接触受压的长度范围。',
22:'',
23:r'两部件惯量张量 $\mathsf I_0$ 均在同向正交轴组中表达。求组合体关于总质心的完整惯量张量，解释不同方向的平行轴修正。',
24:r'杆在垂直于端点固定转轴的平面内转动。分别用定点积分和质心分解求动能，验证二者一致。',
25:r'再考虑质量同为 $m$、半轴为 $a,b$ 的均匀椭圆薄片，质心与轴向约定相同。分别从积分求两种薄片的完整惯量张量，并检验垂直轴定理。',
26:r'求完整质心惯量张量，并取半径趋零且质量、长度保持不变的细杆极限，求过质心、与杆夹角为 $\alpha$ 的轴惯量。',
27:r'求球心惯量张量和任意过球心轴的惯量，用质量积分与对称性相互核验。',
28:r'求质心惯量张量和三根主轴，列出变量代换、体积元及积分限，并检验球形极限。',
29:r'同时求质心位置，说明移点后三个惯量中哪一个保持不变。',
30:r'分别求 $C$、$O$ 为原点时的完整惯量张量，以直接积分和平行轴定理交叉核验。',
31:'',
32:r'数值结果用 $mc^2$ 作惯量单位，给出特征方程、本征值和一组单位正交本征矢量。',
33:r'求该轴的方向惯量，说明它是否必为顶点惯量张量的主轴，并核验正方体特例。',
34:r'求关于 $O$ 的完整惯量张量、三个主惯量及一组正交主轴，以质心和平行轴定理校验。',
35:r'求角动量和动能时，角速度分量均指同一瞬时的本体坐标分量。',
36:r'同时求质心速度，并说明角速度方向不是主轴时，动能仍应如何计算。',
37:r'采用本章欧拉角约定，保留所有进动、章动与自转交叉项，并用质心平动加相对转动核验。',
38:r'取驱动方向为正、初始转角为 $q_0$；假设装置能克服启动静摩擦。求角加速度、$\omega(t)$、$q(t)$ 及转过 $\Delta q>0$ 后的转速，并作功和能量核验。',
39:r'取偏离竖直向下的有向角为 $q$，杆质量为 $m$，$0<|q_0|<\pi$，忽略轴摩擦。求非线性运动方程、小振动周期与初值解、最低点速率及轴反力的求法。',
40:r'悬轴方向保持不变，允许在刚体或刚性延长支架上选择悬点。求周期关于 $h$ 的函数、极小值及两端极限。',
41:r'取两轴承沿 $+z$ 由 $A$ 至 $B$，间距 $L$；$\vect e_x$ 随杆转动。求两轴承的附加横向反力，解释静平衡是否足够。',
42:r'进一步给出两个不同校正平面 $z_a,z_b$ 上所需的质量半径矢量及其安装方位。',
43:r'取底面相对地面的抬角 $\theta$ 为正；给出任意回落位置与即将触地时的有向角速度、角加速度。',
44:r'另求重物下降高度 $h$ 后的速率，并用全系统能量验证。',
45:r'明确反力是轴承作用于盘轴系统的力；分别求最大模，并说明最大值是否同时出现。',
46:r'取 $x$ 向右、$y$ 向上、逆时针为正；再代入 $m=8\,\mathrm{kg}$、$L=0.5\,\mathrm m$、$\omega=4\,\mathrm{s^{-1}}$、$g=9.8\,\mathrm{m\,s^{-2}}$。',
47:r'取 $x,y>0$，逆时针为正，写出本体系的取向和两条极迹适用的弧段。',
48:r'设坡面向右下倾斜；同时求保证纯滚动所需的最小静摩擦系数，并检验实心圆柱特例。',
49:r'绳在圆盘左侧与轮缘相切，取逆时针为正；给出动力学、能量和瞬心三种求解，并核查约束方向。',
50:r'四点均指当前位于指定位置的材料点；使用统一的基点速度和加速度公式逐点代入。',
51:r'在两个满足垂直条件的轮缘点中，指定 $\vect r_{AM}=r\vect e_t$，其中 $\vect e_t=\vect k\times\vect e_r$。同时给出相对转臂的自转率。',
52:r'写出初值能量积分、纯滚动的摩擦条件及接触保持条件；小振动解应满足给定初值。',
53:r'分别记两轮之间张力为 $T$、悬挂段为 $S$；要求写出提升的驱动力矩条件。',
54:r'取向右、向上为正，画明四个接触力，检查双接触假设并说明停止后方程是否仍适用。',
55:r'分别用基点速度、沿连杆投影和瞬心几何核验，说明装配支路的作用。',
56:r'取 $x$ 向右、$y$ 向上，逆时针为正；先由几何和速度约束求 $AB$ 长度及角速度，再求加速度。',
57:r'求解时同时检查总水平动量和摩擦耗散，明确球的接触点速度与质心速度的区别。',
58:r'假设 $A$ 即沿给定半径 $R$ 的圆周运动，$\vartheta(0)=\vartheta_0$；写出任意时刻的速度、加速度，并检验直线飞行极限。',
59:r'在无外力矩且主惯量互不相同的条件下，分别对绕三根主轴的解线性化，求横向扰动频率或增长率并判断稳定性。',
60:r'陀螺轴对称，$I_1=I_2=A,I_3=C$，无外力矩；取初始横向分量沿本体 $\vect e_1$。求本体有向旋转频率、空间进动率及 $\vect\omega,\vect L,\vect e_3$ 两两夹角，并求欧拉角自转率。',
61:r'模型为轴对称重陀螺，$I_1=I_2=A,I_3=C$。列出定常进动存在条件，比较慢进动近似及精确值。',
62:r'其中 $A,C$ 是固定支点处的横向、轴向主惯量，质心位于 $+\vect e_3$ 方向距离 $l$。求另一章动转向点的条件和高速自转近似的最大下倾量。',
63:r'位置矢量从圆心量起，积分方向从 $+z$ 看为逆时针。写出参数化与各分量积分，并解释闭合路径为何不保证此加权积分为零。',
64:r'所有旋转率保留电荷 $q$ 的符号；写出未截断的旋转系方程和被忽略项，说明弱场近似的尺度条件。',
65:r'此处 $\omega_c$ 是无磁场谐振子固有频率，$\Omega=-qB/(2m)$ 为有向拉莫尔率。求惯性系两个有向横向模态频率，展开至二阶，并解释自由粒子极限。',
66:r'求共振角频率、普通频率、共振翻转角速率及理想 $90^\circ$、$180^\circ$ 脉冲时间；说明若 $B_1$ 改指线偏振峰值，答案应如何变化。'
}
spans=[];rows=[]
for kind in ['example','exercise']:
 for n,m in enumerate(re.finditer(r'\\'+kind+r'\{([^}]+)\}',s),1):
  a=m.end(); b=s.index(r'\solution',a); old=s[a:b]
  lab=re.match(r'\s*\\label\{[^}]+\}',old); assert lab,(kind,n)
  content=old[lab.end():]
  # Retain the original body figures immediately before the complete new problem statement.
  figures=[]
  for f in re.finditer(r'(?:% BEGIN ORIGINAL FIGURES\s*)?\\(?:OriginalFigure\[[^\]]+\]|TeachingFigure)\{[^}]+\}\{[^\n]+\}(?:\s*% END ORIGINAL FIGURES)?',content):figures.append(f[0])
  for f in figures:content=content.replace(f,'',1)
  content=content.replace('% BEGIN ORIGINAL FIGURES','').replace('% END ORIGINAL FIGURES','').strip()
  if kind=='example':
   if n==25:content=r'质量为 $m$ 的均匀矩形薄片边长 $a,b$，质心为原点，$x,y$ 沿边，$z$ 垂直片面。'
   if n==31:content=r'均匀正方体质量 $m$、边长 $a$，取一顶点 $O$ 为原点，三条正棱分别沿 $x,y,z$。求关于 $O$ 的全部主惯量和一组单位正交主轴，并说明重根主轴是否唯一。'
   if n==33:content=r'均匀长方体质量 $m$，边长 $a,b,c$，顶点 $O$ 为原点，三条棱沿坐标正轴。转轴为连接 $O$ 与对顶点的整条体对角线。'
   if n==39:content=r'均匀细杆长 $L$，绕端点理想水平轴在竖直平面摆动，初始偏角 $q_0$、初始静止。'
   content+='\n'+asks[n]
  key=('ex' if kind=='example' else 'tr')+f'{n:02}'; cap=('例' if kind=='example' else '训练题')+str(n)+'题图'
  macro='LongQuestionStatement' if kind=='example' and n==22 else 'QuestionStatement'
  new=lab[0]+'\n'+'\n'.join(figures)+'\n\\'+macro+'{'+content.strip()+'}{'+key+'}{'+cap+'}\n'
  spans.append((a,b,new));rows.append({'kind':kind,'number':n,'title':m[1],'statement':content.strip(),'diagram':'题图/'+key+'.tex'})
for a,b,new in sorted(spans,reverse=True):s=s[:a]+new+s[b:]
# Remove only the terminal source index; keep the textbook homework table.
s=re.sub(r'\\section\*\{课件原图来源索引\}.*?(?=\\end\{document\})','',s,flags=re.S)
s=s.replace(r'\newcommand{\important}[1]{\par\smallskip\noindent\colorbox{soft}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{#1}}\par\smallskip}',r'\newcommand{\important}[1]{\par\smallskip\noindent #1\par\smallskip}')
s=s.replace(r'\subsubsection*{自测\theexercise',r'\subsubsection*{训练题\theexercise').replace('自测与解答','训练题与解答').replace('自测题','训练题')
s=re.sub(r'\\newcommand\{\\Needspace\}\[1\]\{[^\n]+\}',r'\\newcommand{\\Needspace}[1]{\\par\\if@nobreak\\else\\penalty0\\begingroup\\dimen0=#1\\relax\\dimen2=\\pagegoal\\advance\\dimen2 by-\\pagetotal\\ifdim\\dimen0>\\dimen2\\newpage\\fi\\endgroup\\fi}',s,count=1)
# Unwrap boxed expressions with balanced braces.
while r'\boxed{' in s:
 a=s.index(r'\boxed{');p=a+len(r'\boxed{');d=1;q=p
 while d:
  if s[q]=='{':d+=1
  elif s[q]=='}':d-=1
  q+=1
 s=s[:a]+s[p:q-1]+s[q:]
macros=r'''
\newsavebox{\QuestionDrawing}
\newcommand{\QuestionStatement}[3]{%
\par\noindent\begin{minipage}{\linewidth}%
\begin{minipage}[t]{.63\linewidth}\vspace{0pt}\setlength{\parindent}{0pt}#1\end{minipage}\hfill%
\begin{minipage}[t]{.34\linewidth}\vspace{2pt}\centering%
\sbox{\QuestionDrawing}{\input{题图/#2.tex}}%
\resizebox{.98\linewidth}{!}{\usebox{\QuestionDrawing}}\par\vspace{3pt}{\small #3}%
\end{minipage}\end{minipage}\par\smallskip}
\newcommand{\LongQuestionStatement}[3]{\par #1\par\smallskip\noindent\begin{minipage}{\linewidth}\centering\sbox{\QuestionDrawing}{\input{题图/#2.tex}}\resizebox{.42\linewidth}{!}{\usebox{\QuestionDrawing}}\par{\small #3}\end{minipage}\par\smallskip}
\newcounter{solutionstep}
\newcommand{\Step}[1]{\ifnum\value{solutionstep}>0\par\smallskip\noindent\fi\stepcounter{solutionstep}\textbf{（\arabic{solutionstep}）#1}\quad}
'''
s=s.replace(r'\begin{document}',macros+'\n'+r'\begin{document}',1)
s=s.replace(r'\newcommand{\solution}{\par\noindent\textbf{解}\quad}',r'\newcommand{\solution}{\setcounter{solutionstep}{0}\par\nopagebreak[4]\smallskip\nopagebreak[4]\noindent\textbf{解答}\quad}')
assert s.count(r'\QuestionStatement{')==95 and s.count(r'\LongQuestionStatement{')==1
assert s.count(r'\OriginalFigure[')==117 and s.count(r'\TeachingFigure{')==59
assert all(x not in s for x in [r'\colorbox{',r'\boxed{','课件原图来源索引','补充绘制'])
(P/(N+'.tex')).write_text(s)
(P/'工作文件/题干题图修订后主稿.tex').write_text(s)
(P/'工作文件/完整题干.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('96 complete statements; 117 original + 59 body figures retained; source index removed')
