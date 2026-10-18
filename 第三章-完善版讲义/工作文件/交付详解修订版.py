from pathlib import Path
import hashlib,json,re,zipfile,fitz,subprocess
P=Path(__file__).resolve().parents[1];N='第三章-刚体力学讲义-完善版'
src=P/'工作文件/详解编译'/(N+'.pdf')
log=(P/'工作文件/详解编译'/(N+'.log')).read_text();warnings=[l for l in log.splitlines() if re.search(r'Warning|Overfull|Underfull|Missing character|^!',l)];assert not warnings,warnings
q=subprocess.run(['/opt/homebrew/bin/qpdf','--check',str(src)],capture_output=True,text=True);assert q.returncode==0
s=(P/(N+'.tex')).read_text()
assert s.count(r'\example{')==66 and s.count(r'\exercise{')==30
assert s.count(r'\QuestionStatement{')+s.count(r'\LongQuestionStatement{')==96
assert s.count(r'\SolutionFigure{')==96 and len(re.findall(r'\\ref\{fig:solution-',s))==96
assert s.count(r'\OriginalFigure[')==117 and s.count(r'\TeachingFigure{')==59
assert all(x not in s for x in ['课件原图来源索引','补充绘制',r'\colorbox{',r'\boxed{'])
final=P/(N+'.pdf');tmp=P/'工作文件/详解修订版交付.pdf'
with fitz.open(src) as d:d.save(tmp,garbage=4,deflate=True)
final.write_bytes(tmp.read_bytes());doc=fitz.open(final);text=''.join(p.get_text() for p in doc)
assert len(re.findall(r'(?:例|训练题)\s*\d+\s*题图',text))==96
assert len(re.findall(r'(?:例|训练题)\s*\d+\s*的计算示意',text))==96
assert '课件原图来源索引' not in text and '补充绘制' not in text
readme=f"""# 第三章 · 刚体力学讲义

本次详解修订版共 {len(doc)} 页，含66道例题和30道训练题。全部96道题有完整题干、独立题图和分步解答；每道解答过程中另有编号分析图，并在解答文字中明确引用图号，说明具体几何、方向或接触条件怎样用于列式。

保留六份课件的完整知识内容、117份课件原图及59幅正文说明图。96幅题图和96幅解答分析图均为可编辑TikZ源码。解答共含建模、投影或受力分析、列式、消元、初条件、数值代入及适用条件等内容；没有深色提示框，文末不列图片来源索引。

## 编辑与编译

主文件：`{N}.tex`。请与下列四个目录一起保存：

- `原图/`：117份正文使用的课件原图PDF。
- `补充图/`：59幅可编辑的正文说明图。
- `题图/`：96幅独立题图。
- `解答图/`：96幅编号解答分析图。

采用XeLaTeX，使用ctex/Fandol、TikZ和常见数学宏包。可运行：

```sh
latexmk -xelatex "{N}.tex"
```

或以XeLaTeX连续编译两次，使目录与交叉引用更新。项目没有绝对路径依赖，上传在线LaTeX编辑器时请上传整个源码包并选择XeLaTeX。

图中的点、箭头、线条、标签和计算关系均可在对应`.tex`中编辑。修改图后重新编译主文件即可更新PDF。
"""
(P/'阅读与编译说明.md').write_text(readme)
files=[P/(N+'.tex'),P/'阅读与编译说明.md']
for folder,pattern,count in [('原图','*.pdf',117),('补充图','*.tex',59),('题图','*.tex',96),('解答图','*.tex',96)]:
 items=sorted(P/folder/(k if k.endswith('.pdf') else k+'.pdf') for k in set(re.findall(r'\\OriginalFigure\[[^\]]+\]\{([^}]+)\}',s))) if folder=='原图' else sorted((P/folder).glob(pattern))
 assert len(items)==count and all(f.exists() for f in items),(folder,len(items));files+=items
archive=P/'第三章-刚体力学-完善版LaTeX源码及图片.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,Path('第三章-刚体力学源码')/f.relative_to(P))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
report={'status':'passed','pdf_pages':len(doc),'examples':66,'training_questions':30,'question_figures':96,'solution_figures':96,'explicit_solution_figure_references':96,'original_figures':117,'body_figures':59,'compile_warnings':warnings,'pdf_sha256':hashlib.sha256(final.read_bytes()).hexdigest(),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256(s.encode()).hexdigest(),'pdf_bytes':final.stat().st_size,'archive_bytes':archive.stat().st_size}
(P/'资料核查/详解修订版交付检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
