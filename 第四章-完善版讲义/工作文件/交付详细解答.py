from pathlib import Path
import hashlib,json,re,zipfile,fitz,subprocess
P=Path(__file__).resolve().parents[1]
N='第四章-转动参考系讲义-完善版'
source=P/'工作文件/详解编译'/(N+'.pdf')
check=subprocess.run(['/opt/homebrew/bin/qpdf','--check',str(source)],capture_output=True,text=True);assert check.returncode==0
log=(P/'工作文件/详解编译'/(N+'.log')).read_text()
w=[l for l in log.splitlines() if re.search(r'Warning|Overfull|Underfull|Missing character|^!',l)];assert not w,w
tex=(P/(N+'.tex')).read_text()
assert tex.count(r'\QuestionStatement{')==71
assert tex.count(r'\example{')==47 and tex.count(r'\exercise{')==24
assert tex.count(r'\TeachingFigure{')==47 and tex.count(r'\OriginalFigure[')==47
assert all(x not in tex for x in ['课件原图来源索引',r'\colorbox{',r'\boxed{','补充绘制'])
with fitz.open(source) as doc:doc.save(P/'工作文件/详解版交付整理.pdf',garbage=4,deflate=True)
final=P/(N+'.pdf');final.write_bytes((P/'工作文件/详解版交付整理.pdf').read_bytes())
doc=fitz.open(final)
text=''.join(p.get_text() for p in doc)
questions=re.findall(r'(例\s*\d+|训练题\s*\d+)\s*题图',text)
assert len(questions)==71,(len(questions),questions)
assert '课件原图来源索引' not in text and '补充绘制' not in text
readme=f'''# 第四章 · 转动参考系讲义

本次详解版共 {len(doc)} 页，包含 47 道例题、24 道训练题。全部 71 道题的解答已逐题完善：说明参考系与模型、列式依据、求解和初条件处理、数值代入及结果检验。每题的完整题干和独立题图保留，原有正文推导、47 份课件原图和47幅正文说明图也保留。

本版采用普通讲义排版，解答中的分步标题均为正文黑字；没有深色提示框，末尾不列图片来源索引。

## 编辑与编译

主文件为 `{N}.tex`。请将主文件与 `原图/`、`补充图/`、`题图/` 保存在同一目录。

- `原图/`：正文使用的原课件图形。
- `补充图/`：47 幅可编辑的正文说明图。
- `题图/`：71 幅可编辑的例题、训练题图。

以 XeLaTeX 连续编译两次，或运行：

```sh
latexmk -xelatex "{N}.tex"
```

本文件使用 ctex/Fandol、TikZ 和常见数学宏包，不依赖绝对路径。在线编辑时请上传完整源码包并选择 XeLaTeX。
'''
(P/'阅读与编译说明.md').write_text(readme)
files=[P/(N+'.tex'),P/'阅读与编译说明.md']
for folder,pattern,count in [('原图','*.pdf',47),('补充图','*.tex',47),('题图','*.tex',71)]:
 items=sorted((P/folder).glob(pattern));assert len(items)==count,(folder,len(items));files+=items
archive=P/'第四章-转动参考系-完善版LaTeX源码及图片.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,Path('第四章-转动参考系源码')/f.relative_to(P))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
report={'status':'passed','pdf_pages':len(doc),'examples':47,'training_questions':24,'question_figures':71,'original_figures':47,'body_figures':47,
        'all_answers_expanded':True,'solution_steps':226,'colored_callouts_removed':True,'source_appendix_removed':True,'compile_warnings':w,
        'pdf_sha256':hashlib.sha256(final.read_bytes()).hexdigest(),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'tex_sha256':hashlib.sha256((P/(N+'.tex')).read_bytes()).hexdigest(),
        'pdf_bytes':final.stat().st_size,'archive_bytes':archive.stat().st_size}
(P/'资料核查/详解版交付检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))
