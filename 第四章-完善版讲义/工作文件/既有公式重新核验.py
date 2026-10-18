import sympy as s, json, math
from pathlib import Path
out=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
 vals=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
 residual=[s.trigsimp(s.simplify(e)) for e in vals]
 ok=all(e==0 for e in residual)
 checks.append({'项目':name,'通过':ok,'残差':[str(e) for e in residual]})
 if not ok: print('FAIL',name,residual)
t=s.symbols('t',real=True); O=s.symbols('O',positive=True);x=s.Function('x')(t);y=s.Function('y')(t);z=s.Function('z')(t)
q=s.Matrix([x,y,z]);Q=s.Matrix([[s.cos(O*t),-s.sin(O*t),0],[s.sin(O*t),s.cos(O*t),0],[0,0,1]]);Om=s.Matrix([0,0,O])
check('旋转矩阵保持正交',Q.T*Q-s.eye(3));check('速度运输',s.diff(Q*q,t)-Q*(s.diff(q,t)+Om.cross(q)))
check('加速度运输及两倍科氏项',s.diff(Q*q,t,2)-Q*(s.diff(q,t,2)+2*Om.cross(s.diff(q,t))+Om.cross(Om.cross(q))))
g,l,a,m,k,R,u,lam=s.symbols('g l a m k R u lam',positive=True,real=True);th=s.Function('th')(t)
qb=s.Matrix([l*s.sin(th),0,-l*s.cos(th)]);vb=s.diff(qb,t)+Om.cross(qb)
check('调速器速度分量',vb-s.Matrix([l*s.diff(th,t)*s.cos(th),O*l*s.sin(th),l*s.diff(th,t)*s.sin(th)]))
ab=s.diff(qb,t,2)+2*Om.cross(s.diff(qb,t))+Om.cross(Om.cross(qb))
check('调速器加速度分量',ab-s.Matrix([l*s.diff(th,t,2)*s.cos(th)-l*s.diff(th,t)**2*s.sin(th)-O**2*l*s.sin(th),2*O*l*s.diff(th,t)*s.cos(th),l*s.diff(th,t,2)*s.sin(th)+l*s.diff(th,t)**2*s.cos(th)]))
latitude=lam-u*t/R;rc=s.Matrix([R*s.cos(latitude)*s.cos(O*t),R*s.cos(latitude)*s.sin(O*t),R*s.sin(latitude)])
ENU=s.Matrix([[0,-s.sin(lam),s.cos(lam)],[1,0,0],[0,s.cos(lam),s.sin(lam)]])
vc=ENU.T*s.diff(rc,t).subs(t,0);ac=ENU.T*s.diff(rc,t,2).subs(t,0)
check('南行车惯性速度',vc-s.Matrix([O*R*s.cos(lam),-u,0]))
check('南行车惯性加速度',ac-s.Matrix([2*O*u*s.sin(lam),O**2*R*s.sin(lam)*s.cos(lam),-u**2/R-O**2*R*s.cos(lam)**2]))
check('南行车加速度模',ac.dot(ac)-(u**4/R**2+O**4*R**2*s.cos(lam)**2+2*O**2*u**2*(1+s.sin(lam)**2)))
phi=s.symbols('phi',real=True);Us=m*g*l*(1-s.cos(phi))-m*O**2*l**2*s.sin(phi)**2/2
check('轴上摆角方程',-s.diff(Us,phi)/(m*l*l)-s.sin(phi)*(O*O*s.cos(phi)-g/l))
check('轴上摆临界四次势',s.limit(Us.subs(O**2,g/l)/phi**4,phi,0)-m*g*l/8)
Uf=m*g*l*(1-s.cos(phi))-m*O**2*(a+l*s.sin(phi))**2/2
freq=s.diff(Uf,phi,2)/(m*l*l)
check('偏置摆稳定频率',freq.subs(g,O**2*(a+l*s.sin(phi))*s.cos(phi)/s.sin(phi))-O**2*(s.sin(phi)**2+a/(l*s.sin(phi))))
M,L=s.symbols('M L',positive=True);Ur=M*g*L*(1-s.cos(phi))/2-M*O**2*L**2*s.sin(phi)**2/6
check('均匀杆力矩方程',-s.diff(Ur,phi)/(M*L**2/3)-s.sin(phi)*(O**2*s.cos(phi)-3*g/(2*L)))
check('均匀杆临界四次势',s.limit(Ur.subs(O**2,3*g/(2*L))/phi**4,phi,0)-M*g*L/16)
ss=s.symbols('ss',real=True);Fcf=s.integrate(M/L*O**2*ss*s.sin(phi),(ss,0,L));check('杆离心合力',Fcf-M*O**2*L*s.sin(phi)/2)
check('杆离心合力作用位置',s.integrate(ss**2,(ss,0,L))/s.integrate(ss,(ss,0,L))-2*L/3)
check('合力力矩与分布力矩一致',Fcf*(2*L/3)*s.cos(phi)-M*O**2*L**2*s.sin(phi)*s.cos(phi)/3)
u0=s.symbols('u0',real=True);xf=a*s.cosh(O*t)+u0/O*s.sinh(O*t)
check('自由滑珠完整初值解',s.diff(xf,t,2)-O**2*xf)
check('自由滑珠初速度',s.diff(xf,t).subs(t,0)-u0)
J=m*(s.diff(xf,t)**2-O**2*xf**2)/2;check('滑珠雅可比量守恒',s.diff(J,t))
E=m*(s.diff(xf,t)**2+O**2*xf**2)/2;check('滑珠驱动功率',s.diff(E,t)-2*m*O**2*xf*s.diff(xf,t))
qf=s.Matrix([u*t*s.cos(O*t),-u*t*s.sin(O*t),0]);check('自由粒子旋转轨迹',s.diff(qf,t,2)+2*Om.cross(s.diff(qf,t))+Om.cross(Om.cross(qf)))
Oe=s.symbols('Oe',positive=True);ome=s.Matrix([0,Oe*s.cos(lam),Oe*s.sin(lam)]);ve=s.Matrix(s.symbols('ue ve we',real=True));ue,veN,we=ve
check('当地科氏力三分量',-2*ome.cross(ve)-s.Matrix([2*Oe*s.sin(lam)*veN-2*Oe*s.cos(lam)*we,-2*Oe*s.sin(lam)*ue,2*Oe*s.cos(lam)*ue]))
gv=s.Matrix([0,0,-g])-ome.cross(ome.cross(s.Matrix([0,0,R])))
check('有效重力分量',gv-s.Matrix([0,-Oe**2*R*s.sin(lam)*s.cos(lam),-g+Oe**2*R*s.cos(lam)**2]))
check('有效重力模',gv.dot(gv)-(g*g-2*g*Oe**2*R*s.cos(lam)**2+Oe**4*R**2*s.cos(lam)**2))
f=s.symbols('f',nonzero=True,real=True);uI=u*s.cos(f*t);vI=-u*s.sin(f*t)
check('惯性圆东西方程',s.diff(uI,t)-f*vI);check('惯性圆北向方程',s.diff(vI,t)+f*uI)
h,w0,v0=s.symbols('h w0 v0',real=True);c=s.symbols('c',real=True);sig=s.symbols('sig',real=True)
pj=s.Matrix([u0*t+(sig*v0-c*w0)*t*t+c*g*t**3/3,v0*t-sig*u0*t*t,h+w0*t-g*t*t/2+c*u0*t*t])
basev=s.Matrix([u0,v0,w0-g*t]);check('任意抛体一阶积分',s.diff(pj,t,2)-(s.Matrix([0,0,-g])-2*s.Matrix([0,c,sig]).cross(basev)))
check('上抛返回偏西',(-c*w0*t*t+c*g*t**3/3).subs(t,2*w0/g)+4*c*w0**3/(3*g*g))
ww=2*Oe;C=s.cos(lam);S=s.sin(lam)
fall=s.Matrix([g*C*(t/ww-s.sin(ww*t)/ww**2),-g*S*C*(t*t/2-(1-s.cos(ww*t))/ww**2),h-g*S*S*t*t/2-g*C*C*(1-s.cos(ww*t))/ww**2])
check('常重力落体三维精确积分',s.diff(fall,t,2)-s.Matrix([0,0,-g])+2*ome.cross(s.diff(fall,t)))
K=s.symbols('K',positive=True);w=s.symbols('w',positive=True);A,B=s.symbols('A B');zeta=s.exp(-s.I*sig*t)*(A*s.cos(K*t)+B*s.sin(K*t))
check('傅科复变量通解',s.expand(s.diff(zeta,t,2)+2*s.I*sig*s.diff(zeta,t)+w*w*zeta).subs(w*w,K*K-sig*sig))
zrest=zeta.subs({A:a,B:s.I*sig*a/K});check('傅科静释初速度',s.diff(zrest,t).subs(t,0))
r=s.Matrix(s.symbols('rx ry rz'));vp=s.Matrix(s.symbols('vx vy vz'));om=s.Matrix(s.symbols('Ox Oy Oz'));vi=vp+om.cross(r)
check('雅可比代数关系',m*vi.dot(vi)/2-om.dot(r.cross(m*vi))-(m*vp.dot(vp)/2-m*om.cross(r).dot(om.cross(r))/2))

