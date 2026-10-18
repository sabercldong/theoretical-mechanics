from pathlib import Path
import sympy as S
import numpy as np
import json
out={}
t=S.symbols('t',real=True);a,l,w1,w2=S.symbols('a l w1 w2',real=True)
q=w1*t;s=w2*t
e1=S.Matrix([0,S.sin(q),-S.cos(q)])
e2=S.Matrix([0,S.cos(q),S.sin(q)])
e3=S.Matrix([1,0,0])
rB=l*e1+a*S.cos(s)*e2+a*S.sin(s)*e3
rC=l*e1-a*S.sin(s)*e2+a*S.cos(s)*e3
vB=-a*w1*S.cos(s)*e1+(l*w1-a*w2*S.sin(s))*e2+a*w2*S.cos(s)*e3
vC=a*w1*S.sin(s)*e1+(l*w1-a*w2*S.cos(s))*e2-a*w2*S.sin(s)*e3
aB=(2*a*w1*w2*S.sin(s)-l*w1**2)*e1-a*(w1**2+w2**2)*S.cos(s)*e2-a*w2**2*S.sin(s)*e3
aC=(2*a*w1*w2*S.cos(s)-l*w1**2)*e1+a*(w1**2+w2**2)*S.sin(s)*e2-a*w2**2*S.cos(s)*e3
for key,expr in [('摆杆圆盘B速度',S.diff(rB,t)-vB),('摆杆圆盘C速度',S.diff(rC,t)-vC),('摆杆圆盘B加速度',S.diff(rB,t,2)-aB),('摆杆圆盘C加速度',S.diff(rC,t,2)-aC)]:
 out[key]=[str(S.simplify(x)) for x in expr]
Q,L,O=S.symbols('q L Omega',real=True,positive=True)
d=S.sqrt(L**2-a**2*S.sin(Q)**2)
psi=S.asin(a*S.sin(Q)/L)
alpha=-a*O**2*(L**2-a**2)*S.sin(Q)/d**3
acc=-a*O**2*S.cos(Q)+a**2*O**2*S.cos(2*Q)/d+a**4*O**2*S.sin(Q)**2*S.cos(Q)**2/d**3
out['曲柄角加速度']=str(S.simplify(S.diff(a*O*S.cos(Q)/d,Q)*O-alpha))
out['滑块加速度']=str(S.trigsimp(S.diff(a*S.cos(Q)-d,Q,2)*O**2-acc))
m,M,v,R=S.symbols('m M v R',positive=True)
D=7*M+2*m
vb=(5*M+2*m)*v/D;V=2*m*v/D;om=5*M*v/(D*R)
out['球板动量']=str(S.simplify(m*vb+M*V-m*v))
out['球板滚动条件']=str(S.simplify(vb-R*om-V))
out['球板能量损失']=str(S.simplify(m*v**2/2-(m*vb**2+M*V**2+S.Rational(2,5)*m*R**2*om**2)/2-m*M*v**2/D))
phi,theta,psi=np.deg2rad([25,45,-20])
N=np.array([np.cos(phi),np.sin(phi),0.])
H=np.array([-np.sin(phi),np.cos(phi),0.])
zeta=np.array([0.,0.,1.])
Hp=np.cos(theta)*H+np.sin(theta)*zeta
z=-np.sin(theta)*H+np.cos(theta)*zeta
x=np.cos(psi)*N+np.sin(psi)*Hp
y=-np.sin(psi)*N+np.cos(psi)*Hp
axes=np.column_stack([x,y,z])
proj=1.65*np.array([[1.,-.55,0.],[0.,-.35,1.]])
out['欧拉三步图正交误差']=float(np.max(abs(axes.T@axes-np.eye(3))))
out['欧拉三步图行列式']=float(np.linalg.det(axes))
out['欧拉三步图投影']={k:list(np.round(proj@v,5)) for k,v in [('N',N),('H',H),("H'",Hp),('z',z),('x',x),('y',y)]}
p=Path(__file__).with_suffix('.json')
p.write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
