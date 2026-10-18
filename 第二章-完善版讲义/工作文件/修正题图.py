from pathlib import Path
P=Path(__file__).resolve().parent
p=P/'生成逐题题图.py';s=p.read_text()
start='# BEGIN QA CORRECTIONS'
if start in s:s=s[:s.index(start)]+s[s.index('EM=',s.index(start)):]
fix=r"""# BEGIN QA CORRECTIONS
F['hemishell']=F['hemishell'].replace(r'\node at(.7,.35){$a$};',r'\draw[->](.3,-.55)--(.7,.38);\node at(.15,-.65){$a$};')
F['parabola']=F['parabola'].replace(r'\draw[dashed](-.85,.7225)--(-.85,1.96);\node at(-1.2,1.25){$\dd x$};',r'\draw[dashed](-.9,.81)--(-.9,1.96);\draw[dashed](-.65,.4225)--(-.65,1.96);\draw[<->](-.9,2.2)--(-.65,2.2);\node[above]at(-.775,2.2){$\dd x$};')
F['slider']=F['slider'].replace(r'\node[below]at(2.4,0)',r'\node[below]at(2.4,-.22)').replace(r'\node at(.55,.9)',r'\node at(.25,1.05)')
F['jumpcart']=F['jumpcart'].replace('(1.4,.6)','(1.3,.533975)')
F['monkeys_unequal']=r'''\draw(0,2.6)circle(.6);\draw(-.6,2.6)--(-.6,.2);\draw(.6,2.6)--(.6,-.7);\fill(-.6,.2)circle(4pt)node[below left]{$m$};\fill(.6,-.7)circle(4pt)node[below right]{$m\prime$};\draw[dashed](-1.8,2.6)--(1.8,2.6);\node at(0,2.6){$O$};\node at(0,3.55){$I_p=0$};\draw[<->](-1.7,.2)--(-1.7,2.6)node[midway,left]{$s$};\draw[<->](1.7,-.7)--(1.7,2.6)node[midway,right]{$s\prime$};\draw[->](-.95,.3)--(-.95,1.2)node[midway,left]{$a$};\draw[->](.95,-.6)--(.95,.3)node[midway,right]{$a\prime$};'''
F['orbitspin']=F['orbitspin'].replace(r'\draw[->](2.25,0)arc(0:-90:.65);\node at(2.7,-.5){$\omega$};',r'\draw[->](2.58,.3)arc(17:-42:1.025);\node at(2.95,-.6){$\omega$};').replace(r'node[right]{$m$}',r'node[left=3pt]{$m$}')
F['springpair']=F['springpair'].replace(r'$\vect v_1$',r'$k\delta$').replace(r'$\vect v_2$',r'$k\delta$')+r'\node at(1.5,1.55){初态 $v_1=v_2=0$};'
F['groundpair']=F['groundpair'].replace(r'node[below]{$1,m$}',r'node[below left=3pt]{$1,m$}')+r'\draw[->](0,-.08)--(0,-.95)node[right]{$mg$};'
F['roughpair']=F['groundpair']+r'\draw[->](0,0)--(.9,0)node[midway,below]{$f$};\node at(2.7,.6){$|f|\le\mu_sN$};'
F['impactpair']=r'''\draw[thick](-.7,0)--(3.7,0);\coordinate(A)at(.2,0);\coordinate(B)at(2.5,1.3);\draw[very thick](A)--(B);\fill(A)circle(4pt)node[below left]{$q$};\fill(B)circle(4pt)node[right]{$2$};\fill(1.35,.65)circle(2pt)node[above]{$C$};\draw[->,thick](A)--(.2,1.5)node[left]{$K\vect n$};\draw[->](3.1,1.1)--(3.1,.3)node[right]{$\vect v^-$};\node at(1.7,-.65){接触点 $q$ 的法向冲量};'''
F['horizontalimpact']=F['horizontalimpact'].replace('2.7,.15','2.7,0').replace('(0,.15)','(0,0)').replace('(2.2,.2)--(2.2,1.2)node[left]',r'(2.7,0)--(2.7,1.2)node[left]').replace('(2.7,1.4)--(2.7,.5)','(3.2,1.4)--(3.2,.5)')
F['repulse']=r'''\draw[->,gray](-2.2,0)--(2.3,0)node[right]{$x$};\fill(0,0)circle(3pt)node[below]{$O$};\draw[dashed](-2,1)--(-.8,1);\draw[->,thick](-2,1)--(-1.3,1)node[above]{$v_\infty$};\draw[<->](-2.1,0)--(-2.1,1)node[midway,left]{$\rho$};\coordinate(Q)at(-.6,1.3);\draw[thick](-2,1)..controls(-1.5,1)and(-1.25,1)..(Q)..controls(.05,1.6)and(.8,2.4)..(1.5,3.2);\draw[dashed](0,0)--(Q)node[midway,right]{$a$};\fill(Q)circle(2pt)node[above left]{$Q$};\draw[->](Q)--(.31,1.72)node[right]{$\vect v_Q\perp OQ$};\node at(.5,-.65){最近点 $\dot r=0$};'''
F['unequalrod']=r'''\draw[very thick](0,0)--(0,2.7);\fill(0,0)circle(4pt)node[left]{$1,m_1$};\fill(0,2.7)circle(4pt)node[left]{$2,m_2$};\fill(0,1.75)circle(2pt)node[left]{$C$};\draw[<->](.6,0)--(.6,1.75)node[midway,right]{$d_1=\frac{m_2L}{M}$};\draw[<->](.6,1.75)--(.6,2.7)node[midway,right]{$d_2=\frac{m_1L}{M}$};\draw[->,thick](0,0)--(1.8,0)node[right]{$J$};\node at(.9,3.5){$M=m_1+m_2,\quad d_1+d_2=L$};'''
F['springstick']=F['springtransverse'].replace(r'$v_0$',r'$V_0/2$').replace('$1,m$','$1,2m$')+r'\node at(1.9,2.15){碰后：入射球已粘连};'
F['threebeads']=F['threebeads'].replace(r'node[right]{$M$}',r'node[below right=3pt]{$M$}').replace(r'\node at(.7,1){$a$};',r'\node at(.5,.55){$a$};')
F['highestthrow']=r'''\draw[->,gray](-.2,0)--(4,0)node[right]{$x$};\draw[dashed,domain=0:3.7,samples=35]plot(\x,{1.8-.32*(\x-1.8)^2});\coordinate(C)at(1.8,1.8);\fill(C)circle(3pt)node[above]{$C$};\draw[->,thick](C)--(3.5,1.8)node[above right]{$\delta v_H$};\draw[->,thick](C)--(.4,1.8)node[above left]{$\delta v_O$};\draw[->](3.5,1.2)--(3.5,.5)node[right]{$g$};\node at(1.8,2.65){相对质心的水平速度增量};\node at(1.8,-.6){$m_H=W/g,\quad m_O=w/g$};'''
F['velocitycircle']=r'''\draw[->,gray](-.3,0)--(4,0)node[right]{$v_x$};\draw[->,gray](0,-1.3)--(0,1.9)node[above]{$v_y$};\draw(2,0)circle(1);\coordinate(C)at(2,0);\coordinate(Pp)at(2.451498,.892272);\coordinate(Pm)at(1.080591,.393303);\draw[thick](0,0)--(3.4,1.2375);\draw[->](C)--(Pp);\draw[->,dashed](C)--(Pm);\fill(Pp)circle(2pt)node[above right]{$P_+$};\fill(Pm)circle(2pt)node[above left]{$P_-$};\node[below]at(0,0){$O$};\node[below]at(C){$C$};\draw(.7,0)arc(0:20:.7);\node at(1,.16){$\theta$};\draw(2.42,0)arc(0:63.16018:.42);\node at(2.67,.35){$\Theta_+$};\draw(2.6,0)arc(0:156.83982:.6);\node at(1.7,.83){$\Theta_-$};\node at(2,-1.6){代表构形 $\lambda=2,\ \theta=20^\circ$};'''
F['rocket']=F['rocket'].replace('$u=v-c$',r'$u_{\rm rel}=-c$')+r'\node at(0,-1.8){对地排气 $u=v-c$};'
F['rocketpad']=F['rocket'].replace(r'\draw[->,thick](0,2.7)--(0,3.5)node[right]{$v$};',r'\node at(0,3.1){台上阶段 $v=0$};')+r'\draw[thick](-1.1,-.1)--(1.1,-.1);\draw[->](-.9,.1)--(-.9,1)node[left]{$N\ge0$};'
F['gun']=F['gun'].replace('$U<0$',r'$U_{\rm rel}=-u$')+r'\node at(1,-1.6){相对喷速模型：$U=v-u$};'
F['squarewell']=F['squarewell'].replace(r'\node[above]at(1,0){$d$};',r'\node[below left]at(1,0){$d$};')
# END QA CORRECTIONS
"""
s=s.replace('EM=',fix+'EM=',1)
s=s.replace("if prefix=='tr' and n==8:body=body.replace(r'$\\alpha$',r'$\\alpha=0$')",r"""if prefix=='tr' and n==8:
   body=r'\draw[thick](0,0)rectangle(2,.6);\draw[very thick](1,.6)--(2.7,.6);\draw(.4,-.15)circle(.18);\draw(1.5,-.15)circle(.18);\node at(1,.3){$M$};\fill(2.7,.6)circle(3pt)node[above]{$m$};\draw[->](2.7,.6)--(3.9,.6)node[above]{$V$};\draw[->](.5,-.8)--(-.5,-.8)node[left]{$U$};\node at(1.8,1.6){炮管水平};'""")
s=s.replace("if prefix=='ex' and n==46:body=body.replace('$C,t_0$','$C$')",r"""if prefix=='ex' and n==46:body=F['highestthrow'].replace(r'$\delta v_H$',r'$\delta v_1$').replace(r'$\delta v_O$',r'$\delta v_2$').replace(r'$m_H=W/g,\quad m_O=w/g$',r'$m_1\delta v_1+m_2\delta v_2=0$')
  if prefix=='tr' and n==11:body=body.replace(r'$O\prime$',r'$A$').replace(r'$\vect U$',r'$\vect v_A$')""")
s=s.replace(r'node[above]{$B,m$};\draw[->](A)',r'node[above left=3pt]{$B,m$};\draw[->](A)')
p.write_text(s)
# Signed relative angular momentum expansion.
p=P/'详解扩展数据.py';s=p.read_text();s=s.replace('L_{A,z}^{\\rm rel}=mvtu-mvtu=0',r'L_{A,z}^{\rm rel}=(vt)m(-u)-(-ut)mv=0');p.write_text(s)
