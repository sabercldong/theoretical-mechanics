from pathlib import Path
import re,json,csv,hashlib,shutil,zipfile,fitz,subprocess

P=Path(__file__).resolve().parents[1]
NAME='第四章-转动参考系讲义-完善版'

def brace(s,i):
    d=1;j=i+1
    while d:
        if s[j]=='{' and s[j-1]!='\\':d+=1
        if s[j]=='}' and s[j-1]!='\\':d-=1
        j+=1
    return s[i+1:j-1],j

def main():
    src=P/'工作文件/编译'/(NAME+'.pdf');pdf=P/(NAME+'.pdf')
    check=subprocess.run(['qpdf','--check',str(src)],capture_output=True,text=True)
    assert check.returncode==0,check.stdout+check.stderr
    compact=P/'工作文件/交付无损整理.pdf'
    with fitz.open(src) as source_doc:
        source_doc.save(compact,garbage=4,deflate=True)
    shutil.copy2(compact,pdf)
    d=fitz.open(pdf);s=(P/(NAME+'.tex')).read_text()
    aux=(P/'工作文件/编译'/(NAME+'.aux')).read_text();labels={}
    for m in re.finditer(r'\\newlabel\{([^}]+)\}\{',aux):
        val,_=brace(aux,m.end()-1);num,j=brace(val,0);page,j=brace(val,j)
        labels[m[1]]={'number':num,'page':page}
    body=next(x[2] for x in d.get_toc() if x[1]=='转动基矢与矢量求导')
    assert body>=2
    originals=json.loads((P/'工作文件/整合原图清单.json').read_text())
    provenance=[]
    for r in originals:
        v=labels['fig:orig-'+r['key']];f=P/'原图'/(r['key']+'.pdf')
        provenance.append({'key':r['key'],'图号':v['number'],'讲义印刷页码':v['page'],'PDF页码':int(v['page'])+body-1,
                           '文件':str(f.relative_to(P)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
                           '课件':r['deck'],'课件页码':r['page'],'主题':r['topic'],'图题':r['caption'],
                           '裁剪坐标':r.get('crop_rect_pt'),'来源与处理':r.get('notes',[]),
                           'source_pdf':r.get('source_pdf'),'source_media':r.get('source_media')})
    (P/'资料核查/插图溯源.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2))
    models=json.loads((P/'资料核查/模型图来源与核对.json').read_text())
    for r in models:
        v=labels['fig:lesson-'+r['key']]
        r.update({'图号':v['number'],'讲义印刷页码':v['page'],'PDF页码':int(v['page'])+body-1})
        assert hashlib.sha256((P/r['file']).read_bytes()).hexdigest()==r['sha256']
    (P/'资料核查/模型图来源与核对.json').write_text(json.dumps(models,ensure_ascii=False,indent=2))
    anchors=json.loads((P/'工作文件/正文定位标记.json').read_text())
    titles={r['title']:r['key'] for r in anchors if r['kind']=='example'}
    rows=[]
    for letter in 'ab':
        audit=json.loads((P/f'工作文件/内容核对-{letter}.json').read_text())
        included=[]
        preparation_reports=list(audit.get('source_preparation_reports',[]))
        if audit.get('compatibility_report'):
            preparation_reports.append(audit['compatibility_report'].removeprefix('工作文件/'))
        for report in preparation_reports:
            original=P/'工作文件'/report
            if original.is_file():
                copied=P/'资料核查'/f'原图处理核验-{letter}-{original.name}'
                shutil.copy2(original,copied)
                included.append(str(copied.relative_to(P)))
        audit['included_preparation_reports']=included
        (P/f'资料核查/课件内容与原图核对-{letter}.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
        for r in audit['pages']:
            loc=r['lecture_location'];keys=[]
            if isinstance(loc,list):loc='；'.join(loc)
            for m in re.finditer(r'4\.(\d+)(?:\.(\d+))?',loc):
                key=f'sub:c4-{m[1]}.{m[2]}' if m[2] else f'sec:c4-{m[1]}'
                if key not in keys:keys.append(key)
            title=r.get('example_title')
            if isinstance(title,str) and title in titles:keys.insert(0,titles[title])
            elif isinstance(title,list):
                keys=[titles[t] for t in title if t in titles]+keys
            if ('作业' in r['topic'] or '作业' in loc) and (r['deck'],r['page']) in [('c4-1',29),('c4-2',26)]:keys.append('appendix:coursework')
            if (r['deck'],r['page'])==('c4-1',30):keys.append('appendix:study')
            assert keys,(r['deck'],r['page'],loc)
            for k in keys:assert k in labels,(r,k)
            rows.append({'课件':r['deck'],'课件页码':r['page'],'内容':r['topic'],'讲义位置':loc,
                         '定位标记':'；'.join(keys),'讲义印刷页码':'；'.join(labels[k]['page'] for k in keys),
                         'PDF页码':'；'.join(str(int(labels[k]['page'])+body-1) for k in keys),
                         '说明':r.get('notes','')})
    rows.sort(key=lambda r:(r['课件'],r['课件页码']))
    assert len(rows)==75 and len({(r['课件'],r['课件页码']) for r in rows})==75
    for deck,count in [('c4-1',30),('c4-2',45)]:
        assert [r['课件页码'] for r in rows if r['课件']==deck]==list(range(1,count+1))
    (P/'资料核查/75页课件内容对应表.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    with (P/'资料核查/75页课件内容对应表.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    warnings=[x for x in (P/'工作文件/编译'/(NAME+'.log')).read_text().splitlines() if re.search(r'Warning|Overfull|Underfull|Missing character|^!',x)]
    assert not warnings,warnings
    assert '补充绘制' not in ''.join(page.get_text() for page in d)
    assert s.count(r'\example{')==47 and s.count(r'\exercise{')==24
    readme=f'''# 第四章 · 转动参考系讲义（完善版）

本册 PDF 共 {len(d)} 页，包含 47 道例题、24 道自测及详细解答、{len(originals)+47} 个编号插图。覆盖原项目中第四章的 2 份 PPT、75 页课件，其中包括 7 张隐藏页。

## 编辑与编译

主文件为 `{NAME}.tex`，请与 `原图/`、`补充图/` 保持在同一目录。
使用 TeX Live 或 MacTeX，以 XeLaTeX 连续编译两次，或运行：

```sh
latexmk -xelatex "{NAME}.tex"
```

本包采用 ctex/Fandol 字体、TikZ 和常见数学宏包。上传在线编辑器时应上传完整源码包并选择 XeLaTeX；主文件不依赖绝对路径或其他章节。

## 内容与图片

- 完整保留既有详细稿的正文、47 道例题、24 道自测及 47 幅可编辑模型图。
- 加入 {len(originals)} 份从原课件提取的图形或动画代表帧。重复图按教学内容合并；照片、图形保持来源内容，少数旧字体编码与公式对象的兼容恢复见核对记录。
- 裁片中混入的课件模板背景已从工作副本的母版中清理；原图对象、线条、箭头及媒体内容均保留，具体处理见插图溯源及课件核对记录。
- 原图与模型图统一采用普通图题和连续编号；必要的符号对应关系写在图题中。
- 正文覆盖矢量运输公式、速度与加速度变换、惯性力、相对平衡、旋转约束、地球自转、环流、落体偏转、傅科摆及旋转系能量。
- 原课件仅列教材作业题号的页已保留题号，未捏造教材题干。

## 核查资料

`资料核查/75页课件内容对应表.csv` 逐页定位课件到讲义，PDF 页码含封面，印刷页码依页脚计。插图溯源文件记录原课件、页码、裁剪和资产哈希；模型图记录对应可编辑文件。

已复核课件图文对应、全册排版与交叉引用，并对关键计算作符号和数值检查。关键计算的具体范围列于 `关键计算核验.json`，不把局部核验等同于全部例题的独立重推。
'''
    (P/'阅读与编译说明.md').write_text(readme)
    files=[P/(NAME+'.tex'),P/'阅读与编译说明.md']+[P/r['文件'] for r in provenance]+[P/r['file'] for r in models]
    files += [P/'资料核查'/n for n in ['插图溯源.json','模型图来源与核对.json','75页课件内容对应表.csv','75页课件内容对应表.json','原课件校验.json','正文与配图保留检查.json','关键计算核验.json']]
    files += [P/f'资料核查/课件内容与原图核对-{x}.json' for x in 'ab']
    files += [f for f in (P/'资料核查').glob('终稿逐页核查-v2-*.json')]
    files += [f for f in (P/'资料核查').glob('终稿变化页核查-v3-*.json')]
    files += [f for f in (P/'资料核查').glob('原图处理核验-*.json')]
    files += [P/'资料核查/模型图独立核查.json']
    z=P/'第四章-转动参考系-完善版LaTeX源码及图片.zip'
    with zipfile.ZipFile(z,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as f:
        for x in files:f.write(x,Path('第四章-转动参考系源码')/x.relative_to(P))
    with zipfile.ZipFile(z) as f:assert f.testzip() is None
    report={'pdf_pages':len(d),'body_start_pdf_page':body,'examples':47,'exercises':24,
            'original_assets':len(originals),'model_figures':47,'numbered_figures':len(originals)+47,
            'source_slides':75,'source_decks':2,'warnings':warnings,
            'pdf_resource_deduplication':'合并完全相同的对象与数据流；不下采样、不有损编码；独立源码编译另逐页验证文字与像素。',
            'compiled_pdf_bytes':src.stat().st_size,'delivery_pdf_bytes':pdf.stat().st_size,
            'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
            'tex_sha256':hashlib.sha256((P/(NAME+'.tex')).read_bytes()).hexdigest(),
            'archive_sha256':hashlib.sha256(z.read_bytes()).hexdigest()}
    (P/'资料核查/交付文件检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
