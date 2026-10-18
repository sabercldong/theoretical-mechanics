from pathlib import Path
import json
P=Path(__file__).resolve().parents[1];D=P/'解答图';D.mkdir(exist_ok=True)
E={
1:(r'顶点 $A,B,C$ 与中线交点 $G$',r'\vect r=\vect a+u(\vect b-\vect a)+v(\vect c-\vect a)',r'\vect R=(\vect a+\vect b+\vect c)/3'),
2:(r'位于 $y=\sqrt3R/4$ 的两个负质量圆孔',r'M=\sigma\pi(R^2-2r^2)',r'Y_C=-\sqrt3Rr^2/[2(R^2-2r^2)]'),
3:(r'半球的水平截面和厚壳内外半径',r'A(z)=\pi(a^2-z^2)',r'Z_{\rm shell}=3(b^4-a^4)/[8(b^3-a^3)]'),
4:(r'$x\ge0$ 半圆截面的形心及顶点高度',r'\bar x(z)=4a(1-z/h)/(3\pi)',r'X_C=a/\pi,\quad Z_C=h/4'),
5:(r'两条竖直边界间宽为 $\dd x$ 的面积条',r'\dd A=(a-kx^2)\dd x',r'Y_C=3a/5'),
6:(r'三条截距为 $2,4,8$ 的坐标棱',r'x=2u,\ y=4v,\ z=8w',r'\vect R=(1/2,1,2)'),
7:(r'高度 $z$ 的截面及其密度权重',r'\dd m=\rho_0(1+z/a)\pi(a^2-z^2)\dd z',r'M=11\pi\rho_0a^3/12,\quad Z_C=23a/55'),
8:(r'两根等长杆的中点和沿水平轴移动的滑块 $B$',r'\vect P=\sum_i m_i\vect v_i',r'X_C=l(2m_1+2m_2)\cos\theta/(2m_1+m_2)'),
9:(r'爆炸点 $C$ 后的质心轨迹与重力方向',r'\vect R=\vect R_0+\vect V_0t+\vect g t^2/2',r'\sum_i m_i\vect r_i=M\vect R'),
10:(r'偏心转子在初始上方的位置',r'\vect a_C=-m_2e\omega^2\vect e_r/(m_1+m_2)',r'\vect N=(D\sin\omega t,G-D\cos\omega t)'),
11:(r'倾斜炮管方向与炮身的水平反冲',r'MU+m(U+V\cos\alpha)=0',r'U=-mV\cos\alpha/(M+m)'),
12:(r'跳入的 $60^\circ$ 水平投影与跳出的相对速度',r'150v_*=100+50(2\cos60^\circ)',r'v_{\rm cart}=1+\sqrt3/6'),
13:(r'同一车上各人的同时或依次离车',r'\Delta V_j=-mv/[M+(N-j+1)m]',r'|V_{\rm seq}|=\sum_{j=1}^N mv/[M+jm]'),
14:(r'摆长 $l$、角度 $\theta$ 与水平活动支点',r'(m_A+m_B)\dot X+m_Bl\dot\theta\cos\theta=0',r'k^2=(m_A+m_B)g/(m_Al)'),
15:(r'两质点到相遇点的互补距离',r'm_1x_1+m_2x_2=m_2L',r'x_{\rm meet}=m_2L/(m_1+m_2)'),
16:(r'冲量沿 $AB$ 的径向分量与垂直分量',r'v_{Ar}=v_{Br}=J\cos\alpha/(m_A+m_B)',r'K=m_AJ\cos\alpha/(m_A+m_B)'),
17:(r'人向上、球向下与沟底高度差',r'm_1u=m_2w,\quad h=wt+gt^2/2',r't=u/g,\quad u^2=gh/(m_1/m_2+1/2)'),
18:(r'移动点 $A$ 到粒子的有向位置矢量',r'\vect s=(vt,-ut),\quad\vect p=(mv,0)',r'L_{A,z}^{\rm abs}=muvt,\quad L_{A,z}^{\rm rel}=0'),
19:(r'A侧绳上升与B侧绳下降的速度约束',r'v_A=u,\quad v_B=v-u',r'(2mr^2+I_p)u=mr^2v'),
20:(r'两猴到轮轴水平面的不同高度 $s,s^{\prime}$',r'ma-m^{\prime}a^{\prime}=(m^{\prime}-m)g',r't^2=2(ms-m^{\prime}s^{\prime})/[(m^{\prime}-m)g]'),
21:(r'下端冲量 $J$ 到质心 $C$ 的垂直力臂',r'V_C=J/(2m),\quad I_C=ml^2/2',r'\omega=J/(ml)'),
22:(r'杆与 $OC$ 夹 $45^\circ$ 时的两个径向外力',r'\vect\tau_C=\vect s\times(\vect F_B-\vect F_A)',r'\vect F=k\vect r\ \Rightarrow\ \vect\tau_C=0'),
23:(r'$f-r$ 平面上有方向的闭合路径',r'W_{\rm int}=\oint f\dd r',r'W=(f_{\rm high}-f_{\rm low})(r_{\max}-r_{\min})'),
24:(r'质心的逆时针公转与两球的顺时针自转',r'T=m\Omega^2R^2+m\omega^2r^2',r'L_{O,z}=2m\Omega R^2-2m\omega r^2'),
25:(r'单次升高 $H$ 和从静止加速到 $V$ 的示例过程',r'\hbox{单次示例：}\quad E_{\rm mech}=MgH+MV^2/2',r'm_{\rm food}=E_{\rm mech}/(\eta q_{\rm food})'),
26:(r'弹簧经过原长时相反方向的两速度',r'm_1\vect v_1+m_2\vect v_2=\vect0',r'|p_1|=|p_2|=\delta\sqrt{\mu k}'),
27:(r'两球距离从 $a$ 缩到 $a/2$ 时的相向速度',r'\mu w^2/2=Gm_1m_2/a',r'w=\sqrt{2G(m_1+m_2)/a}'),
28:(r'固定端 $O$、可变球半径 $r$ 与切向转动',r'(I_t+mr^2)\omega=(I_t+ml^2/4)\omega_0',r'v_{\rm out}^2=\dot r_{\rm out}^2+l^2\omega_{\rm out}^2'),
29:(r'两球的水平质心约束及上球高度 $l\cos\theta$',r'\dot\theta^2=4g(\cos\alpha-\cos\theta)/[l(1+\sin^2\theta)]',r'N>0\quad(\alpha\le\theta<\pi/2)'),
30:(r'下端固定时的法向 $N$ 与有符号摩擦 $f$',r'\dot\theta^2=2g(\cos\alpha-\cos\theta)/l',r'|f|\le\mu_sN\quad\hbox{取首次越界}'),
31:(r'上端冲量产生的离地参数 $\Lambda$',r'N(0^+)=mg(2-\Lambda)',r'\Lambda>2:\quad\ddot y_1(0^+)=g(\Lambda/2-1)>0'),
32:(r'接触点 $q$ 的法线与质心偏置力臂',r'm_{\rm eff}^{-1}=M^{-1}+b_n^2/I_C',r'K=-(1+e)m_{\rm eff}v_n^-'),
33:(r'离地后两端旋转高度与首次接触事件',r'y_2/l=(1-\tau^2+\cos2\tau)/2',r'\tau_*=0.8900586\ldots,\quad y_1>0'),
34:(r'水平杆右端球2承受的法向冲量',r'1/m_{\rm eff}=1/(2m)+(l/2)^2/I_C=1/m',r'K=(1+e)mv,\quad v_{2y}^+=ev'),
35:(r'桌沿 $O$ 处沿杆正向 $\vect e$ 与实际摩擦 $|f|$ 的分解',r'N=9mg\cos\theta/5,\quad f=-12mg\sin\theta/5',r'\mu_s=4\tan\alpha/3'),
36:(r'右球 $m$ 与左球 $2m$ 的相对距离',r'R=a/3+v_0t/3,\quad\ddot q+\omega^2(q-a)=0',r'x_1=R+2q/3,\quad x_2=R-q/3'),
37:(r'两天体到同一个质心 $C$ 的反向位置',r'\mu\ddot{\vect r}=-K\vect r/r^3',r'T^2=4\pi^2a_r^3/[G(m_S+m_E)]'),
38:(r'两星间距 $L$ 与质心半径之和',r'R_1=M_2L/(M_1+M_2)',r'\Omega^2=G(M_1+M_2)/L^3'),
39:(r'$\rho>0$ 时最近点 $Q$ 处垂直于径矢 $OQ$ 的切向速度',r'\mu v_\infty^2/2=L^2/(2\mu a^2)+mc/(2a^2)',r'a^2=\rho^2+3c/(2v_\infty^2)'),
40:(r'偏置质心 $C$ 与下端到质心的距离 $d_1$',r'I_C=\mu L^2,\quad I_C\omega=Jd_1',r'V_C=J/M,\quad\omega=J/(m_1L)'),
41:(r'初始横向速度与相对角动量',r'E_{\rm rel}=mv_0^2/4,\quad L=mav_0/2',r'\beta x_*^2(x_*-1)=x_*+1'),
42:(r'碰后左端粘连质量 $2m$ 的横向速度',r'\mu=2m/3,\quad E_{\rm rel}=mV_0^2/12',r'E_{\rm rel}=mV_0^2/108+2ka^2'),
43:(r'两端对称位置与中球之间的半绳长度 $a$',r'\vect r_\pm=(x_M-a\sin\phi,\pm a\cos\phi)',r'\dot\phi^2=Mv^2/[a^2(M+2m\sin^2\phi)]'),
44:(r'光滑钉两侧可变径向长度与各自的切向速度',r'r_1+r_2=4a,\quad |L_1|=mav,\quad |L_2|=3mav',r'1=\dot r_1^2/v^2+[x^{-2}+9(4-x)^{-2}]/2'),
45:(r'最高点处两物体相对质心的水平速度增量',r'W\delta v_H+w\delta v_O=0',r'x_H-x_O=u v_0\sin\alpha/g'),
46:(r'最高点的水平爆炸增量及相同下落时间',r'E=\mu w^2/2,\quad t_d=v/g',r'd=(v/g)\sqrt{2E/\mu}'),
47:(r'入射球与初始静止靶的同一直线速度',r'm_1v_1+m_2v_2=m_1u,\quad v_2-v_1=u',r'v_1=(m_1-m_2)u/M,\quad v_2=2m_1u/M'),
48:(r'两条互相垂直的等质量出射速度',r'\Theta=2\theta,\quad |v_1|=u\cos\theta',r'E_1/E_{\rm in}=\cos^2\theta'),
49:(r'实验室入射方向及对应的相对散射偏角',r'b=K\cot(\Theta/2)/(2E_{\rm rel})',r'f_C=[K/(4E_{\rm rel})]^2\sin^{-4}(\Theta/2)'),
50:(r'同一射线与速度圆的两个交点 $P_+,P_-$',r'\Theta_1=\theta+\arcsin(2\sin\theta)',r'\Theta_2=\theta+\pi-\arcsin(2\sin\theta)'),
51:(r'两交点对应的速度长度与质心偏角',r'D_\pm=\lambda\cos\theta\pm\sqrt{1-\lambda^2\sin^2\theta}',r'f_L=\sum_{j\ \rm allowed} f_C(\Theta_j)D_j^2/h'),
52:(r'中点与端点到固定铰 $A$ 的不同距离',r'mv_0L/2=I_A\omega,\quad I_A=9mL^2/4',r'v_{\rm mid}=v_0/9,\quad J_{A,x}=-2mv_0/9'),
53:(r'对地静止的小块与运动主体的粘连',r'(m+\delta m)v_+=mv',r'\Delta T_{\rm loss}=m\delta m v^2/[2(m+\delta m)]'),
54:(r'向后的相对喷速与向上的主体速度',r'm\dot v=-mg-c\dot m',r'v=v_0+c\ln(m_0/m)-gt'),
55:(r'发射台上的单向支持力及离台阈值',r'N=mg-cq\ge0\quad(v=0)',r'm_L=cq/g,\quad t_L=(m_0-m_L)/q'),
56:(r'静止来流进入向下运动的雨滴',r'\dd[(M+\lambda t)v]/\dd t=(M+\lambda t)g',r'v=g(Mt+\lambda t^2/2)/(M+\lambda t)'),
57:(r'球形雨滴的半径增长与静止来流',r'\dot r=c_s/(4\pi\rho)=\lambda',r'v=g(r^4-a^4)/(4\lambda r^3)'),
58:(r'自由下落直段和已静止的地面绳堆',r'R=\sigma gh+\sigma v^2,\quad v^2=2gh',r'R=3\sigma gh\quad(0\le h<l)'),
59:(r'同速链条的水平段与悬垂段',r'\sigma l\dot x^2/2-\sigma gx^2/2=-\sigma gl^2/8',r'x=(l/2)\cosh(\sqrt{g/l}\,t)'),
60:(r'相对枪喷出方向与有符号对地子弹速度',r'\dd(mv)/\dd t+qU=-\mu_fmg',r'U=-u\quad\hbox{或}\quad U=v-u'),
61:(r'自由粒子随时间伸长的位置矢量',r'D(\tau)-D(0)=mv^2\tau',r'2\overline T+\overline W=mv^2\ne0'),
62:(r'有界振动位置与速度的周期相位',r'D=-mA^2\omega\sin2\omega t/2',r'2\overline T+\overline W=[D(\tau)-D(0)]/\tau'),
63:(r'质心系内各粒子的相对位置与成对引力',r'W=\sum_{i<j}-Gm_im_j/r_{ij}=U',r'2\overline T+\overline U=0,\quad E=-\overline T'),
64:(r'平衡点两侧振动的弹簧势能',r'W=x(-kx)=-2U',r'\overline T=\overline U=kA^2/4'),
65:(r'中心距离小于硬核距离 $d$ 的禁入区',r'f(r)=-1\ (r<d),\quad f(r)=0\ (r>d)',r'B_2=-2\pi\int f r^2\dd r=2\pi d^3/3'),
66:(r'硬核和吸引壳在 $d,a$ 两处的分段边界',r'f=-1,\quad e^{\epsilon/(k_B\Theta)}-1,\quad0',r'B_2=2\pi[d^3-(a^3-d^3)(e^{\epsilon/(k_B\Theta)}-1)]/3')}
T={
1:(r'相距 $a$ 的两条反向力作用线',r'\vect F_1+\vect F_2=0',r'\vect\tau_O=-aF\vect k'),
2:(r'靠近重球的质心 $C$ 及两段距离',r'm_1d_1=m_2d_2,\quad d_1+d_2=L',r'm_2=3m_1:\quad d_1=3L/4'),
3:(r'半径 $a$ 的上半圆线元',r'\dd m=\lambda a\dd\varphi',r'Y_C=a\int_0^\pi\sin\varphi\dd\varphi/\pi=2a/\pi'),
4:(r'密度随 $x$ 增大的杆段',r'M=3\lambda_0L/2,\quad J=5\lambda_0L^2/6',r'X_C=J/M=5L/9'),
5:(r'偏向正 $x$ 的孔心 $H$',r'J_x=-\sigma\pi r^2d',r'X_C=-r^2d/(R^2-r^2)'),
6:(r'恒定外力和质心初始动量的不同方向',r'\vect P=\vect P_0+\vect Ft',r'\vect R=\vect R_0+\vect P_0t/M+\vect Ft^2/(2M)'),
7:(r'匀速平移的新参考系及各粒子速度减量',r'\vect v_i^{\prime}=\vect v_i-\vect U',r'T^{\prime}=T-\vect U\cdot\vect P+MU^2/2'),
8:(r'水平炮管的出膛速度与炮身反冲',r'v-U=V\quad\hbox{或}\quad v=V',r'U=-mV/(M+m)\quad\hbox{或}\quad U=-mV/M'),
9:(r'A、B两侧绳速度相反的约束',r'(2mr^2+I_p)u=mr^2v',r'I_p=mr^2:\quad v_A=v/3,\quad v_B=2v/3'),
10:(r'移动点 $A$ 引入的力臂变化',r'\dot{\vect L}_A=\vect\tau_A-\vect v_A\times\vect P',r'\vect\tau_A=0\ \Rightarrow\ \dot{\vect L}_A=-\vect v_A\times\vect P'),
11:(r'任意移动基点 $A$ 及其速度',r'T=\tfrac12Mv_A^2+T_{\rm rel}+\vect v_A\cdot(\vect P-M\vect v_A)',r'A=C:\quad\vect P-M\vect v_A=0'),
12:(r'球到固定端的半径与管的转动惯量',r'\omega_{\rm out}/\omega_0=(4\eta+3)/[4(\eta+3)]',r'\eta\to0:\quad\omega_{\rm out}\to\omega_0/4'),
13:(r'杆倒平前两端的水平速度和上球竖直速度',r'v_{1x}=-l\dot\theta\cos\theta/2',r'v_{1x}\to0,\quad v_{2y}\to-\sqrt{2gl\cos\alpha}'),
14:(r'一般初始悬长 $x_0$ 与下滑方向',r'\ddot x=(g/l)x',r'v_{\rm exit}^2=v_0^2+g(l^2-x_0^2)/l'),
15:(r'相对圆轨道的弹簧张力与切向速度',r'k(r_0-a)r_0^3=L^2/\mu',r'W^{\prime\prime}(r_0)=k(4-3a/r_0)>0'),
16:(r'两星间距 $L$ 与共同质心的轨道',r'T\propto L^{3/2}/\sqrt{M_1+M_2}',r'M_{\rm tot}\mapsto2M_{\rm tot}:\quad T^{\prime}=T/\sqrt2'),
17:(r'位置的 $x,y$ 分量及不同线性回复系数',r'\ddot x=-\omega_x^2x,\quad\ddot y=-\omega_y^2y',r'\dot L_z=\mu(\omega_x^2-\omega_y^2)xy'),
18:(r'从原点作速度圆切线形成的直角三角形',r'\sin\theta_{\max}=1/3',r'\max(E_2/E_{\rm in})=3/4\quad(\Theta=\pi)'),
19:(r'等质量的半角关系及出射角域',r'\dd\Omega_C/\dd\Omega_L=4\cos\theta',r'f_L=\cos\theta/\pi,\quad P(\theta\le\theta_0)=\sin^2\theta_0'),
20:(r'碰后共同速度对应的质心平移',r'V=m_1u/(m_1+m_2)',r'\Delta T=\mu u^2/2'),
21:(r'相对排气方向和燃烧段质量变化',r'q=m_f/t_b,\quad m_0=2m_f',r'v_b=c\ln2-gt_b'),
22:(r'静止凝结物的入流与下落方向',r'z=\lambda t/M\ll1,\quad\ln(1+z)=z-z^2/2+\cdots',r's=gt^2/2-\lambda gt^3/(6M)+O(\lambda^2)'),
23:(r'两体相对位置与成对力的点积',r'W_{12}=\vect r_{12}\cdot\vect F_{12}',r'[W]=[D]/[t]=\mathrm{kg\,m^2\,s^{-2}}'),
24:(r'两种幂次势能的不同齐次性',r'W=U_{-1}-2U_2',r'2\overline T=-\overline U_{-1}+2\overline U_2\quad(\tau\to\infty)')}
assert set(E)==set(range(1,67));assert set(T)==set(range(1,25))
rows=[]
for prefix,data in [('ex',E),('tr',T)]:
 for n,(feature,eq1,eq2) in data.items():
  key=f'{prefix}{n:02}';s=(P/'题图'/(key+'.tex')).read_text().replace(r'\end{tikzpicture}','')
  if key=='ex26':
   s=s.replace('$k\\delta$',r'$\vect v_1$',1).replace('$k\\delta$',r'$\vect v_2$',1).replace('$a-\\delta$','$a$').replace(r'初态 $v_1=v_2=0$',r'经过原长：弹性势能为0')
  s+=r'''\coordinate(AnalysisTop)at($(current bounding box.north east)+(.8,0)$);
\node[anchor=north west,align=left,font=\small]at(AnalysisTop){\textbf{约束与计算}\\[6pt]$'''+eq1+r'''$\\[6pt]$\Downarrow$\\[6pt]$'''+eq2+r'''$};
\end{tikzpicture}
'''
  (D/(key+'.tex')).write_text(s)
  caption=('例' if prefix=='ex' else '训练题')+str(n)+'的分析与计算'
  note=r'图~\ref{fig:solution-'+key+'}~中'+feature+'，给出了本题列式所用的方向、位置或分区关系；图右侧列出由这些条件得到的关键方程及下一步计算。'
  rows.append(dict(key=key,feature=feature,caption=caption,note=note,first_relation=eq1,second_relation=eq2))
(P/'工作文件/解答图与推导对应.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('90 solution-stage diagrams generated')
