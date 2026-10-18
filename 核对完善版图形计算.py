from pathlib import Path
import json,math
import numpy as np
import sympy as S
from scipy.optimize import brentq, minimize_scalar

ROOT=Path(__file__).resolve().parent
t=S.symbols('t',real=True)
checks1={};checks2={}
for z in [S.Rational(1,4),S.Integer(1),S.Rational(3,2)]:
    if z<1:
        w=S.sqrt(1-z*z);x=S.exp(-z*t)*(S.cos(w*t)+z/w*S.sin(w*t))
    elif z==1:x=(1+t)*S.exp(-t)
    else:
        a=-z+S.sqrt(z*z-1);b=-z-S.sqrt(z*z-1);x=(-b*S.exp(a*t)+a*S.exp(b*t))/(a-b)
    assert S.simplify(S.diff(x,t,2)+2*z*S.diff(x,t)+x)==0
    assert S.simplify(x.subs(t,0))==1 and S.simplify(S.diff(x,t).subs(t,0))==0
checks1['阻尼响应']='三种阻尼比1/4、1、3/2均满足原微分方程及相同初始条件x/x0=1、初速度0。'
X=t+S.sin(t);Y=S.cos(t)-1
assert S.simplify(S.diff(X,t,2)-S.diff(Y,t))==0
assert S.simplify(S.diff(Y,t,2)-(1-S.diff(X,t)))==0
assert S.simplify((S.diff(X,t)**2+S.diff(Y,t)**2)/2-Y)==2
checks1['电磁漂移']='无量纲轨迹满足洛伦兹方程；初速为2倍漂移速度，动能减电场功保持常量。'
q=S.symbols('q',real=True);W=(q*q-1)**2
for root in [-S.sqrt(S.Rational(8,5)),-S.sqrt(S.Rational(2,5)),S.sqrt(S.Rational(2,5)),S.sqrt(S.Rational(8,5))]:
    assert S.simplify(W.subs(q,root)-S.Rational(9,25))==0
assert S.diff(W,q,2).subs(q,1)==8
checks1['双势阱']='0.36U0的四个转向点与阱底二阶导8U0/a²通过解析核对。'
G=-1/q+1/(2*q*q)
assert G.subs(q,S.Rational(5,8))==G.subs(q,S.Rational(5,2))==S.Rational(-8,25)
assert S.diff(G,q).subs(q,1)==0 and S.diff(G,q,2).subs(q,1)>0
checks1['引力有效势']='示例能量-0.32下两个转向点0.625与2.5、稳定圆轨道q=1一致。'
f=lambda x:x*(1+x)*math.exp(-x)-.4
rmin=brentq(f,.1,1);rmax=brentq(f,3,6)
wy=lambda x:.2/x**2-math.exp(-x)/x
rinv2=brentq(lambda x:(2+x)*math.exp(-x)-1,.5,2)
assert abs(rmax-3.8375185906)<1e-8
checks1['屏蔽有效势']={'first_minimum_q':rmin,'first_outer_maximum_q':rmax,'outer_height':wy(rmax),'second_maximum_q':rinv2}
i=math.asin(.6);j=math.asin(.4);chi=2*(i-j)
A=np.array([-1.44,1.08]);direction=np.array([math.cos(j-i),math.sin(j-i)])
B=A+3.6*math.cos(j)*direction
assert abs(np.linalg.norm(B)-1.8)<1e-12
assert np.linalg.norm(B-np.array([1.77106908,.32142544]))<1e-8
checks1['势阱折射']={'incidence_deg':math.degrees(i),'inside_deg':math.degrees(j),'deflection_deg':math.degrees(chi),'exit_point':B.tolist()}

y1=lambda x:.5*(1-x*x-math.cos(2*x));y2=lambda x:.5*(1-x*x+math.cos(2*x))
hit=brentq(y2,.8,1);nextlower=brentq(y1,1.2,1.5)
assert y1(hit)>0 and hit<nextlower and all(y2(float(x))>0 for x in np.linspace(0,hit,300)[:-1])
checks2['强冲量首碰']={'tau':hit,'upper_x_over_l':hit+.5*math.sin(2*hit),'lower_y_over_l':y1(hit),'free_extension_lower_root':nextlower}
v1=(1+2*S.cos(t))/3;v2=(1-S.cos(t))/3
assert S.simplify(v1+2*v2)==1
assert v1.subs(t,0)==1 and v2.subs(t,0)==0
checks2['弹簧双球速度']='质量加权动量m v1+2m v2=m v0恒定，初速度(v0,0)正确。'
theta=math.radians(17);lam=2
branches=[theta+math.asin(lam*math.sin(theta)),theta+math.pi-math.asin(lam*math.sin(theta))]
for big in branches:assert abs(math.atan2(math.sin(big),lam+math.cos(big))-theta)<1e-12
checks2['重粒子散射']={'lambda':lam,'lab_angle_deg':17,'cm_angles_deg':list(map(math.degrees,branches)),'maximum_lab_angle_deg':math.degrees(math.asin(1/lam))}
alpha=math.radians(10);mu=.2
demand=lambda x:(3*math.cos(x)-2*math.cos(alpha))*math.sin(x)/(1-2*math.cos(alpha)*math.cos(x)+3*math.cos(x)**2)
first=brentq(lambda x:demand(x)-mu,math.radians(25),math.radians(30))
second=brentq(lambda x:demand(x)-mu,math.radians(32),math.radians(40))
last=brentq(lambda x:demand(x)+mu,math.radians(50),math.radians(60))
assert all(abs(demand(float(x)))<=mu+1e-12 for x in np.linspace(alpha,first,300))
checks2['静摩擦首次越界']={'alpha_deg':10,'mu_s':mu,'first_deg':math.degrees(first),'later_hypothetical_crossings_deg':[math.degrees(second),math.degrees(last)]}
spring=lambda x:1/x**2+.55*(x-1)**2
outer=brentq(lambda x:spring(x)-1,2,2.5)
assert abs(spring(1)-1)<1e-12 and abs(outer-2.2012254432)<1e-8
checks2['弹簧有效势']={'beta':.55,'turning_points':[1,outer]}
rocket=S.log(2/(3-2*t))-(t-S.Rational(1,2))
assert rocket.subs(t,S.Rational(1,2))==0
assert S.diff(rocket,t).subs(t,S.Rational(1,2))==0
height=S.integrate(rocket,(t,S.Rational(1,2),1))
assert S.simplify(height-(S.Rational(3,8)-S.log(2)/2))==0
checks2['延迟起飞火箭']={'burnout_speed':float(rocket.subs(t,1)),'burnout_height':float(height),'launch_time_fraction':.5}
assert S.integrate(-S.sin(2*t)/2,(t,0,2*S.pi))==0
assert S.integrate(S.sin(t)**2,(t,0,2*S.pi))/(2*S.pi)==S.Rational(1,2)
checks2['谐振子位力与能量']='周期内D的平均为0，T/E和U/E平均均为1/2；瞬时曲线符合最大位移静止释放。'
for chapter,checks in [('第一章',checks1),('第二章',checks2)]:
    result={'status':'passed','scope':'新增定量图的解析关系、参数、根值与初始条件核对；未声称全册例题独立重推。','checks':checks}
    (ROOT/(chapter+'-完善版讲义')/'资料核查/新增定量图计算核验.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(chapter,len(checks),'checks passed')
