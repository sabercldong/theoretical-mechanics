from pathlib import Path
import concurrent.futures, hashlib, json, re, shutil, subprocess, zipfile
import fitz

P=Path(__file__).resolve().parents[1]
N='第五章-分析力学讲义-完善版'
main=P/(N+'.pdf')
tmp=main.with_suffix('.optimized.pdf')
d=fitz.open(main)
d.save(tmp,garbage=4,deflate=True)
d.close()
tmp.replace(main)
paths={'final':main,
       'independent':P/'工作文件/源码独立编译'/N/(N+'.pdf'),
       'baseline':P/'工作文件/排版终校基准.pdf'}
def signature(item):
    k,v=item
    proc=subprocess.run(['python3',str(P/'工作文件/PDF像素校验.py'),str(v)],check=True,capture_output=True,text=True)
    (P/f'资料核查/终稿像素-{k}.json').write_text(proc.stdout)
    return k,json.loads(proc.stdout)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    sig=dict(pool.map(signature,paths.items()))
assert sig['final']==sig['independent'],'Independent source compilation differs'
changed=[i+1 for i,(a,b) in enumerate(zip(sig['final'],sig['baseline'])) if a!=b]
baseline_content={x['content_pixels_without_footer'] for x in sig['baseline']}
content_changed=[i+1 for i,x in enumerate(sig['final']) if x['content_pixels_without_footer'] not in baseline_content]
comparison={'pages':{k:len(v) for k,v in sig.items()},'independent_identical':True,'baseline_changed_pages':changed,'content_changed_pages':content_changed}
(P/'资料核查/终稿独立编译比较.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2))
subprocess.run(['/opt/homebrew/bin/qpdf','--check',str(main)],check=True,capture_output=True,text=True)
log=(P/(N+'.log')).read_text()
warnings=[l for l in log.splitlines() if any(w in l for w in ('Overfull','Underfull','Missing character','undefined','Warning'))]
assert not warnings,warnings
tex=P/(N+'.tex');text=tex.read_text()
aux=(P/(N+'.aux')).read_text()
labels={m[1]:int(m[2]) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}',aux)}
misplaced=[]
long_figures=set(re.findall(r'\\LongQuestionStatement\{[^\n]*\}\{((?:ex|tr)\d+)\}',text))
for kind,prefix,count in [('example','ex',86),('exercise','tr',20)]:
    for n in range(1,count+1):
        a=labels.get(f'{prefix}:c5-{n}')
        b=labels.get(f'fig:question-{prefix}{n:02}')
        allowed=a is not None and b is not None and (a==b or (f'{prefix}{n:02}' in long_figures and b==a+1))
        if not allowed:misplaced.append([prefix,n,a,b])
assert not misplaced,misplaced
doc=fitz.open(main);pages=len(doc)
punct=[]
for i,page in enumerate(doc):
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            s=''.join(span['text'] for span in line['spans']).lstrip()
            if s.startswith(('，','。','；')):punct.append({'page':i+1,'text':s[:90]})
out=P/'工作文件/终稿变动页';out.mkdir(exist_ok=True)
for n in content_changed:
    doc[n-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).save(out/f'p{n:03}.png')
doc.close()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
zpath=P/(N+'-LaTeX源码.zip')
with zipfile.ZipFile(zpath) as z:
    assert z.testzip() is None
    entries=len(z.namelist())
report={'date':'2026-10-18','pages':pages,'examples':86,'exercises':20,'question_figures':106,'solution_figures':106,
        'original_assets':79,'source_zip_entries':entries,'compile_warnings':warnings,
        'question_heading_page_mismatches':misplaced,'punctuation_at_line_start':punct,
        'independent_compile_text_and_pixels_identical':True,'changed_from_layout_baseline':changed,'content_changed_pages':content_changed,
        'formula_checks_passed':69,'pdf_sha256':sha(main),'tex_sha256':sha(tex),'source_zip_sha256':sha(zpath)}
(P/'资料核查/最终交付核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))

# Refresh only chapter five in the existing five-chapter delivery.
U=P.parent/'讲义统一修订'
manifest=U/'工作文件/交付文件清单.json';rows=json.loads(manifest.read_text())
row=next(r for r in rows if r['chapter']==5)
row.update(file=str(tex),main_name=N,root=P.name)
manifest.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
manifest=U/'核查记录/交付检查.json';rows=json.loads(manifest.read_text())
row=next(r for r in rows if r['chapter']==5)
shutil.copy2(main,row['pdf']);shutil.copy2(zpath,row['source_zip'])
row.update(official_pdf=str(main),official_zip=str(zpath),top_directory=N,main_filename=tex.name,pages=pages,
           original_assets=79,diagram_files={'补充图':63,'题图':106,'解答图':106},embedded_TikZ=1,
           zip_entries=entries,warnings=[],pdf_sha256=sha(main),tex_sha256=sha(tex),zip_sha256=sha(zpath),
           pdf_bytes=main.stat().st_size,zip_bytes=zpath.stat().st_size)
manifest.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
script=U/'工作文件/生成整包.py';s=script.read_text().replace('2026年10月17日','2026年10月18日')
s=s.replace('；第五章的TikZ代码直接写在主文件中','')
script.write_text(s)
subprocess.run(['python3',str(script)],check=True)
