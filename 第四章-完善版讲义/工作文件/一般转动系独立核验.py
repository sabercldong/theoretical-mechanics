from pathlib import Path
import json
import sympy as s

t=s.symbols('t',real=True)
theta=s.Function('theta')(t);phi=s.Function('phi')(t)
rz=s.Matrix([[s.cos(theta),-s.sin(theta),0],[s.sin(theta),s.cos(theta),0],[0,0,1]])
rx=s.Matrix([[1,0,0],[0,s.cos(phi),-s.sin(phi)],[0,s.sin(phi),s.cos(phi)]])
Q=rz*rx
q=s.Matrix([s.Function(n)(t) for n in ['x','y','z']])
origin=s.Matrix([t**3,s.sin(2*t),t**2])
omega=s.Matrix([s.diff(phi,t),s.diff(theta,t)*s.sin(phi),s.diff(theta,t)*s.cos(phi)])
def cross_matrix(v):
    return s.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
checks=[]
def check(name,expr):
    vals=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    residuals=[s.trigsimp(s.expand(v)) for v in vals]
    ok=all(v==0 for v in residuals)
    checks.append({'项目':name,'通过':ok,'残差':[str(v) for v in residuals]})
    assert ok,(name,residuals)

check('两级非共轴转动保持正交',Q.T*Q-s.eye(3))
check('从旋转矩阵导数恢复三维角速度',Q.T*Q.diff(t)-cross_matrix(omega))
check('移动原点和非匀速空间转动的速度通式',
      (origin+Q*q).diff(t)-origin.diff(t)-Q*(q.diff(t)+omega.cross(q)))
check('完整加速度：平动、相对、欧拉、向轴和两倍科氏项',
      (origin+Q*q).diff(t,2)-origin.diff(t,2)
      -Q*(q.diff(t,2)+omega.diff(t).cross(q)+omega.cross(omega.cross(q))+2*omega.cross(q.diff(t))))
check('角速度本身两系求导相同',(Q*omega).diff(t)-Q*omega.diff(t))
check('科氏惯性力相对功率为零',q.diff(t).dot(omega.cross(q.diff(t))))
report={'status':'passed','检查数':len(checks),'说明':'使用两级非共轴、非匀速转动和加速原点，直接对惯性系位置求导，与讲义通式比较；不以此代替所有例题的逐题重推。','项目':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'status':'passed','checks':len(checks)},ensure_ascii=False))
