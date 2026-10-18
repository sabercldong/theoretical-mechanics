from pathlib import Path
import json
P=Path(__file__).resolve().parents[1];D=P/'题图';D.mkdir(exist_ok=True)
F={}
F['translate']=r'''\draw[dashed](0,0)circle(1.15);\draw[->,gray](-1.5,0)--(2.6,0)node[right]{$x$};\draw[->,gray](0,-1.4)--(0,2.1)node[above]{$y$};\coordinate(C)at(.81,.81);\draw[thick](.36,.56)rectangle(1.86,1.26);\fill(C)circle(2pt)node[above left]{$C$};\fill(1.65,1.06)circle(2pt)node[above]{$P$};\draw(0,0)--(C)node[midway,above left]{$R$};\draw[->](1.3,-.3)arc(-15:30:1.35);\node at(1.7,-.5){$\Omega$};\node[below left]at(0,0){$O$};'''
F['base']=r'''\draw[rounded corners](.2,.5)--(.5,2)--(2.8,2.5)--(3.7,1.2)--(2.7,.1)--cycle;\fill(.5,.7)circle(2pt)node[left]{$O$};\fill(1.7,1.3)circle(2pt)node[below]{$C$};\fill(2.9,2)circle(2pt)node[right]{$A$};\draw[->](.5,.7)--(1.7,1.3)node[midway,above left]{$\vect\rho_{OC}$};\draw[->](1.7,1.3)--(2.9,2)node[midway,below right]{$\vect\rho_{CA}$};\draw[->](.5,.7)--(2.9,2)node[midway,above left=10pt]{$\vect\rho_{OA}$};'''
F['axes']=r'''\draw[->](0,0)--(2.8,0)node[right]{$x$};\draw[->](0,0)--(0,2.6)node[above]{$z$};\draw[->](0,0)--(-1.2,-1)node[below left]{$y$};\node[below right]at(0,0){$O$};\draw[->,thick](0,0)--(1.6,1.65)node[right]{$\vect r_{OA}$};\fill(1.6,1.65)circle(2pt)node[above]{$A$};\draw[->,thick](-.6,.8)--(.15,2.1)node[left]{$\vect\omega$};'''
F['turntable']=r'''\draw(0,0)ellipse(1.6 and .4);\draw[->](0,-.4)--(0,2.6)node[above]{$\vect k,\Omega$};\draw[thick](0,1.15)--(2,1.15);\draw(1.45,1.15)ellipse(.3 and .95);\draw[->](1.45,1.15)--(2.8,1.15)node[right]{$\vect e_r,\omega$};\node[left]at(0,1.15){$O$};\node at(1.75,-.7){转台};'''
F['top']=r'''\draw[->,gray](0,-.3)--(0,3.15)node[above]{$\zeta,\vect k$};\draw[->,thick](0,0)--(1.65,2.65)node[above right]{$\vect n$};\draw[thick,rotate=-32](0,1.8)ellipse(.8 and .2);\draw(0,.8)arc(90:58:.8);\node at(.4,1.02){$\theta$};\node[below left]at(0,0){$O$};\node at(2,1.5){$\omega$};\draw[->](-.4,2.55)arc(180:0:.4 and .15);\node[left]at(-.45,2.55){$\Omega$};'''
# Draw a disk perpendicular to its axis using orthogonal projected directions, centered ON the axis.
F['top']=F['top'].replace(r'\draw[thick,rotate=-32](0,1.8)ellipse(.8 and .2);',r'\draw[thick,rotate around={-32:(1,1.6)}](1,1.6)ellipse(.8 and .2);')
F['hanging']=r'''\foreach \x in {0,2.7}{\draw[dashed](\x,2.8)--(\x,0);\fill(\x,2.7)circle(2pt);\draw[thick](\x,2.7)--++(.7,-1.9);}\draw[rotate around={20:(.7,.8)}](.7,.8)ellipse(.65 and .18);\draw(3.4,.8)ellipse(.65 and .18);\node at(.2,3.25){$\Omega\vect k$};\node at(2.9,3.25){$\Omega\vect k$};\node at(.75,.2){(a) 法线沿杆};\node at(3.2,.2){(b) 法线竖直};\node at(1.2,1.7){$\beta$};\node at(4,1.7){$\beta$};\node at(.1,-.4){$\omega\vect n$};\node at(3,-.4){$\omega\vect k$};'''
F['swingdisk']=r'''\draw[dashed](0,2.7)--(0,-.3);\fill(0,2.7)circle(2pt)node[left]{$O$};\draw[very thick](0,2.7)--(0,.5)node[midway,right]{$l$};\draw(0,.5)ellipse(1.15 and .32);\fill(0,.5)circle(2pt)node[above left]{$A$};\fill(1.15,.5)circle(2pt)node[right]{$C$};\fill(0,.18)circle(2pt)node[below]{$B$};\draw[->](-1.5,2.7)--(1.6,2.7)node[right]{$\vect e_3,\omega_1$};\node[left]at(-.1,1.4){$\omega_2$};\node at(0,-.7){$t=0,\ AC\parallel\vect e_3$};'''
F['euler']=r'''\draw[->](0,0)--(2.4,0)node[right]{$\xi$};\draw[->](0,0)--(0,2.8)node[above]{$\zeta$};\draw[->](0,0)--(-1,-.9)node[below]{$\eta$};\draw[->,thick](0,0)--(1.3,2.4)node[above right]{$z$};\draw[->](0,0)--(2,-.9)node[right]{$N$};\draw(0,.8)arc(90:62:.8);\node at(.35,1.02){$\theta$};\node at(1.1,-.2){$\varphi$};\node at(1.95,1.1){$\psi$};\node[below left]at(0,0){$O$};'''
F['earth']=r'''\draw(0,0)circle(1);\draw[dashed](-1.4,0)--(1.4,0);\draw[->,gray](0,-1.3)--(0,2)node[above]{$\zeta$};\draw[->,thick](-.55,-1.1)--(.8,1.6)node[above right]{$z,\omega$};\draw(0,.6)arc(90:63.4:.6);\node at(.3,.85){$\varepsilon$};\node at(0,-1.7){质心轨道：平移};'''
F['satellite']=r'''\draw[dashed](0,0)circle(1.6);\fill(0,0)circle(4pt)node[below]{$O$};\foreach \a in {0,90,180}{\begin{scope}[rotate=\a]\draw[thick](1.4,-.25)rectangle(1.8,.25);\draw[->](1.6,0)--(.85,0);\end{scope}}\node[right]at(1.8,.25){卫星};\draw[->](40:1.6)arc(40:65:1.6);\node at(1.4,1.5){$\Omega$};\node at(0,-2){$\vect e_1$ 指向 $O$};'''
F['cone']=r'''\draw[thick](-.4,0)--(3.7,0);\draw[thick](0,0)--(3.1,0)--(1.55,2.15)--cycle;\draw[dashed](0,0)--(2.32,1.075)node[right]{$h,\vect e_z$};\draw(0,0)--(0,2.7)node[above]{$\zeta$};\node[below left]at(0,0){$O$};\node[below]at(2.5,0){接触母线 $\vect u$};\draw(.7,0)arc(0:25:.7);\node at(1,.25){$\alpha$};\fill(1.55,2.15)circle(2pt)node[above]{$A$};'''
F['vslider']=r'''\draw[thick](-.15,-.5)--(-.15,3);\draw[thick](.15,-.5)--(.15,3);\fill(0,0)circle(2pt)node[left=5pt]{$O$};\coordinate(A)at(1.2,-.5);\coordinate(B)at(0,2.2);\draw[thick](0,0)--(A)node[midway,below]{$a$};\draw[very thick](A)--(B)node[midway,right]{$L$};\draw[fill=white](-.22,2)rectangle(.22,2.4);\node[left]at(-.3,2.2){$B$};\fill(A)circle(2pt)node[right]{$A$};\draw[->](0,-.5)--(0,-1.3)node[below]{$\xi$};\draw[->](0,0)--(2.2,0)node[right]{$\eta$};\node at(.75,.45){$q$};\node at(.3,1.4){$\psi$};'''
F['finite']=r'''\draw[->](0,0)--(2.7,0)node[right]{$x$};\draw[->](0,0)--(0,2.4)node[above]{$z$};\draw[->](0,0)--(-1,-.9)node[below left]{$y$};\draw[->,thick](0,0)--(1.7,0)node[midway,below]{$R_xR_y\vect e_z$};\draw[->,thick](0,0)--(.9,.81)node[right]{$R_yR_x\vect e_z$};\node at(1.2,-1.5){每次 $\pi/2$，固定轴};'''
F['parallel']=r'''\draw[gray](-.3,0)--(3.5,0)node[right]{$x$};\fill(.6,0)circle(2pt);\fill(2.7,0)circle(2pt);\draw[->,thick](.6,0)--(.6,1.6)node[above]{$F_1$};\draw[->,thick](2.7,0)--(2.7,1.1)node[above]{$F_2$};\node[below]at(.6,0){$x_1$};\node[below]at(2.7,0){$x_2$};\node at(1.6,-.8){力按 $+y$ 有向取值};'''
F['couple']=r'''\draw[thick](0,0)--(3,0);\draw[->,thick](0,.7)--(0,-.7)node[below]{$F$};\draw[->,thick](3,-.7)--(3,.7)node[above]{$F$};\draw[<->](0,-1.3)--(3,-1.3)node[midway,below]{$d$};\node at(1.5,.8){$\odot\vect k$};'''
F['wrench']=r'''\draw[->,thick](0,0)--(0,2.4)node[above]{$F\vect k$};\draw[->](-.55,.7)arc(180:490:.55 and .2);\node[right]at(.6,.6){$C\vect k$};\fill(0,0)circle(2pt)node[below]{$O$};'''
F['rodedge']=r'''\draw(-.3,0)--(3.7,0);\draw[gray](1.8,0)--(1.8,1.35)--(3.6,1.35);\draw[very thick](0,0)--(3.2,2.4);\fill(0,0)circle(2pt)node[below]{$A$};\fill(1.8,1.35)circle(2pt)node[right]{$B$};\draw[->](1.8,1.35)--(1.2,2.15)node[left]{$N_1$};\draw[->](0,0)--(0,1.1)node[left]{$N_2$};\draw[->](0,0)--(.9,0)node[below]{$f$};\draw[->](1.6,1.2)--(1.6,.25)node[left]{$P$};\node at(.8,.3){$\varphi$};\node[right]at(3.6,.65){$h$};'''
F['lrods']=r'''\fill(0,2.7)circle(2pt)node[above]{$A$};\draw[dashed](0,2.7)--(0,-.4);\draw[very thick](0,2.7)--(1,0)node[midway,right]{$a$};\draw[very thick](1,0)--(-1.1,-.78)node[midway,below]{$b$};\node at(.25,1.9){$\theta$};\node[right]at(1,0){$B$};\draw[->](.5,1.35)--(.5,.6)node[left]{$m_1g$};\draw[->](-.05,-.39)--(-.05,-1.2)node[right]{$m_2g$};'''
F['wallrod']=r'''\draw[thick](0,-.5)--(0,3);\draw[very thick](0,0)--(3.4,2.55);\fill(0,0)circle(2pt)node[left]{$O$};\fill(1.65,1.24)circle(2pt)node[right]{$B$};\draw[->](0,0)--(1,0)node[below]{$N_O$};\draw[->](1.65,1.24)--(1.05,2.04)node[left]{$N_B$};\draw[->](1.7,1.275)--(1.7,.4)node[right]{$P$};\draw[<->](0,-.5)--(1.65,-.5)node[midway,below]{$d$};\node at(.7,.25){$\theta$};'''
F['bowl']=r'''\draw[thick](-1.7,0)arc(180:360:1.7);\draw[dashed](-1.7,0)--(1.7,0);\draw[very thick](-1.23,-1.18)--(2.7,.4);\fill(-1.23,-1.18)circle(2pt)node[below]{$B$};\fill(1.7,0)circle(2pt)node[above]{$C$};\fill(0,0)circle(2pt)node[above]{$O$};\draw[dashed](0,0)--(-1.23,-1.18)node[midway,left]{$r$};\node at(.3,-.6){$BC=c$};\node at(2,1){杆长 $l$};'''
F['logs']=r'''\foreach \row in {0,...,4}{\pgfmathtruncatemacro{\last}{4-\row}\foreach \j in {0,...,\last}{\draw({.38*(2*\j+\row)},{.38+.65818*\row})circle(.38);}}\draw(-.5,0)--(3.6,0);\draw[->,thick](-.85,.38)--(-.38,.38)node[midway,above]{$F$};\draw[->,thick](3.9,.38)--(3.42,.38)node[midway,above]{$F$};\node at(1.5,-.65){$5+4+3+2+1$};'''
F['blocks']=r'''\draw[gray,->](-2,0)--(2.3,0)node[right]{$x$};\draw(-1.6,-.45)rectangle(-.6,.45);\draw(.6,-.45)rectangle(1.6,.45);\node at(-1.1,.75){$m,\mathsf I_0$};\node at(1.1,.75){$m,\mathsf I_0$};\fill(0,0)circle(2pt)node[below]{$C$};\draw[<->](-1.1,-.8)--(0,-.8)node[midway,below]{$a$};\draw[<->](0,-.8)--(1.1,-.8)node[midway,below]{$a$};'''
F['rod']=r'''\draw[very thick](0,0)--(2.2,1.9)node[above right]{$A$};\fill(0,0)circle(2pt)node[below left]{$O$};\fill(1.1,.95)circle(2pt)node[below right]{$C$};\node at(.55,1.1){$L$};\draw[->](-.15,1.1)arc(100:35:1.1);\node at(1,1.7){$\omega$};'''
F['lamina']=r'''\draw(-1.5,-.7)rectangle(1.5,.7);\draw[->,gray](-1.8,0)--(2,0)node[right]{$x$};\draw[->,gray](0,-1)--(0,1.3)node[above]{$y$};\node[below left]at(0,0){$C$};\node at(0,-1.3){矩形 $a\times b$};\begin{scope}[yshift=-3.1cm]\draw(0,0)ellipse(1.5 and .7);\draw[->](0,0)--(1.5,0)node[midway,below]{$a$};\draw[->](0,0)--(0,.7)node[midway,left]{$b$};\node at(0,-1.2){椭圆半轴 $a,b$};\end{scope}'''
F['cylinder']=r'''\draw(0,0)ellipse(1 and .3);\draw(0,2.2)ellipse(1 and .3);\draw(-1,0)--(-1,2.2);\draw(1,0)--(1,2.2);\draw[->,gray](0,-.5)--(0,3)node[above]{$z$};\fill(0,1.1)circle(2pt)node[left]{$C$};\draw[<->](1.5,0)--(1.5,2.2)node[midway,right]{$L$};\draw(0,2.2)--(1,2.2)node[midway,above]{$a$};'''
F['sphere']=r'''\draw(0,0)circle(1.4);\draw[dashed](0,0)ellipse(1.4 and .35);\draw[->](0,-1.6)--(0,2)node[above]{$z$};\draw[->](0,0)--(1.7,0)node[right]{$x$};\draw[->](0,0)--(-1,-.75)node[below left]{$y$};\node[below right]at(0,0){$O=C$};\draw(0,0)--(1,1)node[midway,above]{$a$};'''
F['ellipsoid']=F['sphere'].replace(r'circle(1.4)',r'ellipse(1.65 and 1.15)').replace(r'ellipse(1.4 and .35)',r'ellipse(1.65 and .35)').replace(r'\draw(0,0)--(1,1)node[midway,above]{$a$};',r'\node[below]at(1.4,0){$a$};\node[left]at(0,1){$c$};\node[right]at(-.8,-.6){$b$};')
F['hemisphere']=r'''\draw[thick](-1.5,0)arc(180:0:1.5);\draw(0,0)ellipse(1.5 and .3);\draw[->](0,-.6)--(0,2.1)node[above]{$z$};\draw[->](0,0)--(2,0)node[right]{$x$};\draw[->](0,0)--(-1,-.8)node[below]{$y$};\fill(0,.56)circle(2pt)node[right]{$C$};\node[below right]at(0,0){$O$};\draw[<->](-.55,0)--(-.55,.56)node[midway,left]{$3a/8$};\node at(1.1,.9){$a$};'''
F['cube']=r'''\coordinate(O)at(0,0);\coordinate(X)at(2.1,0);\coordinate(Y)at(-.85,-.7);\coordinate(Z)at(0,2.1);\draw[thick](O)--(X)--(2.1,2.1)--(Z)--cycle;\draw[thick](Y)--(1.25,-.7)--(X);\draw[thick](Y)--(-.85,1.4)--(Z);\draw[thick](-.85,1.4)--(1.25,1.4)--(2.1,2.1);\draw[thick](1.25,-.7)--(1.25,1.4);\draw[dashed](O)--(1.25,1.4);\fill(.625,.7)circle(2pt)node[above left]{$C$};\node[below right]at(O){$O$};\node[right]at(X){$x$};\node[below]at(Y){$y$};\node[above]at(Z){$z$};\node at(1.1,-1.2){棱长 $a$};'''
F['box']=F['cube'].replace('棱长 $a$','棱长 $a,b,c$')
F['triangle']=r'''\draw[thick](0,0)--(2.8,0)--(1.4,2.425)--cycle;\foreach \x/\y in {0/0,2.8/0,1.4/2.425}{\fill(\x,\y)circle(3pt);}\node[below left]at(0,0){$O,m$};\node[below right]at(2.8,0){$m$};\node[above]at(1.4,2.425){$m$};\node[below]at(1.4,0){$a$};\draw[->,gray](0,0)--(3.5,0)node[right]{$x$};\draw[->,gray](0,0)--(0,2.8)node[above]{$y$};'''
F['octant']=r'''\draw[->](0,0)--(2.6,0)node[right]{$x$};\draw[->](0,0)--(-1.2,-1)node[below]{$y$};\draw[->](0,0)--(0,2.6)node[above]{$z$};\draw[thick](2,0)arc(0:90:2);\draw[thick](0,2)..controls(-.5,1.5)and(-1.4,.3)..(-.9,-.75);\draw[thick](-.9,-.75)..controls(.1,-1)and(1.4,-.6)..(2,0);\node[below right]at(0,0){$O$};\node at(1.3,1.4){$a,m$};\node at(.7,-1.4){$x,y,z\ge0$};'''
F['diskgyro']=F['top'].replace(r'$\omega$',r'$\dot\psi$').replace(r'$\Omega$',r'$\dot\varphi$')+r'\node[left]at(.6,1.1){$h$};\node[right]at(1.6,1.55){$m,a$};'
F['drivedisk']=r'''\draw(0,0)circle(1.3);\draw(0,0)--(1.3,0)node[midway,below]{$a$};\fill(0,0)circle(2pt)node[below left]{$O$};\draw[->,thick](1.55,0)arc(0:100:1.55);\node at(.4,1.95){$M$};\draw[->](-1.55,0)arc(180:100:1.55);\node at(-1.5,1.5){$M_f$};\node at(0,-1.8){$m,\omega(0)=0$};'''
F['pendulum']=r'''\draw[dashed](0,2.8)--(0,-.5);\draw[very thick](0,2.8)--(1.3,0)node[midway,right]{$L$};\fill(0,2.8)circle(2pt)node[above left]{$O$};\fill(.65,1.4)circle(2pt)node[right]{$C$};\draw[->](.65,1.4)--(.65,.6)node[left]{$mg$};\draw(0,2)arc(-90:-65:.8);\node at(.3,1.7){$q$};'''
F['physpend']=F['pendulum'].replace(r'node[midway,right]{$L$}',r'node[midway,right]{$h$}').replace(r'\draw[very thick](0,2.8)--(1.3,0)',r'\draw[thick](0,2.8)--(.65,1.4)').replace(r'$q$',r'$\theta$')+r'\draw[rotate around={25:(.65,1.4)}](.65,1.4)ellipse(.55 and 1.05);\node at(1.5,-.5){$I_C=mk^2$};'
F['rotorrod']=r'''\draw[thick](0,-.5)--(0,3);\draw[very thick](-.65,.2)--(.65,2.3)node[right]{$l,m$};\fill(0,1.25)circle(2pt)node[left]{$C$};\draw(-.3,-.15)rectangle(.3,.15);\draw(-.3,2.55)rectangle(.3,2.85);\node[left]at(-.35,0){$A$};\node[left]at(-.35,2.7){$B$};\draw[<->](1.2,0)--(1.2,2.7)node[midway,right]{$L$};\node at(.2,2.1){$\beta$};\node[above]at(0,3){$z,\omega$};'''
F['balance']=r'''\draw[->](-.5,0)--(3.6,0)node[right]{$z$};\foreach \x/\l in {.6/a,2.6/b}{\draw[dashed](\x,-1)--(\x,1.6);\draw[thick](\x,0)--(\x,1);\fill(\x,1)circle(3pt)node[above]{$\vect U_\l$};\node[below]at(\x,-1){$z_\l$};}\node at(1.6,2){两校正平面};'''
F['tipcube']=r'''\draw[thick](-.6,0)--(3.2,0);\begin{scope}[rotate=20]\draw[very thick](0,0)rectangle(2,2);\fill(1,1)circle(2pt)node[above]{$C$};\draw[->](1,1)--++(-.34,-.94)node[below]{$mg$};\end{scope}\fill(0,0)circle(2pt)node[below]{$O$};\draw(.8,0)arc(0:20:.8);\node at(1.15,.2){$\theta$};\node at(2.5,1.8){$a$};'''
F['pulley']=r'''\draw(0,2)circle(.65);\fill(0,2)circle(2pt)node[above]{$O$};\draw(-.65,2)--(-.65,.3);\draw(.65,2)--(.65,-.3);\draw(-.95,-.2)rectangle(-.35,.3);\draw(.35,-.8)rectangle(.95,-.3);\node[left]at(-.95,.05){$m$};\node[right]at(.95,-.55){$2m$};\node at(1.3,2.5){$m,r$};\draw[->](1.4,.3)--(1.4,-.5)node[right]{$a$};'''
F['tiltdisk']=r'''\draw[thick](-1.6,0)--(1.6,0);\draw[rotate=25](0,0)ellipse(.3 and 1.1);\draw[->,thick](0,0)--(1.5,.7)node[right]{$\vect n$};\node[below left]at(0,0){$O$};\node[below]at(-1.5,0){$A$};\node[below]at(1.5,0){$B$};\node at(-.8,-.6){$a$};\node at(.8,-.6){$b$};\draw[->](0,0)--(0,1.8)node[above]{$\vect e_X$};\node at(1,.2){$\beta$};\node at(0,-1.6){$z:A\to B$};'''
F['trod']=r'''\draw[very thick](0,0)--(2.4,0);\draw[very thick](2.4,-1.2)--(2.4,1.2);\fill(0,0)circle(2pt)node[above left]{$O$};\node[right]at(2.4,0){$A$};\node at(1.2,.4){$L,m$};\node at(3,1){$L,m$};\draw[->](.6,-.4)arc(-30:-120:.7);\node at(.6,-1.3){$\omega$};\draw[->](1.2,0)--(1.2,-.8)node[left]{$mg$};\draw[->](2.4,0)--(2.4,-.8)node[right]{$mg$};'''
F['ladder']=r'''\draw[thick](0,3)--(0,0)--(3.3,0);\draw[very thick](0,2.4)--(2.5,0)node[midway,above]{$l$};\node[left]at(0,2.4){$B$};\node[below]at(2.5,0){$A$};\draw[->](2.5,0)--(3.3,0)node[above]{$u$};\draw[dashed](0,2.4)--(2.5,2.4)--(2.5,0);\fill(2.5,2.4)circle(2pt)node[right]{$P$};\node[below left]at(0,0){$O$};'''
F['slope']=r'''\draw[thick](-.4,1.5)--(3.7,-.4);\draw(1.7,1.46)circle(.9);\fill(1.7,1.46)circle(2pt)node[above]{$C$};\draw[->](1.7,1.46)--(1.7,.4)node[left]{$mg$};\draw[->](1.3,.65)--(.4,1.07)node[above]{$f$};\draw[->](1.3,.65)--(1.8,1.73)node[right]{$N$};\node at(2.7,1.8){$a,I_C$};\draw[dashed](2.6,-.1)--(3.6,-.1);\node at(3.1,.15){$\beta$};'''
F['unwind']=r'''\draw[thick](-1.5,3)--(-.4,3);\draw[thick](-.9,3)--(-.9,1);\draw(0,1)circle(.9);\fill(0,1)circle(2pt)node[right]{$C$};\draw[->](-.9,1)--(-.9,2)node[left]{$T$};\draw[->](0,1)--(0,-.4)node[right]{$mg$};\node at(.7,2.3){$r,m$};'''
F['fourpoints']=r'''\draw(0,0)circle(1.25);\draw[thick](-1.8,-1.25)--(2.2,-1.25);\foreach \a/\l in {270/A,180/B,90/C,0/D}{\fill(\a:1.25)circle(2pt)node[shift={(\a:.25)}]{$\l$};}\node[below left]at(0,0){$O$};\draw[->](0,0)--(1.9,0)node[right]{$v,a$};\node at(-1.2,1.75){$R$};'''
F['planet']=r'''\draw(0,0)circle(1.05);\draw(1.75,0)circle(.7);\fill(0,0)circle(2pt)node[left]{$O$};\fill(1.75,0)circle(2pt)node[right]{$A$};\draw[dashed](0,0)--(1.75,0);\fill(1.75,.7)circle(2pt)node[above]{$M$};\draw(1.75,0)--(1.75,.7);\node at(-.5,.4){$R$};\node at(2.25,-.5){$r$};\draw[->](1.75,-1)--(1.75,-.3)node[right]{$\Omega$};\node at(.5,-1.6){固定轮};'''
F['groove']=r'''\draw[thick](-1.8,0)arc(180:360:1.8);\draw[dashed](0,0)--(0,-1.8);\coordinate(C)at(.65,-1.12);\draw(C)circle(.5);\draw[dashed](0,0)--(C)node[midway,right]{$q$};\fill(0,0)circle(2pt)node[above]{$O$};\fill(C)circle(2pt)node[below left]{$C$};\node at(.25,-.7){$\varphi$};\node at(1.4,-.6){$r$};\node at(-1.3,-1.5){$R$};'''
F['hoist']=r'''\draw(-1.2,1.5)circle(.6);\draw(1.2,1.5)circle(.6);\draw(-1.2,2.1)--(1.2,2.1);\draw(1.8,1.5)--(1.8,-.3);\draw(1.5,-.8)rectangle(2.1,-.3);\node at(-1.2,1.5){$A$};\node at(1.2,1.5){$B$};\node[right]at(2.1,-.5){$C,P_3$};\node at(-1.3,.5){$P_1,r_1$};\node at(1,.5){$P_2,r_2$};\node at(0,2.4){$T$};\node[right]at(1.8,.5){$S$};\draw[->](-1.9,1.6)arc(170:70:.75);\node at(-1.6,2.7){$M_1$};'''
F['corner']=r'''\draw[thick](0,3)--(0,0)--(3.3,0);\draw(1,1)circle(1);\draw[->](0,1)--(.8,1)node[above]{$N_A$};\draw[->](0,1)--(0,1.9)node[left]{$f_A$};\draw[->](1,0)--(1,.8)node[right]{$N_B$};\draw[->](1,0)--(.2,0)node[below]{$f_B$};\draw[->](1.4,2.3)arc(60:130:.7);\node[right]at(1.8,2.4){$\omega_0$};\node at(1.5,1){$Q,r$};'''
F['hslider']=r'''\draw[thick](-.4,0)--(3.5,0);\coordinate(A)at(1.2,1.2);\coordinate(B)at(2.4,0);\draw[very thick](0,0)--(A)--(B);\fill(0,0)circle(2pt)node[below]{$O$};\fill(A)circle(2pt)node[above]{$A$};\draw[fill=white](2.15,-.15)rectangle(2.65,.15);\node[below]at(B){$B$};\node at(.75,.3){$\varphi$};\node[left]at(.5,.8){$l$};\node[right]at(1.9,.8){$l$};\node at(-.2,1.3){$\Omega$};'''
F['hslider2']=F['hslider'].replace(r'node[left]at(.5,.8){$l$}',r'node[left]at(.5,.8){$R$}').replace(r'node[right]at(1.9,.8){$l$}',r'node[right]at(1.9,.8){$L$}').replace(r'$\varphi$',r'$45^\circ$')+r'\node at(2.3,.45){$30^\circ$};'
# Ensure the 30-degree rod is also geometrically 30 degrees in the diagram.
F['hslider2']=F['hslider2'].replace('(2.4,0)','(3.278,0)').replace('(2.15,-.15)rectangle(2.65,.15)','(3.03,-.15)rectangle(3.53,.15)').replace('(-.4,0)--(3.5,0)','(-.4,0)--(4,0)').replace('at(1.9,.8)','at(2.4,.9)').replace('at(2.3,.45)','at(2.8,.25)')
F['ballboard']=r'''\draw[thick](-1.4,-.4)rectangle(2.1,0);\draw(.1,.8)circle(.8);\fill(.1,.8)circle(2pt)node[right]{$m,r$};\node at(1.7,-.2){$M$};\draw[->](.6,-.9)--(1.9,-.9)node[midway,below]{$v$};\node at(-.3,2){球初始静止};\node at(.2,-1.7){下支承光滑};'''
F['ballboard_rev']=F['ballboard'].replace('球初始静止','板初始静止').replace(r'\draw[->](.6,-.9)--(1.9,-.9)node[midway,below]{$v$};',r'\draw[->](.2,1.75)--(1.4,1.75)node[midway,above]{$v$};')
F['propeller']=r'''\draw[->](0,0)--(2.5,0)node[right]{$\vect i$};\draw[->](0,0)--(-1,-.8)node[below left]{$\vect j,u$};\draw[->](0,0)--(0,2.6)node[above]{$\vect k$};\draw[dashed](0,0)circle(1.7);\draw[very thick](0,0)--(1,1.37)node[above right]{$B$};\node at(.8,.55){$l$};\node[below right]at(0,0){$A$};\node at(.33,1.1){$\vartheta$};\node at(-1.3,1.6){$\omega_s$};'''
F['principal']=r'''\draw[->](0,0)--(2.4,0)node[right]{$\vect e_1,I_1$};\draw[->](0,0)--(-1,-.9)node[below left]{$\vect e_2,I_2$};\draw[->](0,0)--(0,2.4)node[above]{$\vect e_3,I_3$};\draw[->,thick](0,0)--(.4,1.9)node[right]{$\vect\omega$};\node at(.8,-1.6){$I_1<I_2<I_3$};'''
F['freegyro']=r'''\draw[->,thick](0,0)--(0,2.8)node[above]{$\vect L$};\draw[->](0,0)--(1.05,2.1)node[above right]{$\vect e_3$};\draw[->](0,0)--(-.55,2.5)node[above left]{$\vect\omega$};\node[below]at(0,0){$O$};\node at(.35,1.2){$\theta$};\node at(1.8,.3){$I_1=I_2=A$};\node at(1.4,-.3){$I_3=C$};'''
# In this example C>A: omega is further tilted from the symmetry axis than L, on the same meridian.
F['freegyro']=F['freegyro'].replace('(-.55,2.5)','(-.55,2.5)')
F['heavytop']=F['top'].replace(r'$\omega$',r'$s$')+r'\fill(.68,1.1)circle(2pt)node[right]{$C$};\draw[->](.68,1.1)--(.68,.3)node[right]{$mg$};\node[left]at(.25,.65){$l$};'
F['weightedloop']=r'''\draw(0,0)circle(1.4);\draw[->,gray](-1.7,0)--(2,0)node[right]{$x$};\draw[->,gray](0,-1.7)--(0,2)node[above]{$y$};\draw[->,thick](0,0)--(.99,.99)node[midway,left]{$\vect r$};\draw[->](.99,.99)--(.4,1.58)node[above]{$\dd\vect s$};\draw[->,thick](.1,-2.2)--(1.5,-2.2)node[right]{$\vect B$};\node[below left]at(0,0){$O$};'''
F['larmor']=r'''\draw[->](0,-.3)--(0,3)node[above]{$\vect B$};\draw[dashed](0,1.8)ellipse(1.2 and .4);\draw[->,thick](0,0)--(1,2)node[above right]{$\vect L$};\node[below]at(0,0){$O$};\node at(1.3,.6){$\vect\Omega_L=-\gamma\vect B$};'''
F['charged']=r'''\draw[->](0,-.3)--(0,2.9)node[above]{$\vect B$};\draw[dashed](0,1.25)ellipse(1.5 and .45);\fill(1.1,1.55)circle(3pt)node[right]{$q,m$};\fill(0,1.25)circle(2pt)node[left]{$O$};\draw[->](0,1.25)--(1.1,1.55)node[midway,above]{$\vect r$};\node at(.3,-.7){中心势 $U(r)$};'''
F['harmonic']=F['charged'].replace('中心势 $U(r)$',r'$U=m\omega_c^2r^2/2$')
F['nmr']=r'''\draw[->](0,0)--(0,2.9)node[above]{$B_0$};\draw[->](0,0)--(2,0)node[right]{$B_1$};\draw[->,thick](0,0)--(1.3,2)node[right]{$\vect\mu$};\draw[dashed](-.6,.2)arc(180:360:.6 and .2);\node[below left]at(0,0){$O$};\node at(1.2,-.8){共振旋转分量};'''
F['length']=r'''\fill(0,0)circle(2pt)node[below]{$A$};\fill(2.3,1)circle(2pt)node[right]{$B$};\draw[very thick](0,0)--(2.3,1)node[midway,below]{$l$};\draw[->](2.3,1)--(1.8,2.15)node[above]{$\vect v_B-\vect v_A$};\draw[dashed](0,0)circle(2.51);'''
F['instant']=r'''\draw[gray](-1.2,0)--(3,0);\fill(0,0)circle(2pt)node[below]{$A$};\fill(2,0)circle(2pt)node[below]{$B$};\draw[->](0,0)--(0,1.2)node[above]{$u$};\draw[->](2,0)--(2,2)node[above]{$w$};\draw[<->](0,-.6)--(2,-.6)node[midway,below]{$d$};'''
F['threepoints']=r'''\draw[thick](0,0)--(2.8,0)--(1,2)--cycle;\fill(0,0)circle(2pt)node[below]{$A$};\fill(2.8,0)circle(2pt)node[below]{$B$};\fill(1,2)circle(2pt)node[above]{$D$};\node at(1.4,.65){$M_A=M_B=M_D=0$};'''
F['forceshift']=r'''\fill(0,0)circle(2pt)node[below]{$O$};\fill(2.5,0)circle(2pt)node[below]{$A$};\fill(1.6,1.8)circle(2pt)node[left]{$P_i$};\draw[->](0,0)--(1.6,1.8)node[midway,left]{$\vect r_{OP_i}$};\draw[->](2.5,0)--(1.6,1.8);\draw[->,thick](1.6,1.8)--(2.7,2.3)node[right]{$\vect F_i$};\draw[->](0,0)--(2.5,0)node[midway,below]{$\vect r_{OA}$};'''
F['threeforcecouple']=r'''\draw[->,thick](0,0)--(1.3,0)node[above]{$F\vect i$};\draw[->,thick](0,0)--(0,1.3)node[left]{$F\vect j$};\draw[->,thick](2,0)--(.9,-1.1)node[below]{$-F(\vect i+\vect j)$};\node[below left]at(0,0){$O$};\node[above]at(2,0){$(a,0)$};\draw[->](2.8,.3)arc(0:260:.4);\node at(2.7,1.1){$M_c=aF$};'''
F['rodaxis']=r'''\draw[very thick](-1.3,-1)--(1.3,1)node[above right]{$L,m$};\draw[->](0,-1.6)--(0,2)node[above]{$\vect n$};\fill(0,0)circle(2pt)node[below right]{$C$};\node at(.35,.65){$\beta$};'''
F['offsetsphere']=F['sphere']+r'\draw[thick](2,-1.4)--(2,1.5);\draw[<->](0,-1.7)--(2,-1.7)node[midway,below]{$d$};'
F['degenerate']=r'''\draw(0,0)ellipse(1.6 and .5);\draw[->](0,0)--(2,0)node[right]{$\vect e_1$};\draw[->](0,0)--(-.85,-.9)node[below]{$\vect e_2$};\draw[->](0,0)--(0,2)node[above]{$\vect e_3,C$};\draw[->,thick](0,0)--(1.1,.65)node[right]{$\vect e'_1$};\node at(0,-1.5){横向重根 $A,A$};'''
F['ringdisk']=r'''\draw[thick](-1.7,.4)--(2.8,-1);\draw(-.7,1.2)circle(.7);\draw(.95,.68)circle(.7);\draw(.95,.68)--(1.65,.68);\node at(-.7,2.2){圆环};\node at(1,1.7){圆盘};\node at(.3,-1.4){同半径 $a$，坡角 $\beta$};'''
F['torquefree']=F['principal'].replace(r'$I_1<I_2<I_3$',r'$\vect M=0,\quad \vect L=\mathrm{const}$')
F['nutation']=r'''\draw[->](0,0)--(3.8,0)node[right]{$u=\cos\theta$};\draw[->](0,-.4)--(0,2.1)node[above]{$f(u)$};\draw[thick]plot[smooth]coordinates{(.3,-.3)(.8,0)(1.4,1)(2.2,1.25)(3,0)(3.3,-.4)};\node[below]at(.8,0){$u_-$};\node[below]at(3,0){$u_+$};\draw[dashed](1.8,0)--(1.8,1.3);\node[above]at(1.8,1.4){$K/P$};'''
F['frequency']=r'''\draw[->](0,0)--(0,2.8)node[above]{$B$};\draw(0,1.4)ellipse(1.1 and .35);\draw[->](1.1,1.4)arc(0:150:1.1 and .35);\node at(0,-.5){$\omega_0=|\gamma|B$};\node at(0,-1.1){$f_0=\omega_0/(2\pi)$};'''
F['levels']=r'''\draw[thick](-1.2,2)--(1.2,2);\draw[thick](-1.2,0)--(1.2,0);\node[left]at(-1.2,2){$E_+$};\node[left]at(-1.2,0){$E_-$};\draw[<->](.6,0)--(.6,2)node[midway,right]{$\Delta E$};\node at(0,-.8){$\mu_z=\pm\gamma\hbar/2$};'''
EM=['translate','base','axes','turntable','top','hanging','swingdisk','euler','earth','satellite','cone','vslider','euler','finite','parallel','couple','wrench','rodedge','lrods','wallrod','bowl','logs','blocks','rod','lamina','cylinder','sphere','ellipsoid','hemisphere','cube','cube','box','box','triangle','octant','cube','diskgyro','drivedisk','pendulum','physpend','rotorrod','balance','tipcube','pulley','tiltdisk','trod','ladder','slope','unwind','fourpoints','planet','groove','hoist','corner','hslider','hslider2','ballboard','propeller','principal','freegyro','heavytop','heavytop','weightedloop','charged','harmonic','nmr']
TM=['length','translate','finite','instant','euler','top','threepoints','slope','forceshift','threeforcecouple','rodaxis','offsetsphere','hemisphere','degenerate','ringdisk','physpend','rotorrod','fourpoints','planet','ballboard_rev','torquefree','principal','freegyro','heavytop','heavytop','nutation','larmor','frequency','levels','nmr']
assert len(EM)==66 and len(TM)==30
rows=[]
start=r'\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth,every node/.style={font=\small,inner sep=1.5pt,text=black},line width=.65pt]'
for prefix,keys in [('ex',EM),('tr',TM)]:
 for n,k in enumerate(keys,1):
  body=F[k]
  if prefix=='tr' and n==17:body=body.replace('$l,m$','$L,m$').replace('$L$','$d$').replace(r'$z,\omega$',r'$z,\Omega$')
  if prefix=='tr' and n==18:body=body.replace('$v,a$','$v$')
  if prefix=='tr' and n==19:body=body.replace('$M$','$P$')
  if prefix=='tr' and n==5:body=body.replace('$(1.3,2.4)$','$(0,2.4)$')
  # Corrections found by independent visual review.
  if k=='translate':
   body=body.replace('(.36,.56)rectangle(1.86,1.26)','(.06,.46)rectangle(1.56,1.16)').replace('(1.65,1.06)','(1.35,1.01)')
  if prefix=='ex' and n==3:body=body.replace('(-.6,.8)--(.15,2.1)node[left]','(-.6,.8)--(.15,-.2)node[left]')
  if prefix=='ex' and n==37:
   body=body.replace(r'\node[left]at(.6,1.1){$h$};',r'\node[left]at(.32,.5){$h$};').replace(r'\node[right]at(1.6,1.55){$m,a$};',r'\node[right]at(1.8,2){$m,a$};').replace(r'\node at(2,1.5){$\dot\psi$};',r'\node at(2.4,1){$\dot\psi$};')
  if prefix=='ex' and n==38:
   body=body.replace(r'\draw[->](-1.55,0)arc(180:100:1.55);',r'\draw[->](-1.85,0)arc(180:125:1.85);').replace('at(-1.5,1.5)','at(-2.05,1.3)')
  if prefix=='ex' and n==39:body=body.replace(r'node[midway,right]{$L$}',r'node[pos=.77,right]{$L$}')
  if prefix=='ex' and n==43:body=body.replace(r'node[below]{$mg$}',r'node[right=3pt]{$mg$}')
  if k=='fourpoints':body=body.replace(r'\draw[->](0,0)--(1.9,0)node[right]',r'\draw[->](0,.4)--(1.8,.4)node[right]')
  if prefix=='ex' and n==53:body=body.replace(r'\draw[->](-1.9,1.6)arc(170:70:.75);',r'\draw[->](-1.2,2.3)arc(90:190:.8);')
  if prefix=='ex' and n==54:body=body.replace(r'\node at(1.5,1){$Q,r$};',r'\node at(1.5,1.6){$Q,r$};')
  if prefix=='ex' and n==56:body=body.replace(r'\node at(2.8,.25){$30^\circ$};',r'\node at(3,.7){$30^\circ$};')
  if prefix=='ex' and n==62:body=body.replace(r'\draw[->](-.4,2.55)arc(180:0:.4 and .15);','').replace(r'$\Omega$',r'$\dot\varphi(0)=0$')
  if prefix=='tr' and n==5:
   body=r'\draw[->,thick](0,-.3)--(0,2.7)node[above]{$z=\zeta$};\draw[->,gray](0,0)--(2.4,0)node[right]{$\xi$};\draw[->,gray](0,0)--(-1,-.8)node[below left]{$\eta$};\draw[->,thick](0,0)--(1.55,.8)node[right]{$x$};\draw[->,thick](0,0)--(-.9,1.3)node[left]{$y$};\draw[->](.7,0)arc(0:27:.7);\node at(1.4,-.6){$\chi=\varphi+\psi$};\node at(1.4,2){$\theta=0$，节点轴不唯一};'
  if prefix=='tr' and n==7:body=body.replace(r'\node at(1.4,.65){$M_A=M_B=M_D=0$};',r'\node at(1.4,2.65){$M_A=M_B=M_D=0$};')
  if k=='slope':
   body=body.replace('(1.7,1.46)','(1.7,1.5206)').replace('(1.3,.65)','(1.3215,.7047)').replace('at(2.7,1.8)','at(2.95,2.2)')
  if prefix=='tr' and n==10:
   body=body.replace(r'\draw[->](2.8,.3)arc(0:260:.4);',r'\draw[->](3.3,.3)arc(0:260:.4);').replace('at(2.7,1.1)','at(3.1,1.2)')
  if prefix=='tr' and n==15:
   body=r'\draw[thick](-1.7,.4)--(2.8,-1);\draw(-.7,.822)circle(.7);\draw(.95,.309)circle(.7);\draw(.95,.309)--(1.65,.309);\node at(-.7,1.85){圆环};\node at(1,1.35){圆盘};\node at(.3,-1.55){同半径 $a$，坡角 $\beta$};'
  if prefix=='tr' and n==18:
   body=body.replace(r'270/A',r'270/P').replace(r'$O$',r'$C$')
  if prefix=='tr' and n==19:body=body.replace(r'$A$',r'$C$').replace(r'$\Omega$',r'$\Omega\vect k$')
  if prefix=='tr' and n==20:body=body.replace(r'$m,r$',r'$m,R$')
  if prefix=='tr' and n==22:
   body=body.replace(r'(0,0)--(.4,1.9)node[right]{$\vect\omega$}',r'(0,0)--(-.75,-.6)node[above left]{$\Omega\vect e_2$}')
  if prefix=='tr' and n==29:
   body=body.replace(r'$E_+$',r'$E_{\rm high}$').replace(r'$E_-$',r'$E_{\rm low}$').replace(r'$\Delta E$',r'$|\Delta E|$')
  if k=='slope':
   body=body.replace('(1.7,1.5206)','(1.7,1.51884)').replace('(1.3215,.7047)','(1.3219,.7021)')
   body=body.replace(r'circle(2pt)node[above]{$C$}',r'circle(2pt)node[above left]{$C$}').replace(r'node[right]{$N$}',r'node[right=4pt]{$N$}')
  if k=='planet':
   body=body.replace(r'\draw[->](1.75,-1)--(1.75,-.3)node[right]{$\Omega$};',r'\draw[->](.2,1.35)arc(82:145:1.365);\node at(-.8,1.65){$\Omega\vect k$};')
   body=body.replace(r'\draw[->](1.75,-1)--(1.75,-.3)node[right]{$\Omega\vect k$};',r'\draw[->](.2,1.35)arc(82:145:1.365);\node at(-.8,1.65){$\Omega\vect k$};')
  if prefix=='ex' and n==52:
   body=body.replace('(.65,-1.12)','(.65,-1.12583)').replace(r'\node at(.25,-.7){$\varphi$};',r'\draw(0,-.45)arc(-90:-60:.45);\node at(.25,-.38){$\varphi$};').replace('node[midway,right]{$q$}','node[pos=.6,right=4pt]{$q$}')
  if prefix=='tr' and n==23:body+=r'\node at(.4,-1){$C>A,\ s>0$ 示意};'
  if k in ['sphere','ellipsoid','offsetsphere']:
   body=body.replace(r'\node[below right]at(0,0){$O=C$};',r'\node at(.45,-.65){$O=C$};')
  if k=='hemisphere':body=body.replace(r'\draw[<->](-.55,0)--(-.55,.56)node[midway,left]{$3a/8$};',r'\draw[dashed](0,.56)--(-1.85,.56);\draw[<->](-1.85,0)--(-1.85,.56)node[midway,left]{$3a/8$};')
  if prefix=='ex' and n==22:body=body.replace(r'$5+4+3+2+1$',r'第（3）问：底层侧推截面')
  if k=='cone':
   body=body.replace('(1.55,2.15)','(1.99264,2.37474)').replace('(2.32,1.075)','(2.54632,1.18737)')
  if prefix=='ex' and n==24:body=body.replace(r'\node at(.55,1.1){$L$};',r'\node at(1.55,.65){$L$};')
  if prefix=='ex' and n==43:body=body.replace('++(-.34,-.94)','++(-.238,-.658)')
  if prefix=='ex' and n==3:body=body.replace(r'(-.6,.8)--(.15,-.2)node[left]{$\vect\omega$}',r'(-.6,.8)--(.15,-.2)node[midway,left=4pt]{$\vect\omega$}')
  if k in ['sphere','ellipsoid','offsetsphere']:body=body.replace(r'at(.45,-.65){$O=C$}',r'at(.8,-.65){$O=C$}')
  if prefix=='ex' and n==52:
   body=body.replace(r'node[pos=.6,right=4pt]{$q$}','').replace(r'\node at(.25,-.38){$\varphi$};',r'\node at(.55,-.25){$\varphi$};\node at(1.2,.45){$OC=q$};')
  if prefix=='tr' and n==5:body=body.replace(r'\node at(1.4,2){$\theta=0$，节点轴不唯一};',r'\node at(1.4,2){$\theta=0$};\node at(.8,-1.4){节点轴不唯一};')
  if prefix=='tr' and n==18:
   body=r'\draw(0,0)circle(1.25);\draw[thick](-1.8,-1.25)--(2.2,-1.25);\fill(0,-1.25)circle(2pt)node[below]{$P$};\fill(0,0)circle(2pt)node[below left]{$C$};\draw[->](0,.4)--(1.8,.4)node[right]{$v$};\node at(-1.2,1.75){$R$};'
  if prefix=='tr' and n==20:body=body.replace(r'circle(2pt)node[right]{$m,R$};',r'circle(2pt);\node[left]at(-.85,.8){$m,R$};')
  if k in ['sphere','ellipsoid','offsetsphere']:body=body.replace(r'\node at(.8,-.65){$O=C$};',r'\node[fill=white,inner sep=2pt] at(.8,-.65){$O=C$};')
  if prefix=='ex' and n==1:body=body.replace(r'{$P$}',r'{$A$}')
  if prefix=='tr' and n==2:body=body.replace(r'node[above left]{$C$}',r'node[above left]{$A$}')
  if prefix=='ex' and n==21:
   body+=r'\draw[dashed](1.7,0)--(2.8,0);\draw(2.3,0)arc(0:21.9:.6);\node at(2.55,.13){$\theta$};'
  if prefix=='ex' and n==44:
   body=body.replace('(1.4,.3)--(1.4,-.5)','(1.9,.3)--(1.9,-.5)')
   body+=r'\draw[->,thick](-.65,.45)--(-.65,1.4)node[midway,left]{$T_1$};\draw[->,thick](.65,.1)--(.65,1.1)node[midway,right]{$T_2$};'
  if prefix=='ex' and n==47:
   body+=r'\draw[->,ink](2.5,0)--(1.92,.557)node[above right]{$\vect e_1$};\draw[->,ink](2.5,0)--(1.94,-.58)node[below]{$\vect e_2$};'
  key=f'{prefix}{n:02}';(D/(key+'.tex')).write_text(start+'\n'+body+'\n\\end{tikzpicture}\n'); rows.append({'key':key,'family':k,'path':'题图/'+key+'.tex'})
(P/'工作文件/逐题题图清单.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('96 editable problem diagrams written')
