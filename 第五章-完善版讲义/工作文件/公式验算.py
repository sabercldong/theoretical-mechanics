from pathlib import Path
import sympy as s,json
out=[]
def check(name,expr):
    if isinstance(expr,s.MatrixBase): residual=[s.simplify(s.trigsimp(v)) for v in expr]
    elif isinstance(expr,(list,tuple)):residual=[s.simplify(s.trigsimp(v)) for v in expr]
    else:residual=[s.simplify(s.trigsimp(expr))]
    ok=all(v==0 for v in residual)
    out.append({'项目':name,'通过':ok,'残差':[str(v) for v in residual]})
q,x,th,r,t,m,l,k,g,a,v0,w,E,J,al=s.symbols('q x theta r t m l k g a v0 omega E J alpha',positive=True)
xd,td,xdd,tdd=s.symbols('xd td xdd tdd',real=True)
def dt(f):return s.diff(f,x)*xd+s.diff(f,th)*td+s.diff(f,xd)*xdd+s.diff(f,td)*tdd
L=m*xd**2+m*l*xd*td*s.cos(th)+m*l*l*td**2/2-k*x*x/2+m*g*l*s.cos(th)
check('滑块摆精确平动EL',dt(s.diff(L,xd))-s.diff(L,x)-(2*m*xdd+m*l*(tdd*s.cos(th)-td**2*s.sin(th))+k*x))
check('滑块摆精确摆角EL与交叉项抵消',dt(s.diff(L,td))-s.diff(L,th)-(m*l*xdd*s.cos(th)+m*l*l*tdd+m*g*l*s.sin(th)))
px,pt=s.symbols('px pt',real=True);D=1+s.sin(th)**2
H=(l*l*px*px-2*l*px*pt*s.cos(th)+2*pt*pt)/(2*m*l*l*D)+k*x*x/2-m*g*l*s.cos(th)
vx=(l*px-pt*s.cos(th))/(m*l*D);vt=(2*pt-l*px*s.cos(th))/(m*l*l*D)
check('精确Hamilton方程xdot',s.diff(H,px)-vx);check('精确Hamilton方程thetadot',s.diff(H,pt)-vt)
check('精确Hamilton方程pxdot',-s.diff(H,x)+k*x)
check('精确Hamilton方程ptdot',-s.diff(H,th)+m*l*vx*vt*s.sin(th)+m*g*l*s.sin(th))
check('速度反解与动量两关系',[m*(2*vx+l*vt*s.cos(th))-px,m*l*(l*vt+vx*s.cos(th))-pt])
check('勒让德变换回代',px*vx+pt*vt-L.subs({xd:vx,td:vt})-H)
y=s.symbols('y');M=m*s.Matrix([[2,l],[l,l*l]]);K=s.diag(k,m*g*l)
check('滑块摆久期多项式',(K-y*M).det()/(m*m*l*l)-(y*y-(k/m+2*g/l)*y+k*g/(m*l)))
for sign in [1,-1]:
 yy=(k/m+2*g/l+sign*s.sqrt((k/m)**2+4*(g/l)**2))/2
 check(f'滑块摆频率根{sign}',y*y-(k/m+2*g/l)*y+k*g/(m*l) if False else (yy*yy-(k/m+2*g/l)*yy+k*g/(m*l)))
Mm=m*l*l*s.Matrix([[2,1],[1,1]]);Km=m*g*l*s.diag(2,1)
for sign in [1,-1]:
 yy=(2+sign*s.sqrt(2))*g/l;aa=s.Matrix([1,-sign*s.sqrt(2)])
 check(f'双单摆本征模式{sign}',(Km-yy*Mm)*aa)
