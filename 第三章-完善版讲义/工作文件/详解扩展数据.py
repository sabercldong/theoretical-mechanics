# Additional derivations are question-specific; existing substantive material is retained.
E={}
E[1]=r'''\Step{确定运动类型与基点}
平台的各边方向保持不变，因此姿态矩阵为常矩阵、刚体角速度为零。取中心 $C$ 为基点，对任意材料点 $A$，有
\[
\vect r_A(t)=\vect r_C(t)+\vect\rho_A,\qquad
\vect r_C=R(\cos\Omega t\,\vect i+\sin\Omega t\,\vect j),
\]
其中 $\vect\rho_A=\vect r_A-\vect r_C$ 在空间中为常矢量。
\Step{分别求导，不引入绕中心的转动}
固定空间基矢的导数为零，故
\[
\vect v_A=\dot{\vect r}_C
=R\Omega(-\sin\Omega t\,\vect i+\cos\Omega t\,\vect j),
\]
\[
\vect a_A=\ddot{\vect r}_C
=-R\Omega^2(\cos\Omega t\,\vect i+\sin\Omega t\,\vect j).
\]
因 $\dot{\vect\rho}_A=0$，所有点在同一时刻的速度和加速度均相同。
\Step{检验轨迹与极限}
$|\vect v_A|=R|\Omega|$、$|\vect a_A|=R\Omega^2$，且两者正交。
$t=0$ 时 $\vect v_A=R\Omega\vect j$、$\vect a_A=-R\Omega^2\vect i$，与切向速度、法向加速度一致。
每点的圆形轨迹圆心相对原点平移了 $\vect\rho_A$，所以这是曲线平动。
$\Omega\to0$ 时两者同时趋零。这里的向心加速度指向各点自身轨迹的圆心；它不意味着平台绕 $C$ 转动。'''
E[2]=r'''\Step{统一位置矢量的表达基底}
题给 $\vect\rho_{OC}$、$\vect\rho_{OA}$ 是本体坐标中的常列矢量。设 $\mathsf R(t)$ 将本体分量变为空间分量，则
\[
\vect r_C=\vect r_O+\mathsf R\vect\rho_{OC},\quad
\vect\rho_{CA}=\vect\rho_{OA}-\vect\rho_{OC}.
\]
$\mathsf R$ 只描述三根体轴的取向，改变基点不会改变它。
\Step{写出两种位置分解并验证相等}
以 $O$ 为基点：$\vect r_A=\vect r_O+\mathsf R\vect\rho_{OA}$；以 $C$ 为基点：
\[
\vect r_A=\vect r_C+\mathsf R\vect\rho_{CA}
=\vect r_O+\mathsf R\vect\rho_{OC}
+\mathsf R(\vect\rho_{OA}-\vect\rho_{OC}).
\]
中间两项相消，恢复第一种表达。
\Step{求导得到同一速度场}
由 $\dot{\mathsf R}\vect\rho=\vect\omega\times(\mathsf R\vect\rho)$，
\[
\vect v_C=\vect v_O+\vect\omega\times\vect r_{OC},\qquad
\vect v_A=\vect v_O+\vect\omega\times\vect r_{OA}
=\vect v_C+\vect\omega\times\vect r_{CA}.
\]
若 $O$ 是地面固定铰点，令 $\vect v_O=0$；若铰点随机构运动，则保留该项。
变化的是平移部分和相对位置，角速度及物体姿态完全相同。'''
E[6]=r'''\Step{明确两个相对转轴}
角速度合成要把相对转动和支架转动写在同一空间中。取竖直向上为 $\vect k$；第一种盘法线 $\vect n$ 与它夹角 $\beta$，故
$\vect n\cdot\vect k=\cos\beta$。第二种盘法线始终为 $\vect k$。
\Step{求垂直于杆的圆盘}
第一种机构有
\[
\vect\omega_1=\Omega\vect k+\omega\vect n,\qquad
|\vect\omega_1|=\sqrt{\Omega^2+\omega^2+2\Omega\omega\cos\beta}.
\]
若 $\Omega,\omega$ 为常数，$\dot{\vect n}=\Omega\vect k\times\vect n$，所以
$\vect\alpha_1=\Omega\omega\vect k\times\vect n$。
其非零值来自杆方向的改变；盘面垂直于杆，不能把盘法线当作竖直方向。
\Step{求保持水平的圆盘并比较}
第二种机构的两次姿态转动都绕竖直方向，因此
\[
\vect\omega_2=(\Omega+\omega)\vect k,\qquad
|\vect\omega_2|=|\Omega+\omega|,\qquad \vect\alpha_2=0.
\]
杆的倾斜改变圆盘中心的平移轨迹，却不改变已经由万向约束确定的盘面方向。
当 $\beta=0$，两式一致；当 $\omega=-\Omega$，第二种圆盘姿态在空间固定，第一种一般仍有转动。
若 $\omega$ 改为相对地面测得的绝对盘转速，第二式应直接写 $\omega\vect k$，不可再加支架转速。'''
E[9]=r'''\Step{分开质心轨道与本体姿态}
地球年周运动确定质心位置 $\vect r_C(t)$；刚体姿态由自转轴和地表标记相对于空间轴的方向确定。题设自转轴不进动，节点方向固定，因而
$\theta(t)=\varepsilon$、$\varphi(t)=\varphi_0$。
\Step{利用初值积分自转角}
由 $\dot\psi=\omega$、$\psi(0)=\psi_0$，
\[
\psi(t)=\psi_0+\omega t,\qquad
\mathsf R(t)=R_z(\varphi_0)R_x(\varepsilon)R_z(\psi_0+\omega t).
\]
它把固定轴倾角、固定方位和地表标记的日转动分别表示出来。
\Step{由欧拉运动学求总角速度}
一般合成为
$\vect\omega=\dot\varphi\vect e_\zeta+\dot\theta\vect e_N+\dot\psi\vect e_z$，故本题
\[
\vect\omega=\omega\vect e_z,\qquad
(\omega_x,\omega_y,\omega_z)=(0,0,\omega).
\]
惯性系中 $\vect e_z$ 固定，因此恒定 $\omega$ 还意味着 $\vect\alpha=0$。
若今后加入慢进动 $\dot\varphi\ne0$，则轴向分量改为
$\omega_z=\dot\psi+\dot\varphi\cos\varepsilon$。
公转不会自动产生额外的本体自转项；只有另用随公转的坐标架描述时，才须作参考系角速度换算。'''
E[10]=r'''\Step{用朝向约束直接建立体轴}
令卫星轨道位置为
$\vect r_C=R(\cos\Omega t,\sin\Omega t,0)$。
朝向中心的体轴为
\[
\vect e_1=(-\cos\Omega t,-\sin\Omega t,0),\quad
\vect e_3=\vect k,\quad
\vect e_2=\vect e_3\times\vect e_1=(\sin\Omega t,-\cos\Omega t,0).
\]
这三根轴保持右手正交，并满足题设的朝向条件。
\Step{写出姿态矩阵与角速度}
以三根体轴为空间分量列向量，得到
\[
\mathsf R(t)=R_z(\pi+\Omega t),\qquad
\vect\omega=\Omega\vect k.
\]
在欧拉角奇异位置，可取 $\theta=0,\varphi=0,\psi=\pi+\Omega t$。
此时单独的 $\varphi,\psi$ 不唯一，能够确定的是它们的和。
\Step{比较两种观察系并检查周期}
惯性系中自转周期为 $2\pi/|\Omega|$，与公转周期相同；每绕行一周，朝内的标记方向也转一周。
随轨道架以 $\Omega\vect k$ 转动时，卫星相对于它的角速度为零。
例如轨道转过 $\pi/2$，$\vect e_1$ 从 $-\vect i$ 变到 $-\vect j$，其空间方向已改变。
因此“同一面朝向中心”规定的是相对轨道架的固定姿态，同时要求惯性系中的同步自转。'''
E[12]=r'''\Step{从装配支路建立几何方程}
以向下的 $\xi$ 轴和向右的 $\eta$ 轴为固定正交轴，$B$ 位于 $A$ 上方，且 $BA$ 初始沿 $+\xi$。设连杆相对 $+\xi$ 的有向角为 $\psi$，由水平方向投影
\[
L\sin\psi=a\sin q,\qquad q=\Omega t.
\]
题设 $L>a$ 保证 $|\sin\psi|<1$；取连续支路 $\cos\psi>0$，有
$\psi(t)=\arcsin[a\sin(\Omega t)/L]$，并满足 $\psi(0)=0$。
\Step{对约束求导，而非令连杆匀速}
\[
L\cos\psi\,\dot\psi=a\Omega\cos\Omega t,\qquad
L\cos\psi=\sqrt{L^2-a^2\sin^2\Omega t}.
\]
所以
\[
\vect\omega_{AB}=\frac{a\Omega\cos\Omega t}{\sqrt{L^2-a^2\sin^2\Omega t}}\vect e_\zeta.
\]
连杆姿态可用奇异位置的一种欧拉角选择表示：$\theta=0,\varphi=0$，第三角为上述 $\psi$；实际可测量的平面姿态由总平面转角给出。
\Step{检查特殊位置与变化率}
$t=0$ 时 $\dot\psi=a\Omega/L$；$q=\pi/2$ 时 $\dot\psi=0$，连杆瞬时平动而非全体静止。
再求导得
\[
\ddot\psi=-\frac{a\Omega^2(L^2-a^2)\sin\Omega t}{(L^2-a^2\sin^2\Omega t)^{3/2}}.
\]
因此曲柄匀速不保证连杆匀速。当 $a/L\ll1$，$\psi\simeq(a/L)\sin\Omega t$，恢复小摆角近似。'''
E[13]=r'''\Step{选取不含多角混合的矩阵元}
由约定 $R=R_z(\varphi)R_x(\theta)R_z(\psi)$ 的乘积，第三列与第三行给出
\[
R_{13}=\sin\varphi\sin\theta,\quad R_{23}=-\cos\varphi\sin\theta,
\quad R_{33}=\cos\theta,
\]
\[
R_{31}=\sin\theta\sin\psi,\qquad R_{32}=\sin\theta\cos\psi.
\]
这些元素分离了三个角的依赖。
\Step{利用倾角范围确定分支}
$0<\theta<\pi$ 时 $\sin\theta>0$，因此
\[
\theta=\arccos R_{33},\quad
\varphi=\operatorname{atan2}(R_{13},-R_{23}),\quad
\psi=\operatorname{atan2}(R_{31},R_{32}).
\]
$\operatorname{atan2}(y,x)$ 同时使用正弦、余弦符号，可区分四个象限。各方位角在模 $2\pi$ 意义下确定；连续跟踪时还需展开跨越 $\pm\pi$ 的跳变。
\Step{回代与奇异性检验}
将三角代回全部九个元素，应恢复给定的 $R$；数值输入还应满足 $R^{\mathsf T}R=\mathsf1,\det R=1$。
在 $\theta=0$ 时，$R=R_z(\varphi+\psi)$，只能求和角；在 $\theta=\pi$ 时只能确定对应的差角组合。
此时反正切的两个输入同时为零，不可强行给出唯一的两个方位角。
例如取 $\varphi=\pi/3,\theta=\pi/4,\psi=-\pi/6$，上述三组矩阵元保留了 $\psi<0$ 的象限信息，反解可恢复原角。'''
E[14]=r'''\Step{固定主动转动与乘法顺序}
作用于列矢量时先发生的转动写在右侧。基本矩阵为
\[
R_x=\begin{pmatrix}1&0&0\\0&0&-1\\0&1&0\end{pmatrix},\qquad
R_y=\begin{pmatrix}0&0&1\\0&1&0\\-1&0&0\end{pmatrix}.
\]
因此“先 $y$ 后 $x$”是 $R_xR_y$，“先 $x$ 后 $y$”是 $R_yR_x$。
\Step{逐项相乘与跟踪标记方向}
\[
R_xR_y=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\qquad
R_yR_x=\begin{pmatrix}0&1&0\\0&0&-1\\-1&0&0\end{pmatrix}.
\]
各自第三列就是初始 $\vect e_z$ 的像：分别为 $\vect e_x$ 与 $-\vect e_y$，故最终姿态不同。
第一矩阵满足 $R(1,1,1)^{\mathsf T}=(1,1,1)^{\mathsf T}$，转轴为 $(1,1,1)/\sqrt3$。
由 $\operatorname{tr}R=1+2\cos\gamma=0$，合成转角 $\gamma=2\pi/3$。
它不同于把两个直角矢量相加所得到的模 $\pi/\sqrt2$。
\Step{说明角速度为何仍可相加}
对小参数 $\epsilon$，
\[
R_x(\epsilon)R_y(\epsilon)=\mathsf1+\epsilon(T_x+T_y)+O(\epsilon^2).
\]
交换次序仅影响二阶项 $\epsilon^2(T_xT_y-T_yT_x)$。
因此一阶无穷小转动可相加，并在除以时间后取极限得到角速度的矢量合成；有限姿态的组合仍须按顺序乘矩阵。'''
E[16]=r'''\Step{计算主矢与矩的方向}
可取左力作用于 $(0,0)$、方向向下，右力作用于 $(d,0)$、方向向上。两力分别为 $-F\vect j,F\vect j$，于是
\[
\vect F_{\text{主}}=-F\vect j+F\vect j=\vect0,\qquad
\vect M_O=(d\vect i)\times(F\vect j)=Fd\vect k.
\]
从 $+z$ 看为逆时针，符合题设；$d$ 必须是两条作用线的垂直距离。
\Step{直接检验移点不变性}
对任意 $A=(x_A,y_A)$，两力矩的 $z$ 分量为
\[
(-x_A)(-F)+(d-x_A)F=Fd.
\]
也可用式\eqref{eq:momenttranslation}：
$\vect M_A=\vect M_O-\vect r_{OA}\times\vect F_{\text{主}}=Fd\vect k$。
把整个力偶平移任意矢量 $\vect b$，新增矩为 $\vect b\times(-F\vect j+F\vect j)=0$，结论相同。
\Step{解释等效条件与限制}
只要 $Fd$ 和矩方向不变，改变两力大小、间距或整体位置都保持刚体整体的力学效果。
若以一力替代，非零单力必有非零主矢，而本题主矢为零，故不能等效。
$F\to0$ 或 $d\to0$ 时力偶矩趋零；单独给出两个反向力而不说明作用线间距，不能确定其转动效果。
力偶可作为自由矩处理，但真实施力位置仍会影响物体内部应力。'''
E[17]=r'''\Step{写出力系的不变量}
本题主矢 $\vect F=F\vect k$，主矩 $\vect M_O=C\vect k$，且
\[
\vect F\cdot\vect M_O=FC\ne0.
\]
将取矩点移至任意 $A$，主矩改为 $\vect M_A=\vect M_O-\vect r_{OA}\times\vect F$；与主矢点乘时，叉积项恒为零。因此上述内积与取矩点无关。
\Step{证明不存在等效单力}
若一力 $\vect F$ 作用于某位置 $\vect r=(x,y,z)$，它关于 $O$ 的矩为
\[
\vect r\times\vect F=(Fy,-Fx,0).
\]
其轴向分量恒为零，无法等于 $(0,0,C)$。
等价地，任何单力都满足 $\vect F\cdot(\vect r\times\vect F)=0$，与本题的非零不变量矛盾。
\Step{确定最简形式与中心轴}
关于 $A=(x,y,z)$ 的主矩为 $(-Fy,Fx,C)$，其模平方为
$F^2(x^2+y^2)+C^2$。
最小值在 $x=y=0$，因此中心轴是整个 $z$ 轴。最简形式仍为沿该轴的力 $F\vect k$ 加同轴自由矩 $C\vect k$，可称为力螺旋，螺距 $C/F$ 的量纲为长度。
只有 $C=0$ 才能退化为本题原点处的单力；给定条件明确排除了这一情形。'''
E[23]=r'''\Step{确认总质心与公共基底}
两质量相等且中心位于 $\pm a\vect e_x$，总质心确在原点 $C$。
部件张量都已沿同一组平行正交轴表达，因此不必先作姿态变换；总质量为 $2m$。
\Step{逐个应用张量平行轴定理}
对于任一部件，位移矢量 $\vect a_\pm=\pm a\vect e_x$，有
\[
\vect a_\pm\vect a_\pm^{\mathsf T}=a^2\operatorname{diag}(1,0,0),\qquad
m(a^2\mathsf1-\vect a_\pm\vect a_\pm^{\mathsf T})=ma^2\operatorname{diag}(0,1,1).
\]
两部分直接相加，得到
\[
\mathsf I_C=2\mathsf I_0+2ma^2\begin{pmatrix}0&0&0\\0&1&0\\0&0&1\end{pmatrix}.
\]
交叉元仍为原部件对应交叉元的两倍，并没有因为组合对称就自动消失。
\Step{从轴距理解结果并推广}
$x$ 轴经过两个部件质心，惯量没有平移增量；$y,z$ 轴各与部件中心轴相距 $a$，每块都增加 $ma^2$。
若部件间距从 $2a$ 变为 $4a$，平移部分乘四，自身部分不变。
当两部件姿态不同，正确通式是
\[
\mathsf I_{\text{总},O}=\sum_\alpha\left[R_\alpha\mathsf I_{\alpha,C}R_\alpha^{\mathsf T}
+m_\alpha(a_\alpha^2\mathsf1-\vect a_\alpha\vect a_\alpha^{\mathsf T})\right].
\]
所有项都须用同一个原点和同一公共基底；$a=0$ 时恢复 $2\mathsf I_0$。'''
E[24]=r'''\Step{直接用各质元速度积分}
从固定端点 $O$ 沿杆取 $s\in[0,L]$，$\dd m=(m/L)\dd s$。
杆与转轴垂直，质元速度为 $|\omega|s$，所以
\[
T=\frac12\frac mL\int_0^L\omega^2s^2\dd s
=\frac12\frac mL\omega^2\frac{L^3}{3}
=\frac{mL^2\omega^2}{6},\qquad I_O=\frac{mL^2}{3}.
\]
\Step{改以质心分解平动和转动}
质心在 $L/2$ 处，故 $v_C=|\omega|L/2$。用质心坐标 $u\in[-L/2,L/2]$，
\[
I_C=\frac mL\int_{-L/2}^{L/2}u^2\dd u=\frac{mL^2}{12}.
\]
由于 $\int u\dd m=0$，速度平方展开的平动和转动混合项积分为零。于是
\[
T=\frac12mv_C^2+\frac12I_C\omega^2
=\frac{mL^2\omega^2}{8}+\frac{mL^2\omega^2}{24}
=\frac{mL^2\omega^2}{6}.
\]
\Step{用平行轴与能量比例核验}
$I_O=I_C+m(L/2)^2=mL^2/3$，故 $\frac12I_O\omega^2$ 与前两条路线一致。
质心平动能与相对质心转动能之比是 $3:1$，即总能量的四分之三来自质心平动。
若把固定端点的转动能之外再加一次质心平动能，会重复计数；若只保留 $\frac12I_C\omega^2$，则遗漏平动能。
两种分解均描述同一个物体、同一真实运动。'''
E[38]=r'''\Step{确定惯量与净驱动力矩}
均匀盘绕中心对称轴的惯量为 $I_z=ma^2/2$。按驱动方向取正，盘转动时驱动力矩为 $+M$，阻矩为 $-M_f$；故净矩为 $M-M_f>0$。
\Step{列转动方程并积分初值}
\[
I_z\dot\omega=M-M_f,\qquad
\alpha=\frac{2(M-M_f)}{ma^2}=\text{常数}.
\]
先用 $\omega(0)=0$ 积分，再用 $q(0)=q_0$ 积分，得到
\[
\omega(t)=\frac{2(M-M_f)}{ma^2}t,\qquad
q(t)=q_0+\frac{M-M_f}{ma^2}t^2.
\]
惯量把力矩的单位 $\mathrm{kg\,m^2s^{-2}}$ 转为角加速度单位 $\mathrm{s^{-2}}$。
\Step{消去时间与核验能量}
由 $\omega\dd\omega=\alpha\dd q$，
\[
\omega^2=2\alpha\Delta q=\frac{4(M-M_f)\Delta q}{ma^2}.
\]
净功 $(M-M_f)\Delta q$ 恰为 $\frac12I_z\omega^2$；驱动输入功 $M\Delta q$ 分成动能与耗散 $M_f\Delta q$。
在 $M_f=0$ 时恢复理想恒矩加速；$M\downarrow M_f$ 时加速度趋零。
本题已明示可启动，若真实启动静摩擦上限大于 $M$，则初始静止不能直接套用此滑动阻矩模型。'''
E[39]=r'''\Step{由重力矩建立非线性方程}
端点惯量 $I_O=mL^2/3$，质心距轴 $h=L/2$。以竖直向下为 $q=0$，重力的回复矩为 $-mgh\sin q$，因此
\[
\frac{mL^2}{3}\ddot q=-mg\frac L2\sin q,\qquad
\ddot q+\frac{3g}{2L}\sin q=0.
\]
\Step{在线性近似中应用初值}
当 $|q_0|\ll1$，以弧度计有 $\sin q\simeq q$。令
$\omega_0=\sqrt{3g/(2L)}$，通解为 $q=A\cos\omega_0t+B\sin\omega_0t$。
由 $q(0)=q_0,\dot q(0)=0$ 得
\[
q(t)\simeq q_0\cos\omega_0t,\qquad
\tau_0=2\pi\sqrt{\frac{2L}{3g}}.
\]
对应的等效单摆长为 $2L/3$。小振动频率 $\omega_0$ 不是摆杆某瞬间的真实角速度 $\dot q$。
\Step{用精确能量求最低点速率}
以最低点势能为零，
\[
\frac12I_O\dot q^2+mgh(1-\cos q)=mgh(1-\cos q_0).
\]
所以 $\dot q^2=(3g/L)(\cos q-\cos q_0)$，到 $q=0$ 时
$|\dot q|=\sqrt{3g(1-\cos q_0)/L}$。初始 $q_0>0$ 的第一次回落取负根，$q_0<0$ 则取正根。
\Step{说明支反力的独立求法}
取径向单位矢量从轴指向质心、切向沿 $q$ 增大方向，
$\vect a_C=h\ddot q\vect e_t-h\dot q^2\vect e_r$。
由 $\vect R_O-mg\vect j=m\vect a_C$ 可求轴反力。
例如最低点径向向下、切向加速度为零，故 $R_y=mg+mh\dot q^2$，显然一般大于静重。'''
E[40]=r'''\Step{写出依赖悬点的惯量与回复系数}
悬轴方向不变时，中心轴惯量 $I_C=mk^2$ 为常量；距质心 $h$ 的平行悬轴有
$I_O=m(k^2+h^2)$。
对质心位于悬轴下方的小摆角 $q$，方程为
$m(k^2+h^2)\ddot q+mghq=0$，于是
\[
\tau_0(h)=2\pi\sqrt{\frac{k^2+h^2}{gh}},\qquad
\tau_0^2=\frac{4\pi^2}{g}\left(h+\frac{k^2}{h}\right).
\]
\Step{求驻点并检查是否为最小值}
因周期为正，极小化 $\tau_0$ 等价于极小化
$F(h)=h+k^2/h$。有
\[
F'(h)=1-\frac{k^2}{h^2}=0\ \Longrightarrow\ h=k,\qquad
F''(h)=\frac{2k^2}{h^3}>0.
\]
又由 $h+k^2/h\ge2k$，可知它还是 $h>0$ 上的全局最小值：
\[
\tau_{\min}=2\pi\sqrt{\frac{2k}{g}},\qquad
\ell_{\text{等效,min}}=2k.
\]
\Step{检查边界与可安装范围}
$h\to0^+$ 时回复矩趋零而 $I_C$ 非零，周期发散；$h\to\infty$ 时惯量随 $h^2$ 增长快于回复系数，周期也发散。
所以两种效应的竞争产生有限最优距离。
本题允许延长支架；若实际悬点只能在一个有限区间内选择，且该区间不包含 $k$，则应比较区间端点，而不能给出不可实现的悬点。'''
E[41]=r'''\Step{由杆方向写出中心惯量张量}
随杆转动的正交基中，$\vect n=(\sin\beta,0,\cos\beta)$，令 $J=ml^2/12$。细杆的中心张量为
\[
\mathsf I_C=J(\mathsf1-\vect n\vect n^{\mathsf T}),\quad
I_{xz}=-J\sin\beta\cos\beta,\quad I_{yz}=0.
\]
负号来自张量交叉元的定义 $I_{xz}=-\int xz\dd m$。
\Step{用角动量的空间导数求所需力偶}
总角速度为 $\omega\vect e_z$，故
$\vect L_C=\omega(I_{xz}\vect e_x+I_{zz}\vect e_z)$。
分量恒定，但 $\dot{\vect e}_x=\omega\vect e_y$，所以
\[
\vect M_C=\frac{\dd\vect L_C}{\dd t}=I_{xz}\omega^2\vect e_y.
\]
质心不作横向运动，附加反力之和必须为零。
\Step{用轴承间距把力偶还原为两力}
设 $\Delta\vect R_B=R\vect e_x$，则 $\Delta\vect R_A=-R\vect e_x$。关于任一点，这对力的矩都是
$L\vect e_z\times(R\vect e_x)=LR\vect e_y$。
与所需力偶比较，有
\[
\Delta R_{Bx}=\frac{I_{xz}\omega^2}{L}
=-\frac{ml^2\omega^2}{12L}\sin\beta\cos\beta,\qquad
\Delta R_{Ax}=-\Delta R_{Bx}.
\]
其空间方向随轴一起转动。这里求的是附加横向反力，竖直静载分配需轴向支承资料。
$\beta=0$ 或 $\pi/2$ 时交叉元为零；$\omega\to0$ 时附加载荷按平方趋零。质心在轴上只消除偏心合力，并不自动消除这个力偶。'''
E[42]=r'''\Step{区分零合力与零力偶条件}
在恒速转动中，每个小质量需要横向向心力 $-m_i\omega^2\vect e_i$。零附加合力要求
\[
\vect U=\sum_i m_i\vect e_i=0.
\]
对横截面原点取矩，轴向位置使这些力额外形成力偶，其消失要求
\[
\vect V=\sum_i m_i z_i\vect e_i=0.
\]
这两个横向矢量条件共四个标量。第一条件等价于质心在轴上；两者一起才使该轴成为中心主轴。
\Step{建立两个校正平面的线性方程}
把校正质量与半径的乘积矢量记为 $\vect U_a,\vect U_b$，则
\[
\vect U_a+\vect U_b=-\vect U,\qquad
z_a\vect U_a+z_b\vect U_b=-\vect V.
\]
第二式减第一式的 $z_b$ 倍，得到
$(z_a-z_b)\vect U_a=z_b\vect U-\vect V$，因此
\[
\vect U_a=\frac{z_b\vect U-\vect V}{z_a-z_b},\qquad
\vect U_b=\frac{\vect V-z_a\vect U}{z_a-z_b}.
\]
\Step{回代、安装与单平面特例}
两式相加恰为 $-\vect U$，分别乘 $z_a,z_b$ 再相加恰为 $-\vect V$，故消元结果满足原条件。
选定安装半径 $r_a$ 时，校正质量 $m_a=|\vect U_a|/r_a$，方位由 $\vect U_a$ 的方向确定，另一平面同理。
单平面 $z_c$ 只能给出 $\vect V_c=z_c\vect U_c$，仅当原不平衡满足 $\vect V=z_c\vect U$ 才可一次消除。
$z_a\to z_b$ 时一般需要很大的校正量，反映两个平面趋于重合后失去独立调节力偶的能力。'''
E[43]=r'''\Step{建立质心位置和固定棱惯量}
在垂直铰棱的截面内取 $O$ 为原点，底面抬角为 $\theta$。质心坐标为
\[
x_C=\frac a2(\cos\theta-\sin\theta),\quad
y_C=\frac a2(\sin\theta+\cos\theta).
\]
中心平行轴惯量是 $ma^2/6$，质心到棱的距离为 $a/\sqrt2$，所以
$I_O=ma^2/6+m(a/\sqrt2)^2=2ma^2/3$。
\Step{用能量和初值求回落角速度}
铰反力对固定棱不做功，由 $\dot\theta(0)=0$，
\[
\frac12I_O\dot\theta^2+mg y_C(\theta)=mg y_C(\theta_0).
\]
因 $0<\theta<\theta_0<\pi/4$ 为回落支路，取负根：
\[
\dot\theta=-\sqrt{\frac{3g}{2a}
[\sin\theta_0+\cos\theta_0-\sin\theta-\cos\theta]}.
\]
令 $\theta=0$，得到即将触地的速度
$-\sqrt{3g(\sin\theta_0+\cos\theta_0-1)/(2a)}$。
\Step{用有向重力矩求角加速度}
重力矩为 $-mgx_C$，因此
\[
\ddot\theta=-\frac{3g}{4a}(\cos\theta-\sin\theta).
\]
在给定支路它为负，与回落方向一致；触地前为 $-3g/(4a)$。
当 $\theta_0\to0$ 时触地前速率趋零；$\theta_0=\pi/4$ 的精确静止初态位于不稳定平衡，理想方程不会自行选边。
碰撞后的角速度必须另给冲量或恢复系数模型，不能延用碰撞前的能量积分。'''
E[44]=r'''\Step{分别隔离两物块与滑轮}
轻物 $m$ 向上、重物 $2m$ 向下取正，共同加速度大小为 $a$，两张力记为 $T_1,T_2$。对两个物块：
\[
T_1-mg=ma,\qquad 2mg-T_2=2ma.
\]
绳与轮无滑动，轮的顺时针角加速度为 $a/r$。滑轮惯量 $I=mr^2/2$，因此
\[
(T_2-T_1)r=I\frac ar\quad\Longrightarrow\quad T_2-T_1=\frac12ma.
\]
\Step{消元并回代求张力}
由前两式 $T_1=m(g+a)$、$T_2=2m(g-a)$，相减代入第三式：
$mg-3ma=ma/2$，故
\[
a=\frac{2g}{7},\qquad
T_1=\frac97mg,\quad T_2=\frac{10}{7}mg,\quad
\alpha_{\text{顺时针}}=\frac{2g}{7r}.
\]
两张力皆正，且 $mg<T_1<T_2<2mg$，与两物块的加速方向相容。由静止释放后 $v(t)=2gt/7$。
\Step{独立检查高度与速度的关系}
重物下降 $h$，轻物上升同样的 $h$，总重力势能减少 $mgh$；滑轮也有转动能：
\[
mgh=\frac12mv^2+\frac12(2m)v^2+\frac12\left(\frac12mr^2\right)\frac{v^2}{r^2}
=\frac74mv^2.
\]
所以 $v=\sqrt{4gh/7}$，与 $v^2=2ah$ 一致。
若忽略滑轮质量，相当于把有效惯性分母从 $7m/2$ 改为 $3m$，会误得 $a=g/3$；无滑动只约束运动，并不保证两侧张力相等。'''
E[45]=r'''\Step{从主惯量写出实际轴向的张量}
薄盘沿法线的主惯量为 $mr^2/2$，盘内为 $mr^2/4$。令 $J=mr^2/4$，有
\[
\mathsf I_O=J(\mathsf1+\vect n\vect n^{\mathsf T}),\quad
I_{xz}=J\sin\beta\cos\beta=\frac{mr^2}{8}\sin2\beta,
\quad I_{yz}=0.
\]
绕实际轴的 $I_{zz}=J(1+\cos^2\beta)$。即使质心在轴上，只要 $I_{xz}\ne0$，轴也不是主轴。
\Step{先分配重力静载，再求动力力偶}
令 $\vect e_X$ 为固定向上方向。由静力平衡与关于 $O$ 的矩平衡，
\[
G_A+G_B=mg,\quad -aG_A+bG_B=0,
\quad G_A=\frac{mgb}{a+b},\ G_B=\frac{mga}{a+b}.
\]
恒速转动所需力偶为 $I_{xz}\omega^2\vect e_y(t)$。令动力附加反力为
$\Delta\vect R_B=D\vect e_x(t)$、$\Delta\vect R_A=-D\vect e_x(t)$，其力偶为 $(a+b)D\vect e_y(t)$，所以
\[
D=\frac{mr^2\omega^2\sin2\beta}{8(a+b)}.
\]
\Step{在固定空间方向合成整周期反力}
$t=0$ 时 $\vect e_x=\vect e_X$，并有 $\vect e_x(t)\cdot\vect e_X=\cos\omega t$。于是
\[
\vect R_A=G_A\vect e_X-D\vect e_x(t),\qquad
\vect R_B=G_B\vect e_X+D\vect e_x(t),
\]
\[
R_A^2=G_A^2+D^2-2G_AD\cos\omega t,\quad
R_B^2=G_B^2+D^2+2G_BD\cos\omega t.
\]
\Step{求最大模并检查退化姿态}
余弦在 $[-1,1]$ 内变化，故两轴承各自最大压力为
$R_{A,\max}=G_A+|D|$、$R_{B,\max}=G_B+|D|$，若 $D\ne0$，最大值相位相差 $\pi$。
所有轴承中的最大值为 $\max(G_A,G_B)+|D|$。
当 $\beta=0$ 或 $\pi/2$，$D=0$，恢复纯静载；当 $\omega$ 加倍时，附加力增至四倍。压力取力的模，因此盘轴作用于轴承的反力虽方向相反，最大压力数值相同。'''
E[46]=r'''\Step{分别计算两根杆的惯量与总质心}
水平杆关于端点 $O$ 的惯量是 $mL^2/3$；竖杆中心在距 $O$ 为 $L$ 的 $A$，故其惯量为 $mL^2/12+mL^2$。相加得
\[
I_O=\frac{17}{12}mL^2,\quad
x_C=\frac{m(L/2)+mL}{2m}=\frac{3L}{4},\quad y_C=0.
\]
\Step{以固定轴取矩求有向角加速度}
两重力关于 $O$ 的矩为 $-mg(L/2)-mgL=-3mgL/2$，因此
\[
\alpha=-\frac{3mgL/2}{17mL^2/12}=-\frac{18g}{17L}.
\]
记顺时针角加速度大小 $\beta=18g/(17L)$。给定瞬时角速度也为顺时针，但离心型加速度含 $\omega^2$，不受其符号影响。
\Step{由质心加速度求轴反力}
\[
\vect a_C=\alpha\vect k\times\left(\frac{3L}{4}\vect i\right)
-\omega^2\frac{3L}{4}\vect i
=-\frac{3L\omega^2}{4}\vect i-\frac{3L\beta}{4}\vect j.
\]
总质量为 $2m$，动量方程 $\vect R_O-2mg\vect j=2m\vect a_C$ 给出
\[
R_{Ox}=-\frac32mL\omega^2,\qquad
R_{Oy}=2mg-\frac32mL\beta=\frac7{17}mg.
\]
\Step{代入数值并核验量纲}
给定 $m=8,L=0.5,\omega=4,g=9.8$（均为 SI 单位），得
$\beta=20.75294\,\mathrm{s^{-2}}$，
$R_{Ox}=-96\,\mathrm N$、$R_{Oy}=32.28235\,\mathrm N$，
$|\vect R_O|=101.28253\,\mathrm N$。
向左反力提供质心的法向加速度，向下的质心切向加速度使向上轴反力小于总重；仅有轴力矩方程不能确定这两个反力分量。'''
E[47]=r'''\Step{由两端速度确定瞬时角速度中心}
$A$ 的速度水平，故瞬心在过 $A$ 的竖线上；$B$ 的速度竖直，故瞬心在过 $B$ 的横线上。交点为 $P=(x,y)$。
由刚体速度式，$\vect v_A=\omega\vect k\times(0,-y)=\omega y\vect i$，所以
\[
\omega=\frac uy>0.
\]
对长度约束求导，$x\dot x+y\dot y=0$，故
$\vect v_B=-xu\vect j/y$，与绕 $P$ 的速度一致。
\Step{消去时间得到空间极迹}
瞬心坐标为 $(x_P,y_P)=(x,y)$，而 $x^2+y^2=l^2$，因此
\[
x_P^2+y_P^2=l^2,\qquad x_P>0,\ y_P>0.
\]
空间极迹是墙脚为圆心、半径 $l$ 的第一象限圆弧；它描述的是各瞬时不同的速度零点在空间的位置。
\Step{投影到固定在梯子上的正交轴}
以 $A$ 为本体原点，令 $\vect e_1=(-x,y)/l$ 沿 $AB$，
$\vect e_2=(-y,-x)/l=\vect k\times\vect e_1$。因 $\vect r_{AP}=(0,y)$，
\[
q_1=\vect r_{AP}\cdot\vect e_1=\frac{y^2}{l},\qquad
q_2=\vect r_{AP}\cdot\vect e_2=-\frac{xy}{l}.
\]
代入约束得 $q_1^2+q_2^2=lq_1$，整理为
\[
(q_1-l/2)^2+q_2^2=l^2/4,\qquad q_2<0.
\]
本体极迹是以梯子中点为圆心、直径 $l$ 的下半圆弧。
$y\to0$ 时 $\omega=u/y$ 发散，说明等速拖动的理想模型在梯子即将放平时要求无界转速。'''
E[49]=r'''\Step{从固定绳段确定无滑动约束}
绳沿圆盘左侧竖直相切。圆心向下速率记为 $v$，逆时针角速度为 $\omega$。
接触材料点相对圆心为 $-r\vect i$，绝对速度为 $-(v+r\omega)\vect j$。
绳固定，故 $v=-r\omega$，求导得 $a=-r\alpha$。
\Step{列平动与绕质心转动方程}
下降取正，绳张力向上，且关于质心产生顺时针矩：
\[
ma=mg-T,\qquad I_C\alpha=-Tr,\qquad I_C=\frac12mr^2.
\]
将 $\alpha=-a/r$ 代入第二式，得 $T=I_Ca/r^2=ma/2$；再代入第一式：
\[
\frac32ma=mg\quad\Longrightarrow\quad a=\frac23g,\quad T=\frac13mg,
\quad\alpha=-\frac{2g}{3r}.
\]
\Step{用功与能量独立验证}
接触点速度为零，张力对盘的总功率为零。下降高度 $x$ 后
\[
mgx=\frac12mv^2+\frac12I_C\frac{v^2}{r^2}=\frac34mv^2.
\]
由此 $v^2=4gx/3$，再用 $v^2=2ax$ 得到相同的 $a$。
\Step{用瞬心取矩并核查适用条件}
这一几何中接触点到质心距离恒为 $r$，质心仅竖直平移，关于接触瞬心的方程可写为
$-mgr=(I_C+mr^2)\alpha$，故仍有 $\alpha=-2g/(3r)$。
接触瞬心取矩的简式依赖本题的约束，不能无条件用于加速移动的任意取矩点。
本题只有一条绳段承重；若换成两绳段的动滑轮，受力及约束都须重新建立。'''
E[50]=r'''\Step{用纯滚动条件确定角运动}
取 $\vect i$ 向右、$\vect j$ 向上、$\vect k$ 向外。底部点瞬时无滑动，
$0=v\vect i+\omega\vect k\times(-R\vect j)$，故
$\omega=-v/R$、$\alpha=-a/R$。
对任意轮缘材料点 $P$，统一使用
\[
\vect v_P=v\vect i+\omega\vect k\times\vect r_{OP},\quad
\vect a_P=a\vect i+\alpha\vect k\times\vect r_{OP}-\omega^2\vect r_{OP}.
\]
\Step{逐点代入相对位置求速度}
四点的相对位置依次为 $-R\vect j,-R\vect i,R\vect j,R\vect i$，所以
\[
\vect v_A=0,\quad \vect v_B=v(\vect i+\vect j),\quad
\vect v_C=2v\vect i,\quad \vect v_D=v(\vect i-\vect j).
\]
例如左点 $B$ 的自转速度向上，和轮心的向右速度合成，故两分量均为正。
\Step{分别计算平移、切向和法向加速度}
以 $B$ 为例：轮心项为 $a\vect i$，切向项为 $a\vect j$，法向项为 $(v^2/R)\vect i$。四点结果为
\[
\vect a_A=\frac{v^2}{R}\vect j,\qquad
\vect a_B=\left(a+\frac{v^2}{R}\right)\vect i+a\vect j,
\]
\[
\vect a_C=2a\vect i-\frac{v^2}{R}\vect j,\qquad
\vect a_D=\left(a-\frac{v^2}{R}\right)\vect i-a\vect j.
\]
\Step{检查瞬心与匀速极限}
$a=0$ 时轮心无加速度，但轮缘仍有大小 $v^2/R$ 的指向轮心的法向加速度。
底部点的水平平移项和切向项相消，竖直项保留，因此它速度为零而加速度不为零。
不能对“每时刻位于底部的不同材料点速度为零”直接求导，来代替跟踪同一个材料点的加速度。'''
E[51]=r'''\Step{由中心轨迹求平移速度}
外接使 $OA=R+r$。令 $\vect e_r$ 从 $O$ 指向 $A$，$\vect e_t=\vect k\times\vect e_r$，则
$\vect v_A=(R+r)\Omega\vect e_t$。
\Step{在真实接触点施加无滑动条件}
行星轮上的接触点 $P$ 满足 $\vect r_{AP}=-r\vect e_r$。设其绝对自转为 $\omega\vect k$，固定大轮接触点速度为零，因此
\[
0=\vect v_P=\vect v_A+\omega\vect k\times(-r\vect e_r)
=[(R+r)\Omega-r\omega]\vect e_t.
\]
故 $\omega=(1+R/r)\Omega$，与转臂同向。
转臂架自身以 $\Omega$ 转动，故相对自转率是
$\omega_{\text{相对}}=\omega-\Omega=(R/r)\Omega$，两者不可混用。
\Step{计算题定轮缘点的速度}
题设选 $\vect r_{AM}=r\vect e_t$，由 $\vect k\times\vect e_t=-\vect e_r$，
\[
\vect v_M=(R+r)\Omega\vect e_t-r\omega\vect e_r
=(R+r)\Omega(\vect e_t-\vect e_r).
\]
两单位方向正交，故 $|\vect v_M|=\sqrt2(R+r)|\Omega|$。
\Step{检查接触点、对侧点与等半径极限}
把 $\vect r_{AP}=-r\vect e_r$ 代回速度式确为零；对侧点 $+r\vect e_r$ 的速度为 $2\vect v_A$。
若 $R=r$，绝对自转率为 $2\Omega$，相对转臂仅为 $\Omega$。
这些特殊位置说明不能只根据轮心轨迹或周长比，忽略参考架转动来推算绝对自转。'''
E[53]=r'''\Step{分别隔离两轮与被提升物体}
两轮轴固定但有惯量。取收绳、提升对应的角加速度为正，轮间张力为 $T$、悬挂段为 $S$，则
\[
I_A\alpha_1=M_1-Tr_1,\quad
I_B\alpha_2=(T-S)r_2,\quad
\frac{P_3}{g}a=S-P_3.
\]
无伸长、无滑动使 $a=r_1\alpha_1=r_2\alpha_2$。
\Step{按有效平动惯性消元}
第一式除以 $r_1$、第二式除以 $r_2$，代入约束得到
\[
T=\frac{M_1}{r_1}-\frac{I_A}{r_1^2}a,\qquad
T-S=\frac{I_B}{r_2^2}a,\quad S=P_3+\frac{P_3}{g}a.
\]
相加消去两张力，有
\[
a=\frac{M_1/r_1-P_3}{P_3/g+I_A/r_1^2+I_B/r_2^2}.
\]
\Step{代入均匀圆盘惯量并求张力}
$I_A=P_1r_1^2/(2g)$、$I_B=P_2r_2^2/(2g)$，所以
\[
a=\frac{2g(M_1/r_1-P_3)}{P_1+P_2+2P_3},\quad
T=\frac{M_1}{r_1}-\frac{P_1a}{2g},\quad S=P_3(1+a/g).
\]
从静止向上加速要求 $M_1>P_3r_1$；等号时静止或匀速均可，具体由初值决定。
\Step{用能量及极限检查}
若提升 $x$，速度 $v$，由静止开始有
\[
(M_1/r_1-P_3)x=\frac12(P_3/g+I_A/r_1^2+I_B/r_2^2)v^2.
\]
与 $v^2=2ax$ 一致。$r_2$ 消去是均匀圆盘的 $I_B\propto r_2^2$ 所致，第二轮仍通过 $P_2$ 增大有效惯性。
两轮惯量趋零时，退化为 $a=g(M_1/(P_3r_1)-1)$，并有 $T=S$。'''
E[54]=r'''\Step{按初始转向确定滑动和摩擦方向}
逆时针转动时，墙接触处材料点向下滑，故墙摩擦 $f_A$ 向上；底部点向右滑，故地面摩擦 $f_B$ 向左。
墙法向 $N_A$ 向右、地面法向 $N_B$ 向上。两接触保持时圆心被几何约束固定。
\Step{联立平动力平衡与动摩擦律}
\[
N_A-f_B=0,\quad N_B+f_A-Q=0,\quad
f_A=\mu N_A,\quad f_B=\mu N_B.
\]
先由水平式 $N_A=\mu N_B$，再代入竖直式：
$(1+\mu^2)N_B=Q$。因此
\[
N_B=\frac Q{1+\mu^2},\quad N_A=\frac{\mu Q}{1+\mu^2},\quad
f_A=\frac{\mu^2Q}{1+\mu^2},\quad f_B=\frac{\mu Q}{1+\mu^2}.
\]
$\mu>0$ 时两法向力都为正，双接触假设成立。
\Step{用摩擦力矩积分角速度}
两摩擦都产生顺时针矩，均匀圆柱惯量 $I_C=Qr^2/(2g)$，所以
\[
I_C\dot\omega=-r(f_A+f_B),\quad
\dot\omega=-\frac{2g\mu(1+\mu)}{r(1+\mu^2)}=-c.
\]
在仍滑动的阶段 $\omega(t)=\omega_0-ct$。首次到零的时刻为
\[
t_* =\frac{r\omega_0(1+\mu^2)}{2g\mu(1+\mu)}.
\]
\Step{检查停止后的接触模型}
$t=t_*$ 后不能继续用动摩擦律外推成反向加速。静止状态可取 $N_B=Q$，其余三力为零。
$\mu\to0$ 时 $t_*\to\infty$；若初始改为顺时针，地面摩擦将向右，水平平衡需要负墙反力，因而原双接触解失效，须另分析脱离墙面的运动。'''
E[55]=r'''\Step{先用几何关系直接求导}
右侧装配支路有 $A=(l\cos\varphi,l\sin\varphi)$，
$B=(2l\cos\varphi,0)$，且 $\dot\varphi=\Omega$。
故 $\vect v_B=-2l\Omega\sin\varphi\vect i$；连杆从 $A$ 向 $B$ 的方位角为 $-\varphi$，所以 $\omega_{AB}=-\Omega$。
在 $\varphi=\pi/4$ 时，$\vect v_B=-\sqrt2l\Omega\vect i$，连杆顺时针转。
\Step{以曲柄端为基点复核两个分量}
\[
\vect v_A=l\Omega(-\sin\varphi\vect i+\cos\varphi\vect j),\quad
\vect r_{AB}=l(\cos\varphi\vect i-\sin\varphi\vect j).
\]
在 $\vect v_B=\vect v_A+\omega_{AB}\vect k\times\vect r_{AB}$ 中，竖直分量为
$0=l(\Omega+\omega_{AB})\cos\varphi$，故在本位置 $\omega_{AB}=-\Omega$；水平分量继而给出同一滑块速度。
\Step{沿连杆投影消去相对转动}
令连杆方向 $\vect n=(\cos\varphi,-\sin\varphi)$。
刚性约束要求两端速度沿连杆的投影相等，故
\[
v_{Bx}\cos\varphi=\vect v_A\cdot\vect n
=-2l\Omega\sin\varphi\cos\varphi.
\]
得到 $v_{Bx}=-2l\Omega\sin\varphi$。投影式消去了连杆转速，仍需速度差求它。
\Step{用瞬心的距离比例检验}
过 $A$ 作 $\vect v_A$ 的垂线，即 $OA$ 延长线；过 $B$ 作竖线，两线交于 $P$。
$45^\circ$ 时 $AP=l,BP=\sqrt2l$，而 $|v_A|=l|\Omega|$，所以 $|\omega_{AB}|=|\Omega|$、$|v_B|=\sqrt2l|\Omega|$。
方向由 $A$ 点的速度判定为顺时针，与向量结果一致。另一装配支路或死点位置须重新检查几何与可除因子。'''
E[56]=r'''\Step{用同一高度关系求连杆长度}
点 $A$ 高度为 $R\sin45^\circ$，连杆竖直投影为 $L\sin30^\circ$，故
$L=\sqrt2R$。取曲柄逆时针速率为 $\Omega$，
\[
\vect v_A=\frac{R\Omega}{\sqrt2}(-\vect i+\vect j),\quad
\vect r_{AB}=\frac{L}{2}(\sqrt3\vect i-\vect j).
\]
\Step{先由速度约束求连杆转速}
由 $v_{By}=0$，
$0=R\Omega/\sqrt2+\omega_{AB}L\sqrt3/2$，所以
$\omega_{AB}=-\Omega/\sqrt3$。
后续加速度中的法向项必须使用这个瞬时转速。
\Step{分别列加速度的两个分量}
曲柄匀速，故 $\vect a_A=-R\Omega^2(\vect i+\vect j)/\sqrt2$。完整基点式为
\[
\vect a_B=\vect a_A+\alpha_{AB}\vect k\times\vect r_{AB}
-\omega_{AB}^2\vect r_{AB}.
\]
竖直约束给出
$0=-R\Omega^2/\sqrt2+\alpha_{AB}L\sqrt3/2+\omega_{AB}^2L/2$，从而
\[
\alpha_{AB}=\frac{2\Omega^2}{3\sqrt3}.
\]
再代入水平分量：
\[
a_{Bx}=-\frac{R\Omega^2}{\sqrt2}+\frac L2\alpha_{AB}
-\frac{\sqrt3L}{2}\frac{\Omega^2}{3}
=-\left(\frac{\sqrt2}{2}+\frac{\sqrt6}{18}\right)R\Omega^2.
\]
\Step{给出方向和投影核验}
连杆角加速度逆时针，滑块加速度向左，大小约为 $0.8431895R\Omega^2$。
沿连杆投影时切向项消失，得
$|a_B|\cos30^\circ=R\Omega^2\cos75^\circ+(\sqrt2/3)R\Omega^2$，与分量法一致。
即使曲柄角加速度为零，连杆的角加速度也不为零；漏掉相对法向项还会给出错误数值。'''
E[57]=r'''\Step{分清球、板受力与接触速度}
球底部相对板初始向左滑，球受摩擦向右、板向左。地面光滑，竖直无加速度，故接触法向力为 $mg$，滑动摩擦大小 $f=\mu mg$。
逆时针角速度为正，球底部点速度为 $v_C+r\omega$，并非 $v_C-r\omega$。
\Step{分别积分球和平板的动力学方程}
实心球 $I_C=2mr^2/5$，有
\[
\dot v_C=\mu g,\quad \dot v_{\text{板}}=-\frac{\mu mg}{M},\quad
\dot\omega=\frac{fr}{I_C}=\frac{5\mu g}{2r}.
\]
用初值 $v_C(0)=\omega(0)=0,v_{\text{板}}(0)=v$，得
$v_C=\mu gt$、$v_{\text{板}}=v-\mu mgt/M$、$r\omega=5\mu gt/2$。
\Step{由首次无相对滑动求过渡时刻}
接触相对速度为
$u=v_C+r\omega-v_{\text{板}}=-v+\mu g(7/2+m/M)t$，其第一次为零时
\[
t_* =\frac{2Mv}{(7M+2m)\mu g}.
\]
记 $D=7M+2m$，此时
\[
v_C^*=\frac{2Mv}{D},\qquad
v_{\text{板}}^*=\frac{7Mv}{D},\qquad r\omega^*=\frac{5Mv}{D}.
\]
它们满足接触约束，且 $mv_C^*+Mv_{\text{板}}^*=Mv$，检查了总水平动量守恒。
\Step{从摩擦功率计算耗散}
球板系统的摩擦总功率为 $f(v_C+r\omega-v_{\text{板}})=fu\le0$。
$|u|$ 从 $v$ 线性减到零，滑动距离为 $vt_*/2$，故
\[
\Delta E=f\frac{vt_*}{2}=\frac{mMv^2}{7M+2m}.
\]
将三个末速度代入 $T_* =mv_C^{*2}/2+I_C\omega^{*2}/2+Mv_{\text{板}}^{*2}/2$，也得到 $Mv^2/2-T_* =\Delta E$。
过渡后无外驱动，可取静摩擦为零，三速度均保持不变；板足够长的条件保证这一时段不发生越界。'''
E[58]=r'''\Step{写明运动轴组的导数}
转弯角速率 $\Omega=u/R$，随飞机转弯的基矢满足
$\dot{\vect i}=\Omega\vect j$、$\dot{\vect j}=-\Omega\vect i$、$\dot{\vect k}=0$。
桨的总角速度为 $\vect\omega=\omega_s\vect j+\Omega\vect k$，故即使两速率恒定，仍有
$\vect\alpha=-\Omega\omega_s\vect i$。
\Step{从桨点相对位置计算绝对速度}
$\vartheta=\vartheta_0+\omega_st$，$\vect r_{AB}=l(\sin\vartheta\vect i+\cos\vartheta\vect k)$。
由 $\vect v_B=u\vect j+\vect\omega\times\vect r_{AB}$，逐项计算得到
\[
\vect v_B=\omega_sl\cos\vartheta\vect i
+(u+\Omega l\sin\vartheta)\vect j-\omega_sl\sin\vartheta\vect k.
\]
第一、三项是绕桨轴的相对速度，切向项包含飞机中心速度及桨点随转弯的牵连速度。
\Step{对空间速度求导，保留基矢变化}
$i$ 分量的求导给出 $-\omega_s^2l\sin\vartheta\vect i+\Omega\omega_sl\cos\vartheta\vect j$；
$j$ 分量的求导给出 $\Omega\omega_sl\cos\vartheta\vect j-\Omega(u+\Omega l\sin\vartheta)\vect i$；
$k$ 分量的求导给出 $-\omega_s^2l\cos\vartheta\vect k$。合并：
\[
\begin{aligned}
\vect a_B={}&-\left[\frac{u^2}{R}+l(\omega_s^2+\Omega^2)\sin\vartheta\right]\vect i\\
&+2\Omega\omega_sl\cos\vartheta\vect j-\omega_s^2l\cos\vartheta\vect k.
\end{aligned}
\]
\Step{用刚体加速度公式和极限检验}
同样的结果可由 $\vect a_A+\vect\alpha\times\vect r_{AB}+\vect\omega\times(\vect\omega\times\vect r_{AB})$ 得到。
两个不同来源的切向交叉项相加，产生系数 $2$。
$R\to\infty$ 且 $u$ 固定时，只剩桨自转的向心加速度；$\omega_s=0$ 时，恢复固定在飞机上的点随转弯运动的加速度。'''
E[59]=r'''\Step{从无外力矩的欧拉方程开始}
在本体主轴系中
\[
I_1\dot\omega_1=(I_2-I_3)\omega_2\omega_3,\quad
I_2\dot\omega_2=(I_3-I_1)\omega_3\omega_1,\quad
I_3\dot\omega_3=(I_1-I_2)\omega_1\omega_2.
\]
绕任一主轴的纯转动为精确解。线性化时保留 $W$ 与横向小扰动的乘积，舍去两个小扰动之积。
\Step{绕最大惯量轴的扰动}
令 $\omega_3=W$，$\omega_1=u,\omega_2=v$，一阶方程为
$I_1\dot u=-(I_3-I_2)Wv$、$I_2\dot v=(I_3-I_1)Wu$。
对第一式求导并代入第二式，得
\[
\ddot u+\nu_3^2u=0,\qquad
\nu_3^2=\frac{(I_3-I_2)(I_3-I_1)}{I_1I_2}W^2>0.
\]
例如 $u(0)=u_0,v(0)=v_0$ 时，
$u=u_0\cos\nu_3t-[(I_3-I_2)W/(I_1\nu_3)]v_0\sin\nu_3t$，扰动有界。
\Step{分别检查最小轴与中间轴}
绕第一轴同理得到
\[
\nu_1^2=\frac{(I_2-I_1)(I_3-I_1)}{I_2I_3}W^2>0,
\]
仍为振荡。绕第二轴，令 $\omega_2=W,\omega_1=u,\omega_3=v$，则
$I_1\dot u=-(I_3-I_2)Wv$、$I_3\dot v=-(I_2-I_1)Wu$，于是
\[
\ddot u-\lambda^2u=0,\qquad
\lambda^2=\frac{(I_2-I_1)(I_3-I_2)}{I_1I_3}W^2>0.
\]
通解含 $e^{\lambda t}$，一般小扰动会增长。
\Step{说明稳定性的含义与范围}
最大、最小惯量轴的自由转动在横向角速度的线性意义下稳定，中间惯量轴不稳定。
沿原轴的微小扰动只改变常转速，不产生上述横向恢复或增长。
当扰动增长到不再很小时须解非线性方程；重根、有外力矩或受轴承约束的转子均须另行分析。'''
E[60]=r'''\Step{积分轴对称自由陀螺的本体方程}
令 $I_1=I_2=A,I_3=C$。无矩时 $\omega_3=s$ 为常数，横向方程为
\[
\dot\omega_1=-n\omega_2,\quad\dot\omega_2=n\omega_1,\quad
n=\frac{C-A}{A}s.
\]
初始横向分量取 $(w,0)$，故
$\omega_1=w\cos nt,\omega_2=w\sin nt$。
代入数据 $n=(3-2)10/2=5\,\mathrm{s^{-1}}$，这是本体分量的有向旋转率。
\Step{由守恒角动量求空间进动率}
\[
L=\sqrt{A^2w^2+C^2s^2}=\sqrt{10^2+30^2}=10\sqrt{10}\,\mathrm{kg\,m^2\,s^{-1}}.
\]
取空间 $\zeta$ 轴沿 $\vect L$。由
$\vect L=A\vect\omega+(C-A)s\vect e_3$，叉乘 $\vect e_3$，得到
$\dot{\vect e}_3=\vect\omega\times\vect e_3=(\vect L/A)\times\vect e_3$。
所以 $\dot\varphi=L/A=5\sqrt{10}\simeq15.81139\,\mathrm{s^{-1}}$。
\Step{求三组夹角，避免混用角速度与角动量}
令 $\alpha=\angle(\vect\omega,\vect e_3)$、$\theta_0=\angle(\vect L,\vect e_3)$，则
\[
\tan\alpha=\frac ws=\frac12,\quad
\tan\theta_0=\frac{Aw}{Cs}=\frac13.
\]
故 $\alpha=26.56505^\circ$、$\theta_0=18.43495^\circ$。
本题 $A,C,s,w$ 均为正，$\vect L$ 与 $\vect\omega$ 在 $\vect e_3$ 的同一侧，二者夹角为
$\alpha-\theta_0=8.13010^\circ$。
\Step{还原欧拉角自转率并核验}
$\omega_3=\dot\psi+\dot\varphi\cos\theta_0=s$，而
$\dot\varphi\cos\theta_0=Cs/A=15\,\mathrm{s^{-1}}$，所以
$\dot\psi=10-15=-5\,\mathrm{s^{-1}}=-n$。
欧拉角自转率为负而实际轴向分量为正，两者关系由进动的轴向投影保证，没有矛盾。
这里 $\theta$ 恒定、角动量空间固定；角速度仍随体轴绕它进动。'''
E[61]=r'''\Step{列出定常进动的代数条件}
固定倾角 $\theta_0$、恒定轴向分量 $s$ 和进动率 $\Omega$ 必须满足倾角方程
\[
A\Omega^2\cos\theta_0-Cs\Omega+mgl=0.
\]
若 $\cos\theta_0\ne0$，实根存在的条件是
$(Cs)^2-4Amgl\cos\theta_0\ge0$。题给 $P=Cs=4\,\mathrm{kg\,m^2\,s^{-1}}$，代入得
$\Omega^2/2-4\Omega+1=0$。
\Step{解二次方程并区分两支}
\[
\Omega_\pm=\frac{4\pm\sqrt{16-2}}{1}
=4\pm\sqrt{14},
\]
即快支 $7.74166\,\mathrm{s^{-1}}$、慢支 $0.25834\,\mathrm{s^{-1}}$。
两支均需相应的初始进动速度；同一个完整初态不会任意选择其一。
\Step{计算欧拉角自转率}
由于 $s=\dot\psi+\Omega\cos\theta_0$，
\[
\dot\psi_+=8-\frac{7.74166}{2}=4.12917\,\mathrm{s^{-1}},\qquad
\dot\psi_-=8-\frac{0.25834}{2}=7.87083\,\mathrm{s^{-1}}.
\]
把它们与对应 $\Omega/2$ 相加都回到给定的轴向分量 $8$，可检查符号。
\Step{评估慢进动近似}
若忽略慢支方程中的二次项，$\Omega_{\text{慢}}\simeq mgl/P=0.25\,\mathrm{s^{-1}}$。
它相对精确慢支低估约 $(0.2583426-0.25)/0.2583426=3.23\%$。
小参数 $Amgl\cos\theta_0/P^2=1/32$ 控制这一近似；快支不可用此式计算。'''
E[62]=r'''\Step{由初值求三个积分常数}
采用 $\theta$ 从竖直向上量起，令 $P=L_3$、$K=L_\zeta$，并从总能量中扣去恒定自转能 $P^2/(2C)$，剩余能量记为 $E'$。初始 $\dot\theta=\dot\varphi=0,\omega_3=s$，故
\[
P=Cs,\qquad K=P\cos\theta_0,\qquad E'=mgl\cos\theta_0.
\]
\Step{求初始倾角加速度与进动率}
进动率由 $K=A\dot\varphi\sin^2\theta+P\cos\theta$ 给出：
\[
\dot\varphi=\frac{P(\cos\theta_0-\cos\theta)}{A\sin^2\theta}.
\]
初始确为零。倾角动力学为
$A\ddot\theta=A\dot\varphi^2\sin\theta\cos\theta-P\dot\varphi\sin\theta+mgl\sin\theta$，所以
$\ddot\theta(0)=mgl\sin\theta_0/A>0$，陀螺开始下倾。
\Step{建立章动转向点方程}
令 $u=\cos\theta,u_0=\cos\theta_0$。约化能量写为
\[
\frac A2\dot\theta^2+\frac{P^2(u_0-u)^2}{2A(1-u^2)}+mglu=mglu_0.
\]
乘以 $2(1-u^2)/A$，得到
\[
\dot u^2=(u_0-u)\left[\frac{2mgl}{A}(1-u^2)-\frac{P^2}{A^2}(u_0-u)\right].
\]
除初始根 $u_0$ 外，另一允许根 $u_1<u_0$ 满足
$2Amgl(1-u_1^2)=P^2(u_0-u_1)$。最大倾角是 $\arccos u_1$，并须检验 $-1\le u_1<u_0$ 及运动区间非负性。
\Step{解释尖点与高速小章动}
令 $\theta=\theta_0+\delta$，在 $|\delta|\ll1$ 时有效势能增量为
$P^2\delta^2/(2A)-mgl\sin\theta_0\delta$。
转向点满足其为零，故
$\delta_{\max}\simeq2Amgl\sin\theta_0/P^2$，要求此量远小于1。
初始轴轨迹速度为零，随后 $\delta\sim t^2$ 而 $\dot\varphi\sim t^2$，形成尖点。高速条件下平均慢进动约 $mgl/P$，但初始瞬间的进动率仍是零，不能直接替换为定常进动。'''
E[63]=r'''\Step{按给定方向参数化圆周}
取 $0\le\chi\le2\pi$，从 $+z$ 看逆时针，则
\[
\vect r=r(\cos\chi\vect i+\sin\chi\vect j),\qquad
\dd\vect s=r(-\sin\chi\vect i+\cos\chi\vect j)\dd\chi.
\]
题设 $\vect B=B\vect i$，所以 $\vect B\cdot\dd\vect s=-Br\sin\chi\dd\chi$。
\Step{逐分量保留位置权重}
\[
\oint(\vect B\cdot\dd\vect s)\vect r
=-Br^2\left[\vect i\int_0^{2\pi}\sin\chi\cos\chi\dd\chi
+\vect j\int_0^{2\pi}\sin^2\chi\dd\chi\right].
\]
第一积分的原函数为 $\sin^2\chi/2$，两端均为零；第二个用 $\sin^2\chi=(1-\cos2\chi)/2$ 得到 $\pi$。故结果为
\[
-\pi Br^2\vect j.
\]
\Step{解释闭合路径不能消去哪一项}
无权积分 $\oint\vect B\cdot\dd\vect s=B\oint\dd x=0$；本题则是 $B\oint\vect r\dd x$，$\vect r$ 沿路径变化，不能从积分中提出。
$x$ 分量是 $B\oint x\dd x=0$，$y$ 分量是 $B\oint y\dd x=-B\pi r^2$，亦可由有向面积核验。
反向绕行会使答案变号，$r\to0$ 时按面积趋零；量纲为磁场乘面积，与每项积分相符。'''
E[64]=r'''\Step{在同一空间中写速度与加速度变换}
恒定旋转角速度取 $\vect\Omega=-q\vect B/(2m)$，与磁场平行。旋转系中的导数记为撇号，则
\[
\vect v=\vect v'+\vect\Omega\times\vect r,\quad
\vect a=\vect a'+2\vect\Omega\times\vect v'
+\vect\Omega\times(\vect\Omega\times\vect r).
\]
中心势具有旋转不变性，所以 $-\nabla U$ 在旋转坐标中保持相同函数形式。
\Step{逐项代回并消去一阶速度项}
用 $q\vect B=-2m\vect\Omega$，有
\[
q\vect v'\times\vect B=2m\vect\Omega\times\vect v',
\]
恰与左侧科里奥利项相消。由牵连速度产生的洛伦兹项则为
\[
q(\vect\Omega\times\vect r)\times\vect B
=2m\vect\Omega\times(\vect\Omega\times\vect r).
\]
再扣除左侧一个离心型项，得到准确的旋转系方程
\[
m\vect a'=-\nabla U+m\vect\Omega\times(\vect\Omega\times\vect r).
\]
\Step{标明弱场近似的阶次与尺度}
最后一项为 $O(B^2)$，因此保留至 $B$ 的一阶时有 $m\vect a'\simeq-\nabla U$。
若无场运动特征频率为 $\omega_{\text{轨道}}$、尺度为 $r_0$，二阶项相对主加速度的量级为
$\Omega^2/\omega_{\text{轨道}}^2$，要求 $|\Omega|\ll\omega_{\text{轨道}}$。
\Step{还原物理含义与方向}
旋转系中轨道在一阶近似下保持无磁场形式；空间系观察到它以 $-q\vect B/(2m)$ 缓慢旋转。
负电荷的进动方向与正电荷相反，不能先取 $|q|$ 再推导。
自由粒子没有可比较的中心力轨道频率，故不能把此弱场结论用于将准确回旋频率误减半。'''
E[65]=r'''\Step{把两个横向方程合成一个复方程}
令 $w=x+\mathrm i y$、$b=qB/m$，由洛伦兹力的两个分量有
\[
\ddot x+\omega_c^2x=b\dot y,\qquad
\ddot y+\omega_c^2y=-b\dot x,
\]
因此 $\ddot w+\mathrm i b\dot w+\omega_c^2w=0$。
\Step{准确代入拉莫尔旋转}
取 $w=e^{\mathrm i\Omega t}w'$，则
$\dot w=e^{\mathrm i\Omega t}(\dot w'+\mathrm i\Omega w')$，
$\ddot w=e^{\mathrm i\Omega t}(\ddot w'+2\mathrm i\Omega\dot w'-\Omega^2w')$。
代入后一阶导数系数为 $\mathrm i(2\Omega+b)$；令 $\Omega=-b/2$，得到
\[
\ddot w'+(\omega_c^2+\Omega^2)w'=0.
\]
纵向没有磁力，仍为 $\ddot z'+\omega_c^2z'=0$。
\Step{还原惯性系模态与二阶展开}
旋转系两模态为 $w'\propto e^{\pm\mathrm i\nu t}$，$\nu=\sqrt{\omega_c^2+\Omega^2}$，所以惯性系的有向横向频率为
\[
\sigma_\pm=\Omega\pm\sqrt{\omega_c^2+\Omega^2}.
\]
在 $|\Omega|\ll\omega_c$ 时，
$\sqrt{\omega_c^2+\Omega^2}=\omega_c+\Omega^2/(2\omega_c)+O(\Omega^4/\omega_c^3)$。
一阶共同变化来自拉莫尔旋转，回复频率的二阶改变仍保留，故此变换不是任意磁场下的完全消磁。
\Step{检查无场与自由粒子极限}
$B=0$ 时两有向频率为 $\pm\omega_c$。
准确式取 $\omega_c=0$ 时，两频率之一为零、另一为 $2\Omega=-qB/m$，恢复静止导引中心和完整回旋运动。
这个极限须用准确式，不能使用已经要求 $|\Omega|\ll\omega_c$ 的展开。'''
E[66]=r'''\Step{统一磁场幅度与频率单位}
本题给定 $\gamma_n$ 的单位为 $\mathrm{rad\,s^{-1}\,T^{-1}}$，因此先得到角频率；普通频率必须另除 $2\pi$。
$B_1=10.0\,\mathrm{\mu T}=1.00\times10^{-5}\,\mathrm T$ 已是同向共振旋转分量，不须先减半。
\Step{计算静场的共振频率}
\[
\omega_0=|\gamma_n|B_0=(2.68\times10^8)(3.00)
=8.04\times10^8\,\mathrm{rad\,s^{-1}},
\]
\[
f_0=\frac{\omega_0}{2\pi}=1.27960574\times10^8\,\mathrm{Hz}
\simeq127.96\,\mathrm{MHz}.
\]
若误把 $8.04\times10^8$ 直接当作 Hz，会多出 $2\pi$ 倍。
\Step{在共振旋转系中积分翻转角}
忽略弛豫和失谐，横向有效场导致角速率
$\omega_1=|\gamma_n|B_1=2680\,\mathrm{rad\,s^{-1}}$。
恒幅矩形脉冲的翻转角为 $\beta=\omega_1\tau$，故
\[
\tau_{90}=\frac{\pi}{2\omega_1}=5.86118032\times10^{-4}\,\mathrm s
\simeq0.5861\,\mathrm{ms},
\]
\[
\tau_{180}=\frac{\pi}{\omega_1}=1.17223606\times10^{-3}\,\mathrm s
\simeq1.1722\,\mathrm{ms}.
\]
两时间之比为 $1:2$，且与 $B_1$ 成反比。
\Step{检查线偏振峰值的另一种约定}
线偏振场 $B_{\text{pk}}\cos\omega t\,\vect i$ 可分为两个反向旋转、幅度各为 $B_{\text{pk}}/2$ 的分量。
若 $10.0\,\mathrm{\mu T}$ 改指该峰值，在旋转波近似下有效 $B_1$ 为 $5.00\,\mathrm{\mu T}$，脉冲时间分别变为 $1.1722$、$2.3445\,\mathrm{ms}$，载频不变。
静场决定共振载频，射频旋转分量决定共振翻转速率；失谐时须改用倾斜有效场，不能直接沿用这些时间。'''
