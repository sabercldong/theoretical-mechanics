from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1];D=P/'解答图';D.mkdir(exist_ok=True)
# Each tuple specifies a concrete geometric/physical connection and two calculation stages.
E={
1:(r'中心 $C$ 的圆周轨迹与固定的 $\overrightarrow{CA}$',r'\vect r_A=\vect r_C+\vect\rho_A',r'\dot{\vect\rho}_A=0\ \Rightarrow\ \vect v_A=\vect v_C'),
2:(r'三角形 $OCA$ 的有向位置分解',r'\vect r_{OA}=\vect r_{OC}+\vect r_{CA}',r'\vect v_A-\vect v_C=\vect\omega\times\vect r_{CA}'),
3:(r'从固定点 $O$ 指向 $A$ 的位置矢量',r'\vect v_A=\vect\omega\times\vect r_{OA}',r'\vect v_A=(1,-7,-5)\ \mathrm{m/s}'),
4:(r'竖直 $\vect k$ 轴与水平 $\vect e_r$ 轴',r'\vect\omega=\Omega\vect k+\omega\vect e_r',r'\vect\alpha=\Omega\omega\vect e_\varphi'),
5:(r'本体轴 $\vect n$ 在竖直与径向的投影',r'\vect n=\sin\theta\vect e_r+\cos\theta\vect k',r'\omega_3=\omega+\Omega\cos\theta'),
6:(r'两种盘面法线对应的不同转轴',r'\vect\omega_1=\Omega\vect k+\omega\vect n',r'\vect\omega_2=(\Omega+\omega)\vect k'),
7:(r'圆心 $A$ 及材料点 $B,C$ 的有向半径',r'\vect\omega=\omega_1\vect e_3+\omega_2\vect e_1',r'\vect v_P=\vect v_A+\vect\omega\times\vect r_{AP}'),
8:(r'节点轴和本体 $z$ 轴的投影关系',r'\omega_z=\Omega\cos\theta_0+\omega',r'\omega_z-\dot\psi=\Omega\cos\theta_0'),
9:(r'固定轴倾角 $\varepsilon$ 与地球本体轴 $z$',r'\dot\theta=\dot\varphi=0',r'\vect\omega=\dot\psi\vect e_z'),
10:(r'由卫星指向 $O$ 的标记方向',r'\mathsf R=R_z(\pi+\Omega t)',r'\vect\omega=\Omega\vect k'),
11:(r'接触母线 $\vect u$ 与最高圆周位置 $A$',r'\vect\omega=\omega\cos\alpha\vect u',r'|\vect v_A|=h|\omega|\sin2\alpha'),
12:(r'连杆 $BA$ 向水平轴的投影',r'L\sin\psi=a\sin q',r'L\cos\psi\dot\psi=a\Omega\cos q'),
13:(r'倾角 $\theta$ 与节点方向的矩阵投影',r'R_{33}=\cos\theta',r'(R_{13},-R_{23})=\sin\theta(\sin\varphi,\cos\varphi)'),
14:(r'同一初始标记方向在两种转序下的像',r'R_xR_y\vect e_z=\vect e_x',r'R_yR_x\vect e_z=-\vect e_y'),
15:(r'两条平行作用线的横向坐标 $x_1,x_2$',r'F=F_1+F_2',r'x_RF=x_1F_1+x_2F_2'),
16:(r'两条反向力的作用线间垂距 $d$',r'\vect F_{\rm main}=0',r'\vect M_A=\vect M_O=Fd\vect k'),
17:(r'同轴的主矢 $F\vect k$ 和主矩 $C\vect k$',r'\vect F\cdot\vect M_O=FC\ne0',r'\vect F\cdot(\vect r\times\vect F)=0'),
18:(r'杆上接触点 $B$ 的法线和 $A$ 处的摩擦分解',r'N_1\,AB=Pl\cos\varphi',r'f=N_1\sin\varphi,\quad N_2=P-N_1\cos\varphi'),
19:(r'两杆中点重力的水平力臂',r'm_1x_1+m_2x_2=0',r'\tan\theta=b^2/(a^2+2ab)'),
20:(r'墙面水平法线和棱边处的杆法线',r'OB=d/\cos\theta',r'N_B\,OB=Pl\cos\theta'),
21:(r'碗心 $O$、碗内端 $B$ 和碗缘 $C$ 的弦关系',r'BC=c=2r\cos\theta',r'l=4c-8r^2/c'),
22:(r'相邻圆柱的法向接触与底层侧推位置',r'\vect f_{ij}=N_{ij}\vect n_{ij}+\tau_{ij}\vect t_{ij}',r'\sum\vect F_i=0,\quad\sum\vect M_i=0'),
23:(r'两个部件中心到横向轴的距离 $a$',r'\Delta\mathsf I=ma^2\operatorname{diag}(0,1,1)',r'\mathsf I_C=2\mathsf I_0+2\Delta\mathsf I'),
24:(r'固定端 $O$、杆中点 $C$ 与全长 $L$',r'v_C=|\omega|L/2',r'T=mv_C^2/2+I_C\omega^2/2'),
25:(r'矩形全边长与椭圆半轴的区别',r'I_z=I_x+I_y',r'I_x^{\rm rect}=mb^2/12,\quad I_x^{\rm ell}=mb^2/4'),
26:(r'圆柱中心轴 $z$ 与横向距离',r'I_z=ma^2/2',r'I_x=I_y=m(3a^2+L^2)/12'),
27:(r'过球心的任意轴与半径 $a$',r'I_x=I_y=I_z',r'I=2ma^2/5'),
28:(r'椭球的三条几何半轴',r'x=au,\ y=bv,\ z=cw',r'I_x=m(b^2+c^2)/5'),
29:(r'球心 $O$ 到质心 $C$ 的轴向位移',r'OC=3a/8',r'I_{Cx}=I_{Ox}-m(3a/8)^2'),
30:(r'正方体顶点 $O$ 与质心 $C$',r'\vect d=\overrightarrow{OC}=a(1,1,1)/2',r'\mathsf I_O=\mathsf I_C+m(d^2\mathsf1-\vect d\vect d^{\mathsf T})'),
31:(r'从顶点指向对顶点的体对角线',r'\vect n_1=(1,1,1)/\sqrt3',r'I_1=ma^2/6,\quad I_2=I_3=11ma^2/12'),
32:(r'顶点三条棱与质心位置',r'\mathsf I_O\vect n=\lambda\vect n',r'\det(\mathsf I_O-\lambda\mathsf1)=0'),
33:(r'通过顶点和质心的同一体对角线',r'\vect n=(a,b,c)/\sqrt{a^2+b^2+c^2}',r'I_{\vect n}=\vect n^{\mathsf T}\mathsf I_C\vect n'),
34:(r'三个离散质量到各坐标轴的距离',r'I_{ij}=\sum m(r^2\delta_{ij}-x_ix_j)',r'\mathsf I\vect n=\lambda\vect n'),
35:(r'第一卦限球体的三个坐标边界',r'x,y,z\ge0,\quad x^2+y^2+z^2\le a^2',r'\vect L=\mathsf I\vect\omega,\quad T=\vect\omega^{\mathsf T}\mathsf I\vect\omega/2'),
36:(r'顶点固定时的质心位置矢量',r'\vect v_C=\vect\omega\times\vect r_{OC}',r'T=mv_C^2/2+\vect\omega^{\mathsf T}\mathsf I_C\vect\omega/2'),
37:(r'固定支点 $O$ 至盘心的距离 $h$',r'A=m(a^2/4+h^2),\quad C=ma^2/2',r'T=A(\dot\theta^2+\dot\varphi^2\sin^2\theta)/2+C\omega_3^2/2'),
38:(r'两个相反方向的力矩',r'I_z\alpha=M-M_f',r'\omega=\alpha t,\quad q-q_0=\alpha t^2/2'),
39:(r'杆中点重力与铰轴 $O$ 的力臂',r'M_O=-mg(L/2)\sin q',r'I_O\ddot q=M_O'),
40:(r'悬轴 $O$ 与质心 $C$ 的距离 $h$',r'\ell_{\rm eq}=h+k^2/h',r'\partial\ell_{\rm eq}/\partial h=0\ \Rightarrow\ h=k'),
41:(r'杆倾角 $\beta$ 与沿轴分开的两个轴承',r'I_{xz}=-ml^2\sin\beta\cos\beta/12',r'L\Delta R_{Bx}=I_{xz}\omega^2'),
42:(r'不同轴向坐标的两个校正平面',r'\vect U_a+\vect U_b=-\vect U',r'z_a\vect U_a+z_b\vect U_b=-\vect V'),
43:(r'抬起底面后质心 $C$ 的高度',r'y_C=a(\sin\theta+\cos\theta)/2',r'I_O\dot\theta^2/2+mg y_C=mg y_C(\theta_0)'),
44:(r'左右两段绳上的不同张力',r'T_1-mg=ma,\quad2mg-T_2=2ma',r'(T_2-T_1)r=I\alpha,\quad a=r\alpha'),
45:(r'盘法线与实际转轴的夹角 $\beta$',r'I_{xz}=mr^2\sin2\beta/8',r'(a+b)D=I_{xz}\omega^2'),
46:(r'两个杆中点的重力作用位置',r'I_O=17mL^2/12,\quad x_C=3L/4',r'\vect R_O-2mg\vect j=2m\vect a_C'),
47:(r'两端速度法线交点 $P$',r'P=(x,y),\quad x^2+y^2=l^2',r'q_1=y^2/l,\quad q_2=-xy/l'),
48:(r'同一个接触点出发的法向与切向反力',r'm\ddot x=mg\sin\beta-f',r'I_C|\alpha|=fa,\quad\ddot x=a|\alpha|'),
49:(r'圆盘左侧切点处的向上张力',r'ma=mg-T,\quad I_C\alpha=-Tr',r'a=-r\alpha\ \Rightarrow\ a=2g/3'),
50:(r'当前处于四个方位的材料点',r'\omega=-v/R,\quad\alpha=-a/R',r'\vect a_P=\vect a_O+\vect\alpha\times\vect r_{OP}-\omega^2\vect r_{OP}'),
51:(r'两轮接触点与垂直于 $OA$ 的半径 $AM$',r'0=(R+r)\Omega-r\omega',r'\omega=(1+R/r)\Omega'),
52:(r'圆槽心 $O$ 至圆柱心 $C$ 的距离 $q$',r'q=R-r,\quad r\dot\theta=-q\dot\varphi',r'3q\ddot\varphi/2+g\sin\varphi=0'),
53:(r'两轮之间和悬挂段的两种张力',r'M_1/r_1-P_3=(P_3/g+I_A/r_1^2+I_B/r_2^2)a',r'T-S=I_Ba/r_2^2'),
54:(r'墙面和地面的四个接触力',r'N_A=f_B,\quad N_B+f_A=Q',r'I_C\dot\omega=-r(f_A+f_B)'),
55:(r'曲柄端 $A$ 与滑块 $B$ 的同杆约束',r'v_{By}=0\ \Rightarrow\ \omega_{AB}=-\Omega',r'v_{Bx}=-2l\Omega\sin\varphi'),
56:(r'曲柄的 $45^\circ$ 位置和连杆的 $30^\circ$ 位置',r'L\sin30^\circ=R\sin45^\circ',r'a_{By}=0\ \Rightarrow\ \alpha_{AB}=2\Omega^2/(3\sqrt3)'),
57:(r'球底部接触点与活动板的相对滑动',r'u=v_C+r\omega-v_{\rm board}',r'u(t_*)=0,\quad t_* =2Mv/[(7M+2m)\mu g]'),
58:(r'桨点 $B$ 在 $\vect i,\vect k$ 平面内的半径',r'\vect r_{AB}=l(\sin\vartheta\vect i+\cos\vartheta\vect k)',r'\dot{\vect i}=\Omega\vect j,\quad\dot{\vect j}=-\Omega\vect i'),
59:(r'三根不同主惯量轴及横向扰动',r'I_i\dot\omega_i=(I_j-I_k)\omega_j\omega_k',r'\ddot u+\nu^2u=0\quad\hbox{or}\quad\ddot u-\lambda^2u=0'),
60:(r'位于同一子午面内的 $\vect\omega,\vect L,\vect e_3$',r'\tan\alpha=w/s,\quad\tan\theta=Aw/(Cs)',r'\dot\varphi=L/A,\quad\dot\psi=-(C-A)s/A'),
61:(r'重力矩与固定倾角 $\theta_0$',r'A\Omega^2\cos\theta_0-Cs\Omega+mgl=0',r'\Omega_\pm=4\pm\sqrt{14}\ \mathrm{s^{-1}}'),
62:(r'倾斜释放时的轴线与重力方向',r'\dot\theta(0)=\dot\varphi(0)=0',r'\ddot\theta(0)=mgl\sin\theta_0/A'),
63:(r'圆周的有向切线 $\dd\vect s$ 与径矢 $\vect r$',r'\vect B\cdot\dd\vect s=-Br\sin\chi\dd\chi',r'B\oint y\dd x=-\pi Br^2'),
64:(r'中心力轨道与磁场方向',r'\vect\Omega=-q\vect B/(2m)',r"m\vect a'= -\nabla U+m\vect\Omega\times(\vect\Omega\times\vect r)"),
65:(r'谐振子横向圆偏振与磁场方向',r"\ddot w'+(\omega_c^2+\Omega^2)w'=0",r'\sigma_\pm=\Omega\pm\sqrt{\omega_c^2+\Omega^2}'),
66:(r'纵向静场与横向共振旋转场',r'\omega_0=|\gamma|B_0,\quad\omega_1=|\gamma|B_1',r'\beta=\omega_1\tau\ \Rightarrow\ \tau_{90}=\pi/(2\omega_1)')}
T={
1:(r'连线 $AB$ 与垂直于它的相对速度',r'\vect r\cdot\vect r=l^2',r'\vect r\cdot(\vect v_B-\vect v_A)=0'),
2:(r'相同圆周轨迹下的固定姿态座舱',r'\dot{\vect b}_P=0\ \Rightarrow\ \vect v_P=\vect v_A',r'\hbox{轮辐:}\quad\vect v_P=\Omega\vect k\times\vect r_{OP}'),
3:(r'标记 $\vect e_z$ 经两种转动顺序的结果',r'R_yR_x\vect e_z=-\vect e_y',r'R_xR_y\vect e_z=\vect e_x'),
4:(r'$A,B$ 两点沿 $y$ 的速度差',r'\omega=(w-u)/d',r'x_P=-ud/(w-u),\quad y_P=0'),
5:(r'重合的 $z,\zeta$ 轴和水平面内的合角',r'\theta=0\ \Rightarrow\ R=R_z(\varphi+\psi)',r'\chi=\varphi+\psi\quad\hbox{唯一确定}'),
6:(r'进动方向在本体轴 $\vect n$ 上的投影',r'\vect e_\zeta\cdot\vect n=\cos\theta',r'\omega_3=\dot\psi+\dot\varphi\cos\theta'),
7:(r'由不共线三点形成的有向面积',r'\Delta=x_{AB}y_{AD}-y_{AB}x_{AD}\ne0',r'F_x=F_y=M_A=0'),
8:(r'接触点的静摩擦和纯滚动约束',r'\vect v_P=\vect v_C+\vect\omega\times\vect r_{CP}=0',r'\mathcal P_f=-fv+fa|\omega|=0'),
9:(r'从 $O,A$ 指向同一作用点 $P_i$ 的位置关系',r'\vect r_{AP_i}=\vect r_{OP_i}-\vect r_{OA}',r'\vect M_A=\vect M_O-\vect r_{OA}\times\vect F'),
10:(r'不共点的三个力及抵消其合矩的独立力偶',r'\sum\vect F_i=0,\quad\sum M_i=-aF',r'M_c=+aF\ \Rightarrow\ \sum M=0'),
11:(r'过质心的转轴与杆的夹角 $\beta$',r'd_\perp=|s\sin\beta|',r'I_\beta=\int d_\perp^2\dd m=mL^2\sin^2\beta/12'),
12:(r'平行球心轴和偏置轴之间的垂距 $d$',r'd_\perp^2=(x-d)^2+y^2',r'I=I_C+md^2'),
13:(r'半球质心沿对称轴的移动',r'z_C=3a/8',r'I_{Cx}=I_{Ox}-mz_C^2,\quad I_{Cz}=I_{Oz}'),
14:(r'重根平面内可以旋转的正交方向',r'\mathsf I\vect u=A\vect u,\quad u_z=0',r"\text{另选正交基：}\quad\vect e_1'\cdot\vect e_2'=0"),
15:(r'两个圆轮与同一斜面的接触',r'\ddot x=g\sin\beta/(1+k)',r'k_{\rm ring}=1,\quad k_{\rm disk}=1/2'),
16:(r'悬点至质心的距离 $h$',r'I_O=I_C+mh^2',r'I_O\ddot\theta+mgh\sin\theta=0'),
17:(r'轴上质心与倾斜杆造成的轴承力偶',r'\vect M_C=\vect\omega\times\vect L_C',r'd\vect e_z\times\Delta\vect R_B=\vect M_C'),
18:(r'当前底部材料点 $P$ 与轮心 $C$',r'\vect v_P=0',r'\vect a_P=-\omega^2\vect r_{CP}=(v^2/R)\vect j'),
19:(r'外滚轮接触点相对轮心的向内半径',r'\omega_{\rm abs}=(1+R/r)\Omega',r'\omega_{\rm rel}=\omega_{\rm abs}-\Omega'),
20:(r'球相对板的初始滑动与摩擦冲量',r'u=v_b-R\omega-V',r'J_* =2mMv/(7M+2m)'),
21:(r'非主轴角速度与固定角动量的关系',r'\vect L=A\vect\omega+(C-A)s\vect e_3',r'\dot{\vect\omega}=-(C-A)s\dot{\vect e}_3/A'),
22:(r'中间惯量轴上的主转动与横向扰动',r'\dot x=-az,\quad\dot z=-bx',r'\ddot x=abx,\quad ab>0'),
23:(r'本体轴绕固定角动量的圆锥运动',r'\dot{\vect e}_3=(\vect L/A)\times\vect e_3',r'\dot\varphi=L/A,\quad\dot\psi=-(C-A)s/A'),
24:(r'竖直方向和本体对称轴上的两个角动量投影',r'P=C\omega_3,\quad K=L_\zeta',r'E=T+mgl\cos\theta'),
25:(r'重陀螺的倾角与进动方向',r'A\Omega^2\cos\theta_0-P\Omega+mgl=0',r'\Omega_{\rm slow}\simeq mgl/P'),
26:(r'章动允许区间内的候选零进动位置 $K/P$',r'\operatorname{sgn}\dot\varphi=\operatorname{sgn}(K-Pu)',r'u_* =K/P\in(u_-,u_+)'),
27:(r'磁场方向及角动量的进动圆锥',r'\dot{\vect L}=\gamma\vect L\times\vect B',r'\vect\Omega_L=-\gamma\vect B'),
28:(r'一周相位 $2\pi$ 与普通频率',r'\omega_0=|\gamma|B',r'f_0=\omega_0/(2\pi)'),
29:(r'两能级的完整间距',r'E_\pm=\mp\gamma\hbar B/2',r'|\Delta E|=\hbar\omega_0=|\gamma|\hbar B'),
30:(r'纵向载频与横向翻转场的独立作用',r'B_0\mapsto2B_0\ \Rightarrow\ \omega_0\mapsto2\omega_0',r'B_1\ \hbox{固定}\ \Rightarrow\ \tau_{90},\tau_{180}\ \hbox{不变}')}
assert set(E)==set(range(1,67));assert set(T)==set(range(1,31))
rows=[]
for prefix,data in [('ex',E),('tr',T)]:
 for n,(feature,eq1,eq2) in data.items():
  key=f'{prefix}{n:02}';s=(P/'题图'/(key+'.tex')).read_text();s=s.replace(r'\end{tikzpicture}','')
  # Two derived relations beside the actual model make a diagram of the calculation stage.
  s+=r'''\coordinate(AnalysisTop)at($(current bounding box.north east)+(.85,0)$);
\node[anchor=north west,align=left,font=\small] at(AnalysisTop){\textbf{约束与计算}\\[6pt]$'''+eq1+r'''$\\[6pt]$\Downarrow$\\[6pt]$'''+eq2+r'''$};
\end{tikzpicture}
'''
  (D/(key+'.tex')).write_text(s)
  caption=('例' if prefix=='ex' else '训练题')+str(n)+'的计算示意'
  # Every reference tells the reader what geometry or direction is used in the derivation.
  note=r'以图~\ref{fig:solution-'+key+'}~中'+feature+'为依据，先写出图右侧第一行的几何或动力学关系，再代入其下方的计算式。'
  rows.append({'key':key,'feature':feature,'caption':caption,'note':note,'first_relation':eq1,'second_relation':eq2})
(P/'工作文件/解答图与推导对应.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('96 editable solution-stage diagrams generated')