U=s.Matrix([[s.Rational(1,2),s.Rational(1,2)],[-1/s.sqrt(2),1/s.sqrt(2)]])
check('双单摆同时对角化动能',U.T*Mm*U-m*l*l*s.diag(1-1/s.sqrt(2),1+1/s.sqrt(2)))
check('双单摆同时对角化势能',U.T*Km*U-m*g*l*s.eye(2))
check('半圆柱频率代入质心',g*(4*r/(3*s.pi))/(s.Rational(3,2)*r*r-2*r*(4*r/(3*s.pi)))-8*g/(r*(9*s.pi-16)))
qq=a*s.cosh(w*t)+(v0/w-g/(2*w*w))*s.sinh(w*t)+g*s.sin(w*t)/(2*w*w)
check('竖直匀转管完整运动残差',s.diff(qq,t,2)-w*w*qq+g*s.sin(w*t));check('竖直匀转管原初值',[qq.subs(t,0)-a,s.diff(qq,t).subs(t,0)-v0])
Om=s.sqrt(4*g/(3*a));ss=2*a-a*s.cos(Om*t);yy=-(ss-a)/4
check('弹性阿特伍德动力学',m*(s.diff(yy,t,2)+s.diff(ss,t,2))+m*g/a*(ss-a)-m*g)
check('弹性阿特伍德主绳张力',2*m*g-2*m*s.diff(ss,t,2)/4-(2*m*g-s.Rational(2,3)*m*g*s.cos(Om*t)))
mu=m/2;vv=s.symbols('v',positive=True);JJ=mu*a*vv/s.sqrt(2)
check('自由双球最大伸长的转动能',JJ*JJ/(2*mu*(4*a)**2)-m*vv*vv/128)
check('自由双球速度条件',(m*vv*vv/2-m*vv*vv/4-m*vv*vv/128-s.Rational(9,2)*k*a*a).subs(vv**2,576*k*a*a/(31*m)))
rr=s.symbols('rr',real=True)
check('孔绳转折多项式分解',4*rr**3-13*rr**2+9-(rr-1)*(4*rr**2-9*rr-9))
check('孔绳两个正转折根',[s.Rational(9,4)/rr**2+rr-s.Rational(13,4) for rr in [s.Integer(1),s.Integer(3)]])
kap,Q,P=s.symbols('kappa Q P',positive=True);qf=s.sqrt(2*Q/kap)*s.cos(P);pf=s.sqrt(2*kap*Q)*s.sin(P)
check('作用量为坐标的正则变换',s.diff(qf,Q)*s.diff(pf,P)-s.diff(qf,P)*s.diff(pf,Q)-1)
UU=Q*(s.sin(P)*s.cos(P)-P)
check('源非线性变换一形式系数',[pf*s.diff(qf,Q)-P-s.diff(UU,Q),pf*s.diff(qf,P)-s.diff(UU,P)])
S=E*(q-t)-a*q**3/3
check('线性动量Hamiltonian的HJ解',s.diff(S,t)+s.diff(S,q)+a*q*q)
x0,p0,F=s.symbols('x0 p0 F');xx=x0+p0*t/m-F*t*t/(2*m);pp=p0-F*t
check('恒力HJ轨道',[s.diff(xx,t)-pp/m,s.diff(pp,t)+F]);check('恒力能量守恒',s.diff(pp*pp/(2*m)+F*xx,t))
# 以坐标定义独立导出三维尺度因子
xi,eta,theta=s.symbols('xi eta theta',positive=True);sig=s.symbols('sigma',positive=True)
vec=s.Matrix([s.sqrt(xi*eta)*s.cos(theta),s.sqrt(xi*eta)*s.sin(theta),(xi-eta)/2]);Jac=vec.jacobian([xi,eta,theta])
check('三维抛物坐标度规',Jac.T*Jac-s.diag((xi+eta)/(4*xi),(xi+eta)/(4*eta),xi*eta))
vec=s.Matrix([sig*s.sqrt((xi*xi-1)*(1-eta*eta))*s.cos(theta),sig*s.sqrt((xi*xi-1)*(1-eta*eta))*s.sin(theta),sig*xi*eta]);Jac=vec.jacobian([xi,eta,theta])
check('长旋转椭球坐标度规',Jac.T*Jac-s.diag(sig*sig*(xi*xi-eta*eta)/(xi*xi-1),sig*sig*(xi*xi-eta*eta)/(1-eta*eta),sig*sig*(xi*xi-1)*(1-eta*eta)))
a1,b1=s.symbols('a1 b1');pxi2=m*(al+E*xi-a1)/(2*xi)-J*J/(4*xi*xi);peta2=m*(-al+E*eta-b1)/(2*eta)-J*J/(4*eta*eta)
check('抛物坐标分离回代Hamiltonian',2*(xi*pxi2+eta*peta2)/(m*(xi+eta))+J*J/(2*m*xi*eta)+(a1+b1)/(xi+eta)-E)
pxi2=2*m*sig*sig*(al-a1+E*xi*xi)/(xi*xi-1)-J*J/(xi*xi-1)**2;peta2=2*m*sig*sig*(-al-b1-E*eta*eta)/(1-eta*eta)-J*J/(1-eta*eta)**2
check('长旋转椭球分离回代Hamiltonian',((xi*xi-1)*pxi2+(1-eta*eta)*peta2+J*J*(1/(xi*xi-1)+1/(1-eta*eta)))/(2*m*sig*sig*(xi*xi-eta*eta))+(a1+b1)/(xi*xi-eta*eta)-E)
B=s.Matrix(s.symbols('B1 B2 B3'));O=s.Matrix(s.symbols('O1 O2 O3'))
def crossmat(v):return s.Matrix([[0,v[2],-v[1]],[-v[2],0,v[0]],[v[1],-v[0],0]])
Eb,Eo=crossmat(B),crossmat(O);eye=s.eye(3);DD=1+B.dot(O)
FF=Eb.row_join(-eye).col_join(eye.row_join(-Eo));Pi=(-Eo).row_join(eye+B*O.T).col_join((-eye-O*B.T).row_join(Eb))/DD
check('Berry修正三组括号共同满足辛矩阵求逆',FF*Pi-s.eye(6))
# 量子相位分解：函数独立，不预设经典方程
A=s.Function('A')(x,t);Sf=s.Function('S')(x,t);hb,Vv=s.symbols('hbar V',real=True);phase=s.exp(s.I*Sf/hb);psi=A*phase
res=s.expand((s.I*hb*s.diff(psi,t)+hb*hb*s.diff(psi,x,2)/(2*m)-Vv*psi)/phase)
expected=-A*(s.diff(Sf,t)+s.diff(Sf,x)**2/(2*m)+Vv-hb*hb*s.diff(A,x,2)/(2*m*A))+s.I*hb*(s.diff(A,t)+s.diff(A,x)*s.diff(Sf,x)/m+A*s.diff(Sf,x,2)/(2*m))
check('薛定谔振幅相位展开',res-expected)
# 球面度规计算联络
R=s.symbols('R',positive=True);coords=[th,q];metric=s.diag(R*R,R*R*s.sin(th)**2);inv=metric.inv()
def Gamma(i,j,k):return s.simplify(sum(inv[i,n]*(s.diff(metric[n,k],coords[j])+s.diff(metric[n,j],coords[k])-s.diff(metric[j,k],coords[n]))/2 for n in range(2)))
check('球面Gamma_theta_phiphi',Gamma(0,1,1)+s.sin(th)*s.cos(th));check('球面Gamma_phi_thetaphi',Gamma(1,0,1)-s.cot(th))
# Liouville 图面积直接由四顶点独立算出
pts=[(4,0),(s.Rational(36,5),0),(s.Rational(39,5),s.Rational(4,5)),(s.Rational(23,5),s.Rational(4,5))]
area=sum(pts[i][0]*pts[(i+1)%4][1]-pts[(i+1)%4][0]*pts[i][1] for i in range(4))/2
check('Liouville图形面积相等',area-s.Rational(8,5)**2)

