from 题设数据 import P
# model diagram, first relation, resulting relation, physical meaning used in the answer.
ROWS=r'''
1|2|\dot x=R\dot\varphi\cos\theta|\dot y=R\dot\varphi\sin\theta|盘面切向由航向角 $\theta$ 决定；沿路径累积的两分量会随航向变化，不能只按终态自转角计算位移。
2|four_models|s=N_{\rm coord}-k|s=1,2,1,3|摆长、球半径与直线滚动约束各消去一个独立位置变量；定点刚体还保留三个姿态参数。
3|4|\dd s^2=(a^2+b^2)\dd u^2|T=\tfrac12m(a^2+b^2)\dot u^2|螺旋线的轴向升高和水平绕转都由同一参数 $u$ 决定，弧长中两部分的平方相加。
4|atwood_pair|y_{\rm left}+y_{\rm right}=C|y_{\rm lower}=y+s|主绳把两侧位移联系起来，却不固定下面弹簧的长度 $s$；驱动环的整体角 $\alpha(t)$ 已由外界规定。
5|tangent_pair|\delta\vect r=l\vect e_\theta\delta\theta|\delta\vect r_{S^2}=R\vect e_\theta\delta\theta+R\sin\theta\vect e_\phi\delta\phi|圆周切向对应单摆唯一变分方向；球面的两个切向箭头分别对应独立的极角、方位角变分。
6|pendulum_force|\delta W=F\delta x-mg\delta y|Q_\theta=Fl\cos\theta-mgl\sin\theta|水平力沿 $+x$、重力沿 $-y$；两力分别与摆球切向位移投影相乘，产生正负不同的广义力。
7|8|\delta W=Q_1\delta\theta_1+Q_2\delta\theta_2|Q_1=Q_2=0|两杆角互相独立；第二杆重心随铰点 $A$ 移动，因此第一角的重力系数还包含整根第二杆的重量。
8|9|x_B=2a\cos\phi|\delta x_B=-2a\sin\phi\,\delta\phi|点 $A,C$ 的切向虚位移共用 $\delta\phi$；滑块 $B$ 只作水平位移，不能再赋予独立竖向变分。
9|10|y_C=l\sin\theta-d\tan\theta|\cos^3\theta=d/l|固定棱边 $O$ 限制杆与墙的交点高度；杆重心 $C$ 的高度随两种几何效应同时变化。
10|11|m_{AB}=\sigma a,\quad m_{BC}=\sigma b|\tan\theta=b^2/(a^2+2ab)|两段质心位置分别按各自杆长和质量加权；铰点 $A$ 的反力不作虚功。
11|12|\delta x_B=-r\frac{\sin(\phi+\psi)}{\cos\psi}\delta\phi|F_A=F_B\frac{\sin(\phi+\psi)}{\cos\psi}|曲柄的切向力与弧向虚位移同向；滑块位移受连杆长度约束，符号由右正方向确定。
12|13|\nabla z=\lambda\nabla f|z_{\min}=\tfrac12;\quad z=1,9|投影图中的直线和偏心圆是允许位置；沿约束交线改变位置时，驻值点的高度一阶变化为零。
13|15|y_B=\sqrt{4l^2-x^2},\quad x=DE|N=-P/\sqrt3|中点横杆长度是所选位移 $x$；将横杆拆去，向外的正试探力与顶点下降的虚功相联系。
14|16|T_2\sin\theta_2=F_2|T_1\sin\theta_1=F_2-F_1|下绳的拉力对两球方向相反；上绳承受两球总重，水平分量对应两外力的代数和。
15|17|\vect v=\dot r\vect e_r+r\dot\phi\vect e_\phi|p_\phi=mr^2\dot\phi=J|径向和横向速度互相垂直，横向分量中的半径因子是离心项和角动量积分的共同来源。
16|18|\dot y=2\dot x,\quad \omega_s=\dot x/R|a_y=\frac{8mg}{3M+8m}|最高点的绳速由柱心平动与圆柱自转同向叠加；地面接触点瞬时静止，静摩擦仍提供转动力矩。
17|19|\omega_1=\dot y/(2r),\quad\omega_2=\dot y/r|T=\tfrac74m\dot y^2|两盘的接触绳速相同，角速度由各自半径决定；两转动惯量都须折算到同一重物速度。
18|20|T=\tfrac m2(\dot r^2+r^2\dot\theta^2)|m\ddot r-mr\dot\theta^2+k(r-a)-mg\cos\theta=0|弹簧实际长度 $r$ 和偏角 $\theta$ 均可独立变化；沿径向与切向投影时，重力分别带余弦和正弦因子。
19|21|\tfrac7{10}m\rho^2\dot\theta^2=mg\rho(1-\cos\theta)|N=\tfrac{mg}{7}(17\cos\theta-10)|法向反力作用在接触处并沿两球心连线；上坡静摩擦提供自转，必须先与摩擦上限比较。
20|22|\vect v_B=\dot x\vect e_x+l\dot\phi\vect e_\phi|T_{\rm cross}=m_2l\dot x\dot\phi\cos\phi|摆球绝对速度是悬点平移与绕悬点运动的矢量和；两箭头的投影产生不能丢掉的动能交叉项。
21|23|\vect v_m=\dot x\vect e_x+\dot s\vect e_s|\Omega^2=\frac{k(M+m)}{m(M+m\sin^2\alpha)}|沿坡向上的 $\dot s$ 与斜面向右的 $\dot x$ 夹角为 $\alpha$，因此速度平方产生正的余弦交叉项。
22|24|v_C=(R+r)\dot\phi=r\omega_s|\omega_{\rm rel}=\omega_s-\dot\phi=R\dot\phi/r|接触点固定不动，把行星轮的公转速度与绝对自转联系；相对曲柄自转须再减去曲柄转速。
23|8|T=\tfrac A2\dot\theta_1^2+\tfrac B2\dot\theta_2^2+C\cos\Delta\dot\theta_1\dot\theta_2|\Delta=\theta_1-\theta_2|两杆重心和铰点 $A$ 的速度共同进入动能；两角的差决定交叉项，端点水平力仍按其虚位移求广义力。
24|cyclic_three|p_\phi=ma^2\sin^2\theta\dot\phi|\dot p_\phi=0|碗面上纬向速度为 $a\sin\theta\dot\phi$；绕竖直轴的对称性使方位角不显含于拉格朗日函数。
25|tube_horizontal|\ddot r=\omega^2r|r=a\cosh\omega t|管的方向随规定角速率转动，径向相对速度与横向牵连速度互相垂直；离管条件是 $r=l$。
26|tube_vertical|y=r\sin\omega t|\ddot r-\omega^2r=-g\sin\omega t|径向正方向沿管，重力在该方向的投影随时间变为 $-mg\sin\omega t$，势能显含时间。
27|26|X=\frac{m_1x_1+m_2x_2}{M},\quad s=x_2-x_1|\mu\ddot s+(k-\mu\omega^2)s=ka|质心坐标描述整体离轴运动，弹性绳长描述两球相对运动；固定转速产生的二次项分别进入两者。
28|27|\vect r=a(1+\cos\theta)\vect e_1+a\sin\theta\vect e_2|\ddot\theta+\omega^2\sin\theta=0|转轴在环上一点 $O$，不能把它当成环心；环心的牵连速度与珠的相对速度在绝对动能中耦合。
29|28|p_y=4m\dot y+m\dot s=0|\ddot s+\frac{4g}{3a}(s-2a)=0|主绳让质量 $2m$ 与上球反向运动，下球还增加相对长度 $s$；消去循环速度后有效质量为 $3m/4$。
30|29|h=r^2\dot\theta,\quad h^2=\tfrac92ga^3|\dot r^2+\frac{h^2}{2r^2}+gr=\tfrac{13}{4}ga|孔下球的位移为 $l-r$，两球都贡献径向动能；桌面球的切向运动由绕孔角动量守恒决定。
31|30|\mu=m/2,\quad J=\mu av/\sqrt2|\tfrac{mv^2}{4}=\tfrac{mv^2}{128}+\tfrac92ka^2|初态相对速度有径向和横向两分量；在最大伸长处仅径向速度为零，绕质心转动动能仍须保留。
32|31|A=2m_1+2I/r^2|\ddot u+\frac{k(A+m_2)}{Am_2}u=0|两轮转动由无滑动条件与车架速度联系；循环积分含转动折算项，地面摩擦可改变真实水平动量。
33|33|\dd t=\frac{\sqrt{1+y'^2}}{\sqrt{2gy}}\dd x|x=a(u-\sin u),\ y=a(1-\cos u)|沿轨道下降获得的速度取决于深度 $y$；弧长元和速度之比决定时间泛函，最低点后须连续改变斜率支。
34|34|\frac{\sigma gy+\lambda}{\sqrt{1+y'^2}}=H|y=a\cosh\frac{x-x_0}{a}+y_0|链元两端张力的水平分量相同，长度乘数决定高度平移；最低点两侧以双曲余弦统一表示。
35|35|\dd A=2\pi y\sqrt{1+y'^2}\dd x|y=a\cosh\frac{x-x_0}{a}|母线高度 $y$ 是旋转半径，直接乘入窄环带面积；两端圆环给两个参数边界条件，半径不能任意平移。
36|geodesic_isoperimetric|\vect L\cdot\vect r=0|\kappa=\text{常数},\quad A_{\max}=l^2/(4\pi)|球面上的固定过心平面截出大圆；平面闭曲线的外法向变分使面积与周长的一阶变化通过曲率相联系。
37|36|ct'(x)=n_1\sin\theta_1-n_2\sin\theta_2|n_1\sin\theta_1=n_2\sin\theta_2|两条光路在界面交点连接，两个角都从法线量起；改变交点会同时改变两段长度，不能各自独立取极值。
38|action_paths|x=x_*+\eta,\quad\eta(t_1)=\eta(t_2)=0|S[x]-S[x_*]=\tfrac m2\int\dot\eta^2\dd t|扰动曲线与直线轨道具有相同两端点，分部积分的端点差因此为零；剩余平方积分判定本例最小性。
39|27|A=\dot\theta+\omega(1+\cos\theta)|\delta S=-ma^2\int(\ddot\theta+\omega^2\sin\theta)\delta\theta\dd t|滑珠的相对角沿环心定义；固定两时刻的位置使角变分端点为零，速度变分须先分部积分再消项。
40|37|p_\psi=c_3,\quad p_\phi=c_z|\dot\phi=\frac{c_z-c_3\cos\theta}{I\sin^2\theta}|竖直轴进动与本体轴自转是两个不同的对称方向；本体轴角速度为 $\dot\psi+\dot\phi\cos\theta$。
41|38|v_C=(R-r)\dot\theta=r\omega_s|\omega_0^2=\frac{5g}{7(R-r)}|圆柱内滚动的球心轨道半径是 $R-r$，接触点 $A$ 瞬时静止，球心平动与球自转可合为绕 $A$ 的动能。
42|39|AC^2=r^2+d^2-2rd\cos\theta|\omega_0^2=\frac{gd}{3r^2/2-2rd}|圆心保持离地高度 $r$，偏心质心随 $\theta$ 升降；接触点到质心的距离决定瞬时惯量。
43|40|Q_\pm=(x_1\pm x_2)/\sqrt2|\omega_+^2=k/m,\quad\omega_-^2=(k+2k')/m|同相位移不改变中间弹簧长度，反相位移加倍改变它的长度；和差方向正好将两种能量同时对角化。
44|cart_modes|\det(K-\lambda M)=0|\lambda^2-(\omega_s^2+2\omega_p^2)\lambda+\omega_s^2\omega_p^2=0|滑块位移与摆球转角的混合惯性来自悬点移动；两侧弹簧的变式只把刚度 $k$ 替换为 $2k$。
45|42|\det(K-\lambda M)=0|\omega_\pm^2=(2\pm\sqrt2)g/l|两杆角均是相对竖直的绝对角；慢模式同相、快模式反相，下球振幅由耦合矩阵给出而非任意指定。
46|legendre|u=f'(x)=ax|g(u)=ux-f(x)=u^2/(2a)|抛物线切线的斜率是新变量 $u$，纵截距为 $-g(u)$；变换先解斜率关系，再计算截距。
47|particle_line|p=m\dot x|\dot x=H_p,\quad\dot p=-H_x|位置 $x$ 与动量 $p$ 共同指定初态，势能曲线的局部斜率决定力的负方向。
48|17|p_r=m\dot r,\quad p_\phi=mr^2\dot\phi|\dot p_r=p_\phi^2/(mr^3)-V'(r)|径向动量对应径向速度，方位角动量对应横向转动；对哈密顿函数按固定动量求径向偏导才能得到离心项。
49|25|p_\theta=ma^2\dot\theta|\dot p_\theta=\frac{p_\phi^2\cos\theta}{ma^2\sin^3\theta}-mga\sin\theta|纬圈半径 $a\sin\theta$ 使方位角动量系数随极角变化；正则偏导须保留此几何因子。
50|22|p=A(q)\dot q,\quad\det A=m_2l^2D|D=m_1+m_2\sin^2\phi>0|悬点的平移与摆的转动形成对称速度矩阵；正行列式允许在任意角度唯一反解两个速度。
51|22|D_0=1+\sin^2\phi|H=\tfrac12(p_x\dot x+p_\phi\dot\phi)+V|等质量并不消除交叉惯性；动能二次齐次性提供勒让德变换的半系数，但角度依赖仍留在分母中。
52|osc_phase|\ddot q+\omega^2q=0|q=q_0\cos\omega t+\frac{p_0}{m\omega}\sin\omega t|相椭圆右端的力沿负动量方向，因而轨道顺时针；初始位置和动量分别决定余弦、正弦系数。
53|coulomb_sphere|p_\theta=mr^2\dot\theta|J^2=p_\theta^2+p_\phi^2/\sin^2\theta|径向吸引力沿核与电子连线，绕核力矩为零；球坐标的速度尺度产生两个角动量项。
54|44|L_x=yp_z-zp_y|\{L_x,L_y\}=L_z|角动量三个分量依次绕三条坐标轴定义；泊松括号逐坐标相乘相减，交换两项会改变结果符号。
55|angular_algebra|\{L_x,H\}=\{L_y,H\}=0|\{\{L_x,L_y\},H\}=0|两项已知守恒量通过括号生成第三方向的旋转量，Jacobi 恒等式把该括号的时间导数拆成两个零项。
56|classical_spread|\Delta q\Delta p=E/\omega|A\to0:\quad\Delta q\Delta p\to0|经典相点和任意小椭圆都可作为状态；相椭圆面积随振幅缩小，而基本泊松括号不随轨道大小改变。
57|canonical_map|\{Q,P\}=Q_qP_p-Q_pP_q|\{aq,p/a\}=\{\ln q,qp\}=1|正则缩放一方向伸长、另一方向压缩，保存有向相面积；对数坐标仅覆盖 $q>0$ 的半平面。
58|action_order|Q=\tfrac12(\kappa q^2+p^2/\kappa)|\{Q,P\}=1|椭圆半径平方标记新坐标 $Q$，其绕行角为新动量 $P$；原点没有唯一角度，必须在局部角支工作。
59|moving_origin|Q=q-a(t),\quad P=p|K=H-\dot aP|移动原点的速度必须从绝对速度扣除；母函数的显含时间项正是这项相对运动修正。
60|45|K=\omega_1P_1+\omega_2P_2|\dot P_i=0,\quad\dot Q_i=\omega_i|每条相椭圆由作用量 $P_i$ 标记，角变量沿轨道匀速增长；面积积分的归一化给出 $P_i=E_i/\omega_i$。
61|hj_linear|S=E(q-t)-aq^3/3|q=t+\beta,\quad p=E-aq^2|能量水平线在相平面中是抛物线，$\dot q=1$ 规定沿横轴向右；参数导数给时间原点常数。
62|two_osc|W=W_x(x,E_x)+W_y(y,E_y)|\partial_{E_i}S=\beta_i|两个振动方向各有独立能量和相位；坐标的转折点对应动量为零，根式积分须按运动方向换支。
63|17|p_r^2=2m[E-V(r)]-J^2/r^2|S=J\phi+\int p_r\dd r-Et|径向运动由有效势限制，方位角由同一常量 $J$ 控制；主函数对两个参数求导分别恢复时间和轨道。
64|sphere_coords|\frac{p_\theta^2}{2m}+\frac{J^2}{2m\sin^2\theta}+b(\theta)=\alpha|p_r^2=2m[E-a(r)-\alpha/r^2]|方位角仍是循环方向，但极角势使完整旋转对称性失去；角向分离常数作为径向有效势的系数。
65|46|\dd s^2=h_\xi^2\dd\xi^2+h_\eta^2\dd\eta^2+\xi\eta\dd\vartheta^2|H=E\ \Longrightarrow\ F_\xi=\alpha,\ F_\eta=-\alpha|两族子午抛物线正交，旋转得到轴对称坐标面；先由线元得到尺度，再把能量方程乘以 $\xi+\eta$ 分离。
66|47|p_i=mh_i^2\dot q_i|H=E\ \Longrightarrow\ F_\xi=\alpha,\ F_\eta=-\alpha|椭圆与双曲线共用焦点 $z=\pm\sigma$；焦距决定所有尺度因子的长度量纲，能量项在两分离式中符号不同。
67|separation|f_i-Eg_i=\alpha_i,\quad\sum_i\alpha_i=0|\det S_{q\gamma}=\pm G/\prod_iD_i|每条分离曲线只涉及一对变量，分离常数之和受约束；能量与其余独立常数共同构成完全积分参数。
68|48|\nabla\cdot\dot{\vect z}=-2\gamma|\mathcal A(t)=e^{-2\gamma t}\mathcal A(0)|无阻尼相椭圆闭合，欠阻尼轨道向内螺旋；相区缩小由流场散度决定，不能将其归入保守哈密顿流。
69|49|p=\pm\sqrt{2m[E-V(x)]}|\lambda^2=-V''(x_*)/m|势能曲线与能量线的交点给径向转折位置；图中远处正势垒必须保留，才能区分跨阱闭轨和向右逃逸。
70|phase_sector|q=\lambda a\cos\vartheta,\quad p=\lambda b\sin\vartheta|\dd q\dd p=ab\lambda\dd\lambda\dd\vartheta|第一象限椭圆扇区随哈密顿流顺时针移动，角宽与半径范围保持，面积应按雅可比积分而非外接矩形估计。
71|euler_flow|\det A_{\rm explicit}=1+h^2\omega^2|\det A_{\rm symplectic}=1|两个更新顺序给出不同的平面线性映射；先动量后位置相当于两次剪切，能保存有向相面积。
72|simple_levels|\mu\kappa/(\hbar^2\chi)=n_r+l+1=n|E_n=-\mu\kappa^2/(2\hbar^2n^2)|负能级在电离限下逐渐密集；原点正则和远处衰减共同限制径向级数，使能量由连续值变为离散值。
73|quantum_spread|\|f\|^2\|g\|^2\ge|\langle f,g\rangle|^2|\Delta x\Delta p\ge\hbar/2|位置、动量分布的宽度是同一量子态的二阶矩；它们通过态向量内积和不可交换算符联系。
74|55|I=|\psi_1|^2+|\psi_2|^2+2\Re(\psi_1^*\psi_2)|I=4|\psi_1|^2\cos^2(\Delta\phi/2)|两条路径在同一屏点叠加复振幅，路径差改变相位差；交叉项不能在叠加前当作两独立概率相加。
75|57|\delta S_{\rm bulk}=\int(-\rho_lu_{tt}+\mathcal T u_{xx})\delta u|\omega_n=n\pi\sqrt{\mathcal T/\rho_l}/l|两端位移为零选择正弦振型，内部曲率通过张力给横向加速度；初形和初速度各确定一组时间系数。
76|standing_mode|\int_0^l\sin^2k_nx\dd x=\int_0^l\cos^2k_nx\dd x=l/2|E_n=MA^2\omega_n^2/4|振型节点固定，位移与速度的时间相位相差四分之一周期；空间平方积分使动能和势能系数完全相同。
77|58|\mathcal L=\rho_su_t^2/2-\mathcal T_s|\nabla u|^2/2|\omega_{nm}=\pi c\sqrt{n^2/a^2+m^2/b^2}|矩形膜两组固定边分别选择一个正弦因子；面元斜率的两个方向同时贡献弹性势能。
78|elastic_waves|\rho_m\vect u_{tt}=(\lambda+\mu)\nabla\nabla\cdot\vect u+\mu\nabla^2\vect u|c_L^2=(\lambda+2\mu)/\rho_m,\quad c_T^2=\mu/\rho_m|纵向位移平行传播方向，横向位移与其垂直；只有纵向分量贡献体积压缩，故两波速不同。
79|sound_wave|\delta\rho_t+\rho_0\nabla\cdot\vect v=0|\delta\rho_{tt}-c_s^2\nabla^2\delta\rho=0|压缩区与稀疏区交替，压强梯度驱动流速；对连续方程求时间导数后可用动量方程消去速度。
80|water_wave|\phi\propto\cosh k(z+h)e^{i(kx-\omega t)}|\omega^2=gk\tanh(kh)|底面无穿透选取双曲余弦的深度分布；自由面上的垂向流速与压力条件把表面位移联系到速度势。
81|59|\delta_\phi S\Rightarrow\nabla\cdot\vect E=\rho_e/\varepsilon_0|\delta_A S\Rightarrow\nabla\times\vect B=\mu_0\vect j+\mu_0\varepsilon_0\vect E_t|电场和磁场先由两个势定义，另外两条无源方程成为恒等式；独立势变分给出有源方程和相应边界项。
82|symmetry|\mathcal J=\vect p\cdot\vect\xi-\mathcal E\tau|\vect\xi=\vect\alpha\times\vect r\Rightarrow\mathcal J=\vect\alpha\cdot\vect L|平移箭头指定线动量方向，绕轴转动指定角动量分量，时间平移对应能量；对称方向须被约束和外场共同保留。
83|complex_phase|\Delta\phi=i\phi,\quad\Delta\phi^*=-i\phi^*|j^\mu=i(\phi\partial^\mu\phi^*-\phi^*\partial^\mu\phi)|复场在复平面上整体转相位，模长不变；对场及共轭场分别求导得到同一守恒流的两部分。
84|energy_flux|e=\rho_lu_t^2/2+\mathcal T u_x^2/2|\partial_te+\partial_x(-\mathcal T u_xu_t)=0|一段弦的能量变化由两端能流差决定；能流方向由局部斜率与横向速度的乘积给出。
85|fluid_cell|\partial_t\rho_m+\nabla\cdot(\rho_m\vect v)=0|\rho_mD_t\vect v=-\nabla P+\vect f|控制体各面的质量通量和压强应力共同进入局部守恒；展开动量输运后，密度导数项由质量方程消去。
86|61|g_{\theta\theta}=R^2,\quad g_{\phi\phi}=R^2\sin^2\theta|\ddot\theta-\sin\theta\cos\theta\dot\phi^2=0|球面切向速度的两个分量由度规计量；半径反力不产生绕球心力矩，空间角动量把轨道限制在过心平面。
'''
def parse_rows(s):
 d={}
 for line in s.strip().splitlines():
  n,fig,a,b,bridge=line.split('|',4);d[int(n)]=dict(fig=int(fig) if fig.isdigit() else fig,a=a,b=b,bridge=bridge)
 return d
