import sympy as s,json
from pathlib import Path
rows=[]
def ck(name,x):
 vals=list(x) if isinstance(x,(list,tuple,s.MatrixBase)) else [x]
 vals=[s.simplify(s.trigsimp(v)) for v in vals];ok=all(v==0 for v in vals)
 rows.append({'name':name,'passed':ok,'residual':[str(v) for v in vals]});assert ok,(name,vals)
m,g,a,b,sig,th,rd,td,r,d=s.symbols('m g a b sigma theta rd td r d',positive=True)
V=-sig*g*((a*a/2+a*b)*s.cos(th)+b*b*s.sin(th)/2)
ck('折杆总势能的一阶驻值',s.diff(V,th)-sig*g*((a*a/2+a*b)*s.sin(th)-b*b*s.cos(th)/2))
I=m*(s.Rational(3,2)*r*r-2*r*d*s.cos(th));qdd=s.symbols('qdd')
ck('半圆柱精确EL方程',I*qdd+s.diff(I,th)*td**2/2+m*g*d*s.sin(th)-(I*qdd+m*r*d*s.sin(th)*td**2+m*g*d*s.sin(th)))
m1,m2,l,px,pp=s.symbols('m1 m2 l px pp',positive=True);D=m1+m2*s.sin(th)**2
H=(m2*l*l*px**2-2*m2*l*s.cos(th)*px*pp+(m1+m2)*pp**2)/(2*m2*l*l*D)-m2*g*l*s.cos(th)
A=px-pp*s.cos(th)/l;B=(m1+m2)*pp-m2*l*s.cos(th)*px
ck('不等质量滑块摆的第四正则方程',-s.diff(H,th)+A*B*s.sin(th)/(l*D**2)+m2*g*l*s.sin(th))
k=s.symbols('k',positive=True);M=s.diag(m,2*m);K=k*s.Matrix([[2,-1],[-1,2]])
ep=[]
for sign in (-1,1):
 lam=(3+sign*s.sqrt(3))/2;v=s.Matrix([1,2-lam]);ck('不等质量振型'+str(sign),(K-k*lam/m*M)*v)
 ep.append(v/s.sqrt((v.T*M*v)[0]))
ck('质量归一振型内积',s.Matrix.hstack(*ep).T*M*s.Matrix.hstack(*ep)-s.eye(2))
q,p,F,t,q0,p0,E=s.symbols('q p F t q0 p0 E',positive=True)
W=-(2*m*(E-F*q))**s.Rational(3,2)/(3*m*F)
ck('恒力HJ特性函数',s.diff(W,q)-s.sqrt(2*m*(E-F*q)))
ck('恒力HJ能量偏导',s.diff(W,E)+s.sqrt(2*m*(E-F*q))/F)
ck('圆盘轨迹入、出切线与盘面方向',[s.Rational(27,10)*s.Rational(1344,1250)-s.Rational(81,25)*s.Rational(112,125)])
ck('驻波两半波与幅度箭头',[s.sin(s.pi*80*s.Rational(9,2)/180),s.sin(s.pi*80*s.Rational(9,8)/180)-1])
R=s.symbols('R',positive=True);om=s.symbols('Omega',real=True)
pos=s.Matrix([R*s.cos(om*t),R*s.sin(om*t),0]);ck('赤道运动法向加速度',pos.diff(t,2)+om**2*pos)
report={'checks':len(rows),'all_passed':all(x['passed'] for x in rows),'results':rows}
(Path(__file__).parent/'本轮新增验算结果.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('new checks',len(rows),'passed')
