from pathlib import Path
import sympy as S,json,math
P=Path(__file__).resolve().parents[1];R=[]
def check(name,expr):
 q=S.simplify(expr);ok=all(S.simplify(x)==0 for x in q) if isinstance(q,S.MatrixBase) else q==0
 R.append(dict(name=name,passed=bool(ok),residual=str(q)));assert ok,(name,q)
x,y,z,a,k,m,M,g,t,v,w,J,l,alpha,theta,lam=S.symbols('x y z a k m M g t v w J l alpha theta lam',positive=True)
u,d=S.symbols('u d',real=True)
# Continuous mass integrals.
check('抛物线弓形面积',S.integrate(a-k*x*x,(x,-S.sqrt(a/k),S.sqrt(a/k)))-4*a*S.sqrt(a/k)/3)
check('抛物线弓形一阶矩',S.integrate((a*a-k*k*x**4)/2,(x,-S.sqrt(a/k),S.sqrt(a/k)))-4*a*a*S.sqrt(a/k)/5)
check('梯度半球质量',S.integrate((1+z/a)*(a*a-z*z),(z,0,a))-11*a**3/12)
check('梯度半球质心矩',S.integrate(z*(1+z/a)*(a*a-z*z),(z,0,a))-23*a**4/60)
check('线密度梯度质量',S.integrate(1+x/l,(x,0,l))-3*l/2)
check('线密度梯度质心矩',S.integrate(x*(1+x/l),(x,0,l))-5*l*l/6)
check('半圆细线质心',S.integrate(a*S.sin(theta),(theta,0,S.pi))/S.pi-2*a/S.pi)
# Momentum and energy constraints.
m1,m2=S.symbols('m_1 m_2',positive=True);mt=m1+m2;mu=m1*m2/mt
check('不等双球冲量惯量',m1*(m2*l/mt)**2+m2*(m1*l/mt)**2-mu*l*l)
check('下端冲量转速',J*(m2*l/mt)/(mu*l*l)-J/(m1*l))
check('冲量平动转动总能',J*J/(2*mt)+(J*m2*l/mt)**2/(2*mu*l*l)-J*J/(2*m1))
check('弹簧原长动能',mu*k*d*d/(2*m1)+mu*k*d*d/(2*m2)-k*d*d/2)
check('跳车两阶段末动量',100*(1+S.sqrt(3)/6)+50*(1-S.sqrt(3)/3)-150)
check('移动点绝对角动量',S.Matrix([v*t,-u*t,0]).cross(S.Matrix([m*v,0,0]))-S.Matrix([0,0,m*u*v*t]))
check('移动点相对角动量',S.Matrix([v*t,-u*t,0]).cross(S.Matrix([m*v,-m*u,0])))
# Ground contact and effective masses.
f= m*g*(3*S.cos(theta)-2*S.cos(alpha))*S.sin(theta)
N= m*g*(1-2*S.cos(alpha)*S.cos(theta)+3*S.cos(theta)**2)
qdot2=2*g*(S.cos(alpha)-S.cos(theta))/l
check('粗地双球水平反力',m*l*(-S.sin(theta)*qdot2+S.cos(theta)*g*S.sin(theta)/l)-f)
check('粗地双球竖直反力',2*m*g-m*l*(S.cos(theta)*qdot2+S.sin(theta)*g*S.sin(theta)/l)-N)
check('水平双球有效质量',1/(2*m)+(l/2)**2/(m*l*l/2)-1/m)
check('强冲量初始支持力',m*g*(4-(4+lam)+2)-m*g*(2-lam))
# Spring two-body evolution and shape coordinates.
omega=S.symbols('omega',positive=True)
x1=a+v*t/3+2*v*S.sin(omega*t)/(3*omega);x2=v*t/3-v*S.sin(omega*t)/(3*omega)
check('自由弹簧两球总动量',m*S.diff(x1,t)+2*m*S.diff(x2,t)-m*v)
check('自由弹簧相对初值',(x1-x2).subs(t,0)-a)
check('自由弹簧速度初值',S.Matrix([S.diff(x1,t).subs(t,0)-v,S.diff(x2,t).subs(t,0)]))
beta=S.symbols('beta',positive=True)
check('弹簧转折因式',x*x-1-beta*x*x*(x-1)**2-(x-1)*(x+1-beta*x*x*(x-1)))
check('绕钉径向转折因式',S.expand(2*x*x*(4-x)**2-(4-x)**2-9*x*x)-2*(x-1)*(x**3-7*x*x+4*x+8))
# Elastic collisions.
v1=(m1-m2)*v/mt;v2=2*m1*v/mt
check('一维弹性动量',m1*v1+m2*v2-m1*v)
check('一维弹性能量',m1*v1*v1+m2*v2*v2-m1*v*v)
check('一维粘连损失',m1*v*v/2-mt*(m1*v/mt)**2/2-mu*v*v/2)
check('等质量出射正交',S.Matrix([(1+S.cos(theta))/2,S.sin(theta)/2]).dot(S.Matrix([(1-S.cos(theta))/2,-S.sin(theta)/2])))
check('各向同性半角归一化',S.integrate(2*S.sin(theta)*S.cos(theta),(theta,0,S.pi/2))-1)
check('重球切线能量最大',4*S.Rational(3)/(1+3)**2-S.Rational(3,4))
# Variable mass integrations.
c,q,m0=S.symbols('c q m_0',positive=True);mass=m0-q*t
h=c*(t-mass/q*S.log(m0/mass))-g*t*t/2
check('恒流火箭高度导数',S.diff(h,t)-(c*S.log(m0/mass)-g*t))
check('恒流火箭加速度',S.diff(c*S.log(m0/mass)-g*t,t)-(c*q/mass-g))
drop_v=g*(M*t+lam*t*t/2)/(M+lam*t)
check('恒增长雨滴动量方程',S.diff((M+lam*t)*drop_v,t)-(M+lam*t)*g)
drop_s=g*t*t/4+M*g*t/(2*lam)-M*M*g*S.log(1+lam*t/M)/(2*lam*lam)
check('恒增长雨滴位移导数',S.diff(drop_s,t)-drop_v)
check('恒增长雨滴加速度',S.diff(drop_v,t)-(g/2+g*M*M/(2*(M+lam*t)**2)))
r=a+lam*t;sv=g*(r-a**4/r**3)/(4*lam)
check('球形凝结雨滴动量方程',S.diff(r**3*sv,t)-g*r**3)
check('球形凝结雨滴加速度',S.diff(sv,t)-g*(1+3*(a/r)**4)/4)
chain=l*S.cosh(S.sqrt(g/l)*t)/2
check('链条双曲函数运动方程',S.diff(chain,t,2)-g*chain/l)
check('链条能量恒等式',S.diff(chain,t)**2-g*(chain**2-l*l/4)/l)
# Finite-time virial and thermodynamic volumes.
A=S.symbols('A',positive=True);D=-m*A*A*omega*S.sin(2*omega*t)/2
T=m*A*A*omega*omega*S.sin(omega*t)**2/2;W=-m*A*A*omega*omega*S.cos(omega*t)**2
check('有限时间位力微分恒等式',S.diff(D,t)-2*T-W)
check('谐振子周期平均动能',S.integrate(T,(t,0,2*S.pi/omega))/(2*S.pi/omega)-m*A*A*omega*omega/4)
check('硬球位力体积',2*S.pi*S.integrate(x*x,(x,0,d))-2*S.pi*d**3/3)
# Numeric branches and events.
numeric={}
root=float(S.nsolve(1-t*t+S.cos(2*t),.89));numeric['强冲量首碰']=dict(tau=root,lower_height=1-root*root)
assert abs(1-root*root+math.cos(2*root))<1e-12 and 1-root*root>0
th=math.radians(20);cc=math.asin(2*math.sin(th));angles=[th+cc,th+math.pi-cc];hh=math.sqrt(1-4*math.sin(th)**2)
Ds=[math.sqrt(5+4*math.cos(x)) for x in angles]
numeric['散射两支']=dict(CM_degrees=[math.degrees(x) for x in angles],D=Ds,Jacobian=[x*x/hh for x in Ds],cross_section_contribution=[(x*x/hh)/math.sin(y/2)**4 for x,y in zip(Ds,angles)])
assert all(abs(math.atan2(math.sin(x),2+math.cos(x))-th)<1e-12 for x in angles)
numeric['绕钉转折根']=float(S.nsolve(x**3-7*x*x+4*x+8,1.65))
assert 1<numeric['绕钉转折根']<2
numeric['延迟火箭']=dict(vb=math.log(2)-.5,zb=3/8-math.log(2)/2)
report=dict(status='passed',symbolic_checks=len(R),checks=R,numeric_checks=numeric,scope='对新增长推导及关键公式的确定性核验，不代替题干、图形与物理条件的人工审阅')
(P/'资料核查/第二章详解计算核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(len(R),'symbolic checks passed; event and branch values verified')