# Independent checks added during the content-depth audit.
x0,nu,gamma=s.symbols('x0 nu gamma',real=True,nonzero=True)
xs=x0*s.cos(nu*t)+u0/nu*s.sin(nu*t)
xn=x0+u0*t
xh=x0*s.cosh(gamma*t)+u0/gamma*s.sinh(gamma*t)
check('双弹簧低速反力与横向绝对加速度',2*m*O*s.diff(xs,t)-2*m*O*(-nu*x0*s.sin(nu*t)+u0*s.cos(nu*t)))
check('双弹簧临界反力',2*m*O*s.diff(xn,t)-2*m*O*u0)
check('双弹簧高速反力',2*m*O*s.diff(xh,t)-2*m*O*(gamma*x0*s.sinh(gamma*t)+u0*s.cosh(gamma*t)))
check('自由滑珠指数初值系数',((a+u0/O)/2*s.exp(O*t)+(a-u0/O)/2*s.exp(-O*t)-xf).rewrite(s.exp))
check('偏置摆小转速频率极限',s.limit((O**2*(s.sin(phi)**2+a/(l*s.sin(phi)))).subs(phi,O**2*a/g),O,0)-g/l)
Tension,qload,ell,xx=s.symbols('Tension qload ell xx',positive=True)
mu=s.symbols('mu',positive=True)
ybelt=qload*xx*(ell-xx)/(2*(Tension-mu*u*u))
check('循环皮带法向运动与张力平衡',Tension*s.diff(ybelt,xx,2)+qload-mu*u*u*s.diff(ybelt,xx,2))
check('小挠度皮带两端条件',s.Matrix([ybelt.subs(xx,0),ybelt.subs(xx,ell)]))
amp,X,Y=s.symbols('amp X Y',real=True)
height=l-s.sqrt(l*l-amp*amp*(X*X+Y*Y))
check('傅科摆竖直约束二阶展开',s.limit(height/amp**2,amp,0)-(X*X+Y*Y)/(2*l))
H,b,f,U,NN=s.symbols('H b f U NN',real=True,nonzero=True)
NL=NN/2-m*f*U*H/b;NR=NN/2+m*f*U*H/b
left=s.Matrix([-b/2,0,0]).cross(s.Matrix([0,0,NL]))
right=s.Matrix([b/2,0,0]).cross(s.Matrix([0,0,NR]))
cor=s.Matrix([0,0,H]).cross(s.Matrix([m*f*U,0,0]))
check('左右支承力与横向载荷的三维力矩',left+right+cor)


rd=s.symbols('rd',positive=True);px,py,rho=s.symbols('px py rho',real=True,nonzero=True)
J2=s.Matrix([[0,-1],[1,0]]);grad=s.Matrix([px,py])
vfric=-rd/(rho*(rd*rd+f*f))*grad+f/(rho*(rd*rd+f*f))*J2*grad
check('含摩擦水平风与压强力科氏力平衡',grad/rho+f*J2*vfric+rd*vfric)

nums={'巴黎进动小时':23.9345/math.sin(math.radians(48.86)),'北京进动小时':23.9345/math.sin(math.radians(39.9)),'14小时惯性圆南纬':-math.degrees(math.asin(23.9345/28)),'临界示例倾角':math.degrees(math.acos(19.6/36)),'临界示例频率':6*math.sqrt(1-(19.6/36)**2)}
result={'总项目':len(checks),'全部通过':all(v['通过'] for v in checks),'项目':checks,'数值核查':nums}
(out/'公式核验结果.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({'总项目':len(checks),'全部通过':result['全部通过'],'数值核查':nums},ensure_ascii=False));assert result['全部通过']