# Avoid literal pipes inside formula fields above.
rows=parse_rows(ROWS.replace(r'\|',r'\Vert ').replace(r'|\nabla u|',r'\lVert\nabla u\rVert').replace(r'|\psi_1|',r'\lvert\psi_1\rvert').replace(r'|\psi_2|',r'\lvert\psi_2\rvert').replace(r'|\langle f,g\rangle|',r'\lvert\langle f,g\rangle\rvert'))
assert len(rows)==86
TRAIN=r'''
1|moving_circle|(x-vt)\delta x+y\delta y=0|\mathcal P=Nv n_x|圆心沿水平箭头移动；同一时刻的切向虚位移垂直反力，真实位移还包含圆心平移。
2|sphere_normal|\nabla\widetilde f=\nabla f/(2a)|\widetilde\lambda=2a\lambda|球面外法向与半径同向；改变约束函数的尺度只改变梯度长度，不改变真实反力。
3|inverted_pendulum|T+mg=0\quad(\theta=\pi)|T=-mg<0|倒立绳球的重力和绳张力都指向下方，无法静力平衡；换刚杆后可由向上推力提供平衡。
4|22|\frac\dd{\dd t}(\dot x\cos\phi)=\ddot x\cos\phi-\dot x\dot\phi\sin\phi|l\ddot\phi+\ddot x\cos\phi+g\sin\phi=0|悬点速度在摆切线方向上的投影随角度改变，时间导数与动能的角度偏导含同一交叉项。
5|tube_horizontal|N=2m\omega\dot r|\dot E=N\omega r=2m\omega^2r\dot r|反力沿管的横向，与牵连速度同向；它对相对径向位移不作功，却向球输送真实能量。
6|momentum_shift|p=m\dot q+b(q)|H=\frac{(p-b)^2}{2m}+V(q)|相平面纵坐标在每个位置平移 $b(q)$；机械速度取决于 $p-b$，不能把新的共轭动量直接除以质量。
7|natural_boundary|y''=-1,\quad y'(1)=0|y=x-x^2/2|左端位置固定，右端仅在竖向自由；右端任意变分使斜率为零，而不是把该端位置额外固定。
8|coordinate_scale|q=Q/c|\omega^2=(k/c^2)/(a_0/c^2)=k/a_0|坐标轴尺度改变时，同一物理振幅的数字变化；动能与势能的二次系数按同一比例变换。
9|unequal_modes|2\lambda^2-6\lambda+3=0|a_+^{\mathsf T}Ma_-=0|两块质量不同，普通坐标长度不再是正确的模式内积；质量矩阵决定两振幅向量的正交权重。
10|degenerate_modes|K-\omega^2M=0|\omega^2=k/m,\quad\dim\ker=2|二维各向同性振子的两个坐标方向等价；在重根处整个平面都是本征子空间，单列余子式不能选出基。
11|momentum_shift|p=P+f_q,\quad Q=q|K=H(Q,P+f_Q,t)+f_t|动量平移既可随位置也可随时间改变；相空间变换图中的竖向位移改变时间导数，须由 $f_t$ 抵消。
12|free_single|G_t=-p/m,\quad\{G,H\}=p/m|\frac{\dd G}{\dd t}=0|自由粒子相流沿水平方向剪切；从当前位置减去已行距离 $pt/m$ 就得到不变的初始位置。
13|constant_force|p^2=2m(E-Fq)|q=q_0+p_0t/m-Ft^2/(2m)|真实力沿势能增加的反方向，动量随时间线性改变；相轨道在转折点由正动量支接到负支。
14|canonical_circle|Q=\sqrt{m\omega}\,q,\quad P=p/\sqrt{m\omega}|K=\tfrac\omega2(Q^2+P^2)|对位置和动量作互逆缩放，把椭圆的两半轴统一；圆面积仍等于原相椭圆面积。
15|free_shear|q-pt/m=q_0\in(0,a)|\mathcal A(t)=ab|上下边动量不变，较高动量的顶边移动得更多；斜边是随流物质边界，面积应沿斜边围成的区域计算。
16|phase_sector|\rho=F(H)\Rightarrow\{\rho,H\}=0|C=\beta\omega/(2\pi)|完整能量壳上的指数分布对转动不变，单个象限的初区则随轨道旋转，沿流密度仍保持。
17|standing_mode|T=\rho_llA^2\omega_n^2\sin^2\omega_nt/4|E=\rho_llA^2\omega_n^2/4|定端正弦振型的平方空间积分为 $l/2$；动能与势能的时间互补使总能量保持不变。
18|60|Q=\int_\Omega j^0\dd V|\dot Q=-\oint_{\partial\Omega}\vect j\cdot\vect n\dd S|边界外法向规定正出流，区域内总荷的减少量恰等于净流出量；局部无源并不关闭边界。
19|equator|\theta=\pi/2,\quad\phi=\phi_0+\Omega t|\vect r=R(\cos\phi,\sin\phi,0)|赤道是过球心平面的截线，速度沿其切向；极点处方位角不唯一与真实运动奇异是不同问题。
20|wkb|Q_{\rm quantum}\sim\hbar^2/(2ml_A^2)|Q_{\rm quantum}/T\sim(\hbar/(pl_A))^2|振幅包络和快速变化相位有不同空间尺度；波长远短于包络尺度时，量子势才可相对经典动能忽略。
'''
training=parse_rows(TRAIN)
assert len(training)==20
