E={
15:r'''\Step{分别说明两个框架如何运动}
进动框架只跟着含竖轴与 $\vect n$ 的平面转动，其角速度为 $\Om_f=\Omega_p\vect e_Z$。材料相对该框架还绕 $\vect n$ 转动，角速度为 $\omega_s\vect n$。因此完全随体框架的总角速度为
\[
\vect\omega_B=\Omega_p\vect e_Z+\omega_s\vect n.
\]
这是矢量相加，不能把两角速率的模直接相加；具体有
\[
\omega_B^2=\Omega_p^2+\omega_s^2+2\Omega_p\omega_s\cos\alpha.
\]
\Step{在进动框架中计算轴上点速度}
轴上点 $\vect r=h\vect n$ 的相对自转速度为
\[
\vect v'_f=\omega_s\vect n\times(h\vect n)=0.
\]
故其绝对速度为 $\vect v=\Omega_p\vect e_Z\times h\vect n$，速率为 $|\Omega_p|\,|h|\sin\alpha$。该点绕竖轴运动的半径正是 $|h|\sin\alpha$。
\Step{换到随体系核验并检查角加速度}
在完全随体系中 $\vect v'_B=0$，且
\[
\vect v=\vect\omega_B\times h\vect n
=\Omega_p\vect e_Z\times h\vect n,
\]
因为自转项的叉乘仍为零。这个结论只适用于轴上点，轴外材料点一般受自转影响。

若 $\Omega_p,\omega_s$ 的数值都恒定，轴向仍满足 $\dot{\vect n}=\Omega_p\vect e_Z\times\vect n$，所以
\[
\dot{\vect\omega}_B=\omega_s\Omega_p\vect e_Z\times\vect n.
\]
总角加速度可以非零；计算轴外点加速度时，不能因两个角速率恒定就删去欧拉加速度项。''',
23:r'''\Step{选取随框架转动的单自由度模型}
以向下竖直线为 $\theta=0$，向轴外倾斜为正。小球的距轴距离为 $\rho=l\sin\theta$。在动系中，重力竖直向下，离心力 $m\Omega^2l\sin\theta$ 水平向外，杆力沿杆；杆力在摆动切向没有分量。科氏力垂直摆动平面，在这一自由度上的投影也为零。
\Step{沿摆角增大的切向列式}
重力的投影为 $-mg\sin\theta$，离心力的投影为 $m\Omega^2l\sin\theta\cos\theta$，相对切向加速度为 $l\ddot\theta$，故
\begin{equation}
\ddot\theta=\sin\theta\left(\Omega^2\cos\theta-\frac gl\right).\label{eq:rotpend}
\end{equation}
令 $\ddot\theta=0$，应保留乘积为零的两类可能：竖直分支 $\theta_0=0$，以及
\[
\cos\theta_0=\frac{g}{\Omega^2l}.
\]
倾斜分支需要右侧不大于 $1$，因此临界角速率为 $\Omega_c=\sqrt{g/l}$；严格高于临界时出现非零倾角。若用有符号角度，两侧有 $\pm\theta_0$ 两个对称位置。
\Step{用真实受力求杆力}
相对平衡时，小球在惯性系中作水平圆周运动，竖直加速度为零。因此
\[
T\cos\theta_0=mg,\qquad T\sin\theta_0=m\Omega^2l\sin\theta_0.
\]
倾斜分支给出 $T=m\Omega^2l=mg/\cos\theta_0$；竖直分支直接给出 $T=mg$。必须先区分分支，不能直接除以 $\sin\theta_0$。
\Step{补充倒立位置的物理限制}
若杆可承压，还存在 $\theta_0=\pi$ 的向上倒立平衡。线性化得到扰动满足 $\ddot\eta=(\Omega^2+g/l)\eta$，因此始终不稳定。绳只能受拉，不能无条件把这个可承压刚杆分支算作绳摆的可实现平衡。''',
24:r'''\Step{先判断倾斜分支是否存在}
轴上悬点摆的临界角速率为
\[
\Omega_c=\sqrt{\frac gl}=\sqrt{\frac{9.80}{0.50}}
=4.427\,\mathrm{s^{-1}}.
\]
题设 $\Omega=6.0\,\mathrm{s^{-1}}>\Omega_c$，所以稳定倾斜分支存在。平衡条件给出
\[
\cos\theta_0=\frac{g}{\Omega^2l}=\frac{9.80}{36\times0.50}
=0.54444,\qquad \theta_0\approx57.01^\circ.
\]
\Step{从真实受力求单位质量杆力}
由 $T\cos\theta_0=mg$，
\[
\frac Tm=\frac{g}{\cos\theta_0}=\Omega^2l
=36\times0.50=18.0\,\mathrm{m/s^2}.
\]
$T/m$ 的单位是加速度，而 $T$ 本身的单位才是牛顿；题目未给小球质量，不影响求 $T/m$。
\Step{线性化而不是套用静止单摆周期}
令 $\theta=\theta_0+\eta$，运动方程右侧记为 $F(\theta)$。有
\[
F'(\theta)=\Omega^2\cos2\theta-\frac gl\cos\theta.
\]
使用平衡关系 $g/l=\Omega^2\cos\theta_0$，得 $F'(\theta_0)=-\Omega^2\sin^2\theta_0$，所以
\[
\ddot\eta+\omega_\eta^2\eta=0,\qquad
\omega_\eta=\Omega\sin\theta_0
=6\sqrt{1-0.54444^2}\approx5.033\,\mathrm{s^{-1}}.
\]
\[
T_\eta=\frac{2\pi}{\omega_\eta}\approx1.248\,\mathrm s.
\]
频率平方为正，确认该倾斜平衡在规定的摆动平面内稳定；这里的周期不是 $2\pi\sqrt{l/g}$。''',
25:r'''\Step{先确定真实的距轴距离}
悬点本身已经离轴 $a$，小球又向外偏出 $l\sin\varphi$，因此
\[
\rho=a+l\sin\varphi.
\]
框架匀速转动、小球相对静止，故没有科氏项或欧拉项；以转轴为原点时，离心力大小为 $m\Omega^2\rho$。
\Step{分别列水平和竖直平衡}
绳张力沿绳指向悬点，其水平分量向内、竖直分量向上。动系中的平衡为
\[
T\sin\varphi=m\Omega^2(a+l\sin\varphi),\qquad
T\cos\varphi=mg.
\]
第二式先给出 $T=mg/\cos\varphi$，再代入第一式消去张力，得到
\begin{equation}
g\tan\varphi=\Omega^2(a+l\sin\varphi),\qquad
T=\frac{mg}{\cos\varphi}.\label{eq:offsetpend}
\end{equation}
给定 $\Omega$ 时，第一式一般须数值求根，再用第二式求张力；不能擅自删去 $a$。
\Step{用极限核验建模}
$a=0$ 时回到轴上悬点摆的方程；而 $a>0,\Omega\ne0$ 时，代入 $\varphi=0$ 会使左侧为零、右侧为 $\Omega^2a>0$，所以竖直位置不再平衡。绳摆还要求 $T\ge0$，通常取 $0\le\varphi<\pi/2$ 的外倾分支。悬点随框架的圆周加速度已经包含在关于转轴的离心项内，不能再重复加入一份悬点平动惯性力。''',
27:r'''\Step{把液体看作在转动系中静止}
液体相对容器无速度，所以科氏力为零。每单位体积受重力 $-\rho g\vect e_z$ 和离心力 $\rho\Omega^2r\vect e_r$。静力平衡为
\[
\nabla p=\rho(\Omega^2r\vect e_r-g\vect e_z),
\quad p_r=\rho\Omega^2r,\quad p_z=-\rho g.
\]
离轴越远压强越高，位置越高压强越低。
\Step{沿同一自由表面使用等压条件}
自由表面气压相同，沿表面移动时 $\dd p=p_r\dd r+p_z\dd z=0$，因而
\[
\Omega^2r\dd r-g\dd z=0,\qquad
\frac{\dd z}{\dd r}=\frac{\Omega^2r}{g}.
\]
积分得到
\[
z(r)=z_0+\frac{\Omega^2r^2}{2g},
\]
绕轴旋转即为抛物面。正号说明液面在外侧升高。
\Step{用体积约束确定高度常数}
仅由局部平衡不能确定 $z_0$。例如容器半径为 $b$、静止液深为 $H$，且尚未露底或溢出，则体积守恒要求
\[
\pi b^2H=2\pi\int_0^b\left(z_0+\frac{\Omega^2r^2}{2g}\right)r\dd r,
\quad z_0=H-\frac{\Omega^2b^2}{4g}.
\]
若计算出的中心高度低于底面，就必须重新处理露底边界，不能继续把整个底面都当成被液体覆盖。$\Omega\to0$ 时恢复水平液面。''',
28:r'''\Step{沿管列动力学方程}
取随管转动的 $\vect e_1$ 沿管、$\vect e_2=\vect e_z\times\vect e_1$。重力与竖直支持力相互抵消；光滑管沿轴没有真实力。动系沿管方向只有离心力 $m\Omega^2x$，故 $\ddot x=\Omega^2x$。
\Step{解微分方程并代入两个初条件}
$\Omega\ne0$ 时通解可写为 $x=C\cosh\Omega t+D\sinh\Omega t$。由 $x(0)=a$ 得 $C=a$，由 $\dot x(0)=u_0$ 得 $D=u_0/\Omega$，所以
\begin{equation}
\ddot x=\Omega^2x,\qquad x=a\cosh\Omega t+\frac{u_0}{\Omega}\sinh\Omega t.
\label{eq:freebead}
\end{equation}
相对速度为 $\dot x=a\Omega\sinh\Omega t+u_0\cosh\Omega t$。若 $a>0,u_0=0$，珠子从相对静止开始向外加速，而非保持匀速。
\Step{用横向约束求真实反力}
珠子始终在管轴上，相对横坐标及其二阶导数为零，但绝对横向加速度不为零。加速度变换给出
\[
\vect a=(\ddot x-\Omega^2x)\vect e_1+2\Omega\dot x\vect e_2
=2\Omega\dot x\vect e_2.
\]
故管对珠子的横向、竖直反力为
\begin{equation}
N_2=2m\Omega\dot x,\qquad N_z=mg.\label{eq:beadreaction}
\end{equation}
压力大小为 $2m|\Omega\dot x|$，珠子对管的力与管对珠子的力方向相反。合成横向与竖直两项，总接触力大小为
\[
N_{\rm total}=m\sqrt{g^2+4\Omega^2\dot x^2}.
\]
\Step{检查极限与能量来源}
利用 $\sinh\Omega t\sim\Omega t$、$\cosh\Omega t\sim1$，$\Omega\to0$ 时有 $x\to a+u_0t$。非零转速时指数增长由维持管转速的驱动装置供能，并不违反能量守恒；有限长管的解只能使用到珠子抵达端部为止。''',
29:r'''\Step{把规定运动先转换成相对加速度}
题设 $x=a+ut$，$u>0$ 恒定，所以 $\dot x=u$、$\ddot x=0$。这项运动约束由控制装置实现，不能套用自由珠的 $\ddot x=\Omega^2x$。
\Step{由沿管牛顿方程反求控制力}
设真实控制力的有符号分量为 $F_1$，以沿管向外为正。动系方程为
\[
m\ddot x=F_1+m\Omega^2x.
\]
代入规定的 $\ddot x=0$，得到
\[
F_1(t)=-m\Omega^2(a+ut).
\]
在 $a+ut>0$ 的阶段，控制力必须向轴内，以抵消相对运动中的离心驱动。
\Step{求横向反力与相对功率}
横向反力仍需维持珠子随管转向，因此 $N_2=2m\Omega u$。控制力相对功率为
\[
P'_1=F_1\dot x=-m\Omega^2(a+ut)u<0.
\]
它在动系中取走能量，而侧壁在惯性系中可输入功率 $N_2\Omega x=2m\Omega^2xu$，两者净输入为 $m\Omega^2xu$。这正等于惯性动能 $m(u^2+\Omega^2x^2)/2$ 的增长率。没有沿管控制力的被动光滑管不能维持题设匀速外滑。''',
30:r'''\Step{先合成两根弹簧的真实恢复力}
滑块向正方向偏移 $x$ 时，一根弹簧拉伸、一根压缩，两者的力都指向圆心，故 $F_x=-kx-kx=-2kx$。在动系中再加离心力 $m\Omega^2x$，得到
\begin{equation}
\ddot x+\left(\frac{2k}{m}-\Omega^2\right)x=0.\label{eq:springs}
\end{equation}
令 $\Omega_c=\sqrt{2k/m}$。必须按系数的正、零、负分别求解。
\Step{低于临界时施加初条件}
若 $\omega_s=\sqrt{2k/m-\Omega^2}>0$，通解为 $A\cos\omega_st+B\sin\omega_st$。由初位置、初速度得
\[
x=x_0\cos\omega_st+\frac{u_0}{\omega_s}\sin\omega_st,
\quad T_s=\frac{2\pi}{\omega_s}.
\]
圆心是稳定平衡。转速上升使有效恢复系数减小，振动周期变长。
\Step{临界和超临界分别求解}
临界时 $\ddot x=0$，故 $x=x_0+u_0t$，一般为漂移而非周期振动。超临界时令 $\gamma=\sqrt{\Omega^2-2k/m}$，则
\[
x=x_0\cosh\gamma t+\frac{u_0}{\gamma}\sinh\gamma t
=\frac{x_0+u_0/\gamma}{2}e^{\gamma t}+\frac{x_0-u_0/\gamma}{2}e^{-\gamma t}.
\]
一般初值含增长模态，圆心不稳定；但 $x_0=u_0=0$ 的精确解始终为零。特别取 $u_0=-\gamma x_0$ 时仅余衰减模态，也不能据此把平衡判作稳定。
\Step{用横向方程求侧压力}
弹簧没有横向分量，槽壁必须提供绝对横向加速度 $2\Omega\dot x$，故槽对块的反力为 $N_2=2m\Omega\dot x$。块对槽壁的力反向，压力大小为 $2m|\Omega\dot x|$。各区间先对相应 $x(t)$ 求导再代入，反力的符号随相对速度改变。''',
31:r'''\Step{判断转速区间并求频率}
两根弹簧的合刚度为 $2k=10.0\,\mathrm{N/m}$，所以
\[
\frac{2k}{m}=\frac{10.0}{0.20}=50.0\,\mathrm{s^{-2}},\quad
\Omega^2=25.0\,\mathrm{s^{-2}}.
\]
因此处于稳定振动区间，$\omega_s=\sqrt{50-25}=5.0\,\mathrm{s^{-1}}$，周期 $T_s=2\pi/5\approx1.257\,\mathrm s$。
\Step{由释放条件确定振动解}
通解为 $x=A\cos5t+B\sin5t$。$x(0)=0.040\,\mathrm m$ 给出 $A=0.040\,\mathrm m$；$\dot x(0)=0$ 给出 $B=0$。于是
\[
x(t)=0.040\cos5t\,\mathrm m,\qquad
\dot x(t)=-0.200\sin5t\,\mathrm{m/s}.
\]
\Step{反求横向反力并求最大值}
由 $N_2=2m\Omega\dot x$，
\[
N_2=2\times0.20\times5.0\times(-0.200\sin5t)
=-0.400\sin5t\,\mathrm N.
\]
所以最大侧压力大小为 $0.400\,\mathrm N$。在位移转折点相对速度为零，侧压力为零；经过圆心时速率最大，侧压力也最大。若问块对槽壁的有向力，应把上述 $N_2$ 再取反。''',
32:r'''\Step{先利用惯性系中的简单运动}
无真实力时惯性速度恒定，故 $X=ut,Y=0$。动系相对惯性系转过 $\Omega t$，反向坐标变换为
\[
x=X\cos\Omega t+Y\sin\Omega t=ut\cos\Omega t,
\quad y=-X\sin\Omega t+Y\cos\Omega t=-ut\sin\Omega t.
\]
当 $t\ge0$，动系极坐标满足 $r=ut$、$\phi=-\Omega t$，即从原点向外顺时针展开的螺线。
\Step{计算导数以核验动力学}
\begin{align*}
\dot x&=u\cos\Omega t-u\Omega t\sin\Omega t,\\
\dot y&=-u\sin\Omega t-u\Omega t\cos\Omega t,\\
\ddot x&=-2u\Omega\sin\Omega t-u\Omega^2t\cos\Omega t,\\
\ddot y&=-2u\Omega\cos\Omega t+u\Omega^2t\sin\Omega t.
\end{align*}
无真实力时，动系方程为
\[
\ddot x=\Omega^2x+2\Omega\dot y,\qquad
\ddot y=\Omega^2y-2\Omega\dot x.
\]
将前两式代入右侧，正好分别得到所列的 $\ddot x,\ddot y$。
\Step{检查初条件与物理含义}
$t=0$ 时 $x=y=0$、$\dot x=u,\dot y=0$，符合两系初始轴重合。动系轨迹虽弯曲，惯性系仍是匀速直线；弯曲来自参考系转动，不需要真实力。''',
33:r'''\Step{先算统一的离心加速度尺度}
所有纬度共用 $\Omega_E^2R$。代入数值，
\[
\Omega_E^2R=(7.292115\times10^{-5})^2\times6.371\times10^6
\approx0.03388\,\mathrm{m/s^2}.
\]
它在赤道处全部沿天向，与重力反向，使有效重力减少 $0.03388\,\mathrm{m/s^2}$；极点到转轴距离为零，离心项为零。
\Step{在中纬度先投影再讨论大小}
纬度 $\lambda$ 处的离心加速度分量为
\[
a_{{\rm cf},N}=-\Omega_E^2R\sin\lambda\cos\lambda,
\quad a_{{\rm cf},U}=\Omega_E^2R\cos^2\lambda.
\]
在 $45^\circ$，它们分别约为 $-0.01694$ 和 $+0.01694\,\mathrm{m/s^2}$，水平分量指向赤道；总离心加速度大小为
\[
a_{\rm cf}=\Omega_E^2R\cos45^\circ\approx0.02396\,\mathrm{m/s^2}.
\]
不能把总量与竖直减少量混同。
\Step{计算铅垂偏角并作量级比较}
有效重力的向下分量为 $g_0-a_{{\rm cf},U}$，故偏角大小满足
\[
\tan\delta=\frac{0.01694}{9.81-0.01694},\qquad
\delta\approx0.0991^\circ.
\]
若相对速度垂直地轴，科氏加速度达到 $2\Omega_Eu$。令它与 $45^\circ$ 处总离心加速度相等，得
\[
u_*\simeq\frac{\Omega_ER\cos45^\circ}{2}\approx164\,\mathrm{m/s}.
\]
其他运动方向还须乘速度与地轴夹角的正弦；若只比较水平或竖直影响，则须分别投影。
\Step{明确球形模型的精度边界}
这些数值只比较同一球形引力场中的自转效应。真实地球的扁率也改变半径和引力场，不能据此精确预测赤道与极点的全部重力差。实验测得的静止重力通常已含离心修正，写局部方程时不可重复减去。

以地面点为原点的小区域内，引力梯度与离心梯度仍可能存在。只求一阶科氏效应时通常把有效重力当作常矢量；报告二阶修正时，须同时检查这些被舍去的项。''',
34:r'''\Step{先写出球形模型的预测}
若纯引力加速度 $g_0$ 不随纬度改变，极点没有离心修正，赤道的有效重力减少 $\Omega_E^2R$，因此
\[
\Delta g_{\rm sph}=g_{\rm pole}-g_{\rm eq}=\Omega_E^2R
\approx0.03388\,\mathrm{m/s^2}.
\]
这个差值来自同一球面上离心效应随纬度改变。
\Step{与题给实际差值作数值比较}
题给代表数值之差为
\[
\Delta g_{\rm given}=9.832-9.780=0.052\,\mathrm{m/s^2}.
\]
模型比该差值少约 $0.01812\,\mathrm{m/s^2}$，只解释了约 $0.03388/0.052\approx65.2\%$。
\Step{定位差异的模型来源}
球形模型中应计入的离心项已经完整使用，不能再增加一份离心力来凑足差值。真实地球的赤道半径与极半径不同，质量分布和非球形引力场也改变重力，因此纯引力部分本身就会随纬度变化。应升级几何和引力模型，而不是重复计算已包含的自转项。''',
35:r'''\Step{在惯性系中确定纬线运动的角速度}
纬线到地轴距离为 $\rho=R\cos\lambda$。物体相对地面东向速度为有符号量 $u$，因此惯性方位角速度是
\[
\omega_{\rm abs}=\Omega_E+\frac{u}{R\cos\lambda}.
\]
沿纬线的向心加速度指向地轴，其大小为 $\omega_{\rm abs}^2\rho$。
\Step{把向轴加速度投影到天向}
从地轴向外的柱坐标单位矢量满足 $\vect e_\rho=\cos\lambda\vect e_U-\sin\lambda\vect e_N$，故
\begin{align*}
a_U&=-\omega_{\rm abs}^2R\cos^2\lambda\\
&=-\Omega_E^2R\cos^2\lambda-2\Omega_Eu\cos\lambda-\frac{u^2}{R}.
\end{align*}
由径向牛顿方程 $N_U-mg_0=ma_U$，得到
\begin{equation}
\frac{N_U}{m}=g_0-\Omega_E^2R\cos^2\lambda-2\Omega_Eu\cos\lambda-\frac{u^2}{R}.
\label{eq:eotvos}
\end{equation}
\Step{逐项解释称重差}
静止离心修正与曲率项对同速东、西行驶相同。线性修正为
\[
\Delta(N_U/m)=-2\Omega_Eu\cos\lambda,
\]
它随方向反号，使东行减轻、西行加重。若以地面静止时的有效重力 $g$ 建立局部水平模型，并忽略曲率，便得到
\[
N/m=g-2\Omega_Eu\cos\lambda.
\]
此时不可再重复减去静止离心项。
\Step{说明水平引导与数量级}
同一向轴加速度还具有北向分量 $a_N=\omega_{\rm abs}^2R\sin\lambda\cos\lambda$，需要道路或轨道的水平引导力。因此 $N_U$ 只是总约束力的径向分量，未必等于总接触力大小。

例如取纬度 $45^\circ$，相对速率为 $200\,\mathrm{m/s}$。分别代入可得
\[
2\Omega_Eu\cos\lambda\approx0.02063\,\mathrm{m/s^2},\qquad
u^2/R\approx0.00628\,\mathrm{m/s^2}.
\]
这两项有不同的来源和近似阶次，必须先明确所用模型再比较。''',
36:r'''\Step{用运动旋向判断半球}
惯性圆的速度满足 $\dot u=fv$、$\dot v=-fu$，所以速度矢量以有符号角速率 $-f$ 转动。俯视逆时针意味着 $f<0$，即在南半球。先判断符号，再由周期求纬度大小。
\Step{从周期求科氏参数与纬度}
惯性圆周期为 $T_I=2\pi/|f|$，而 $f=2\Omega_E\sin\lambda$、$\Omega_E=2\pi/D$，故
\[
|\sin\lambda|=\frac{D}{2T_I}=\frac{23.9345}{28}\approx0.85480.
\]
结合南半球的负号，
\[
\lambda=-\arcsin0.85480\approx-58.738^\circ.
\]
另有 $|f|=2\pi/(14\times3600)\approx1.247\times10^{-4}\,\mathrm{s^{-1}}$。
\Step{用速率求半径并检查假设}
惯性圆的向心加速度为 $U^2/r_I$，科氏加速度为 $|f|U$，所以
\[
r_I=\frac U{|f|}=\frac{0.20}{1.247\times10^{-4}}
\approx1.60\times10^3\,\mathrm m=1.60\,\mathrm{km}.
\]
只有压强梯度、摩擦等水平作用可忽略时，才可这样反推纬度。一般海洋涡旋即使旋向和周期相同，也不一定属于惯性圆。''',
37:r'''\Step{从水平分量方程写地转平衡}
取东为 $x$、北为 $y$，水平动力学为
\[
\dot u=-\frac{p_x}{\rho}+fv,\qquad
\dot v=-\frac{p_y}{\rho}-fu.
\]
地转近似忽略加速度与摩擦，因此
\[
v_g=\frac{p_x}{\rho f},\qquad u_g=-\frac{p_y}{\rho f}.
\]
\Step{分别代入压强梯度}
$p_x=0$ 给出 $v_g=0$。向北压强增加意味着 $p_y>0$，所以
\[
u_g=-\frac{1.2\times10^{-3}}{1.2\times10^{-4}}
=-10\,\mathrm{m/s}.
\]
负号表示气流向西，速率为 $10\,\mathrm{m/s}$，沿东西向等压线流动。
\Step{用力的方向作独立检验}
压强梯度力为 $-(p_y/\rho)\vect e_N$，向南。西向速度代入科氏惯性力 $-mf\vect e_U\times(-10\vect e_E)$，方向向北，正好抵消。面向西时左侧为南方，因此低压在气流左侧，与北半球地转风规则一致。''',
38:r'''\Step{比较方程中两项的典型大小}
水平对流加速度尺度约为 $U^2/L$，科氏加速度尺度约为 $|f|U$，两者之比为
\[
\mathrm{Ro}=\frac{U^2/L}{|f|U}=\frac{U}{|f|L}.
\]
这个无量纲数可先判断地球自转是否足以主导旋向。
\Step{代入题设尺度}
\[
\frac{U^2}{L}=\frac{0.10^2}{0.10}=0.10\,\mathrm{m/s^2},
\quad |f|U=10^{-4}\times0.10=10^{-5}\,\mathrm{m/s^2},
\]
\[
\mathrm{Ro}=\frac{0.10}{10^{-4}\times0.10}=10^4\gg1.
\]
因此本例惯性效应比科氏效应大约四个数量级。
\Step{据量级判断可观测结论}
一般小容器的形状、注水残余旋转、排水孔不对称和初始扰动足以控制旋向，不能仅凭通常排水旋涡判断半球。这个判断不是说科氏力严格为零，而是说它在给定尺度下很弱。若要用精密长时实验分辨它，还需另行控制初始扰动、黏性及排水过程。''',
39:r'''\Step{先求不含自转的零阶下落}
令 $c=\Omega_E\cos\lambda$。初位置 $(0,0,h)$、初速度为零，在零阶有
\[
z^{(0)}=h-\frac12gt^2,\quad\dot z^{(0)}=-gt,
\qquad x^{(0)}=y^{(0)}=0.
\]
计算自转一阶修正时，科氏项中的速度只需代入这个零阶速度。
\Step{连续两次积分求东向位移}
东西向方程给出 $\ddot x^{(1)}=-2c\dot z^{(0)}=2cgt$。使用 $x^{(1)}(0)=\dot x^{(1)}(0)=0$，
\[
\dot x^{(1)}=\int_0^t2cgq\,\dd q=cgt^2,
\qquad x^{(1)}=\int_0^tcgq^2\,\dd q=\frac13cgt^3.
\]
零阶水平速度为零，所以北向、竖直的一阶驱动都为零，$y^{(1)}=z^{(1)}=0$。
\Step{由落地条件确定积分终点}
$z=0$ 给出 $t_0=\sqrt{2h/g}$；本题一阶竖直修正为零，因此落地时间到一阶仍为 $t_0$。代入得
\begin{equation}
d_E=\frac{\Omega_E\cos\lambda}{3}\sqrt{\frac{8h^3}{g}}.\label{eq:eastfall}
\end{equation}
\Step{检查方向、量纲与适用范围}
南、北半球都有 $\cos\lambda\ge0$，所以一般均偏东，极点的一阶偏移为零。根号项量纲为长度乘时间，乘角速率后为长度。结果按 $h^{3/2}$ 增长，但依赖无阻力、局部恒重力及短时近似；$y^{(1)}=0$ 并不意味着更高阶的南北偏移也必为零。''',
40:r'''\Step{先计算公共的自转投影}
在纬度 $45^\circ$，$c=\Omega_E\cos45^\circ\approx5.1563\times10^{-5}\,\mathrm{s^{-1}}$。每个高度都使用
\[
t_0=\sqrt{\frac{2h}{g}},\qquad d_E=\frac13cgt_0^3.
\]
先算时间再代入位移，可避免遗漏 $t^3$ 或混淆角度单位。
\Step{分别计算两个高度}
$h=100\,\mathrm m$ 时，
\[
t_0=\sqrt{\frac{200}{9.81}}\approx4.515\,\mathrm s,
\quad d_E=\frac{5.1563\times10^{-5}\times9.81\times4.515^3}{3}
\approx0.01552\,\mathrm m.
\]
$h=500\,\mathrm m$ 时，
\[
t_0=\sqrt{\frac{1000}{9.81}}\approx10.10\,\mathrm s,
\quad d_E\approx0.1735\,\mathrm m.
\]
即两者分别偏东约 $1.55\,\mathrm{cm}$ 与 $17.35\,\mathrm{cm}$。
\Step{用比例关系交叉检查}
公式给出 $d_E\propto h^{3/2}$，因此高度增为五倍时，偏移应增为 $5^{3/2}\approx11.18$ 倍；$0.1735/0.01552$ 与此一致。这些数值针对理想真空模型，真实高处落体的阻力和气流可能改变时间与偏移。''',
41:r'''\Step{保留上升和下降全过程的零阶速度}
令 $c=\Omega_E\cos\lambda$。竖直零阶解为 $z=w_0t-gt^2/2$、$\dot z=w_0-gt$，返回时间 $T_0=2w_0/g$。代入东西向科氏项，
\[
\ddot x=-2c(w_0-gt).
\]
在最高点前后，右侧分别为负、正，表示上升时向西、下降时向东的加速度。
\Step{分别积分速度与位置}
初始东西位置和速度都为零，因此
\[
\dot x=-2cw_0t+cgt^2,
\qquad x=-cw_0t^2+\frac13cgt^3.
\]
代入 $T_0=2w_0/g$，得到 $\dot x(T_0)=0$，而
\begin{equation}
x(T_0)=-\frac{4\Omega_E\cos\lambda\,w_0^3}{3g^2}.\label{eq:verticalthrow}
\end{equation}
\Step{解释为什么位移没有抵消}
加速度的前后积分抵消，使最终东西速度恢复为零，但速度在飞行中并非零。事实上 $\dot x=cgt(t-T_0)$，在 $0<t<T_0$ 时始终非正，故整个飞行中西向位移持续累积。下降段向东加速只是把西向速度逐渐减至零，没有把质点送回原铅垂线。

例如 $\lambda=45^\circ,w_0=50\,\mathrm{m/s}$ 时，$T_0\approx10.19\,\mathrm s$，偏西约 $0.0893\,\mathrm m$。''',
42:r'''\Step{先算零阶飞行时间}
本题 $w_0=v_0=0$，$u_0=100\,\mathrm{m/s}$，在 $45^\circ$ 有 $c=\sigma=\Omega_E/\sqrt2\approx5.1563\times10^{-5}\,\mathrm{s^{-1}}$。不含自转时
\[
T_0=\sqrt{\frac{2h}{g}}=\sqrt{\frac{200}{9.81}}\approx4.51524\,\mathrm s,
\quad x_0=u_0T_0\approx451.524\,\mathrm m.
\]
\Step{先由竖直方程求落地时间修正}
一阶竖直轨迹为 $z=h-gt^2/2+cu_0t^2$。令 $T=T_0+\delta T$，只保留一阶，
\[
0=-gT_0\delta T+cu_0T_0^2,
\quad\delta T=\frac{cu_0T_0}{g}\approx0.002373\,\mathrm s.
\]
东向发射的竖直科氏加速度向上，故飞行时间略微延长，符号合理。
\Step{把时间修正也代入东向射程}
一阶有 $x(t)=u_0t+cgt^3/3$、$y(t)=-\sigma u_0t^2$。在落地时
\[
\delta x=u_0\delta T+\frac13cgT_0^3
\approx0.2373+0.01552=0.2528\,\mathrm m,
\]
\[
y_{\rm land}=-\sigma u_0T_0^2\approx-0.1051\,\mathrm m.
\]
因此总东向射程约为 $451.777\,\mathrm m$，并偏南约 $10.51\,\mathrm{cm}$。将 $\delta T$ 代入已经是一阶的偏移项只产生二阶量，可舍去；但零阶射程中的 $u_0\delta T$ 必须保留。阻力、曲率及重力梯度不属于本题模型。''',
43:r'''\Step{把两个小效应的高度依赖分别写出}
零阶下落时间 $T_0=\sqrt{2h/g}$。固定释放偏差 $u_i$ 给出东西位移 $u_iT_0$，自转的一阶落体东偏为 $\Omega_E\cos\lambda\,gT_0^3/3$。在题设忽略 $O(\Omega_Eu_i^2)$ 等项的精度下，
\[
x_{\rm land}(h)=u_i\sqrt{\frac{2h}{g}}
+\frac{\Omega_E\cos\lambda}{3}\sqrt{\frac{8h^3}{g}}.
\]
前者按 $h^{1/2}$、后者按 $h^{3/2}$ 增长，单一高度的测量不能可靠区分二者。
\Step{把模型化成可以拟合的直线}
两边除以 $\sqrt h$，令 $Y=x_{\rm land}/\sqrt h$、$H=h$，则
\[
Y=b+sH,\qquad b=u_i\sqrt{\frac2g},\qquad
s=\frac{\Omega_E\cos\lambda}{3}\sqrt{\frac8g}.
\]
在多个高度测量后，作 $Y$ 对 $H$ 的图：截距反映固定释放速度偏差，斜率反映理想自转偏转；由截距可反算 $u_i=b\sqrt{g/2}$。
\Step{说明拟合所检验的假设}
高度改变时必须保持同一装置的 $u_i$ 近似不变，且各次均满足同一重力与阻力近似。若装置偏差随高度变化，或空气阻力显著改变下落时间，拟合不再具有上述简单解释。重复测量可降低随机散差，但不能自动消除固定的系统偏差。''',
44:r'''\Step{从通解中的两个初条件确定常数}
线性傅科模型的通解为 $\zeta=e^{-\mathrm i\sigma t}(A\cos\kappa t+B\sin\kappa t)$。初位置给出 $A=a$；求导后在 $t=0$ 有
\[
\dot\zeta(0)=-\mathrm i\sigma A+\kappa B=0,
\quad B=\mathrm i\frac{\sigma a}{\kappa}.
\]
因此完整初值解为
\begin{equation}
\zeta=a e^{-\mathrm i\sigma t}\left(\cos\kappa t+\mathrm i\frac\sigma\kappa\sin\kappa t\right).
\label{eq:foucaultrest}
\end{equation}
\Step{展开为可以核对的实坐标}
用 $e^{-\mathrm i\sigma t}=\cos\sigma t-\mathrm i\sin\sigma t$ 相乘，分别取实部、虚部，得
\begin{align*}
x&=a\left(\cos\sigma t\cos\kappa t+\frac\sigma\kappa\sin\sigma t\sin\kappa t\right),\\
y&=a\left(-\sin\sigma t\cos\kappa t+\frac\sigma\kappa\cos\sigma t\sin\kappa t\right).
\end{align*}
$t=0$ 时直接得到 $x=a,y=0$；由复速度关系可同时确认 $\dot x=\dot y=0$。
\Step{在慢转坐标中识别轨迹}
令 $w=e^{\mathrm i\sigma t}\zeta=X_s+\mathrm iY_s$，则
\[
X_s=a\cos\kappa t,\qquad Y_s=\frac{a\sigma}{\kappa}\sin\kappa t.
\]
当 $\sigma\ne0$ 时，这是一条半长轴 $a$、半短轴 $a|\sigma|/\kappa$ 的椭圆；主轴相对地面以角速率 $-\sigma$ 慢转。赤道处 $\sigma=0$，退化为不进动的直线振动。
\Step{说明为何小项仍要保留}
若直接删去正弦项，写成 $a e^{-\mathrm i\sigma t}\cos\kappa t$，会得到 $\dot\zeta(0)=-\mathrm i\sigma a$，与静止释放矛盾。只有人为给定这一非零初速度，才有严格的慢转直线解。真实地球的 $|\sigma|/\kappa$ 很小，椭圆很细，所以“摆面慢进动”是良好近似，但不能因此省略初条件校验。''',
45:r'''\Step{区分慢进动与快振动的时间尺度}
摆面慢转角速率为 $-\Omega_E\sin\lambda$，进动周期按 $360^\circ$ 定义为
\[
T_P=\frac{2\pi}{\Omega_E|\sin\lambda|}=\frac D{|\sin\lambda|},
\quad |\dot\alpha|=\frac{360^\circ}{D}|\sin\lambda|.
\]
三处均在北半球，俯视摆面主轴都顺时针进动。
\Step{逐地代入纬度}
巴黎有 $\sin48.86^\circ\approx0.75310$，因此 $T_P\approx23.9345/0.75310=31.78\,\mathrm h$，进动速率约 $360/31.78=11.33^\circ/\mathrm h$。

北京有 $\sin39.90^\circ\approx0.64145$，因此 $T_P\approx37.31\,\mathrm h$，进动速率约 $9.65^\circ/\mathrm h$。北极 $\sin\lambda=1$，周期恰为恒星日 $23.9345\,\mathrm h$，速率约 $15.041^\circ/\mathrm h$。
\Step{另算摆球的快振动周期}
快振动的一阶近似频率为 $\omega_0=\sqrt{g/l}$，所以
\[
T_0=2\pi\sqrt{\frac lg}=2\pi\sqrt{\frac{67}{9.81}}
\approx16.42\,\mathrm s.
\]
快周期为秒量级，慢进动周期为几十小时，两者不是同一周期。理想模型中质量在方程两边约去，所以这些周期不依赖摆球质量。无向主轴在半个进动周期后也重合，但不能把它称为通常约定的 $360^\circ$ 进动周期。''',
46:r'''\Step{由位移求相对动能与离心势}
已知 $x=a\cosh\Omega t$，先求 $\dot x=a\Omega\sinh\Omega t$。取真实势 $U=0$，有
\[
T'=\frac12ma^2\Omega^2\sinh^2\Omega t,
\qquad U_{\rm cf}=-\frac12ma^2\Omega^2\cosh^2\Omega t.
\]
利用 $\cosh^2q-\sinh^2q=1$，得到 $J=T'+U_{\rm cf}=-ma^2\Omega^2/2$，与时间无关。
\Step{从惯性系能量与角动量独立计算}
惯性速度由径向 $\dot x$ 与切向 $\Omega x$ 合成，故
\[
E=\frac12m(\dot x^2+\Omega^2x^2),\qquad L_z=m\Omega x^2.
\]
因此
\[
E-\Omega L_z=\frac12m\dot x^2-\frac12m\Omega^2x^2
=-\frac12ma^2\Omega^2,
\]
与前法一致。
\Step{解释机械能为何增长}
求导并使用 $\ddot x=\Omega^2x$，得到
\[
\dot E=m\dot x\ddot x+m\Omega^2x\dot x
=2m\Omega^2x\dot x=\Omega\dot L_z.
\]
这正是管侧壁反力的惯性系功率，能量由维持转速的电机提供。守恒的是组合 $E-\Omega L_z$，并非 $E$ 本身。$t=0$ 时 $J=-m\Omega^2a^2/2$ 也可直接由初始相对静止读出。''',
47:r'''\Step{先代入相对静止的条件}
物块相对盘静止，故 $T'=0$，且半径 $a$ 与真实势 $U$ 都不变。瞬时雅可比量为
\[
J=U-\frac12ma^2\Omega(t)^2.
\]
对时间求导时必须对角速率也求导，得到 $\dot J=-ma^2\Omega\dot\Omega$，通常不为零。
\Step{用惯性角动量核验变化率}
物块切向速度为 $a\Omega$，所以
\[
L_z=ma^2\Omega,\qquad-\dot\Omega L_z=-ma^2\Omega\dot\Omega=\dot J.
\]
与变转速系的功率公式一致。若 $\dot\Omega=0$，才恢复本题中的恒定 $J$。
\Step{分别求惯性动能与真实驱动功率}
惯性动能 $T=ma^2\Omega^2/2$，所以 $\dot T=ma^2\Omega\dot\Omega$。所需切向约束力为 $F_\theta=ma\dot\Omega$，它的惯性系功率为
\[
P=F_\theta(a\Omega)=ma^2\Omega\dot\Omega=\dot T.
\]
径向约束力垂直速度，不做功。加速时驱动输入能量，减速时可取回能量；相对动能始终为零，并不等于惯性系没有能量交换。'''
}
