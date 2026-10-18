from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
D=P/'题图';D.mkdir(exist_ok=True)
# All figures depict stated geometry/initial conditions; arrows in problem drawings are not computed answers.
start=r'''\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth,every node/.style={font=\small,inner sep=1.5pt,text=black},line width=.65pt]
'''
end='\n\\end{tikzpicture}\n'
def fig(body):return start+body+end
F={}
F['frame']=r'''\draw[->,gray] (0,0)--(3.5,0)node[right]{$X$};\draw[->,gray](0,0)--(0,2.7)node[above]{$Y$};
\draw[->](0,0)--(2.9,1.67)node[right]{$\vect e_1$};\draw[->](0,0)--(-1.1,1.91)node[above]{$\vect e_2$};
\draw[->](.9,0)arc(0:30:.9);\node at(1.18,.3){$\theta$};\node[below left]at(0,0){$O$};
\draw[->](2.6,2.15)arc(0:115:.5);\node at(2.4,2.85){$\Omega$};'''
F['frame_gmoving']=F['frame']+r'\draw[->,very thick,ink](0,0)--(1.95,1.125)node[midway,above]{$\vect G$};'
F['frame_gfixed']=F['frame']+r'\draw[->,very thick,ink](0,0)--(2.1,0)node[midway,below]{$\vect G$};'
F['frame_force']=F['frame']+r'\draw[->,very thick,ink](.6,-.65)--(2.5,-.65)node[midway,below]{$F_0\vect E_X$};'
F['zero']=r'''\node at(0,2.3){(a) $\Omega=0$};\node at(2.6,2.3){(b) $v'=0$};
\fill(0,1.55)circle(2pt);\draw[->](0,1.55)--(.9,1.55)node[right]{$\vect v'$};
\fill(2.6,1.55)circle(2pt);\draw[->](2.6,1.55)--(2.6,2.05)node[right]{$\Om$};
\node at(1.2,.6){(c) $\vect v'\parallel\Om$};\draw[->](.6,-.2)--(.6,.35)node[left]{$\Om$};\draw[->](1.7,-.2)--(1.7,.35)node[right]{$\vect v'$};'''
F['tube']=r'''\draw[thick](-.2,-.13)--(3.4,-.13);\draw[thick](-.2,.13)--(3.4,.13);
\draw[->,gray](0,-.65)--(0,1.5)node[above]{$\vect e_2$};\draw[->,gray](0,0)--(3.8,0)node[right]{$\vect e_1$};
\fill(0,0)circle(2pt)node[below left]{$O$};\fill(2,0)circle(3pt)node[above right=5pt]{$m$};
\draw[<->](0,-.5)--(2,-.5)node[midway,below]{$x$};\draw[->,thick](2,.5)--(3,.5)node[midway,above]{$\dot x$};
\draw[->](.1,.55)arc(0:120:.45);\node at(-.4,1.15){$\Omega$};'''
F['tube_u']=F['tube'].replace(r'$\dot x$',r'$u$').replace(r'$x$',r'$r$')
F['tube_R']=F['tube_u'].replace(r'\draw[<->](0,-.5)--(2,-.5)node[midway,below]{$r$};','').replace(r'\fill(2,0)circle(3pt)node[above right=5pt]{$m$};','')+r'\fill(1.13,0)circle(2.5pt)node[above=7pt]{$P_1$};\fill(3.4,0)circle(2.5pt)node[above=7pt]{$P_2$};\draw[dashed](1.13,-.13)--(1.13,-.65);\draw[<->](0,-.65)--(1.13,-.65)node[midway,below]{$R/3$};\draw[dashed](3.4,-.13)--(3.4,-1.25);\draw[<->](0,-1.25)--(3.4,-1.25)node[midway,below]{$R$};'
F['tube_c']=F['tube'].replace(r'$\dot x$',r'$\dot r$').replace(r'$x$',r'$r$')+r'\node[align=center]at(1.75,1.55){$|\vect v|=c$\\$r(0)=0$};'
F['tube_end']=F['tube']+r'\draw[dashed](3.4,-.25)--(3.4,.9)node[above]{$L$};\node at(1.4,-1.1){$x(0)=a,\ \dot x(0)=0$};'
F['tube_power']=F['tube']+r'\draw[->,thick,ink](2,0)--(2,1.35)node[above]{$N_2$};'
F['cart']=r'''\draw[rounded corners=2pt](-.5,-.6)rectangle(2.9,.05);\draw(0,-.78)circle(.18);\draw(2.3,-.78)circle(.18);
\draw[->,gray](0,0)--(3.4,0)node[right]{$X$};\draw[thick](0,0)--(2.6,1.5)node[right]{$\vect e_1$};
\draw[->](0,0)--(-.8,1.39)node[above]{$\vect e_2$};\fill(1.65,.95)circle(3pt)node[above]{$m$};
\draw[->](1.8,1.25)--(2.6,1.71)node[midway,above]{$u$};\draw[->](.8,-1.2)--(2.2,-1.2)node[midway,below]{$A\vect E_X$};
\draw(.7,0)arc(0:30:.7);\node at(.95,.25){$\theta$};\node[below left]at(0,0){$O'$};\node at(.2,2){$\Omega\vect e_z$};'''
F['circle']=r'''\draw(0,0)circle(1.45);\draw[->,gray](-1.8,0)--(1.95,0)node[right]{$x$};\draw[->,gray](0,-1.75)--(0,1.9)node[above]{$y$};
\coordinate(P)at(35:1.45);\draw[->](0,0)--(P)node[midway,above]{$a$};\fill(P)circle(3pt)node[right]{$P$};
\draw[->,thick](35:1.45)arc(35:75:1.45);\node at(1.3,1.65){$\nu$};\draw[->](-1.45,-1.45)arc(225:295:2.05);\node at(0,-2.35){$\Omega$};\node[below left]at(0,0){$O$};'''
F['circle_reverse']=F['circle'].replace(r'arc(35:75:1.45)',r'arc(35:-5:1.45)').replace(r'$\nu$',r'$\nu=-\Omega$')
F['eccentric']=r'''\draw[->,gray](-.3,0)--(3.9,0)node[right]{$\vect e_1$};\draw[->,gray](0,-1.4)--(0,1.9)node[above]{$\vect e_2$};
\draw(2.1,0)circle(1.12);\fill(0,0)circle(2pt)node[below left]{$O$};\fill(2.1,0)circle(2pt)node[below]{$C$};
\coordinate(P)at(2.74,.917);\draw(2.1,0)--(P)node[midway,right]{$a$};\fill(P)circle(3pt)node[above]{$P$};
\draw[<->](0,-.55)--(2.1,-.55)node[midway,below]{$d$};\draw(2.65,0)arc(0:55:.55);\node at(2.8,.28){$\psi$};\node at(.8,1.45){$\Omega$};\node at(2.8,1.65){$\nu$};'''
F['nested']=r'''\node (S) at(0,2.3){$S$};\node (S1) at(2.2,2.3){$S_1$};\node (S2) at(4.4,2.3){$S_2$};
\draw[->,shorten <=4pt,shorten >=4pt](S)--(S1)node[midway,above]{$\Om_1$};\draw[->,shorten <=4pt,shorten >=4pt](S1)--(S2)node[midway,above]{$\Om_{21}$};
\fill(1,0)circle(2pt)node[left]{$O$};\draw[->](1,0)--(3.7,1.2)node[midway,above]{$\vect r$};\fill(3.7,1.2)circle(3pt)node[right]{$P$};\node at(2.6,-.55){$P$ 固定在 $S_2$};'''
F['precession']=r'''\draw[->,gray](0,-.3)--(0,3.3)node[above]{$Z$};\draw[->,thick](0,0)--(1.7,2.7)node[above]{$\vect n$};
\fill(1.08,1.72)circle(3pt)node[right]{$P$};\node[left]at(0,0){$O$};\node at(.9,.85){$h$};
\draw(0,.9)arc(90:58:.9);\node at(.35,1.13){$\alpha$};
\draw[->](-.45,2.65)arc(180:0:.45 and .18);\node[left]at(-.45,2.7){$\Omega_p$};
\node[right]at(1.8,2.1){$\omega_s$};'''
F['axispoint']=r'''\draw[->](0,-.2)--(0,3.3)node[above]{$\vect n,\ \Om$};\fill(0,0)circle(2pt)node[left]{$O$};\fill(0,2.05)circle(3pt)node[right]{$P(m)$};\draw[<->](-.6,0)--(-.6,2.05)node[midway,left]{$h$};\draw[dashed](-1.5,0)--(1.6,0);\node at(0,-.6){点 $P$ 位于转轴上};'''
F['four']=r'''\fill(0,0)circle(3pt)node[below left]{$P$};\draw[->,thick](0,0)--(1.6,0)node[right]{$+u\vect e_r$};\draw[->,thick](0,0)--(-1.6,0)node[left]{$-u\vect e_r$};\draw[->,thick](0,0)--(0,1.5)node[above]{$+u\vect e_\theta$};\draw[->,thick](0,0)--(0,-1.4)node[below]{$-u\vect e_\theta$};\node at(1.75,1.3){$\odot\ \Om$};'''
F['belt']=r'''\draw(-1.4,0)circle(.75);\draw(1.4,0)circle(.75);\draw(-1.4,.75)--(1.4,.75);\draw(-1.4,-.75)--(1.4,-.75);
\draw[->,gray](-2.35,0)--(2.55,0)node[right]{$x$};\draw[->,gray](0,-1.2)--(0,1.65)node[above]{$y$};
\fill(0,.75)circle(3pt)node[above left]{$P$};\node[below left]at(0,0){$O$};\draw[->,thick](.2,1.05)--(1.2,1.05)node[midway,above]{$u$};\draw[<->](-.4,0)--(-.4,.75)node[midway,left]{$a$};\node at(1.8,1.7){$\Omega_c>0$};'''
F['liquid']=r'''\draw[thick](0,2.6)--(0,0)--(2.3,0)--(2.3,2.6);\draw(0,2.3)--(2.3,2.3);\node at(1.15,1.2){$\rho$};\fill(.65,.6)circle(2pt)node[left]{$z$};\fill(.65,1.8)circle(2pt)node[left]{$z+h$};\draw[<->](1.9,.6)--(1.9,1.8)node[midway,right]{$h$};\draw[->](3,.5)--(3,2.1)node[above]{$A\vect e_z$};\draw[->](-.8,2.2)--(-.8,1.1)node[below]{$g$};'''
F['flight']=r'''\draw(-.99,1.01)arc(225:315:1.4);\draw(2.01,1.19)arc(135:45:1.4);
\fill(0,.6)circle(3pt);\fill(3,1.6)circle(3pt);\draw[->](0,.6)--(0,1.65)node[above]{$\vect a$};\draw[->](3,1.6)--(3,.55)node[below]{$\vect a$};
\draw[->](0,.6)--(.8,.6)node[right]{$V$};\draw[->](3,1.6)--(3.8,1.6)node[right]{$V$};\node at(0,-.2){最低点};\node at(3,2.3){最高点};\node at(1.5,2.9){曲率半径 $\rho_c$};'''
F['disk']=r'''\draw(0,0)circle(1.5);\draw[->,gray](-1.75,0)--(2,0)node[right]{$\vect e_r$};\draw[->,gray](1,0)--(1,1.4)node[above]{$\vect e_\theta$};\draw[fill=white](.82,-.17)rectangle(1.18,.17);\node[below]at(1,-.2){$m$};\draw[<->](0,-.55)--(1,-.55)node[midway,below]{$a$};\node[left]at(0,0){$O$};\draw[->](-.4,1.78)arc(103:145:1.82);\node at(-.55,2){$\Omega(t)$};'''
F['disk_fixed']=F['disk'].replace(r'$\Omega(t)$',r'$\Omega$')
F['pendulum']=r'''\draw[dashed](0,-.3)--(0,3.3);\coordinate(A)at(0,2.8);\coordinate(P)at(1.45,.29);\draw[very thick](A)--(P)node[midway,right]{$l$};\fill(A)circle(2pt)node[above left]{$O$};\fill(P)circle(3pt)node[below right]{$m$};\draw(0,1.95)arc(-90:-60:.85);\node at(.33,1.6){$\theta$};\draw[->](-.8,2.8)--(-.8,1.8)node[below]{$g$};\draw[->](-.4,3.05)arc(180:0:.4 and .15);\node[right]at(.45,3.1){$\Omega$};'''
F['governor']=F['pendulum']+r'\draw[->](1.15,.9)arc(-60:-40:2.1);\node[right]at(1.8,1.05){$\dot\theta$};'
F['offset']=r'''\draw[dashed](-.9,-.3)--(-.9,3.5);\draw[thick](-.9,2.8)--(.5,2.8);\draw[dashed](.5,2.8)--(.5,0);\draw[very thick](.5,2.8)--(1.95,.29)node[midway,right]{$l$};\fill(.5,2.8)circle(2pt)node[above]{$A$};\fill(1.95,.29)circle(3pt)node[below right]{$m$};\draw[<->](-.9,3.2)--(.5,3.2)node[midway,above]{$a$};\draw(.5,1.95)arc(-90:-60:.85);\node at(.84,1.6){$\varphi$};\node[left]at(-.9,2){$\Omega$};\draw[->](2.7,2.3)--(2.7,1.3)node[below]{$g$};'''
F['rod']=F['pendulum'].replace(r'node[midway,right]{$l$}',r'node[midway,right]{$L,M$}').replace(r'\fill(P)circle(3pt)node[below right]{$m$};','').replace(r'$\theta$',r'$\varphi$')
F['rotliquid']=r'''\draw[thick](-1.6,2.3)--(-1.6,0)--(1.6,0)--(1.6,2.3);\draw[smooth,domain=-1.6:1.6,samples=30]plot(\x,{.7+.4*\x*\x});\draw[->,gray](0,0)--(0,2.8)node[above]{$z$};\draw[->,gray](0,0)--(2.2,0)node[right]{$r$};\node at(.95,1.8){$z(r)$};\draw[->](-.4,2.4)arc(180:0:.4 and .12);\node[left]at(-.5,2.4){$\Omega$};\draw[->](2.1,2.3)--(2.1,1.4)node[right]{$g$};'''
F['spring']=r'''\draw(0,0)circle(1.9);\draw[thick](-1.8,-.2)--(1.8,-.2);\draw[thick](-1.8,.2)--(1.8,.2);\draw[fill=white](.35,-.28)rectangle(.95,.28);\node[above]at(.65,.3){$m$};\draw[decorate,decoration={zigzag,segment length=5pt,amplitude=2pt}](-1.8,0)--(.35,0);\draw[decorate,decoration={zigzag,segment length=5pt,amplitude=2pt}](.95,0)--(1.8,0);\node at(-.9,.5){$k$};\node at(1.4,.5){$k$};\node[below left]at(0,0){$O$};\draw[<->](0,-.7)--(.65,-.7)node[midway,below]{$x$};\draw[->](-.67,2.06)arc(108:142:2.17);\node at(-.5,2.4){$\Omega$};'''
F['free']=F['frame']+r'\draw[->,very thick,ink](.5,-.65)--(2.1,-.65)node[midway,below]{$u\vect E_X$};\node at(.6,-1.3){$P(0)=O$};'
F['earth']=r'''\draw(0,0)circle(1.55);\draw[dashed](-1.8,0)--(1.8,0);\draw[->,gray](0,-1.8)--(0,2.1)node[above]{$\Omega_E$};\coordinate(P)at(35:1.55);\draw(0,0)--(P)node[midway,above]{$R$};\fill(P)circle(2.5pt)node[below right]{$P$};\draw[->](P)--++(35:.9)node[right]{$\vect e_U$};\draw[->](P)--++(125:.85)node[above]{$\vect e_N$};\draw(.65,0)arc(0:35:.65);\node at(.88,.26){$\lambda$};\node[below left]at(0,0){$O$};\node at(.9,-1.8){子午面};'''
F['southcar']=F['earth']+r'\draw[->,thick](P)--++(-55:.8)node[below right]{$u$};'
F['weight']=r'''\draw[->,gray](-1.9,0)--(2,0)node[right]{东};\draw[->,gray](0,-.5)--(0,1.9)node[above]{天};\draw[fill=white](-1.2,.15)rectangle(-.5,.5);\draw[fill=white](.5,.15)rectangle(1.2,.5);\draw[->](-.6,.9)--(-1.5,.9)node[left]{$U$};\draw[->](.6,.9)--(1.5,.9)node[right]{$U$};\node at(-.85,-.6){西行};\node at(.85,-.6){东行};\node at(0,-1.2){同一纬度 $\lambda$};'''
F['inertialcircle']=r'''\draw[->,gray](-1.8,0)--(2.1,0)node[right]{东};\draw[->,gray](0,-2.1)--(0,1.05)node[above]{北};\draw[dashed](0,-.9)circle(.9);\fill(0,0)circle(2.5pt)node[above left]{$O$};\draw[->,thick](0,0)--(1.2,0)node[midway,above]{$U$};\node at(-1.2,-1.5){$f>0$};'''
F['circle14']=r'''\draw(0,0)circle(1.35);\draw[->,thick](1.35,0)arc(0:65:1.35);\node at(0,0){$T_I=14\,\mathrm h$};\draw[->,gray](-1.8,-1.8)--(.9,-1.8)node[right]{东};\draw[->,gray](-1.8,-1.8)--(-1.8,.9)node[above]{北};\node at(.2,-2.35){俯视逆时针};'''
F['wind']=r'''\draw[->,gray](0,0)--(3.7,0)node[right]{东};\draw[->,gray](0,0)--(0,2.8)node[above]{北};\foreach \y in {.6,1.3,2}{\draw[gray](.35,\y)--(3.1,\y);}\draw[->,thick](3.2,.7)--(3.2,2.1)node[above]{$\nabla p$};\node at(1.6,2.45){高压};\node at(1.6,.25){低压};\node at(1.6,-.55){$f>0$};'''
F['sink']=r'''\draw(0,0)ellipse(1.7 and .65);\draw(-1.7,0)--(-1.3,-1.35);\draw(1.7,0)--(1.3,-1.35);\draw(-1.3,-1.35)arc(180:360:1.3 and .3);\draw[->](-.6,.15)..controls(0,.8)and(1.2,.15)..(.55,-.1);\node at(.1,.75){$U$};\draw[<->](-1.7,1.4)--(1.7,1.4)node[midway,above]{$L$};\node at(0,-2){$|f|$ 已知};'''
F['cyclone']=r'''\draw(0,0)circle(.6);\draw(0,0)circle(1.2);\draw(0,0)circle(1.75);\node at(0,0){低压};\draw[->,thick](.8,0)--(1.65,0)node[above right]{$p_r>0$};\draw[->](1.2,0)arc(0:65:1.2);\node at(.85,1.45){$V>0$};\node at(0,-2.2){北半球 $f>0$};'''
F['drop']=r'''\draw[thick](-.6,0)--(3.1,0);\draw[->,gray](0,0)--(3.4,0)node[right]{东 $x$};\draw[->,gray](0,0)--(0,3)node[above]{天 $z$};\fill(0,2.35)circle(3pt)node[right]{释放点};\draw[dashed](0,0)--(0,2.35);\draw[<->](-.55,0)--(-.55,2.35)node[midway,left]{$h$};\draw[->](2,2.1)--(2,1.1)node[right]{$g$};\node at(1.3,-.6){$\vect v'(0)=0$};'''
F['drop_two']=F['drop'].replace(r'$h$',r'$h_1,h_2$')
F['drop_error']=F['drop'].replace(r'$\vect v\'(0)=0$',r'$u_i$ 固定')+r'\draw[->,thick](0,2.35)--(1.15,2.35)node[above]{$u_i$};'
F['throwup']=r'''\draw[thick](-.6,0)--(2.7,0);\draw[->,gray](0,0)--(3,0)node[right]{东 $x$};\draw[->,gray](0,0)--(0,3)node[above]{天 $z$};\fill(0,.15)circle(3pt);\draw[->,thick](.25,.25)--(.25,1.7)node[right]{$w_0$};\draw[->](1.8,2.4)--(1.8,1.35)node[right]{$g$};\node at(1.1,-.6){返回 $z=0$};'''
F['throweast']=F['drop'].replace(r'node[right]{释放点}',r'node[above left]{$P_0$}').replace(r'$\vect v\'(0)=0$',r'$u_0>0$')+r'\draw[->,thick](0,2.35)--(1.5,2.35)node[midway,above]{$u_0$};'
F['thrownorth']=F['throweast'].replace(r'东 $x$',r'北 $y$').replace(r'$u_0$',r'$v_0$').replace(r'$u_0>0$',r'$v_0>0$')+r'\node at(2.6,1.9){东 $x$: $\odot$};'
F['foucault']=r'''\draw[->,gray](-1.8,0)--(2.1,0)node[right]{东 $x$};\draw[->,gray](0,-1.3)--(0,2.05)node[right]{北 $y$};\draw[dashed](0,0)circle(1.25);\draw[thick](0,0)--(1.25,0);\fill(1.25,0)circle(3pt)node[below right]{$P_0$};\draw[<->](0,-.45)--(1.25,-.45)node[midway,below]{$a$};\node at(.1,-1.6){$\dot x(0)=\dot y(0)=0$};\node at(.25,3.1){水平投影，摆长 $l$};'''
F['period']=r'''\draw(0,0)circle(1.3);\draw[dashed](-1.6,0)--(1.6,0);\draw[->](0,-1.6)--(0,1.75)node[above]{$\Omega_E$};\foreach \a/\lab in {39.9/B,48.86/P,90/N}{\fill(\a:1.3)circle(2pt);}\draw(39.9:1.3)--(2.0,.2)node[right]{北京};\draw(48.86:1.3)--(2,1)node[right]{巴黎};\node[left]at(0,1.3){北极};\node at(.5,-2){$D=23.9345\,\mathrm h$};'''
F['period_compare']=r'''\draw[->,gray](-1.4,0)--(1.4,0);\draw[->,gray](0,-1.25)--(0,1.45);\draw[thick](-1,-.45)--(1,.45);\draw[->](.9,.9)arc(45:-20:1.27);\node at(0,-1.85){傅科摆主轴};\begin{scope}[xshift=3.8cm]\draw(0,0)circle(1);\draw[->](1,0)arc(0:-60:1);\node at(0,-1.85){惯性圆};\end{scope}\node at(1.8,2){$\lambda=60^\circ$};'''
# Use an explicitly defined diagram for each question so its figure remains independently editable.
EM=['frame_gmoving','frame_gfixed','frame','frame','tube_u','cart','zero','tube_R','tube_c','governor','circle','circle_reverse','eccentric','nested','precession','southcar','axispoint','four','belt','liquid','flight','disk','pendulum','pendulum','offset','rod','rotliquid','tube','tube_u','spring','spring','free','earth','earth','weight','circle14','wind','sink','drop','drop_two','throwup','throweast','drop_error','foucault','period','tube','disk']
TM=['frame_gfixed','circle','cart','tube_c','disk_fixed','tube_end','spring','tube_power','pendulum','offset','rod','pendulum','earth','weight','inertialcircle','cyclone','drop','throwup','thrownorth','throweast','foucault','period_compare','spring','frame_force']
assert len(EM)==47 and len(TM)==24
rows=[]
for prefix,keys in [('ex',EM),('tr',TM)]:
 for n,k in enumerate(keys,1):
  body=F[k]
  if prefix=='ex' and n==12:body=F['circle_reverse']
  if prefix=='tr' and n==3:body=F['cart'].replace(r'$\theta$',r'$\theta(0)=0$')
  if k=='drop_error':body=body.replace(r'\node at(1.3,-.6){$\vect v\'(0)=0$};','')
  if k in ['throweast','thrownorth']:body=body.replace(r'\node at(1.3,-.6){$\vect v\'(0)=0$};','')
  if k in ['drop_error','throweast','thrownorth']:
   body=body.replace(r"\node at(1.3,-.6){$\vect v'(0)=0$};",'')
  if prefix=='tr' and n==3:
   body=F['tube'].replace(r'$\dot x$',r'$u$').replace(r'$x$',r'$a$').replace(r'$O$',r"$O'$").replace(r'$\vect e_1$',r'$X$').replace(r'$\vect e_2$',r'$Y$')+r'\draw[->](.8,-1.3)--(2.3,-1.3)node[midway,below]{$A\vect E_X$};\node at(2,1.5){$t=0$};'
  if prefix=='ex' and n==29:body=body.replace(r'$r$',r'$x$')
  if prefix=='ex' and n==35:body=body.replace(r'$U$',r'$|u|$')
  if prefix=='ex' and n==43:body=body.replace(r'node[right]{释放点}',r'node[above left]{释放点}')
  if prefix=='tr' and n==19:body=body.replace(r'\node at(2.6,1.9)',r'\node at(2.8,3.25)')
  filename=f'{prefix}{n:02}.tex';(D/filename).write_text(fig(body))
  rows.append({'kind':prefix,'number':n,'file':'题图/'+filename,'model':k})
(P/'工作文件/题图清单.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('71 independently editable diagrams written')
