from pathlib import Path
import json,math
import sympy as S
P=Path(__file__).resolve().parents[1]
checks=[]
def ok(name,expression):
 vals=list(expression) if isinstance(expression,S.MatrixBase) else [expression]
 residuals=[S.simplify(S.trigsimp(q)) for q in vals]
 assert all(q==0 for q in residuals),(name,residuals)
 checks.append({'item':name,'passed':True,'residuals':[str(q) for q in residuals]})
t=S.symbols('t',real=True);O,a,u,A,m,k,l,g,R,d,nu=S.symbols('Omega a u A m k l g R d nu',positive=True,real=True)
x0,u0=S.symbols('x0 u0',real=True);th=S.Function('theta')(t)
Q=S.Matrix([[S.cos(th),-S.sin(th),0],[S.sin(th),S.cos(th),0],[0,0,1]])
ok('旋转矩阵的反对称角速度矩阵',S.diff(Q,t)*Q.T-S.Matrix([[0,-S.diff(th,t),0],[S.diff(th,t),0,0],[0,0,0]]))
er=S.Matrix([S.cos(O*t),S.sin(O*t),0]);et=S.Matrix([-S.sin(O*t),S.cos(O*t),0])
r=(a+u*t)*er
ok('规定径向匀速运动的绝对加速度',S.diff(r,t,2)-(-O**2*(a+u*t)*er+2*O*u*et))
ok('加速平动原点的旋转管',S.diff(S.Matrix([A*t**2/2,0,0])+r,t,2)-(S.Matrix([A,0,0])-O**2*(a+u*t)*er+2*O*u*et))
psi=nu*t;ep=S.cos(psi)*er+S.sin(psi)*et
ok('偏心圆槽的完整加速度',S.diff(d*er+a*ep,t,2)-(-O**2*d*er-a*(O+nu)**2*ep))
c=S.symbols('c',positive=True)
rr=c/O*S.sin(O*t)
ok('恒绝对速率轨道约束',S.diff(rr,t)**2+O**2*rr**2-c**2)
X=rr*S.cos(O*t);Y=rr*S.sin(O*t)
ok('恒速径向运动的圆轨道',X**2+(Y-c/(2*O))**2-(c/(2*O))**2)
phi=S.symbols('phi',real=True)
F=S.sin(phi)*(O**2*S.cos(phi)-g/l)
ok('轴上摆倾斜分支的小振动频率',S.diff(F,phi).subs(g,O**2*l*S.cos(phi))+O**2*S.sin(phi)**2)
Fo=O**2*(a/l+S.sin(phi))*S.cos(phi)-g/l*S.sin(phi)
ok('偏置悬点平面内小振动频率',S.diff(Fo,phi).subs(g,O**2*l*(a/l+S.sin(phi))*S.cos(phi)/S.sin(phi))+O**2*(S.sin(phi)**2+a/(l*S.sin(phi))))
Up=m*g*l*(1-S.cos(phi))-m*g*l*S.sin(phi)**2/2
ok('临界质点摆的四次有效势',S.series(Up,phi,0,6).removeO()-m*g*l*phi**4/8)
M,L=S.symbols('M L',positive=True)
Ur=M*g*L/2*(1-S.cos(phi))-M*(3*g/(2*L))*L**2/6*S.sin(phi)**2
ok('临界均匀杆的四次有效势',S.series(Ur,phi,0,6).removeO()-M*g*L*phi**4/16)
s=S.symbols('s',real=True)
ok('均匀杆的质量一阶矩',S.integrate(s*M/L,(s,0,L))-M*L/2)
ok('均匀杆的惯量和离心力矩质量因子',S.integrate(s*s*M/L,(s,0,L))-M*L**2/3)
ok('分布离心力的等效作用点',S.integrate(s*s*M/L,(s,0,L))/S.integrate(s*M/L,(s,0,L))-2*L/3)
b,H=S.symbols('b H',positive=True);rho=S.symbols('rho',real=True)
z0=H-O**2*b**2/(4*g)
ok('旋转液体自由表面的体积约束',2*S.pi*S.integrate((z0+O**2*rho**2/(2*g))*rho,(rho,0,b))-S.pi*b*b*H)
xb=a*S.cosh(O*t)+u0/O*S.sinh(O*t)
ok('自由滑珠微分方程',S.diff(xb,t,2)-O**2*xb)
ok('自由滑珠初位置',xb.subs(t,0)-a)
ok('自由滑珠初速度',S.diff(xb,t).subs(t,0)-u0)
om,gam=S.symbols('om gam',positive=True)
for name,xt,coeff in [('稳定弹簧',x0*S.cos(om*t)+u0/om*S.sin(om*t),om**2),('临界弹簧',x0+u0*t,S.S(0)),('超临界弹簧',x0*S.cosh(gam*t)+u0/gam*S.sinh(gam*t),-gam**2)]:
 ok(name+'方程',S.diff(xt,t,2)+coeff*xt);ok(name+'初位置',xt.subs(t,0)-x0);ok(name+'初速度',S.diff(xt,t).subs(t,0)-u0)
