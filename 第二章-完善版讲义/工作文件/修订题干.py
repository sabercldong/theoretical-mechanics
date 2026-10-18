from pathlib import Path
import re,json
from 题目解析 import commands
P=Path(__file__).resolve().parents[1];N='第二章-质点组力学讲义-完善版'
s=(P/'工作文件/详解修订前备份'/(N+'.tex')).read_text()
more={1:r'以 $G$ 表示质心、$D$ 表示 $BC$ 中点，说明中线上的分割比；积分中须给出质量或面积权重。',2:r'同时写出保证两个完整圆孔位于盘内且互不重叠的半径范围。',3:r'取赤道面为 $z=0$、对称轴向上，$0\le a<b$；检验实心极限与薄壳极限。',4:r'以底面中心为原点、轴向上为 $z$，补齐半圆截面的一阶矩积分。',5:r'写出积分域及面积元，分别计算面积与一阶矩，并检验质心是否在薄片内部。',6:r'坐标均用同一长度单位。写出三重积分上下限和质量密度如何约去。',7:r'取球心为原点，$z\ge0,\rho_0>0$；与相同半径的均匀半球比较。',8:r'另以各部件质心速度直接求和，核验总动量。',9:r'明确上述结论在所有碎片尚未接触地面时成立；说明某碎片先落地后应如何判断。',10:r'同时给出支承合力的变化范围，并说明仅用动量定理能否确定支承力偶。',11:r'取 $0\le\alpha<\pi/2$，用速度合成及水平动量两条关系独立列式，检查重炮车极限。',12:r'速度数字的单位均为 $\mathrm{m/s}$，要求区分对地速度与离车后的相对速度。',13:r'$N$ 为正整数、$M,m,v>0$。逐次跳离时，各人速度均相对于其离车后的车测量。',14:r'取 $X(0)=X_0$，$|\theta_0|\ll1$；若摆角来自自由小振动，再求 $k$。',15:r'忽略绳的质量，设两人可视为质点；另求各自相对初始位置移动的距离和距离之比。',16:r'将从 $A$ 指向 $B$ 的连线取为 $+x$，垂直冲量分量取为 $+y$；求约束冲量并检查绳是否绷紧。',17:r'抛球前二者具有相同水平速度 $v$、竖直总动量为零。再求每个重复周期的时间、水平距离及首次抛掷提供的竖直动能。',18:r'分别用绝对速度与相对于 $A$ 的速度定义角动量，保留两种定义的运输修正项。',19:r'$v(t)$ 指 $B$ 相对于本侧绳的有向向上爬速，不是对地速率；两种情形初始轮与猴均静止。',20:r'设 $m,m\prime,s,s\prime>0$，说明实数正时间的存在条件，以及 $m=m\prime$ 的退化情形。',21:r'另将 $J=40\,\mathrm{N\,s}$、$m=1\,\mathrm{kg}$、$l=10\,\mathrm m$ 代入求质心速度和转速；检验初态。',22:r'要求判断质心是否沿初始径向直线、杆是否转动，以及关于 $O$ 的总角动量是否守恒。',23:r'以 $f$ 表示促使 $r$ 增大的有向内力，画出一周期的 $f$--$r$ 过程并说明机械能的来源。',24:r'其中 $\omega$ 相对不旋转的质心平动系定义。另讨论某瞬时两球自转平面的法线与质心速度平行时，角动量两部分如何合成；不额外指定持续进动。',25:r'将上升高度、速度变化、重复次数和效率均作为待测参数，给出符号估算式、单位换算与理论下限；题设不要求无依据的唯一数值。',26:r'两球质量分别为 $m_1,m_2>0$；另求此时各球速率并说明内力合力为零与内力功的区别。',27:r'写出两个速度的方向，并用折合质量求相对速率进行交叉核验。',28:r'区分径向相对管速率 $v_r$ 与切向牵连速率 $l\omega_{\rm out}$，核验角动量和能量守恒。',29:r'给出任意允许倾角下的速度、接触支持力及接地分支的可行条件。',30:r'两质量均为 $m$ 的球由长 $l$ 的刚性轻杆连接，下球接触水平粗糙地面，上球在右上方；杆从竖直向下球的方向偏转角 $\theta$，从 $\theta=\alpha\in(0,\pi/2)$ 静止释放。摩擦向右取正，并检查初始姿态是否已需起滑。',31:r'杆相对竖直的有向倒角为 $\theta$，向右倒下取正。必须检查支持力非负性，并在需要时切换到自由飞行分支。',32:r'模型由两个点质量和无质量刚杆组成，重力冲量在短碰撞中可忽略。允许用总质量 $M$、质心惯量 $I_C$ 和接触点力臂表示结果，给出单点接触冲量。',33:r'本题两质量均为 $m$，长 $l$ 的轻杆初始竖直，下球在光滑水平地面，上球初受向右冲量 $J$；$\Lambda=J^2/(m^2gl)=4$，无空气阻力。要求排除释放时刻的平凡零根，比较两端首次返回地面的正时间。',34:r'地面固定且光滑，恢复系数为 $e\in[0,1]$，竖直向上取正；说明这一特殊姿态结论为何不能推广至任意倾角。',35:r'同时核查接触法向力为正，并区分最大静摩擦系数与动摩擦系数。',36:r'写出初条件如何决定相位，并验证总动量、总能量和两球的初始速度。',37:r'相对矢量取 $\vect r=\vect r_S-\vect r_E$；用 $L,E_{\rm rel}$ 表示轨道参数，明确束缚轨道的周期与质心系中的真实位置。',38:r'区分两星间距和各自绕质心的半径，分别用任一恒星和折合质点核验。',39:r'$\rho\ge0$ 是相对入射轨迹的冲量参数；证明径向转向点仍有角向运动，并检查正碰及无相互作用极限。',40:r'记 $M=m_1+m_2$，将杆两端相对质心的半径分别写明，核查位置、速度初值。',41:r'给出外侧转折点的方程与物理解的选取条件，说明最大间距时相对总速度是否为零。',42:r'分别处理短时粘连碰撞与碰后弹簧运动，列出各阶段能量、角动量的适用条件。',43:r'只研究端球首次相碰之前，绳只能传递拉力；对张力的计算须计入中间球自身的加速度。',44:r'两个角动量均关于固定钉 $O$ 计算，求极值时必须限制在能量允许的实际可达区间。',45:r'以共同原定落点为比较基准，注明重量与质量的换算，以及质量加权落点是否改变。',46:r'若块1速度增量向前，另求两块的对地水平速度，并说明 $u$ 为什么不出现在间距中。',47:r'碰撞期间水平外冲量可忽略，取入射方向为正；从动量与相对速度反向条件推导，检验等质量、重靶和轻靶三种极限。',48:r'靶质子最初静止，碰撞无外冲量；用质心角 $\Theta$ 和实验室角 $\theta$ 区分两种角度，并证明两出射速度垂直。',49:r'两粒子质量分别为 $m_1,m_2$，令 $\lambda=m_1/m_2$；定义 $f_C=\dd\sigma/\dd\Omega_C$，从冲量参数与散射角关系给出推导，并说明实验室系如何逐支变换。',50:r'定义 $D=\sqrt{1+\lambda^2+2\lambda\cos\Theta}$、$h=\sqrt{1-\lambda^2\sin^2\theta}$，求每支的 $\dd\Omega_C/\dd\Omega_L$，解释为何需要求和。',51:r'定义 $\lambda=m_1/m_2$、$E_{\rm rel}=\mu u^2/2$、$h=\sqrt{1-\lambda^2\sin^2\theta}$，$D_\pm=\lambda\cos\theta\pm h$、$c_\pm=\cos\Theta_\pm$；分别给出 $\lambda>1,\lambda=1,\lambda<1$ 的允许角域与分支数。',52:r'另求铰点的水平冲量与碰撞动能损失；比较将刚杆替换成竖直柔绳时的初瞬结果。',53:r'$\delta m>0$，$v$ 相对于同一惯性系；明确微元损失率的正负约定。',54:r'竖直模型给定 $m(0)=m_0,v(0)=v_0,z(0)=z_0$ 和干质量 $m_f>0$；说明燃烧结束后的模型及发射台支持条件。',55:r'分清立即起飞、延迟起飞及燃尽前不能起飞三类，并给出熄火后的最高点条件。',56:r'以下落方向为正，$s(0)=0$；检查初值、质量增长趋零及长时间加速度极限。',57:r'初始半径 $a>0$，密度恒定，向下为正；说明长期是否存在有限终端速度。',58:r'分别使用制停质量通量和固定成员全绳动量核验，区分 $h\to l^-$ 与全绳已经静止后的反力。',59:r'只研究 $l/2\le x\le l$ 的导向运动；同时用两开放直段的动量通量式核验。',60:r'速度均取同一地面惯性系，$q,u,M,M\prime>0$；先核查从静止进入并维持所设滑动分支的条件。',61:r'定义 $D=\vect r\cdot m\vect v$、$W=\vect r\cdot\vect F$，在任意 $[0,\tau]$ 上验证 $2\overline T+\overline W=[D(\tau)-D(0)]/\tau$，不得只引用前面的公式编号。',62:r'同时给出有限时间平均和整周期平均的区别，并检验长时间极限。',63:r'假定长期平均的位力边界项消失，在不旋转质心系内讨论；再解释缓慢辐射失能下的收缩加热趋势。',64:r'须写出平均积分，而非仅引用平均值；用位力关系再核验，并说明为何不是瞬时动能等于势能。',65:r'温度为 $\Theta>0$，定义 $B_2=-2\pi\int_0^\infty[\exp(-U/(k_B\Theta))-1]r^2\dd r$；另把结果换成单球半径 $a$ 的表达。',66:r'温度记为 $\Theta>0$，给出 $B_2$ 定义、三段积分和 $B_2=0$ 的温度，注明低密度适用条件。'}
replacements={30:r'质量均为 $m$ 的两球由长 $l$ 的轻刚杆连接，下球在水平粗糙地面、上球在右上方。杆与竖直向上方向成角 $\theta$，初态 $\theta=\alpha\in(0,\pi/2)$、静止。地面最大静摩擦系数为 $\mu_s$；在下球尚未滑动的阶段，求支持力、所需摩擦力及首次起滑条件。',33:r'两等质量 $m$ 的球由长 $l$ 的刚性轻杆连接，初态竖直静止，下球在光滑水平地面。上球获得向右冲量 $J$，令 $\Lambda=J^2/(m^2gl)=4$。求此后哪一球先返回地面及首次碰撞位置。用 $l,\sqrt{l/g}$ 分别作长度和时间单位，排除 $t=0$ 的平凡根。'}
rows=[];spans=[]
for kind in ['example','exercise']:
 for n,a,b,title in commands(s,kind):
  c=s.index(r'\solution',b);old=s[b:c];label=re.match(r'\s*\\label\{[^}]+\}',old)
  lab=label[0].strip() if label else ('\\label{test:c2-'+str(n)+'}' if kind=='exercise' else '')
  stem=old[label.end():].strip() if label else old.strip()
  if kind=='example':
   stem=replacements.get(n,stem)
   if n not in replacements:stem+='\n'+more[n]
  else:
   if n==9:stem=r'两只质量均为 $m$ 的猴子最初静止且同高，轻绳绕固定滑轮，半径 $r$、惯量 $I_p=mr^2$，绳不打滑。猴 $A$ 抓绳不爬，猴 $B$ 以相对本侧绳向上速率 $v$ 爬行。求两猴的对地上升速度，并核验速度合成。'
   if n==12:stem=r'均匀水平细管长 $l$、质量 $M_t$，绕端点竖直光滑轴自由转动；无摩擦小球质量 $m$，初在 $r=l/2$、相对管静止，总初转速为 $\omega_0\ne0$。求球出管时径向、切向及绝对速率，并分别取 $M_t/m\to\infty$ 与 $M_t/m\to0$ 的极限。'
   if n==13:stem=r'两等质量 $m$ 的球由长 $l$ 的轻刚杆连接，下球在光滑水平地面，上球右上。杆与竖直向上成 $\theta$，从 $\theta=\alpha\in(0,\pi/2)$ 静止释放。求上球首次碰地前 $\theta\to\pi/2$ 时下球速度、上球竖直速度及地面支持力，说明是否可直接作碰后值。'
   if n==21:stem+=r'均匀重力为 $g$，无空气阻力，先假设从 $t=0$ 起处于自由飞行；再解释发射台存在时如何核查此假设。'
   if n==22:stem=r'雨滴从静止下落，初始质量 $M$，以恒质量率 $\lambda>0$ 凝结对地静止物质，无空气阻力。其位移为 $s=gt^2/4+Mgt/(2\lambda)-M^2g\ln(1+\lambda t/M)/(2\lambda^2)$。在固定有限 $t$ 下展开并求 $\lambda\to0$ 的极限，解释表观发散项怎样相消。'
  key=('ex' if kind=='example' else 'tr')+f'{n:02}';cap=('例' if kind=='example' else '训练题')+str(n)+'题图'
  macro='LongQuestionStatement' if (kind=='example' and n in [30,31,43,51,55]) else 'QuestionStatement'
  spans.append((b,c,'\n'+lab+'\n\\'+macro+'{'+stem+'}{'+key+'}{'+cap+'}\n'))
  rows.append({'kind':kind,'number':n,'title':title,'stem':stem,'key':key})
