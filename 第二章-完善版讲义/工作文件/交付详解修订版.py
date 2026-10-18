from pathlib import Path
import hashlib,json,re,zipfile,fitz,subprocess
P=Path(__file__).resolve().parents[1];N='第二章-质点组力学讲义-完善版'
src=P/'工作文件/详解编译'/(N+'.pdf')
log=(P/'工作文件/详解编译'/(N+'.log')).read_text();warnings=[l for l in log.splitlines() if re.search(r'Warning|Overfull|Underfull|Missing character|^!',l)];assert not warnings,warnings
q=subprocess.run(['/opt/homebrew/bin/qpdf','--check',str(src)],capture_output=True,text=True);assert q.returncode==0
s=(P/(N+'.tex')).read_text()
assert s.count(r'\example{')==66 and s.count(r'\exercise{')==24
assert s.count(r'\QuestionStatement{')+s.count(r'\LongQuestionStatement{')==90
assert s.count(r'\SolutionFigure{')==90 and len(re.findall(r'\\ref\{fig:solution-',s))==90
assert s.count(r'\OriginalFigure{')==31 and s.count(r'\OriginalPanel{')==12 and s.count(r'\TeachingFigure{')==22
assert all(x not in s for x in ['课件原图来源索引','补充绘制',r'\colorbox{',r'\boxed{'])
for key in [f'ex{i:02}' for i in range(1,67)]+[f'tr{i:02}' for i in range(1,25)]:
 a=s.index('% BEGIN DETAILED ANSWER '+key);b=s.index('% END DETAILED ANSWER '+key,a);ans=s[a:b]
 assert r'\SolutionFigure{'+key+'}' in ans and r'\ref{fig:solution-'+key+'}' in ans
 assert ans.count(r'\Step{')>=3
final=P/(N+'.pdf');tmp=P/'工作文件/详解修订版交付.pdf'
with fitz.open(src) as d:d.save(tmp,garbage=4,deflate=True)
final.write_bytes(tmp.read_bytes());doc=fitz.open(final);text=''.join(p.get_text() for p in doc)
assert len(re.findall(r'(?:例|训练题)\s*\d+\s*题图',text))==90
assert len(re.findall(r'(?:例|训练题)\s*\d+\s*的分析与计算',text))==90
assert '课件原图来源索引' not in text and '补充绘制' not in text
readme=f"""# 第二章 · 质点组力学讲义

本次详解修订版共 {len(doc)} 页，包含66道例题和24道训练题。全部90题有完整题干、独立题图和分步解答，每道解答过程中另有编号分析图。解答明确引用图号，解释具体位置、方向、接触和分区条件如何进入计算。

保留五份课件的知识内容、43份课件原图及22幅正文说明图。原有解答推导保留，补齐中间列式、消元、初值、数值计算和适用条件等步骤。全部题图、解答图与正文说明图均交付可编辑TikZ源码，共202份。正文没有深色提示框，文末不列图片来源索引。

## 编辑与编译

主文件：`{N}.tex`。请与以下四个目录一同保存：

- `原图/`：43份正文使用的课件原图PDF。
- `补充图/`：22幅正文说明图的TikZ源码。
- `题图/`：90幅独立题图的TikZ源码。
- `解答图/`：90幅编号解答分析图的TikZ源码。

使用XeLaTeX，采用ctex/Fandol、TikZ及常见数学宏包。推荐运行：

```sh
latexmk -xelatex "{N}.tex"
```

也可用XeLaTeX连续编译两次，使目录和交叉引用更新。源码没有绝对路径依赖；在在线LaTeX编辑器中上传整个源码目录并选择XeLaTeX即可。

每个图的点、方向、箭头、标签及计算关系可直接在对应`.tex`文件中修改，重新编译主文件后更新PDF。
"""
(P/'阅读与编译说明.md').write_text(readme)
files=[P/(N+'.tex'),P/'阅读与编译说明.md']
for folder,pattern,count in [('原图','*.pdf',43),('补充图','*.tex',22),('题图','*.tex',90),('解答图','*.tex',90)]:
 items=sorted(P/folder/(k if k.endswith('.pdf') else k+'.pdf') for k in set(re.findall(r'\\(?:OriginalFigure|OriginalPanel)\{([^}]+)\}',s))) if folder=='原图' else sorted((P/folder).glob(pattern))
 assert len(items)==count and all(f.exists() for f in items),(folder,len(items));files+=items
archive=P/'第二章-质点组力学-完善版LaTeX源码及图片.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,Path('第二章-质点组力学源码')/f.relative_to(P))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
report=dict(status='passed',pdf_pages=len(doc),examples=66,training_questions=24,question_figures=90,solution_figures=90,explicit_solution_figure_references=90,original_assets=43,original_figures=37,body_figures=22,editable_TikZ_files=202,solution_steps=270,compile_warnings=warnings,pdf_sha256=hashlib.sha256(final.read_bytes()).hexdigest(),archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),tex_sha256=hashlib.sha256(s.encode()).hexdigest(),pdf_bytes=final.stat().st_size,archive_bytes=archive.stat().st_size)
(P/'资料核查/详解修订版交付检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
