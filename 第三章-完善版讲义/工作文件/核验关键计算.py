from pathlib import Path
import json, runpy, sympy as S, numpy as np

P=Path(__file__).resolve().parents[1]
runpy.run_path(str(P/'工作文件/关键计算复核.py'))
out=json.loads((P/'工作文件/关键计算复核.json').read_text())
for key,val in out.items():
    if key in ['欧拉三步图投影','欧拉三步图行列式','欧拉三步图正交误差']: continue
    assert val=='0' or isinstance(val,list) and set(val)=={'0'},(key,val)
assert out['欧拉三步图正交误差']<1e-12
assert abs(out['欧拉三步图行列式']-1)<1e-12

a,m=S.symbols('a m',positive=True)
r,t,p=S.symbols('r t p',nonnegative=True)
rho=6*m/(S.pi*a**3)
moment_x2=S.simplify(rho*S.integrate(r**4,(r,0,a))*S.integrate(S.sin(t)**3,(t,0,S.pi/2))*S.integrate(S.cos(p)**2,(p,0,S.pi/2)))
moment_xy=S.simplify(rho*S.integrate(r**4,(r,0,a))*S.integrate(S.sin(t)**3,(t,0,S.pi/2))*S.integrate(S.sin(p)*S.cos(p),(p,0,S.pi/2)))
mean_x=S.simplify(rho/m*S.integrate(r**3,(r,0,a))*S.integrate(S.sin(t)**2,(t,0,S.pi/2))*S.integrate(S.cos(p),(p,0,S.pi/2)))
assert moment_x2==m*a*a/5 and moment_xy==2*m*a*a/(5*S.pi) and mean_x==3*a/8
out['八分之一球积分']={'int_x2_dm':str(moment_x2),'int_xy_dm':str(moment_xy),'x_C':str(mean_x)}
half_x_center=S.Rational(2,5)*m*a*a-m*(3*a/8)**2
assert S.simplify(half_x_center/(m*a*a))==S.Rational(83,320)
out['实心半球移轴']={'Ixx_C_over_ma2':'83/320','Izz_C_over_ma2':'2/5','translation_along_z_changes_Izz':False}
M=np.array([[20,-18,-9],[-18,40,-6],[-9,-6,52]],dtype=float)
v,Q=np.linalg.eigh(M)
assert np.max(np.abs(v-np.array([6.826408,50.506181,54.667411])))<5e-7
out['长方体数值主轴']={'eigenvalues':v.tolist(),'residual':float(np.max(abs(M@Q-Q@np.diag(v))))}

theta,A,Pc,K,G,Omega=S.symbols('theta A P K G Omega',real=True)
U=(K-Pc*S.cos(theta))**2/(2*A*S.sin(theta)**2)+G*S.cos(theta)
fixed_K_curvature=S.diff(U,theta,2).subs(K,A*Omega*S.sin(theta)**2+Pc*S.cos(theta)).subs(G,Pc*Omega-A*Omega**2*S.cos(theta))/A
target=(Pc/A-2*Omega*S.cos(theta))**2+Omega**2*S.sin(theta)**2
assert S.trigsimp(fixed_K_curvature-target)==0
out['定常进动小章动频率']={'fixed_P_K_second_derivative_matches':True,'expression':str(target)}

# Reintegrate the exact parameter choices used by the retained trajectory figure.
src=(P.parent/'第三章-刚体力学/工作文件/内容核查/重陀螺轨迹生成.py').read_text()
ns={'__file__':str(P/'工作文件/只读数值核验.py')}
exec(src.split('src=TEX.read_text()',1)[0],ns)
trajectories=[]
for row in ns['records']:
    assert row['energy_error']<1e-9 and row['cycles']==2
    trajectories.append({k:v for k,v in row.items() if k!='points'})
out['重陀螺三个轨迹数值核验']=trajectories
out['verification_scope']='符号与数值复核覆盖摆杆转盘、曲柄滑块、球板过渡、八分之一球积分、半球平移、长方体主轴、定常进动曲率和三类陀螺轨迹；不等同于66道例题全部独立重算。'
out['status']='passed'
(P/'资料核查/关键计算核验.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('All selected symbolic and numerical checks passed.')
