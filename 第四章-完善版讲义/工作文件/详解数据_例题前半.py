E={
1:r'''\Step{先求动系导数}
动系观察者使用随框架转动的基矢 $\vect e_1,\vect e_2$。题设 $\vect G=G_0\vect e_1$ 中三个动系分量为 $(G_0,0,0)$，均不随时间改变，因此
\[
\left(\frac{\dd\vect G}{\dd t}\right)_{S'}=0.
\]
这一步只说明相对框架不变，尚不能判断矢量在空间中是否不变。
\Step{计入基矢转动}
在惯性系中 $\dot{\vect e}_1=\Om\times\vect e_1=\Omega\vect e_2$。由于 $G_0$ 是常量，
\[
\left(\frac{\dd\vect G}{\dd t}\right)_S
=G_0\dot{\vect e}_1=\Omega G_0\vect e_2.
\]
也可用运输定理写成 $0+\Om\times\vect G$，两种计算一致。
\Step{用固定坐标直接核验}
由初始轴线重合，$\vect e_1=\cos\Omega t\,\vect e_X+\sin\Omega t\,\vect e_Y$。逐项求导得
\[
\dot{\vect G}=G_0\Omega(-\sin\Omega t\,\vect e_X+\cos\Omega t\,\vect e_Y)
=G_0\Omega\vect e_2.
\]
该导数垂直于 $\vect G$，故只改变方向、不改变长度；当 $\Omega\to0$ 时两系导数都为零。''',
2:r'''\Step{把固定矢量投影到转动轴}
框架转角为 $\theta=\Omega t$。由基矢关系
\[
\vect e_1=\cos\theta\,\vect e_X+\sin\theta\,\vect e_Y,
\quad\vect e_2=-\sin\theta\,\vect e_X+\cos\theta\,\vect e_Y,
\]
反解得 $\vect e_X=\cos\theta\,\vect e_1-\sin\theta\,\vect e_2$。因此动系分量为
\[
G_1=G_0\cos\Omega t,\qquad G_2=-G_0\sin\Omega t,\qquad G_3=0.
\]
\Step{求动系矢量导数}
求动系导数时只对分量求导，基矢暂视为固定，故
\[
\left(\frac{\dd\vect G}{\dd t}\right)_{S'}
=-\Omega G_0\sin\Omega t\,\vect e_1-\Omega G_0\cos\Omega t\,\vect e_2.
\]
初始时它沿 $-\vect e_2$，符合动系向逆时针转、固定矢量在动系中向顺时针转的几何图像。
\Step{核验运输公式}
另有
\[
\Om\times\vect G
=\Omega G_0\sin\Omega t\,\vect e_1+\Omega G_0\cos\Omega t\,\vect e_2.
\]
两项逐分量抵消，得到 $(\dd\vect G/\dd t)_S=0$。本题与前一例恰好相反：固定的是惯性分量，动系分量必然变化。''',
3:r'''\Step{分别求导与转置}
记 $c_\theta=\cos\theta$、$s_\theta=\sin\theta$。链式法则给出
\[
\dot Q=\dot\theta\begin{pmatrix}-s_\theta&-c_\theta&0\\c_\theta&-s_\theta&0\\0&0&0\end{pmatrix},
\qquad Q^{\mathsf T}=\begin{pmatrix}c_\theta&s_\theta&0\\-s_\theta&c_\theta&0\\0&0&1\end{pmatrix}.
\]
\Step{逐项相乘识别角速度}
例如乘积的 $(1,1)$ 元为 $\dot\theta(-s_\theta c_\theta+c_\theta s_\theta)=0$，$(1,2)$ 元为 $-\dot\theta(s_\theta^2+c_\theta^2)=-\dot\theta$。其余项同理，
\[
\dot Q Q^{\mathsf T}=\begin{pmatrix}0&-\dot\theta&0\\\dot\theta&0&0\\0&0&0\end{pmatrix}.
\]
与一般叉乘矩阵 $[\Om]_\times$ 对照，可读出 $\Omega_X=\Omega_Y=0$、$\Omega_Z=\dot\theta$，即 $\Om=\dot\theta\vect e_Z$。
\Step{说明适用条件}
推导只使用了 $\theta(t)$ 的一阶导数，没有令 $\ddot\theta=0$，所以也适用于非匀速定轴转动。若 $\dot\theta$ 改变符号，转向也随之改变。矩阵 $\dot Q Q^{\mathsf T}$ 的量纲为时间的倒数，与角速度一致。''',
4:r'''\Step{给出两个框架的实际差别}
框架甲的三个轴都固定，所以它的基矢导数均为零，角速度为 $\Om_{\text{甲}}=0$。框架乙虽然保持同一根竖轴，却有
\[
\dot{\vect e}_1=\Omega\vect e_2,\qquad
\dot{\vect e}_2=-\Omega\vect e_1,\qquad \dot{\vect e}_3=0.
\]
因此只比较竖轴导数，无法区分甲、乙。
\Step{从角速度公式说明原因}
由 $\dot{\vect e}_3=\Om\times\vect e_3=0$，只能推出 $\Om$ 平行于 $\vect e_3$ 或为零，不能推出角速度必为零。沿竖轴方向的任意角速度分量都不会改变这根轴本身。
\Step{恢复乙框架的角速度}
用三根基矢共同恢复，
\[
\Om_{\text{乙}}=\frac12\sum_i\vect e_i\times\dot{\vect e}_i
=\frac12\bigl(\Omega\vect e_1\times\vect e_2-\Omega\vect e_2\times\vect e_1\bigr)
=\Omega\vect e_3.
\]
所以两框架并不相同。指定参考系时，除轴向外，还必须交代水平轴绕该轴如何转动。''',
5:r'''\Step{写出相对运动与框架运动}
取随管转动的 $\vect e_1$ 沿管向外，$\vect e_2=\vect e_z\times\vect e_1$。由 $r=r_0+ut$，有
\[
\vect r=r\vect e_1,\quad\vect v'=u\vect e_1,\quad\vect a'=0,
\quad\Om=\Omega\vect e_z,\quad\dot\Om=0.
\]
原点固定，所以没有平动加速度项。
\Step{计算两个非零附加项}
利用 $\vect e_z\times\vect e_1=\vect e_2$、$\vect e_z\times\vect e_2=-\vect e_1$，
\[
\Om\times(\Om\times\vect r)=-\Omega^2r\vect e_1,
\qquad 2\Om\times\vect v'=2\Omega u\vect e_2.
\]
从而绝对加速度为
\[
\vect a=-\Omega^2(r_0+ut)\vect e_1+2\Omega u\vect e_2.
\]
径向分量指向转轴，切向分量沿转动正向。
\Step{检查结果与模型限制}
在固定坐标中写 $\vect r=(r_0+ut)(\cos\Omega t\,\vect e_X+\sin\Omega t\,\vect e_Y)$，二次求导也得到上述两项。$u=0$ 时退化为盘上固定点的向心加速度；$\Omega=0$ 时加速度为零。这里的匀速滑动由装置控制，不能直接当作无沿管力的自由珠运动。''',
6:r'''\Step{先在动系基矢上列完整矢量式}
原点加速度为 $A\vect e_X$，管角速度恒定，珠子的相对加速度为零。故
\[
\vect a=A\vect e_X-\Omega^2r\vect e_1+2\Omega u\vect e_2.
\]
此式已经区分原点平动、向轴加速度与科氏加速度，不能把第一项并入半径 $r$。
\Step{投影原点加速度}
因为 $\vect e_1$ 与 $X$ 轴夹角为 $\theta$，而 $\vect e_2$ 是其逆时针转 $90^\circ$ 的方向，
\[
\vect e_X=\cos\theta\,\vect e_1-\sin\theta\,\vect e_2.
\]
于是
\[
a_1=A\cos\theta-\Omega^2r,\qquad a_2=-A\sin\theta+2\Omega u.
\]
\Step{解释符号并检验}
$-\Omega^2r$ 总沿管向轴内；向外相对运动产生正切向科氏加速度。小车向固定 $X$ 方向加速，其在旋转管轴上的投影则随 $\theta$ 改变。$A=0$ 时恢复固定轴径向管结果；$\theta=0$ 时小车加速度只有沿管分量，切向分量仍为 $2\Omega u$。''',
7:r'''\Step{先写模长条件}
设 $\alpha$ 为 $\Om$ 与 $\vect v'$ 的夹角，则
\[
a_c=2|\Om\times\vect v'|=2\Omega v'|\sin\alpha|.
\]
叉乘为零的充要条件是其中一个矢量为零，或者两个非零矢量平行或反平行。
\Step{逐种判断题设情形}
参考系不转动时 $\Om=0$，没有科氏项；质点固定于动系时 $\vect v'=0$，也没有科氏项；沿转轴运动时 $\vect v'\parallel\Om$，即使相对速率不为零，科氏项仍为零。三种情形均符合上述统一条件。
\Step{排除容易混淆的判断}
相对速率恒定只限制 $v'$ 的大小，并不限制它与转轴的夹角。沿水平径向管匀速外滑就是反例：相对轨迹为直线、速率恒定，却有 $a_c=2\Omega u$。同样，“没有主动力”也不保证科氏项为零。判断时应直接检查叉乘中的两个矢量。''',
8:r'''\Step{速度由两个正交分量合成}
取径向、切向基矢为 $\er,\et$。相对速度为 $u\er$，牵连速度为 $\Omega r\et$，因此
\[
\vect v=u\er+\Omega r\et,\quad v=\sqrt{u^2+\Omega^2r^2},\quad
\tan\beta=\frac{\Omega r}{u}.
\]
这里 $\beta$ 是绝对速度与向外径向的夹角。两位置分别为
\begin{align*}
\vect v_{R/3}&=u\er+\frac{\Omega R}{3}\et,& v_{R/3}&=\sqrt{u^2+\frac{\Omega^2R^2}{9}},\\
\vect v_R&=u\er+\Omega R\et,&v_R&=\sqrt{u^2+\Omega^2R^2}.
\end{align*}
\Step{加速度要计入科氏项}
因为 $\dot r=u$ 恒定，相对加速度为零，但管的转动仍给出
\[
\vect a=-\Omega^2r\er+2\Omega u\et.
\]
所以
\begin{align*}
\vect a_{R/3}&=-\frac{\Omega^2R}{3}\er+2\Omega u\et,\\
\vect a_R&=-\Omega^2R\er+2\Omega u\et,\qquad
|\vect a|=\sqrt{\Omega^4r^2+4\Omega^2u^2}.
\end{align*}
两位置的科氏分量相等，向轴分量却与半径成正比。
\Step{消去时间求轨迹}
由 $r=r_0+ut$、$\theta=\theta_0+\Omega t$，消去 $t$ 得
\[
r=r_0+\frac{u}{\Omega}(\theta-\theta_0).
\]
这是阿基米德螺线的一段。因而管中所见的匀速直线运动，在惯性系中既不是直线，也不是恒速运动。''',
9:r'''\Step{用绝对速率约束求径向方程}
绝对速度为 $\dot r\er+\Omega r\et$，两分量正交。规定 $|\vect v|=c$，即
\[
\dot r^2+\Omega^2r^2=c^2.
\]
最初向外运动，须选 $\dot r=+\sqrt{c^2-\Omega^2r^2}$；这个符号只适用于首个向外阶段。
\Step{积分并施加初条件}
分离变量并由 $r(0)=0$ 定积分，
\[
\int_0^{r(t)}\frac{\dd q}{\sqrt{c^2-\Omega^2q^2}}=t,
\qquad \arcsin\frac{\Omega r}{c}=\Omega t.
\]
因此
\begin{equation}
r(t)=\frac c\Omega\sin\Omega t,\quad\dot r=c\cos\Omega t,
\quad 0\le t\le\frac\pi{2\Omega}.\label{eq:constspeed}
\end{equation}
在 $t_*=\pi/(2\Omega)$ 时，$\dot r=0$、$r_{\max}=c/\Omega$，全部绝对速度都成为切向分量。不能超过此时仍沿用“向外”的正平方根分支。
\Step{还原惯性系中的轨迹}
初始轴重合，$X=r\cos\Omega t$、$Y=r\sin\Omega t$，于是
\[
X=\frac{c}{2\Omega}\sin2\Omega t,\qquad
Y=\frac{c}{2\Omega}(1-\cos2\Omega t).
\]
消去时间得 $X^2+(Y-c/(2\Omega))^2=(c/(2\Omega))^2$。首个向外阶段对应 $X\ge0$ 的半圆，从原点到 $(0,c/\Omega)$；这也说明径向速度变为零并不代表质点绝对停止。''',
10:r'''\Step{分别识别两种运动}
在只随调速器绕竖轴转动的框架中，小球沿摆角增大的方向运动，相对速率为 $v'=l|\dot\theta|$。其距竖轴的距离为 $\rho=l\sin\theta$，故牵连速率为 $v_t=\Omega\rho$。
\Step{说明为何可以平方相加}
相对速度位于径向竖直平面内，牵连速度沿方位切向，垂直该平面，因而
\[
\vect v'\cdot\vect v_t=0,\qquad
v^2=l^2\dot\theta^2+\Omega^2l^2\sin^2\theta.
\]
若不先辨认方向，直接把两个速率相加，会把正交运动误作同向运动。
\Step{代入数值并检查单位}
\[
v'=0.50\times0.20=0.10\,\mathrm{m/s},\quad
\rho=0.50\sin30^\circ=0.25\,\mathrm m,
\]
\[
v_t=6.0\times0.25=1.50\,\mathrm{m/s},\qquad
v=\sqrt{0.10^2+1.50^2}=\sqrt{2.26}\approx1.503\,\mathrm{m/s}.
\]
结果略大于牵连速率，符合较小的正交相对速度只使合速率略有增加的情况。若 $\dot\theta=0$，便退化为小球随框架作定半径圆周运动。''',
11:r'''\Step{相对运动和框架运动分别计算}
槽中心与转轴重合，质点在半径 $a$ 的圆周上，故
\[
\vect v'=a\nu\et,\qquad\vect a'=-a\nu^2\er,
\quad\vect v_t=a\Omega\et,\quad\vect a_t=-a\Omega^2\er.
\]
$\Omega,\nu$ 都带符号，而各自的向心加速度包含平方，不随单独转向改变。
\Step{保留科氏项的有符号乘积}
利用 $\vect e_z\times\et=-\er$，
\[
\vect a_c=2\Omega\vect e_z\times(a\nu\et)=-2a\Omega\nu\er.
\]
当两种转动反向时 $\Omega\nu<0$，这项沿径向向外，并非总是向心。
\Step{合成并用直接法核验}
\begin{equation}
\vect v=a(\Omega+\nu)\et,\qquad
\vect a=-a(\Omega+\nu)^2\er.\label{eq:groove}
\end{equation}
惯性系方位角为 $\theta=\theta_0+(\Omega+\nu)t$，所以直接把它视为角速度 $\Omega+\nu$ 的圆周运动，也给出同样答案。$\nu=0$ 时恢复盘上固定点；$\nu=-\Omega$ 时绝对速度、加速度同时为零。''',
12:r'''\Step{先合成速度}
取正切向为逆时针，珠子相对速度为 $-a\Omega\et$，框架牵连速度为 $+a\Omega\et$，所以
\[
\vect v=-a\Omega\et+a\Omega\et=0.
\]
由于 $\nu=-\Omega$ 始终成立，惯性方位角保持常数，质点在惯性空间确实停在同一点。
\Step{逐项检查加速度}
相对圆周运动给出 $\vect a'=-a\Omega^2\er$；框架向轴项为 $-a\Omega^2\er$。科氏项为
\[
2\Om\times\vect v'=2\Omega\vect e_z\times(-a\Omega\et)
=+2a\Omega^2\er.
\]
因此
\[
\vect a=(-a\Omega^2-a\Omega^2+2a\Omega^2)\er=0.
\]
\Step{指出这个检验的用途}
动系观察者仍看到质点沿槽转动，其相对加速度也不为零；这些量不能与绝对量混同。若把科氏项漏掉系数 $2$，或误认为它总向内，就无法得到这个应当严格成立的静止极限。''',
13:r'''\Step{把偏心圆槽拆成两段位置}
令 $\vect e_\rho=\cos\psi\,\vect e_1+\sin\psi\,\vect e_2$ 指向 $CP$，其正切向为 $\vect e_\psi$。则
\[
\vect r=d\vect e_1+a\vect e_\rho,\quad
\vect v'=a\nu\vect e_\psi,\quad\vect a'=-a\nu^2\vect e_\rho.
\]
其中 $d\vect e_1$ 在盘上固定，所以不贡献相对速度，却贡献牵连加速度。
\Step{分别计算牵连和科氏项}
所有位置都在水平面内，故
\[
\vect a_t=-\Omega^2d\vect e_1-\Omega^2a\vect e_\rho,
\qquad\vect a_c=-2\Omega\nu a\vect e_\rho.
\]
将三项相加，得到
\[
\vect a=-\Omega^2d\vect e_1-a(\Omega+\nu)^2\vect e_\rho.
\]
\Step{用几何分解解释结果}
第一项正是槽中心 $C$ 绕 $O$ 的加速度；第二项是质点相对移动中心 $C$ 的惯性圆周加速度。只有 $d=0$ 才退化为同心槽公式。即使 $\nu=-\Omega$，第二项为零，中心 $C$ 的运动仍可使质点加速，不能把前一例的绝对静止结论直接搬来。''',
14:r'''\Step{选择中间框架计算}
在 $S_1$ 中，质点随 $S_2$ 转动而具有相对速度
\[
\vect v'_1=\Om_{21}\times\vect r.
\]
再加上 $S_1$ 的牵连速度 $\Om_1\times\vect r$，得到
\[
\vect v=(\Om_1+\Om_{21})\times\vect r.
\]
这里所有角速度都必须先表示成同一空间基矢下的矢量。
\Step{改选完全随体框架计算}
因 $P$ 固定在 $S_2$，$\vect v'_2=0$。然而该框架相对惯性系的角速度是总角速度
\[
\Om_2=\Om_1+\Om_{21},
\]
所以仍有 $\vect v=\Om_2\times\vect r$，与前式逐项一致。
\Step{说明常见漏项}
若选择 $S_1$ 却把 $\vect v'_1$ 设为零，就会漏掉第二级转动；若选择 $S_2$ 却只用 $\Om_1$ 作牵连角速度，也会漏掉同一项。框架选择可以改变相对运动与牵连运动的划分，却不能改变同一点的绝对速度。''',
17:r'''\Step{先计算距轴的垂直距离}
位置 $\vect r=h\vect n$ 完全沿转轴，故
\[
\vect R_\perp=\vect r-(\vect r\cdot\vect n)\vect n
=h\vect n-h\vect n=0.
\]
质点到原点的距离虽然是 $|h|$，到转轴的距离却为零。
\Step{直接计算离心力}
由 $\Om=\Omega\vect n$，内层叉乘已经为零：
\[
\Om\times\vect r=\Omega h\vect n\times\vect n=0,
\qquad\vect F_{\rm cf}=-m\Om\times(\Om\times\vect r)=0.
\]
在固定原点、匀速定轴且相对静止的题设下，质点的绝对速度和加速度也都为零。
\Step{说明公式中的半径含义}
标量式 $F_{\rm cf}=m\Omega^2R_\perp$ 中必须使用垂直距轴距离，不能用任意位矢的模。把它写成 $m\Omega^2h$ 会凭空赋予轴上点一个圆周运动。若原点加速或轴向改变，可能另有平动、欧拉惯性力，但那也不是本题的离心力。''',
18:r'''\Step{固定基矢的叉乘规则}
右手正交基矢满足
\[
\vect e_z\times\er=\et,\qquad
\vect e_z\times\et=-\er.
\]
科氏惯性力为 $\vect F_{\rm Co}=-2m\Omega\vect e_z\times\vect v'$，因此要在右手叉乘方向之后再取负号。
\Step{逐一代入四种速度}
\begin{align*}
\vect v'=+u\er&:\quad\vect F_{\rm Co}=-2m\Omega u\et,\\
\vect v'=-u\er&:\quad\vect F_{\rm Co}=+2m\Omega u\et,\\
\vect v'=+u\et&:\quad\vect F_{\rm Co}=+2m\Omega u\er,\\
\vect v'=-u\et&:\quad\vect F_{\rm Co}=-2m\Omega u\er.
\end{align*}
四种情形的力的大小相同，都是 $2m\Omega u$，方向则分别沿负切向、正切向、径向向外、径向向内。
\Step{做方向和功率检验}
从盘上俯视，惯性力总位于相对速度的右侧 $90^\circ$。逐行点乘相应 $\vect v'$ 都得到零，符合科氏力不做相对功的性质。这里求的是惯性力；若求科氏加速度，四个方向必须全部反转。''',
19:r'''\Step{分别写出该质量微元的惯性力}
上跨段中点的位置为 $\vect r=a\vect e_y$，相对速度为 $u\vect e_x$。框架匀速逆时针转动，没有欧拉项。离心力向外，
\[
\vect F_{\rm cf}=m\Omega_c^2a\vect e_y.
\]
又因 $\vect e_z\times\vect e_x=\vect e_y$，科氏惯性力为
\[
\vect F_{\rm Co}=-2m\Omega_cu\vect e_y,
\]
沿该处径向向轴内。
\Step{比较大小而非只凭旋向判断}
两项共线，故
\[
\vect F_{\rm in}=m(\Omega_c^2a-2\Omega_cu)\vect e_y
=m\Omega_c^2a\left(1-\frac{2u}{\Omega_ca}\right)\vect e_y.
\]
当 $u<\Omega_ca/2$ 时合力向外；相等时抵消；当 $u>\Omega_ca/2$ 时合力改为向内。
\Step{说明比较参数的适用范围}
若用轮相对角速率表示循环速率，$u=|\omega_r|a$，本位置的反转条件可写为 $2|\omega_r|>\Omega_c$。这里同时利用了该点距整体转轴也恰为 $a$；在其他距轴半径 $r$ 的位置，须比较 $2u/(\Omega_cr)$。这个合力只表示惯性效应，实际皮带形状仍由张力、运动曲率及端部条件决定。''',
20:r'''\Step{在座舱系建立静力平衡}
座舱没有转动，只有平动惯性力。单位质量真实重力为 $-g\vect e_z$，惯性力对应 $-A\vect e_z$，所以
\[
\vect g_{\rm eff}=-(g+A)\vect e_z.
\]
液体相对静止，取高度方向的小体元，竖直力平衡给出
\[
-\frac{\dd p}{\dd z}-\rho(g+A)=0.
\]
\Step{对两点之间的压强梯度积分}
$\rho,g,A$ 在液柱范围内均视为常量，故
\[
p(z+h)-p(z)=\int_z^{z+h}-\rho(g+A)\,\dd q=-\rho(g+A)h.
\]
当 $g+A>0$ 时上方压强较低，下面减上面的压强差为 $\rho(g+A)h$。
\Step{检查典型极限}
$A=0$ 时恢复通常静液压；向上加速 $A>0$ 时压强梯度增大；自由落体 $A=-g$ 时该理想模型中压强梯度为零；若 $A<-g$，有效重力反向。单位为 $(\mathrm{kg/m^3})(\mathrm{m/s^2})\mathrm m=\mathrm{Pa}$。这些判断来自加速度，而不是舱体速度的方向。''',
21:r'''\Step{把曲率先转换成加速度}
圆弧运动的法向加速度大小为 $V^2/\rho_c$，总指向曲率中心。最低点的加速度向上，最高点的加速度向下。取竖直向上为正，分别有
\[
A_{\rm low}=+\frac{V^2}{\rho_c},\qquad
A_{\rm high}=-\frac{V^2}{\rho_c}.
\]
\Step{由真实受力求有符号支持力}
对乘员在惯性系写 $N-mg=mA$，因而
\[
n=\frac N{mg}=1+\frac Ag.
\]
代入两种 $A$，得到
\[
n_{\rm low}=1+\frac{V^2}{g\rho_c},\qquad
n_{\rm high}=1-\frac{V^2}{g\rho_c}.
\]
舱内有效重力相应为 $-(g+A)\vect e_z$，最低点向下增强，最高点向下减弱。
\Step{解释失重与负载荷}
最高点 $V^2/\rho_c=g$ 时 $N=0$，即失重；若更大，则 $N<0$，维持既定轨迹需要安全带或其他约束向下拉住乘员，不能再由普通座垫单向推力实现。$V\to0$ 时两处均恢复 $n=1$。载荷的直接依据是曲率加速度，不是飞行器正在上升还是下降。''',
22:r'''\Step{写出物块的真实加速度}
物块相对盘静止，半径 $a$ 不变，但框架角速度在变化。绝对加速度为
\[
\vect a=-\Omega^2a\er+\dot\Omega a\et.
\]
由于没有相对速度，本题科氏项为零；切向项来自角加速度。
\Step{由牛顿方程确定摩擦力}
竖直方向没有加速度，所以 $N=mg$。水平方向唯一真实力是静摩擦力，故
\[
\vect f=m\vect a=-m\Omega^2a\er+m\dot\Omega a\et.
\]
两个分量正交，所需摩擦力大小为
\[
f=ma\sqrt{\Omega^4+\dot\Omega^2}.
\]
\Step{施加最大静摩擦条件}
静摩擦力可在 $0$ 与 $\mu_sN$ 之间自行调整，保持不滑动要求
\[
a\sqrt{\Omega^4+\dot\Omega^2}\le\mu_sg.
\]
仅在匀速时才简化为 $\Omega^2a\le\mu_sg$。加速转盘还需要切向摩擦；即使当前 $\Omega$ 很小，也可能因 $|\dot\Omega|$ 大而滑动。$\Omega^4$ 与 $\dot\Omega^2$ 的量纲同为 $\mathrm{s^{-4}}$，根号后再乘 $a$ 正好为加速度。'''
}
