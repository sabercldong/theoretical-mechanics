from pathlib import Path
import sympy as S,json,math
P=Path(__file__).resolve().parents[1];checks=[]
def eq(name,a,b):
 d=S.simplify(a-b);ok=all(x==0 for x in d) if isinstance(d,S.MatrixBase) else d==0;assert ok,(name,d);checks.append({'name':name,'passed':True})
m,M,g,l,L,r,a,b,c,t,w,W,Om,be,h,k,mu,v=S.symbols('m M g l L r a b c t w W Omega beta h k mu v',positive=True)
i,j,z=[S.Matrix(x) for x in [(1,0,0),(0,1,0),(0,0,1)]]
V=S.Matrix([2,1,-1]).cross(S.Matrix([1,-2,3]));eq('例3完整叉积',V,S.Matrix([1,-7,-5]));eq('例3速率平方',V.dot(V),75)
q=S.symbols('q',real=True)
psi=S.asin(a*S.sin(Om*t)/L)
eq('例12连杆角加速度',S.diff(psi,t,2),-a*Om**2*(L**2-a**2)*S.sin(Om*t)/(L**2-a**2*S.sin(Om*t)**2)**S.Rational(3,2))
Rx=S.Matrix([[1,0,0],[0,0,-1],[0,1,0]]);Ry=S.Matrix([[0,0,1],[0,1,0],[-1,0,0]])
eq('例14先y后x',Rx*Ry,S.Matrix([[0,0,1],[1,0,0],[0,1,0]]));eq('例14先x后y',Ry*Rx,S.Matrix([[0,1,0],[0,0,-1],[-1,0,0]]))
eq('例23横向平行轴',2*m*(a*a*S.eye(3)-S.Matrix([a,0,0])*S.Matrix([a,0,0]).T),S.diag(0,2*m*a*a,2*m*a*a))
eq('例24动能分解',m*(w*L/2)**2/2+(m*L*L/12)*w*w/2,m*L*L*w*w/6)
eq('例39最低点能量',2*(m*g*L/2)*(1-S.cos(q))/(m*L*L/3),3*g*(1-S.cos(q))/L)
eq('例40最短周期驻点',S.diff(h+k*k/h,h).subs(h,k),0)
eq('例41力偶还原',L*z.cross(S.Matrix([-m*l*l*w*w*S.sin(be)*S.cos(be)/(12*L),0,0])),S.Matrix([0,-m*l*l*w*w*S.sin(be)*S.cos(be)/12,0]))
Ua,Ub,U,V,za,zb=S.symbols('Ua Ub U V za zb')
ua=(zb*U-V)/(za-zb);ub=(V-za*U)/(za-zb)
eq('例42静不平衡校正',ua+ub,-U);eq('例42偶不平衡校正',za*ua+zb*ub,-V)
xC=a*(S.cos(q)-S.sin(q))/2;yC=a*(S.sin(q)+S.cos(q))/2
eq('例43角加速度',-m*g*xC/(2*m*a*a/3),-3*g*(S.cos(q)-S.sin(q))/(4*a))
acc=2*g/7;T1=9*m*g/7;T2=10*m*g/7
eq('例44轻物动力学',T1-m*g,m*acc);eq('例44重物动力学',2*m*g-T2,2*m*acc);eq('例44滑轮动力学',(T2-T1)*r,m*r*r/2*acc/r)
D=m*r*r*w*w*S.sin(2*be)/(8*(a+b));eq('例45力偶',D*(a+b),m*r*r*S.sin(2*be)*w*w/8)
J=17*m*L*L/12;alpha=-18*g/(17*L)
eq('例46总重力矩',J*alpha,-3*m*g*L/2);eq('例46竖直反力',2*m*g+2*m*3*L/4*alpha,7*m*g/17)
y=S.symbols('y',positive=True);x=S.symbols('x',positive=True)
eq('例47本体极迹',S.expand((y*y/l-l/2)**2+x*x*y*y/l**2-l*l/4).subs(x*x,l*l-y*y),0)
f=m*g*k*k*S.sin(be)/(a*a+k*k);acc=g*S.sin(be)/(1+k*k/a**2)
eq('例48平动方程',m*acc,m*g*S.sin(be)-f);eq('例48转动方程',m*k*k*acc/a,f*a)
eq('例49平动',m*2*g/3,m*g-m*g/3);eq('例49转动',m*r*r/2*(-2*g/(3*r)),-m*g*r/3)
for key,pos,expected in [('A',-r*j,(0,v*v/r,0)),('B',-r*i,(a+v*v/r,a,0)),('C',r*j,(2*a,-v*v/r,0)),('D',r*i,(a-v*v/r,-a,0))]:
 ar=a*i+(-a/r)*z.cross(pos)-(v/r)**2*pos;eq('例50材料点'+key+'加速度',ar,S.Matrix(expected))
