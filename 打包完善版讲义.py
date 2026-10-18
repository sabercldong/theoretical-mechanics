from pathlib import Path
import json,re,csv,hashlib,shutil,zipfile,sys
import fitz

ROOT=Path(__file__).resolve().parent

def brace(s,i):
    n=1;j=i+1
    while n:
        if s[j]=='{' and s[j-1]!='\\':n+=1
        if s[j]=='}' and s[j-1]!='\\':n-=1
        j+=1
    return s[i+1:j-1],j

def package(ch,topic,slides,examples,exercises,first_section):
    P=ROOT/(ch+'-完善版讲义');prior=ROOT/(ch+'-原图版讲义');name=f'{ch}-{topic}讲义-完善版'
    pdf=P/(name+'.pdf');shutil.copy2(P/'工作文件/编译'/(name+'.pdf'),pdf)
    d=fitz.open(pdf);tex=(P/(name+'.tex')).read_text();aux=(P/'工作文件/编译'/(name+'.aux')).read_text()
    labels={}
    for m in re.finditer(r'\\newlabel\{([^}]+)\}\{',aux):
        v,_=brace(aux,m.end()-1);num,j=brace(v,0);page,j=brace(v,j)
        labels[m[1]]={'number':num,'page':page}
    start=next(x[2] for x in d.get_toc() if x[1]==first_section)
    assert len(re.findall(r'\\example\{',tex))==examples
    if ch=='第二章':assert len(re.findall(r'\\exercise\{',tex))==exercises
    else:
        practice=tex.split(r'\section*{自测与练习}',1)[1].split(r'\end{enumerate}',1)[0]
        assert len(re.findall(r'\\item\b',practice))==exercises
    old_rows=json.loads((prior/f'资料核查/{slides}页课件内容对应表.json').read_text())
    for row in old_rows:
        keys=row['定位标记'].split('；');assert all(k in labels for k in keys)
        row['讲义印刷页码']='；'.join(labels[k]['page'] for k in keys)
        row['PDF页码']='；'.join(str(int(labels[k]['page'])+start-1) for k in keys)
    assert len(old_rows)==slides
    (P/f'资料核查/{slides}页课件内容对应表.json').write_text(json.dumps(old_rows,ensure_ascii=False,indent=2))
    with (P/f'资料核查/{slides}页课件内容对应表.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(old_rows[0]));w.writeheader();w.writerows(old_rows)
    originals=json.loads((prior/'资料核查/插图溯源.json').read_text())
    for r in originals:
        pos=labels['fig:orig-'+r['key']];r['图号']=pos['number'];r['讲义印刷页码']=pos['page'];r['PDF页码']=int(pos['page'])+start-1
        assert hashlib.sha256((P/r['文件']).read_bytes()).hexdigest()==r['sha256'],r['key']
    (P/'资料核查/插图溯源.json').write_text(json.dumps(originals,ensure_ascii=False,indent=2))
    figures=json.loads((P/'工作文件/图示修订清单.json').read_text());drawings=[]
    for r in figures:
        pos=labels['fig:lesson-'+r['key']];f=P/'补充图'/(r['key']+'.tex')
        drawings.append({'key':r['key'],'图号':pos['number'],'讲义印刷页码':pos['page'],'PDF页码':int(pos['page'])+start-1,'图题':r['caption'],'来源':r['source'],'文件':str(f.relative_to(P)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'核对':r.get('checks',r.get('revision_notes','图示已核对相关正文、方向和初始条件。'))})
    (P/'资料核查/模型图来源与核对.json').write_text(json.dumps(drawings,ensure_ascii=False,indent=2))
    totalfig=len(set(x['图号'] for x in originals))+len(drawings)
    assert '补充绘制' not in tex
    for f in (P/'补充图').glob('*.tex'):assert '补充绘制' not in f.read_text()
    readme=f'''# {ch} · {topic}讲义（完善版）

本版以项目课件为素材，保留此前完整正文、例题和课件原图，完善模型示意、定量曲线和读图说明。PDF 共 {len(d)} 页，{examples} 道例题、{exercises} 道自测题及解答，{totalfig} 个编号插图。

## 编辑与编译

主文件为 `{name}.tex`。请保持主文件、`原图/` 与 `补充图/` 在同一目录。原图目录存放课件图像；补充图目录内为可以直接修改的 TikZ 源代码。正文采用统一的图题和连续编号。

使用中文 TeX Live 或 MacTeX，以 **XeLaTeX** 连续编译两次：

```sh
xelatex -interaction=nonstopmode -halt-on-error "{name}.tex"
xelatex -interaction=nonstopmode -halt-on-error "{name}.tex"
```

也可运行 `latexmk -xelatex "{name}.tex"`。本包使用 ctex/Fandol 字体、常见数学与图表宏包、TikZ，不依赖项目中的其他章节或外部绝对路径。在线编辑器需上传完整源码包并选择 XeLaTeX。

## 内容与来源

- 保留 {len(originals)} 份课件原图素材，另有 {len(drawings)} 幅以正文模型和公式为依据的可编辑图形。
- `资料核查/{slides}页课件内容对应表.csv` 按原课件每页定位到修订后的讲义页码；PDF 页码含封面，印刷页码按页脚计。
- `资料核查/插图溯源.json` 与 `模型图来源与核对.json` 分别记录原图来源、模型图表达式和核对信息。
- 定量曲线在图题或图中给定参数；没有提供数值比例的受力、约束示意图不用于直接测量。

## 本次完善

{('恢复7幅必要图示，并增加对称双势阱定量图；完善阻尼曲线、电磁漂移坐标、势阱折射角和指数屏蔽势外侧势垒的局部放大。' if ch=='第一章' else '恢复18幅必要图示，并完善厚半球壳、半圆锥截面、静摩擦许可区间和自由弹簧有效势；修正重粒子散射双分支、周期位力示意及火箭排气方向的题干表述。')}

检查覆盖图文符号、参数、关键曲线与边界条件、整册排版、交叉引用和源码包编译。没有把这些检查等同于全部例题的独立重推。
'''
    (P/'阅读与编译说明.md').write_text(readme)
    extra=[P/'资料核查/插图溯源.json',P/'资料核查/模型图来源与核对.json',P/f'资料核查/{slides}页课件内容对应表.csv',P/f'资料核查/{slides}页课件内容对应表.json']
    if (P/'资料核查/动画代表帧记录.json').exists():extra.append(P/'资料核查/动画代表帧记录.json')
    if (P/'资料核查/原课件校验.json').exists():extra.append(P/'资料核查/原课件校验.json')
    extra.append(P/'资料核查/新增定量图计算核验.json')
    files=[P/(name+'.tex'),P/'阅读与编译说明.md']+[P/r['文件'] for r in originals]+[P/r['文件'] for r in drawings]+extra
    archive=P/f'{ch}-{topic}-完善版LaTeX源码及图片.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for f in files:z.write(f,Path(ch+'-'+topic+'源码')/f.relative_to(P))
    with zipfile.ZipFile(archive) as z:assert z.testzip() is None
    report={'pdf_pages':len(d),'examples':examples,'exercises':exercises,'original_assets':len(originals),'model_figures':len(drawings),'numbered_figures':totalfig,'source_slides':slides,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256((P/(name+'.tex')).read_bytes()).hexdigest(),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
    (P/'资料核查/交付文件检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(ch,json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
    if len(sys.argv)==1 or '第一章' in sys.argv[1:]:package('第一章','质点力学',276,79,25,'运动描述与直角坐标')
    if len(sys.argv)==1 or '第二章' in sys.argv[1:]:package('第二章','质点组力学',137,66,24,'质点组的运动学与质心')
