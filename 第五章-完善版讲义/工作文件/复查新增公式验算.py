from pathlib import Path
import json
import sympy as s

out = []

def check(name, expr):
    items = list(expr) if isinstance(expr, (list, tuple, s.MatrixBase)) else [expr]
    residuals = [s.simplify(s.trigsimp(v)) for v in items]
    out.append({'项目': name, '通过': all(v == 0 for v in residuals),
                '残差': [str(v) for v in residuals]})

# 沿真实自由粒子流输运的密度：固定点时间导数不能误当为零。
q, p, t = s.symbols('q p t', real=True)
m, a, b = s.symbols('m a b', positive=True)
rho = s.sqrt(a*b)/s.pi*s.exp(-a*(q-p*t/m)**2-b*p**2)
check('Gaussian沿自由流输运', s.diff(rho,t)+p/m*s.diff(rho,q))
check('Gaussian固定点显时导数', s.diff(rho,t)-2*a*p/m*(q-p*t/m)*rho)
check('Gaussian归一化（平移后独立积分）',
      s.sqrt(a*b)/s.pi*s.sqrt(s.pi/a)*s.sqrt(s.pi/b)-1)

# 从非零余子式实际构造零空间；不假定待证结论。
entries = s.symbols('a1 b1 c1 a2 b2 c2 a3 b3 c3')
R = s.Matrix(3,3,entries)
vec = R[1,:].T.cross(R[2,:].T)
check('三阶余子式振幅向量', R*vec-s.Matrix([R.det(),0,0]))

# 静力伸长与上坡坐标的一致性；由势能再求广义恢复力。
M,k,g = s.symbols('M k g',positive=True)
alpha,z = s.symbols('alpha z',real=True)
delta = m*g*s.sin(alpha)/k
V = k*(delta-z)**2/2+m*g*z*s.sin(alpha)
check('移动楔上坡坐标恢复力', s.diff(V,z)-k*z)

# 参数曲线的一阶积分与正长度悬链约束 Euler 链。
u,c,xc = s.symbols('u c xc',real=True)
A = s.symbols('A',positive=True)
xx=A*(u-s.sin(u)); yy=A*(1-s.cos(u))
yp=s.diff(yy,u)/s.diff(xx,u)
check('摆线独立参数代入第一积分', yy*(1+yp**2)-2*A)
Y=A*s.cosh((q-c)/A)
check('悬链线代入Euler方程的无根号等价式',
      Y*s.diff(Y,q,2)-1-s.diff(Y,q)**2)

# 两个界面角变分：消去固定水平跨度的约束。
th1,th2 = s.symbols('th1 th2',real=True)
h1,h2,n1,n2 = s.symbols('h1 h2 n1 n2',positive=True)
D=h1*s.tan(th1)+h2*s.tan(th2)
C=n1*h1/s.cos(th1)+n2*h2/s.cos(th2)
variation=s.diff(C,th1)-s.diff(C,th2)*s.diff(D,th1)/s.diff(D,th2)
check('折射角变分消去约束',
      variation-h1*(n1*s.sin(th1)-n2*s.sin(th2))/s.cos(th1)**2)

# 完整场张量的指标升降与收缩，独立用矩阵收缩。
E1,E2,E3,B1,B2,B3 = s.symbols('E1 E2 E3 B1 B2 B3',real=True)
cc = s.symbols('c',positive=True)
F = s.Matrix([[0,-E1/cc,-E2/cc,-E3/cc],
              [E1/cc,0,-B3,B2],
              [E2/cc,B3,0,-B1],
              [E3/cc,-B2,B1,0]])
metric=s.diag(1,-1,-1,-1)
Fl=metric*F*metric
check('电磁张量反对称性',F+F.T)
check('电磁张量双指标收缩',
      sum(F[i,j]*Fl[i,j] for i in range(4) for j in range(4))
      -2*(B1**2+B2**2+B3**2-(E1**2+E2**2+E3**2)/cc**2))

# 共动张量实际做洛伦兹变换，然后展开扣除实验系静质量能。
v = s.symbols('v',real=True)
eps,P = s.symbols('epsilon P',real=True)
gam=1/s.sqrt(1-v**2/cc**2)
boost=s.Matrix([[gam,gam*v/cc,0,0],
                [gam*v/cc,gam,0,0],[0,0,1,0],[0,0,0,1]])
vel=s.Matrix([gam*cc,gam*v,0,0])
T=boost*s.diag(eps,P,P,P)*boost.T
check('理想流体洛伦兹张量构造', T-(eps+P)*vel*vel.T/cc**2+P*metric)
rho0,e = s.symbols('rho0 e',real=True)
labrest=gam*rho0*cc**2
energy=(T[0,0].subs(eps,rho0*cc**2+e)-labrest)
energy_series=s.series(energy,v,0,4).removeO()
check('实验系扣静质量后的低速能量系数',
      energy_series-e-rho0*v**2/2-(e+P)*v**2/cc**2)
flux=(cc*T[1,0].subs(eps,rho0*cc**2+e)-labrest*v)
flux_series=s.series(flux,v,0,4).removeO()
check('实验系扣静质量后的低速能流系数',
      flux_series-(e+P)*v-rho0*v**3/2-(e+P)*v**3/cc**2)

# 规范动量与真实横向机械动量应区分；固定端支座力决定后者变化。
L,rhol,Amp,omega = s.symbols('L rho_l Amp omega',positive=True)
x=s.symbols('x',real=True)
for n in [1,2]:
    kn=n*s.pi/L
    field=Amp*s.sin(kn*x)*s.cos(omega*t)
    py=s.integrate(rhol*s.diff(field,t),(x,0,L))
    expected=-rhol*Amp*omega*s.sin(omega*t)*(1-(-1)**n)/kn
    check(f'固定端弦第{n}模机械横向动量',py-expected)

report={'检验数':len(out),'通过数':sum(v['通过'] for v in out),
        '全部通过':all(v['通过'] for v in out),
        '方法':'对本轮新增的关键推导独立代入或从矩阵、参数曲线与输运方程验算；不是全章自动证明。',
        '结果':out}
(Path(__file__).parent/'复查新增公式验算结果.json').write_text(
    json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='结果'},ensure_ascii=False))
print([v for v in out if not v['通过']])
assert report['全部通过']