eq('例51接触点零速度',(a+r)*Om*j+((a+r)/r*Om*z).cross(-r*i),S.zeros(3,1))
phi,phi0=S.symbols('phi phi0',real=True);q0=S.symbols('q0',positive=True)
phi2=4*g/(3*q0)*(S.cos(phi)-S.cos(phi0));N=m*g/3*(7*S.cos(phi)-4*S.cos(phi0))
eq('例52径向方程',m*q0*phi2,N-m*g*S.cos(phi));eq('例52静摩擦系数端点',(m*g*S.sin(phi)/3/N).subs(phi,phi0),S.tan(phi0)/3)
P1,P2,P3,M1,r1,r2=S.symbols('P1 P2 P3 M1 r1 r2',positive=True)
ac=2*g*(M1/r1-P3)/(P1+P2+2*P3);TT=M1/r1-P1*ac/(2*g);SS=P3*(1+ac/g)
eq('例53轮B动力学',TT-SS,P2*ac/(2*g));eq('例53被提升物体',SS-P3,P3/g*ac)
NA=mu*m*g/(1+mu*mu);NB=m*g/(1+mu*mu)
eq('例54竖直力平衡',NB+mu*NA,m*g);eq('例54水平力平衡',NA,mu*NB)
lab=S.sqrt(2)*r;wab=-Om/S.sqrt(3);alph=2*Om*Om/(3*S.sqrt(3));aA=-r*Om*Om/S.sqrt(2)*(i+j);rab=lab*(S.sqrt(3)*i-j)/2
avec=aA+alph*z.cross(rab)-wab*wab*rab
eq('例56连杆竖直加速度',avec[1],0);eq('例56滑块水平加速度',avec[0],-(S.sqrt(2)/2+S.sqrt(6)/18)*r*Om*Om)
D0=7*M+2*m;vs=2*M*v/D0;vp=7*M*v/D0;rs=5*M*v/D0
Ef=m*vs*vs/2+M*vp*vp/2+m*rs*rs/5
eq('例57末水平动量',m*vs+M*vp,M*v);eq('例57接触无滑动',vs+rs,vp);eq('例57完整能量损失',M*v*v/2-Ef,m*M*v*v/D0)
for branch in [4+S.sqrt(14),4-S.sqrt(14)]:eq('例61定常方程根'+str(branch),branch*branch/2-4*branch+1,0)
B,Qcharge,mc,omega0=S.symbols('B Q mc omega0',real=True);om=-Qcharge*B/(2*mc)
eq('例65一阶导数消去',2*om+Qcharge*B/mc,0);eq('例65剩余回复系数',omega0**2-om**2-(Qcharge*B/mc)*om,omega0**2+om**2)
num=[('例46角加速度',float(18*9.8/(17*.5)),20.7529411764706),('例46反力模',math.hypot(96,7/17*8*9.8),101.2825257),('例66普通频率',2.68e8*3/(2*math.pi),127960574.2459),('例66九十度脉冲ms',math.pi/(2*2680)*1000,.5861180324),('例66一百八十度脉冲ms',math.pi/2680*1000,1.1722360648)]
for name,value,expected in num:
 assert math.isclose(value,expected,rel_tol=1e-7,abs_tol=1e-6),(name,value,expected);checks.append({'name':name,'passed':True,'value':value})
report={'status':'passed','count':len(checks),'method':'SymPy exact identities and independent numerical substitution','checks':checks}
(P/'资料核查/详解新增计算核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('passed',len(checks))
