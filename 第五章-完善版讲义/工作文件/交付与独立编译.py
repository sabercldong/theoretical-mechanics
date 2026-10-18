from pathlib import Path
import json,re,hashlib,zipfile,subprocess,shutil,sys
P=Path(__file__).resolve().parents[1];N='第五章-分析力学讲义-完善版'
s=(P/(N+'.tex')).read_text()
assert len(re.findall(r'^\\example\{',s,re.M))==86
assert len(re.findall(r'^\\exercise\{',s,re.M))==20
assert len(re.findall(r'^\\solution\b',s,re.M))==106
assert len(re.findall(r'^\\SolutionFigure\{',s,re.M))==106
assert len(re.findall(r'^\\OriginalFigure\{',s,re.M))==79
assert not any(w in s for w in ('自测','自我检查','理解与检查','图片来源','补充绘制','学习目标','核查建议'))
for d in ('题图','解答图'):assert len(list((P/d).glob('*.tex')))==106
readme=f'''# 第五章：分析力学

主文件：`{N}.tex`。

使用 XeLaTeX 编译，推荐安装带中文及 TikZ 支持的 TeX Live 或 MacTeX。

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error "{N}.tex"
```

也可以连续运行两至三次 `xelatex "{N}.tex"`，直至目录与交叉引用稳定。

本工程包括 86 个例题、20 道训练题及相应解答。`题图/` 和 `解答图/` 中的 212 个 TikZ 文件可直接编辑；`补充图/` 保存正文中的图形及共用模型。`原图/` 保存随正文使用的 79 个课件图单元，须与主文件一同保留。

图中符号、方向和取值范围以各题题干及图题为准。编辑后重新编译，图号、目录、公式编号和交叉引用会自动更新。
'''
(P/'README.md').write_text(readme)
files=[P/(N+'.tex'),P/'README.md']
for folder,ext in [('原图','*.pdf'),('补充图','*.tex'),('题图','*.tex'),('解答图','*.tex')]:files+=sorted((P/folder).glob(ext))
zpath=P/(N+'-LaTeX源码.zip')
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in files:z.write(f,str(Path(N)/f.relative_to(P)))
report={'file_count':len(files),'files':[{'path':str(f.relative_to(P)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files],'zip_sha256':hashlib.sha256(zpath.read_bytes()).hexdigest()}
(P/'资料核查/交付源码清单.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
target=P/'工作文件/源码独立编译'
if target.exists() and '--incremental' not in sys.argv:shutil.rmtree(target)
with zipfile.ZipFile(zpath) as z:z.extractall(target)
root=target/N
with (P/'工作文件/源码独立编译.txt').open('w') as log:
 subprocess.run(['/Users/dongxingxi/.local/bin/latexmk','-xelatex','-interaction=nonstopmode','-halt-on-error',N+'.tex'],cwd=root,stdout=log,stderr=subprocess.STDOUT,check=True)
print('Source ZIP:',zpath,'files',len(files),'standalone compilation successful')
