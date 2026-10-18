T={
1:r'''\Step{把惯性矢量投影到动系}
动系转角为 $\Omega t$，初始轴重合，故
\[
\vect e_X=\cos\Omega t\,\vect e_1-\sin\Omega t\,\vect e_2,
\quad G_1=G\cos\Omega t,\quad G_2=-G\sin\Omega t.
\]
虽然矢量在空间中固定，两个动系分量仍随时间改变。
\Step{只对动系分量求导}
\[
\left(\frac{\dd\vect G}{\dd t}\right)_{S'}
=-G\Omega\sin\Omega t\,\vect e_1-G\Omega\cos\Omega t\,\vect e_2.
\]
该式是矢量表达式，不能再把基矢按惯性系规则求导，否则就把两种导数混用。
\Step{补上运输项并核验}
利用 $\vect e_z\times\vect e_1=\vect e_2$、$\vect e_z\times\vect e_2=-\vect e_1$，
\[
\Om\times\vect G=G\Omega\sin\Omega t\,\vect e_1+G\Omega\cos\Omega t\,\vect e_2.
\]
两式相加严格为零，恢复惯性系中的恒定矢量。$t=0$ 时动系导数为 $-G\Omega\vect e_2$，也与固定矢量相对框架反向转动的直观一致。''',
2:r'''\Step{先算相对运动}
取 $\er$ 从共同原点指向粒子，$\et=\vect e_z\times\er$。相对角速率为有符号常数 $\nu$，所以
\[
\vect v'=a\nu\et,\qquad \vect a'=-a\nu^2\er.
\]
盘的牵连速度为 $a\Omega\et$，绝对速度为 $\vect v=a(\Omega+\nu)\et$。
\Step{逐项合成加速度}
恒定转速使欧拉项为零。向轴项为 $-a\Omega^2\er$，科氏项为
\[
2\Om\times\vect v'=2\Omega\vect e_z\times a\nu\et=-2a\Omega\nu\er.
\]
故
\[
\vect a=-a(\nu^2+2\Omega\nu+\Omega^2)\er
=-a(\Omega+\nu)^2\er.
\]
\Step{检查两个特殊情形}
$\nu=0$ 时粒子固定于盘，得到通常的盘上点速度与向心加速度；$\nu=-\Omega$ 时合成角速率为零，绝对速度、加速度均为零。反向运动时 $\Omega\nu$ 可为负，科氏项可以向外，不能把所有项都事先写成向心方向。''',
3:r'''\Step{确定这一瞬间的相对量}
$x=a+ut$ 给出 $\dot x=u$、$\ddot x=0$。在 $t=0$，$\vect e_1=\vect E_X$、$\vect e_2=\vect E_Y$，位置为 $a\vect E_X$，角速度为 $\Omega\vect e_z$。原点加速度是另一个独立已知量 $A\vect E_X$。
\Step{把完整加速度变换逐项代入}
\[
\vect a=\vect a_O+\vect a'+\dot\Om\times\vect r
+\Om\times(\Om\times\vect r)+2\Om\times\vect v'.
\]
相对项与欧拉项为零；向轴项为 $-\Omega^2a\vect E_X$，科氏项为 $2\Omega u\vect E_Y$，因此
\[
\vect a(0)=(A-\Omega^2a)\vect E_X+2\Omega u\vect E_Y.
\]
\Step{检查遗漏项与极限}
若 $A=0$，结果退化为固定原点旋转管；若 $\Omega=0$，则只有原点加速度 $A\vect E_X$。如果只使用共固定原点的公式，就会少算真实的 $A\vect E_X$；相对匀速也不代表绝对加速度为零。此刻维持所给运动的真实合力就是 $m\vect a(0)$。''',
4:r'''\Step{用两个正交速度分量建立约束}
沿管相对速度是 $\dot r\er$，框架牵连速度是 $\Omega r\et$。恒绝对速率意味着
\[
\dot r^2+\Omega^2r^2=c^2.
\]
最初向外，因此 $\dot r=+\sqrt{c^2-\Omega^2r^2}$。根号非负已经要求 $r\le c/\Omega$。
\Step{积分确定到达极限位置的时间}
从 $r(0)=0$ 出发，
\[
\int_0^r\frac{\dd q}{\sqrt{c^2-\Omega^2q^2}}=t,
\quad r=\frac c\Omega\sin\Omega t,\quad\dot r=c\cos\Omega t.
\]
首次 $\dot r=0$ 对应 $\Omega t_*=\pi/2$，所以
\[
r_{\max}=\frac c\Omega,\qquad t_* =\frac\pi{2\Omega}.
\]
\Step{解释“能走多久”的含义}
这里是首个向外阶段的持续时间，不能宣称整个运动必在此停止。到达 $r_{\max}$ 时径向相对速度为零，但绝对速度仍有切向分量 $\Omega r_{\max}=c$。若随后继续满足恒绝对速率，必须另选回程分支或规定其他控制方式。''',
5:r'''\Step{在惯性系中分析真实受力}
保持相对盘静止时，物体随盘作半径 $a$ 的匀速圆周运动，需要向心加速度 $\Omega^2a$。竖直平衡给出 $N=mg$；水平唯一真实力为静摩擦力，所以
\[
\vect f=-m\Omega^2a\er,\qquad f=m\Omega^2a.
\]
向心力在这里就是静摩擦力的作用，不应再额外列一份“向心力”。
\Step{应用静摩擦上限}
所需摩擦力不能超过 $\mu_sN$，因此
\[
m\Omega^2a\le\mu_smg,
\quad |\Omega|\le\sqrt{\frac{\mu_sg}{a}}.
\]
若把角速率取非负，则最大值为 $\Omega_{\max}=\sqrt{\mu_sg/a}$。
\Step{解释临界状态与参数依赖}
等号表示即将滑动，并非所有较低转速时摩擦力都已达到 $\mu_smg$。质量在不等式中约去，理想条件下临界转速与质量无关；距轴越远，允许转速越低。该公式针对匀速盘，若盘还在加速，须把切向摩擦需求一并计入。''',
6:r'''\Step{先求珠子的相对运动}
沿管没有真实力，动系沿管方程为 $\ddot x=\Omega^2x$。通解为 $C\cosh\Omega t+D\sinh\Omega t$，初条件 $x(0)=a,\dot x(0)=0$ 给出
\[
x=a\cosh\Omega t,\qquad \dot x=a\Omega\sinh\Omega t.
\]
在 $a>0,t>0$ 时位置单调增大，因此首次到端点的时间是唯一的。
\Step{使用端点条件反求时间}
令 $x(t_L)=L$，得到 $\cosh\Omega t_L=L/a>1$，所以
\[
t_L=\frac1\Omega\operatorname{arcosh}\frac La
=\frac1\Omega\ln\left(\frac La+\sqrt{\frac{L^2}{a^2}-1}\right).
\]
\Step{把到端点的速度代入侧压力}
用 $\sinh^2q=\cosh^2q-1$，
\[
\dot x(t_L)=\Omega\sqrt{L^2-a^2},\qquad
|N_2(t_L)|=2m\Omega^2\sqrt{L^2-a^2}.
\]
竖直支持力仍为 $mg$，它与横向反力正交。若求总接触力，应合成为 $m\sqrt{g^2+4\Omega^4(L^2-a^2)}$。这个运动解到珠子到达端部为止，端部碰撞后的运动需要另外建模。''',
7:r'''\Step{求有效恢复系数为零的转速}
两弹簧真实合力为 $-2kx$，动系方程为 $m\ddot x=-2kx+m\Omega^2x$。因此
\[
\Omega_c=\sqrt{\frac{2k}{m}}.
\]
临界时方程退化为 $\ddot x=0$，结合任意初值得到 $x=x_0+u_0t$。除 $u_0=0$ 外，这是匀速漂移，不是周期振动。
\Step{对超临界情形完整求解}
若 $\Omega>\Omega_c$，令 $\gamma=\sqrt{\Omega^2-2k/m}>0$，解为
\[
x=x_0\cosh\gamma t+\frac{u_0}{\gamma}\sinh\gamma t
=C_+e^{\gamma t}+C_-e^{-\gamma t},
\]
其中 $C_+=(x_0+u_0/\gamma)/2$、$C_-=(x_0-u_0/\gamma)/2$。
\Step{把精确零解与稳定性分开}
$x_0=u_0=0$ 给出 $C_+=C_-=0$，故 $x(t)\equiv0$，不会自发产生运动。但任意小扰动通常有 $C_+\ne0$，随后指数增长，因此零平衡不稳定。特殊初值 $u_0=-\gamma x_0$ 消去增长模态，只余衰减轨迹；一条特殊轨迹不改变平衡的稳定性结论。''',
8:r'''\Step{分别写清两系速度}
取 $\vect e_1$ 沿管、$\vect e_2=\vect e_z\times\vect e_1$。珠子相对速度为 $\vect v'=\dot x\vect e_1$，绝对速度为
\[
\vect v=\dot x\vect e_1+\Omega x\vect e_2.
\]
管的横向真实反力为 $\vect N_2=2m\Omega\dot x\vect e_2$。
\Step{由力与各系速度的点积求功率}
\[
P'=\vect N_2\cdot\vect v'=0,
\]
因为反力始终垂直相对运动。惯性系中多出的切向速度与反力同向或反向，故
\[
P=\vect N_2\cdot\vect v=2m\Omega^2x\dot x.
\]
当 $x\dot x>0$ 时约束输入惯性能量，反之可取走能量。
\Step{用转矩功率独立核验}
关于竖轴的力矩为 $\tau_z=xN_2=2m\Omega x\dot x$，所以
\[
\Omega\tau_z=2m\Omega^2x\dot x=P.
\]
光滑约束不做相对功，并不保证在惯性系也不做功；两系使用的速度不同，功率必须相应区分。''',
9:r'''\Step{由切向方程保留所有平衡分支}
摆在随框架转动的竖直平面内运动，方程为
\[
\ddot\theta=F(\theta)=\sin\theta\left(\Omega^2\cos\theta-\frac gl\right).
\]
下半平面的平衡包括 $\theta_0=0$，以及 $\cos\theta_0=g/(\Omega^2l)$；后者只在 $\Omega^2>g/l$ 时有非零解。使用有符号角度时两侧分别为 $\pm\theta_0$。
\Step{线性化竖直分支}
令 $\theta=\eta$，保留小量一阶，得
\[
\ddot\eta+\left(\frac gl-\Omega^2\right)\eta=0.
\]
低于临界时系数为正，为稳定小振动；高于临界时系数为负，存在指数增长扰动，因而不稳定。
\Step{在线性化中使用倾斜平衡条件}
一般有 $F'(\theta)=\Omega^2\cos2\theta-(g/l)\cos\theta$。代入 $g/l=\Omega^2\cos\theta_0$，
\[
F'(\theta_0)=-\Omega^2\sin^2\theta_0,
\qquad\ddot\eta+\Omega^2\sin^2\theta_0\eta=0.
\]
两个倾斜分支均在该平面自由度下稳定，频率为 $\Omega|\sin\theta_0|$。临界点线性频率为零，必须继续看高阶势能，不能由零频率直接判作不稳定。''',
10:r'''\Step{从偏置几何列平衡方程}
平衡时距轴距离为 $a+l\sin\varphi_0$。水平、竖直平衡分别为
\[
T\sin\varphi_0=m\Omega^2(a+l\sin\varphi_0),\qquad T\cos\varphi_0=mg.
\]
消去 $T$，代入给定角度与长度，
\[
\Omega^2=\frac{g\tan\varphi_0}{a+l\sin\varphi_0}
=\frac{9.81/\sqrt3}{0.20+0.50\times0.50}
\approx12.586\,\mathrm{s^{-2}},
\quad\Omega\approx3.548\,\mathrm{s^{-1}}.
\]
\Step{对规定平面内的方程线性化}
其角度方程是
\[
\ddot\varphi=F(\varphi)=\Omega^2\left(\frac al+\sin\varphi\right)\cos\varphi-\frac gl\sin\varphi.
\]
令 $\varphi=\varphi_0+\eta$，则 $\ddot\eta=F'(\varphi_0)\eta$。使用平衡条件化简可得
\[
-F'(\varphi_0)=\Omega^2\left(\sin^2\varphi_0+\frac{a}{l\sin\varphi_0}\right).
\]
括号为正，故该平面内稳定。
\Step{代入数值并区分角频率与周期}
\[
\omega_\varphi^2=12.586\left(0.25+\frac{0.20}{0.50\times0.50}\right)
=12.586\times1.05,
\]
\[
\omega_\varphi\approx3.635\,\mathrm{s^{-1}},\qquad T_\varphi=\frac{2\pi}{\omega_\varphi}\approx1.728\,\mathrm s.
\]
张力同时为 $T=mg/\cos30^\circ$。这些频率针对题设限制的径向竖直平面；若放开方位自由度，须求耦合振动，不能直接沿用这个单自由度结果。''',
11:r'''\Step{对杆的质量分布求积分}
取沿杆坐标 $s$，$\dd m=(M/L)\dd s$。绕铰点的转动惯量为 $I=\int_0^Ls^2\dd m=ML^2/3$。重力矩与离心力矩为
\[
\tau_g=-g\sin\varphi\int_0^Ls\dd m=-\frac{MgL}{2}\sin\varphi,
\]
\[
\tau_{\rm cf}=\Omega^2\sin\varphi\cos\varphi\int_0^Ls^2\dd m
=\frac{M\Omega^2L^2}{3}\sin\varphi\cos\varphi.
\]
\Step{由角动量方程求平衡分支}
由 $I\ddot\varphi=\tau_g+\tau_{\rm cf}$，
\[
\ddot\varphi=\sin\varphi\left(\Omega^2\cos\varphi-\frac{3g}{2L}\right).
\]
非竖直平衡满足 $\cos\varphi_0=3g/(2L\Omega^2)$，故临界角速率为 $\Omega_c=\sqrt{3g/(2L)}$，严格高于临界才有非零倾角。
\Step{判定稳定性并说明质量分布的作用}
将右侧在 $\varphi_0$ 附近求导，并利用平衡条件，得到
\[
\ddot\eta+\Omega^2\sin^2\varphi_0\eta=0,
\quad\omega_\varphi=\Omega|\sin\varphi_0|.
\]
频率平方为正，倾斜分支稳定。若把质量全放到杆端，会得到临界值 $\sqrt{g/L}$；均匀杆的重力矩含一阶质量矩，而惯量与离心力矩含二阶质量矩，两者比值不同，所以不能直接使用杆端质点公式。''',
12:r'''\Step{在临界转速下展开有效势}
轴上旋转摆的有效势为
\[
U_{\rm eff}=mgl(1-\cos\theta)-\frac12m\Omega^2l^2\sin^2\theta.
\]
在 $\Omega^2=g/l$ 时，使用 $1-\cos\theta=\theta^2/2-\theta^4/24+O(\theta^6)$ 与 $\sin^2\theta=\theta^2-\theta^4/3+O(\theta^6)$，得到
\[
U_{\rm eff}=\frac18mgl\theta^4+O(\theta^6).
\]
二次项恰好抵消，但首个非零四次项为正。
\Step{由能量极小判断稳定性}
$\theta=0$ 仍是局部严格势能极小。理想单自由度系统的能量 $ml^2\dot\theta^2/2+U_{\rm eff}$ 守恒，足够小的初始能量限制位移保持在平衡附近，因此是稳定平衡，尽管不具有非零的线性回复频率。
\Step{写出领先非线性运动}
由 $ml^2\ddot\theta=-\partial U_{\rm eff}/\partial\theta$，
\[
\ddot\theta+\frac{g}{2l}\theta^3=0
\]
为领先方程。若最大角振幅为 $A$，能量关系给出 $\dot\theta^2\simeq[g/(4l)](A^4-\theta^4)$，故周期随 $1/A$ 增长，而不是固定的线性简谐周期。零线性频率只表示线性判据失效，不能等同于指数失稳。''',
13:r'''\Step{先将离心加速度分解到当地基矢}
纬度 $\lambda$ 处到地轴的距离为 $R\cos\lambda$。向轴外的柱坐标基矢满足 $\vect e_\rho=\cos\lambda\vect e_U-\sin\lambda\vect e_N$，所以
\[
\vect a_{\rm cf}=\Omega_E^2R\cos\lambda\,\vect e_\rho
=\Omega_E^2R\cos^2\lambda\vect e_U-\Omega_E^2R\sin\lambda\cos\lambda\vect e_N.
\]
\Step{叠加纯引力得到有效重力}
\[
g_N=-\Omega_E^2R\sin\lambda\cos\lambda,\qquad
g_U=-g_0+\Omega_E^2R\cos^2\lambda.
\]
在北半球 $g_N<0$，指向南；在南半球 $g_N>0$，指向北，均朝向赤道。赤道和极点的水平分量为零。
\Step{由分量比求铅垂偏角}
在实际地球的 $g_0>\Omega_E^2R$ 条件下，向下分量为 $-g_U>0$。偏角大小满足
\[
\tan|\delta|=\frac{\Omega_E^2R|\sin\lambda\cos\lambda|}
{g_0-\Omega_E^2R\cos^2\lambda}.
\]
因此有效重力通常不沿地心径向。若只保留离心修正的首阶，$|\delta|\simeq\Omega_E^2R|\sin\lambda\cos\lambda|/g_0$，重力大小的减少约为 $\Omega_E^2R\cos^2\lambda$。''',
14:r'''\Step{给东、西两种运动分别赋有符号速度}
东行取 $u=+U$，西行取 $u=-U$。球形模型中
\[
\frac{N_U(u)}m=g_0-\Omega_E^2R\cos^2\lambda-2\Omega_Eu\cos\lambda-\frac{u^2}{R}.
\]
两个方向的静止离心项、重力项和曲率项都相同，只有关于 $u$ 的线性项改变符号。
\Step{相减时保留符号}
\begin{align*}
\frac{N_{\rm west}-N_{\rm east}}m
&=2\Omega_EU\cos\lambda-(-2\Omega_EU\cos\lambda)\\
&=4\Omega_EU\cos\lambda.
\end{align*}
故西行支持力较大。这不是两车质量发生变化，而是维持各自惯性轨迹所需的支持力不同。
\Step{逐项代入数值}
\[
\Delta N=4\times1000\times7.292115\times10^{-5}\times30\times\cos45^\circ
\approx6.19\,\mathrm N.
\]
这个差值仅约为 $1000\,\mathrm{kg}$ 车辆重力的万分之六。赤道处差值最大；接近极点时因纬线半径趋零，保持非零速率的题设本身也须重新审视。''',
15:r'''\Step{解水平速度方程}
无水平真实力且 $f$ 恒定时，$\dot u=fv$、$\dot v=-fu$。对第一式再求导得 $\ddot u+f^2u=0$。由 $u(0)=U,v(0)=0$，
\[
u(t)=U\cos ft,\qquad v(t)=-U\sin ft.
\]
初始向东后立即出现南向速度，已经可以判断轨迹向右弯。
\Step{用初位置为零积分位置}
\[
x(t)=\frac Uf\sin ft,\qquad y(t)=\frac Uf(\cos ft-1).
\]
移项平方相加，得到
\[
x^2+\left(y+\frac Uf\right)^2=\left(\frac Uf\right)^2.
\]
所以圆心为 $(0,-U/f)$，半径为 $U/f$，从北侧顶点出发向东运动，俯视为顺时针。
\Step{求最大南向位移而非只读半径}
$\cos ft$ 的最小值为 $-1$，在 $t=\pi/f$ 首次达到。因此 $y_{\min}=-2U/f$，最大南向位移大小是 $2U/f$，是圆直径而不是半径。一个完整周期 $2\pi/f$ 后，位置与速度都回到初值。''',
16:r'''\Step{先写忽略曲率的地转平衡}
在半径 $r$ 处取向外为径向正向，逆时针为切向正向。压强梯度力向内，为 $-p_r/\rho$；若 $V>0$，科氏惯性力向外，为 $+fV$。忽略径向加速度时
\[
0=-\frac{p_r}{\rho}+fV,\qquad V_g=\frac{p_r}{\rho f}>0.
\]
故北半球低压的通常地转流为逆时针。
\Step{保留流线曲率建立梯度风方程}
沿圆形流线作稳态运动时，径向加速度为 $-V^2/r$，于是
\[
-\frac{V^2}{r}=-\frac{p_r}{\rho}+fV,
\qquad\frac{V^2}{r}+fV=\frac{p_r}{\rho}.
\]
这不是简单的力相互抵消，而是合力提供所需向心加速度。
\Step{解二次方程并选择通常气旋分支}
\[
V=\frac{-fr+\sqrt{f^2r^2+4rp_r/\rho}}2>0.
\]
选择正号，是因为该支在弱压强梯度下连续趋近地转解。将根号按小参数展开，$V\simeq p_r/(\rho f)$，与前式一致。另一负根并不属于这个通常的弱梯度气旋分支，不能不加讨论就当成同一解。

本题有真实压强梯度力；前题惯性圆没有这项力，所以两题旋向不同，不能只凭“北半球”就套用同一个圆流方向。''',
17:r'''\Step{求零阶落地时间和自转投影}
零阶下落满足 $h-gt_0^2/2=0$，因此
\[
t_0=\sqrt{\frac{2\times50}{9.81}}\approx3.193\,\mathrm s,
\quad c=\Omega_E\cos30^\circ\approx6.315\times10^{-5}\,\mathrm{s^{-1}}.
\]
\Step{从科氏加速度积分到位移}
零阶竖直速度为 $-gt$，所以 $\ddot x=2cgt$。两次积分，并使用初始东西速度和位移为零，得到
\[
\dot x=cgt^2,\qquad x=\frac13cgt^3.
\]
代入落地时间，
\[
d_E=\frac{6.315\times10^{-5}\times9.81\times3.193^3}{3}
\approx0.00672\,\mathrm m=6.72\,\mathrm{mm}.
\]
\Step{交代另外两个方向的精度}
零阶水平速度为零，北向科氏项的一阶驱动也为零，所以本阶 $y=0$；竖直一阶修正同样为零，时间无需作一阶修正。这个结论仅到所保留的精度，不能表述为任意阶下都没有南北偏移。正的东西位移表示偏东，与下落质点向东领先地面的几何解释一致。''',
18:r'''\Step{保留整个飞行阶段的竖直速度}
零阶 $\dot z=w_0-gt$，返回原高度的时间 $T_0=2w_0/g$。令 $c=\Omega_E\cos\lambda$，则
\[
\ddot x=-2c(w_0-gt).
\]
上升时加速度向西，下降时向东；加速度变号本身不能决定净位移是否为零。
\Step{使用初条件分别积分}
由 $x(0)=\dot x(0)=0$，
\[
\dot x=-2cw_0t+cgt^2=cgt(t-T_0),
\quad x=-cw_0t^2+\frac13cgt^3.
\]
因此
\[
\dot x(T_0)=0,\qquad x(T_0)=-\frac{4cw_0^3}{3g^2}.
\]
在非极点处 $c>0$，返回时位置在初始点西侧。
\Step{用速度符号解释积分结果}
对于 $0<t<T_0$，$t-T_0<0$，故 $\dot x$ 始终向西。下降段向东的加速度只是把西向速度逐渐减为零，未使其变成足以返回的东向速度。最终速度相同并不意味着位置相同，二者对应不同次数的时间积分。''',
19:r'''\Step{明确零阶轨迹与速度}
初始仅有北向速度 $v_0$，故 $x^{(0)}=0,y^{(0)}=v_0t,z^{(0)}=h-gt^2/2$。令 $c=\Omega_E\cos\lambda$、$\sigma=\Omega_E\sin\lambda$。把零阶速度代入东西向科氏项，
\[
\ddot x^{(1)}=2\sigma v_0+2cgt.
\]
第一项来自北向运动，第二项来自下落，两者须分别积分。
\Step{积分并处理落地时间}
初始东西速度为零，得到
\[
x^{(1)}=\sigma v_0t^2+\frac13cgt^3.
\]
北向与竖直的一阶驱动都依赖零阶东西速度，而该速度为零，因此本阶 $y=v_0t$、$z=h-gt^2/2$，落地时间没有一阶修正：$T=T_0=\sqrt{2h/g}$。
\Step{写出落点并分析方向}
\[
x_{\rm land}=\sigma v_0T_0^2+\frac13cgT_0^3,
\qquad y_{\rm land}=v_0T_0,\qquad z_{\rm land}=0.
\]
北半球 $\sigma>0,c\ge0$，两项均向东；南半球 $\sigma<0$，北行偏转项向西，下落项仍向东，净偏移由两者大小决定。若 $v_0=0$，结果自然退化为相对静止释放的落体东偏。''',
20:r'''\Step{先由竖直科氏项求时间变化}
东向初速度 $u_0$ 使竖直加速度出现 $+2cu_0$，所以到一阶
\[
z(t)=h-\frac12gt^2+cu_0t^2.
\]
令落地时间为 $T_0+\delta T$，并用 $h-gT_0^2/2=0$，则
\[
0=-gT_0\delta T+cu_0T_0^2,
\quad\delta T=\frac{cu_0T_0}{g}.
\]
\Step{同时展开东向轨迹的终点}
东西向轨迹为 $x(t)=u_0t+cgt^3/3$，因此
\[
x_{\rm land}=u_0T_0+u_0\delta T+\frac13cgT_0^3+O(\Omega_E^2).
\]
其中 $u_0\delta T=cu_0^2T_0/g$ 与 $cgT_0^3/3$ 都是一阶项。不能在已经修正轨迹后，仍用未修正的时间去计算全部射程。
\Step{比较两个贡献的大小}
\[
\frac{u_0\delta T}{cgT_0^3/3}=\frac{3u_0^2}{g^2T_0^2}=\frac{3u_0^2}{2gh}.
\]
当水平初速度较大时，时间修正的贡献甚至更大。只有另有明确的小参数估计，才可在指定误差范围内忽略它；仅因为 $\delta T$ 很小并不足够。''',
21:r'''\Step{由初位置确定第一个复常数}
令 $t=0$，通解给出 $\zeta(0)=A$。初始点为 $x=a,y=0$，所以 $A=a$，是实数。初位置并没有同时决定另一个复常数。
\Step{完整求导后使用静止释放条件}
\begin{align*}
\dot\zeta=e^{-\mathrm i\sigma t}\bigl[&-\mathrm i\sigma(A\cos\kappa t+B\sin\kappa t)\\
&-\kappa A\sin\kappa t+\kappa B\cos\kappa t\bigr].
\end{align*}
$t=0$ 时，$\dot\zeta(0)=-\mathrm i\sigma A+\kappa B$。静止释放要求这个复数的实部和虚部都为零，因此
\[
B=\mathrm i\frac{\sigma a}{\kappa}.
\]
\Step{核验并识别省略项造成的初值改变}
代回有 $-\mathrm i\sigma a+\kappa(\mathrm i\sigma a/\kappa)=0$，故两个初速度分量同时满足题设。若省去正弦项，即令 $B=0$，会得到 $\dot\zeta(0)=-\mathrm i\sigma a$，相当于初始南北速度 $\dot y(0)=-\sigma a$。小系数可以在某些观测精度下近似，但不能在声称满足精确初条件时删去。''',
22:r'''\Step{分别确定两种运动的角速率}
傅科摆的慢转因子是 $e^{-\mathrm i\sigma t}$，$\sigma=\Omega_E\sin\lambda$，主轴慢进动角速率为 $-\sigma$。惯性圆的速度满足 $\dot u=fv,\dot v=-fu$，其旋转角速率为 $-f=-2\sigma$。
\Step{把恒星日换成周期公式}
由 $\Omega_E=2\pi/D$，
\[
T_P=\frac D{|\sin\lambda|},\qquad T_I=\frac D{2|\sin\lambda|}.
\]
在北纬 $60^\circ$，$\sin60^\circ=\sqrt3/2$，所以
\[
T_P=\frac{23.9345}{\sqrt3/2}\approx27.64\,\mathrm h,
\quad T_I\approx13.82\,\mathrm h.
\]
两者从当地上方俯视都为顺时针。
\Step{解释两倍关系而不混用周期含义}
科氏方程含 $2\sigma$，自由水平速度矢量以此角速率旋转；对傅科摆作 $\zeta=e^{-\mathrm i\sigma t}w$ 变换后，快振动的主轴只以 $\sigma$ 慢转。因此 $T_P=2T_I$，并非把两个公式写成同一个“科氏周期”。无向主轴转 $180^\circ$ 后也重合，但题设进动周期按 $360^\circ$ 约定，不能据此再除以二。''',
23:r'''\Step{先求真实势与有效势}
两根弹簧的形变量大小都为 $|x|$，总势能为 $U=2(kx^2/2)=kx^2$。转速恒定时，离心势为 $-m\Omega^2x^2/2$，所以
\[
J=\frac12m\dot x^2+kx^2-\frac12m\Omega^2x^2.
\]
\Step{用运动方程直接检验守恒}
对时间求导并提取 $\dot x$，
\[
\dot J=\dot x\bigl[m\ddot x+(2k-m\Omega^2)x\bigr]=0.
\]
最后一个等号使用了题给运动方程，而不是只凭“科氏力不做功”得出。
\Step{另算惯性机械能变化率}
惯性速度包含径向 $\dot x$ 和切向 $\Omega x$，故
\[
E=\frac12m(\dot x^2+\Omega^2x^2)+kx^2.
\]
代入 $m\ddot x=(m\Omega^2-2k)x$，
\[
\dot E=m\dot x\ddot x+(m\Omega^2+2k)x\dot x
=2m\Omega^2x\dot x.
\]
\Step{用角动量与约束功率解释}
$L_z=m\Omega x^2$，所以 $\Omega\dot L_z=2m\Omega^2x\dot x=\dot E$，也等于侧壁反力 $N_2=2m\Omega\dot x$ 的功率 $N_2\Omega x$。电机可以输入或取回惯性能量，而 $E-\Omega L_z=J$ 保持不变。有效势系数可以为负，因此雅可比量守恒本身也不保证圆心稳定。''',
24:r'''\Step{把惯性静态势写成动系坐标}
两系初始轴重合，坐标关系为 $X=x\cos\Omega t-y\sin\Omega t$。因此
\[
U'(x,y,t)=-F_0(x\cos\Omega t-y\sin\Omega t).
\]
即使惯性系势 $U=-F_0X$ 不显含时间，旋转坐标中固定的同一位置也会扫过不同的 $X$，所以 $U'$ 一般显含时间。
\Step{计算固定动系位置时的偏导数}
保持 $x,y$ 不变求偏导，
\[
\frac{\partial U'}{\partial t}=F_0\Omega(x\sin\Omega t+y\cos\Omega t).
\]
在固定原点、恒定转速且没有其他相对功率的条件下，$\dot J=\partial U'/\partial t$，故本例通常不为零。这里是偏导数，不能把 $x(t),y(t)$ 的时间导数再加入一次。
\Step{用惯性系的能量和力矩核验}
若质点仅受该均匀保守力，惯性机械能 $E$ 守恒；关于竖轴的真实力矩为 $\dot L_z=-F_0Y$，而 $Y=x\sin\Omega t+y\cos\Omega t$。由 $J=E-\Omega L_z$ 得
\[
\dot J=-\Omega\dot L_z=F_0\Omega Y,
\]
与上一偏导数完全相同。
\Step{归纳可以使用守恒量的条件}
需要的是势在所选动系中静态，同时其他真实力和约束不做相对功。绕该轴对称的惯性静态势满足 $U(Q(t)\vect r)=U(\vect r)$，可消去显式时间；固定方向的均匀水平力不满足这种轴对称性。因此“力保守”与“动系雅可比量守恒”不是同一条件。'''
}
