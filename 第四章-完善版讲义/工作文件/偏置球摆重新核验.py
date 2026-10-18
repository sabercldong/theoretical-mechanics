from pathlib import Path
import json
import sympy as s

out = []
def check(name, expr):
    terms = list(expr) if isinstance(expr, (s.MatrixBase, list, tuple)) else [expr]
    residuals = [s.simplify(s.trigsimp(v)) for v in terms]
    out.append({'项目': name, '通过': all(v == 0 for v in residuals),
                '残差': [str(v) for v in residuals]})

# 从三维位置和惯性速度重新生成 L，而非把讲义中的线性式原样代入。
phi, psi, vp, vs, ap, ass = s.symbols('phi psi vp vs ap ass', real=True)
m, l, a, Om, g = s.symbols('m l a Omega g', positive=True)
r = s.Matrix([a+l*s.sin(phi)*s.cos(psi),
              l*s.sin(phi)*s.sin(psi), -l*s.cos(phi)])
vr = r.diff(phi)*vp+r.diff(psi)*vs
vi = vr+s.Matrix([0,0,Om]).cross(r)
U = m*g*l*(1-s.cos(phi))
L = s.expand(m*vi.dot(vi)/2-U)
Td = m*l*l*(vp*vp+s.sin(phi)**2*vs*vs)/2
Ue = U-m*Om**2*(a*a+2*a*l*s.sin(phi)*s.cos(psi)+l*l*s.sin(phi)**2)/2
linear = m*Om*(a*l*s.cos(phi)*s.sin(psi)*vp
              +a*l*s.sin(phi)*s.cos(psi)*vs+l*l*s.sin(phi)**2*vs)
check('三维惯性动能展开成旋转坐标L', L-Td+Ue-linear)

def Dt(f):
    return s.diff(f,phi)*vp+s.diff(f,psi)*vs+s.diff(f,vp)*ap+s.diff(f,vs)*ass
euler = s.Matrix([Dt(s.diff(L,vp))-s.diff(L,phi),
                  Dt(s.diff(L,vs))-s.diff(L,psi)])
equil = {psi:0, vp:0, vs:0, ap:0, ass:0}
ss, cc = s.sin(phi), s.cos(phi)
balance = {g:Om**2*(a+l*ss)*cc/ss}
check('轴外平衡恢复原平衡式', euler.subs(equil).subs(balance))
Mass = euler.jacobian([ap,ass]).subs(equil)/(m*l*l)
Gyro = euler.jacobian([vp,vs]).subs(equil)/(m*l*l)
Stiff = euler.jacobian([phi,psi]).subs(equil).subs(balance)/(m*l*l)
S = s.diag(1, 1/ss)
check('球摆扰动质量矩阵', S*Mass*S-s.eye(2))
check('球摆科氏耦合矩阵', S*Gyro*S-s.Matrix([[0,-2*Om*cc],[2*Om*cc,0]]))
kp = Om**2*(ss**2+a/(l*ss))
ks = Om**2*a/(l*ss)
check('球摆有效势二阶矩阵', S*Stiff*S-s.diag(kp,ks))
w = s.symbols('omega', real=True)
char = (s.diag(kp,ks)-w*w*s.eye(2)
        +s.I*w*s.Matrix([[0,-2*Om*cc],[2*Om*cc,0]])).det()
check('球摆两种频率的久期方程', char-(kp-w*w)*(ks-w*w)+4*Om**2*cc**2*w*w)

# 低转速 a->0 的退化角坐标极限：频率仍为旋转坐标下的普通摆两偏振频率。
wg = s.symbols('omega_g', positive=True)
kvert = wg**2-Om**2
charvert = (kvert-w*w)**2-4*Om**2*w*w
check('轴上竖直球摆的两偏振极限',
      charvert-(w*w-(wg+Om)**2)*(w*w-(wg-Om)**2))


report = {'检验数': len(out), '通过数': sum(v['通过'] for v in out), '全部通过': all(v['通过'] for v in out), '结果':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k != '结果'},ensure_ascii=False))
assert report['全部通过']