# 新增量子能级与数值结构的独立检查
h=s.symbols('h',positive=True);Ah=s.Matrix([[1-h*h*w*w,h/m],[-h*m*w*w,1]]);Js=s.Matrix([[0,1],[-1,0]])
check('辛欧拉矩阵的辛性',Ah.T*Js*Ah-Js)
Ch=s.Matrix([[m*w*w,-h*w*w/2],[-h*w*w/2,1/m]])
check('辛欧拉修正能量守恒',Ah.T*Ch*Ah-Ch)
Be=s.Matrix([[1,h/m],[-h*m*w*w,1]]);Ce=s.diag(m*w*w,1/m)
check('普通显式欧拉每步能量扩张',Be.T*Ce*Be-(1+h*h*w*w)*Ce)
rho,Ln,beta=s.symbols('rho Ln beta',positive=True);ff=s.Function('F')(rho);uu=rho**(Ln+1)*s.exp(-rho/2)*ff
rad=s.diff(uu,rho,2)+(-s.Rational(1,4)+beta/rho-Ln*(Ln+1)/rho**2)*uu
poly=rho*s.diff(ff,rho,2)+(2*Ln+2-rho)*s.diff(ff,rho)+(beta-Ln-1)*ff
check('氢径向方程代换后的多项式方程',s.expand(rad/(rho**Ln*s.exp(-rho/2))-poly))
mu,kappa,n,chi=s.symbols('mu kappa n chi',positive=True)
check('氢能级量子化',(-hb**2*chi**2/(2*mu)+mu*kappa*kappa/(2*hb**2*n*n)).subs(chi,mu*kappa/(hb**2*n)))
report={'检验数':len(out),'通过数':sum(v['通过'] for v in out),'全部通过':all(v['通过'] for v in out),'方法':'从位置、动能、度规或作用量独立导出方程并检查差值；并非全章无误的自动证明。','结果':out}
(Path(__file__).parent/'公式验算结果.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='结果'},ensure_ascii=False));print([v for v in out if not v['通过']]);assert report['全部通过']