for a,b,x in sorted(spans,reverse=True):s=s[:a]+x+s[b:]
s=re.sub(r'\\section\*\{课件原图来源索引\}.*?(?=\\end\{document\})','',s,flags=re.S)
s=s.replace(r'\newcommand{\important}[1]{\par\smallskip\noindent\colorbox{soft}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{#1}}\par\smallskip}',r'\newcommand{\important}[1]{\par\smallskip\noindent #1\par\smallskip}')
s=s.replace('自测','训练题')
s=re.sub(r'\\newcommand\{\\Needspace\}\[1\]\{[^\n]+\}',r'\\newcommand{\\Needspace}[1]{\\par\\if@nobreak\\else\\penalty0\\begingroup\\dimen0=#1\\relax\\dimen2=\\pagegoal\\advance\\dimen2 by-\\pagetotal\\ifdim\\dimen0>\\dimen2\\newpage\\fi\\endgroup\\fi}',s,count=1)
while r'\boxed{' in s:
 a=s.index(r'\boxed{');b=a+len(r'\boxed{');p=b;d=1
 while d:
  if s[p]=='{':d+=1
  elif s[p]=='}':d-=1
  p+=1
 s=s[:a]+s[b:p-1]+s[p:]
c3=(P.parent/'第三章-完善版讲义/第三章-刚体力学讲义-完善版.tex').read_text()
macros=c3[c3.index(r'\newsavebox{\QuestionDrawing}'):c3.index(r'\begin{document}')]
s=s.replace(r'\begin{document}',macros+'\n'+r'\begin{document}',1)
s=s.replace(r'\newcommand{\solution}{\par\noindent\textbf{解}\quad}',r'\newcommand{\solution}{\setcounter{solutionstep}{0}\par\nopagebreak[4]\smallskip\nopagebreak[4]\noindent\textbf{解答}\quad}')
assert s.count(r'\OriginalFigure{')==31 and s.count(r'\OriginalPanel{')==12 and s.count(r'\TeachingFigure{')==22
assert all(x not in s for x in [r'\boxed{',r'\colorbox{','课件原图来源索引','补充绘制'])
(P/(N+'.tex')).write_text(s);(P/'工作文件/题干修订后主稿.tex').write_text(s);(P/'工作文件/完整题干.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('90 standalone problem statements; all original and explanatory figures retained')