xf=u*t*S.cos(O*t);yf=-u*t*S.sin(O*t)
ok('无真实力粒子的动系x方程',S.diff(xf,t,2)-O**2*xf-2*O*S.diff(yf,t))
ok('无真实力粒子的动系y方程',S.diff(yf,t,2)-O**2*yf+2*O*S.diff(xf,t))
lam=S.symbols('lambda',real=True);oe=S.symbols('OmegaE',positive=True)
w=oe+u/(R*S.cos(lam));pos=S.Matrix([R*S.cos(lam)*S.cos(w*t),R*S.cos(lam)*S.sin(w*t),R*S.sin(lam)])
eU=S.Matrix([S.cos(lam),0,S.sin(lam)]);eN=S.Matrix([-S.sin(lam),0,S.cos(lam)])
acc=S.diff(pos,t,2).subs(t,0)
ok('纬线行驶的天向加速度投影',acc.dot(eU)-(-oe**2*R*S.cos(lam)**2-2*oe*u*S.cos(lam)-u*u/R))
ok('纬线运动的北向引导加速度',acc.dot(eN)-w*w*R*S.sin(lam)*S.cos(lam))
f=S.symbols('f',positive=True);xc=u/f*S.sin(f*t);yc=u/f*(S.cos(f*t)-1)
ok('惯性圆x动力学',S.diff(xc,t,2)-f*S.diff(yc,t));ok('惯性圆y动力学',S.diff(yc,t,2)+f*S.diff(xc,t))
ok('惯性圆的圆心和半径',xc**2+(yc+u/f)**2-(u/f)**2)
pr,den,rad=S.symbols('pr den rad',positive=True)
V=(-f*rad+S.sqrt(f*f*rad*rad+4*rad*pr/den))/2
ok('梯度风气旋分支的二次方程',V*V/rad+f*V-pr/den)
w0=S.symbols('w0',positive=True);T0=2*w0/g
xx=-c*w0*t*t+c*g*t**3/3
ok('竖直上抛返回时的东西速度',S.diff(xx,t).subs(t,T0))
ok('竖直上抛返回时的西向位移',xx.subs(t,T0)+4*c*w0**3/(3*g*g))
h=S.symbols('h',positive=True);eps=S.symbols('eps',real=True);Tfall=S.sqrt(2*h/g);delta=c*u*Tfall/g
zland=h-g*(Tfall+eps*delta)**2/2+eps*c*u*(Tfall+eps*delta)**2
ok('东向水平抛射的落地时间一阶修正',S.series(zland,eps,0,2).removeO())
xland=u*(Tfall+eps*delta)+eps*c*g*(Tfall+eps*delta)**3/3
ok('东向水平抛射射程含时间修正',S.series(xland,eps,0,2).removeO()-(u*Tfall+eps*(u*delta+c*g*Tfall**3/3)))
sig,kap,amp=S.symbols('sigma kappa amp',real=True,positive=True)
zeta=amp*S.exp(-S.I*sig*t)*(S.cos(kap*t)+S.I*sig/kap*S.sin(kap*t))
ok('傅科摆完整静止释放解的方程',S.diff(zeta,t,2)+2*S.I*sig*S.diff(zeta,t)+(kap*kap-sig*sig)*zeta)
ok('傅科摆初位置',zeta.subs(t,0)-amp);ok('傅科摆初速度',S.diff(zeta,t).subs(t,0))
x,v,accel=S.symbols('x v accel',real=True)
J=m*v*v/2+k*x*x-m*O*O*x*x/2
Jdot=S.diff(J,x)*v+S.diff(J,v)*accel
ok('双弹簧雅可比量守恒',Jdot.subs(accel,(O*O-2*k/m)*x))
En=m*(v*v+O*O*x*x)/2+k*x*x
ok('双弹簧惯性机械能变化率',(S.diff(En,x)*v+S.diff(En,v)*accel).subs(accel,(O*O-2*k/m)*x)-2*m*O*O*x*v)
F0,y=S.symbols('F0 y',real=True)
Upf=-F0*(x*S.cos(O*t)-y*S.sin(O*t))
ok('旋转坐标中均匀力势的显式时间导数',S.diff(Upf,t)-F0*O*(x*S.sin(O*t)+y*S.cos(O*t)))
# Numerical values are independently evaluated from the problem data, not copied from the text.
num={}
OE=7.292115e-5
num['轴上摆倾角_deg']=math.degrees(math.acos(9.8/(36*.5)))
num['轴上摆小振动角频率']=6*math.sqrt(1-(9.8/18)**2)
num['偏置摆角速率']=math.sqrt((9.81/math.sqrt(3))/(.2+.5*.5))
num['偏置摆小振动角频率']=num['偏置摆角速率']*math.sqrt(1.05)
for hh in [50,100,500]:
 lat=30 if hh==50 else 45;tt=math.sqrt(2*hh/9.81)
 num[f'{hh}m_下落时间']=tt;num[f'{hh}m_东偏米']=OE*math.cos(math.radians(lat))*9.81*tt**3/3
TF=math.sqrt(200/9.81);CP=OE/math.sqrt(2);dt=CP*100*TF/9.81
num['东抛时间修正']=dt;num['东抛射程修正']=100*dt+CP*9.81*TF**3/3;num['东抛北向偏移']=-CP*100*TF**2
num['车辆支持力差']=4*1000*OE*30/math.sqrt(2)
for lat,label in [(48.86,'巴黎'),(39.90,'北京'),(60,'北纬60')]:num[label+'_进动小时']=23.9345/math.sin(math.radians(lat))
num['67m摆快周期']=2*math.pi*math.sqrt(67/9.81)
assert abs(num['轴上摆倾角_deg']-57.01)<.01
assert abs(num['偏置摆小振动角频率']-3.635)<.001
assert abs(num['50m_东偏米']-.00672)<.00001
assert abs(num['东抛射程修正']-.2528)<.0001
assert abs(num['车辆支持力差']-6.19)<.01
report={'status':'passed','sympy_version':S.__version__,'symbolic_checks':len(checks),'all_passed':True,'checks':checks,'numerical_results':num,
 'scope':'核验本轮展开解答所用的关键模型、初值、投影、积分、守恒量和数值；不把这些检查声称为每一句文字的独立证明。'}
(P/'资料核查/详解新增计算核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False))
