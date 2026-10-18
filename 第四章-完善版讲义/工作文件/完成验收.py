from pathlib import Path
import hashlib,json,zipfile
P=Path(__file__).resolve().parents[1]
R=P/'资料核查'
change=json.loads((P/'工作文件/v2至v3页面变化.json').read_text())
v2={};v3={}
reports=[]
for kind,target in [('终稿逐页核查-v2',v2),('终稿变化页核查-v3',v3)]:
    for letter in 'abc':
        f=R/(kind+'-'+letter+'.json')
        d=json.loads(f.read_text());reports.append(f)
        expected='c57b205a4c462fb218270a3b776c1b453244fc114d0be93328af64fb9496bfa3' if target is v2 else change['v3_sha256']
        assert d.get('fixed_pdf_sha256',d.get('pdf_sha256',d.get('sha256')))==expected,(f,'wrong version')
        if target is v3:assert d['status']=='passed',f
        for row in d['pages']:
            n=row.get('physical_page',row.get('page'))
            assert n not in target,(f,n,'duplicate review')
            target[n]={'report':f.name,'result':row}
f=R/'终稿变化页核查-v3-目录.json';d=json.loads(f.read_text());reports.append(f)
for row in d['pages']:v3[row['page']]={'report':f.name,'result':row}
assert set(v2)==set(range(1,88)),sorted(v2)
coverage=[]
for row in change['page_matches']:
    n=row['v3_page']
    if n in v3:
        review=v3[n];method='直接视觉复查';source_page=n
    else:
        old=row['v2_identical_body_pages'];assert old,n
        source_page=old[0];review=v2[source_page];method='正文区域像素与已审阅页一致'
    assert review['result']['status']=='passed',(n,review)
    coverage.append({'page':n,'method':method,'review':review['report'],'review_page':source_page})
assert len(coverage)==85
portable=json.loads((R/'源码包独立编译检查.json').read_text())
assert portable['status']=='passed' and portable['pdf_pages']==85
archive=P/'第四章-转动参考系-完善版LaTeX源码及图片.zip'
pdf=P/'第四章-转动参考系讲义-完善版.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==portable['pdf_sha256']
acceptance={'status':'passed','pdf_pages':85,'final_pdf_sha256':portable['pdf_sha256'],
 'reviewed_uncompressed_pdf_sha256':change['v3_sha256'],'page_review_coverage':coverage,
 'pagination_issue_resolution':'v2 第 50、82 页的孤立尾段已通过页面构建同步修订消除，v3 对应第 50、81 页直接视觉复查通过。',
 'source_slides':75,'examples':47,'selftests_with_answers':24,'original_figures':47,'editable_model_figures':47,
 'portable_compilation':'独立临时目录解包编译，85 页文字与渲染像素全部一致，零警告；最后仅追加核查记录，编译输入哈希保持一致。'}
f=R/'最终验收.json';f.write_text(json.dumps(acceptance,ensure_ascii=False,indent=2));reports.append(f)
f=R/'终校页面复用与变化记录.json';f.write_text(json.dumps(change,ensure_ascii=False,indent=2));reports.append(f)
added=[]
with zipfile.ZipFile(archive,'a',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    names=set(z.namelist())
    for f in reports:
        name='第四章-转动参考系源码/资料核查/'+f.name
        if name in names:assert z.read(name)==f.read_bytes(),name
        else:z.write(f,name);added.append(name)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))
    final_inputs={n:hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if '/资料核查/' not in n}
    assert final_inputs==portable['compile_input_hashes']
sha=hashlib.sha256(archive.read_bytes()).hexdigest()
portable.update({'source_archive_sha256':sha,'post_compile_added_audit_files':added,'compilation_inputs_unchanged_after_report_append':True})
(R/'源码包独立编译检查.json').write_text(json.dumps(portable,ensure_ascii=False,indent=2))
delivery=json.loads((R/'交付文件检查.json').read_text());delivery['archive_sha256']=sha;delivery['final_visual_review']='passed';delivery['portable_compile']='passed'
(R/'交付文件检查.json').write_text(json.dumps(delivery,ensure_ascii=False,indent=2))
print(json.dumps({'status':'passed','pdf_pages':85,'reviewed_pages':len(coverage),'zip_bytes':archive.stat().st_size,'pdf_sha256':portable['pdf_sha256'],'zip_sha256':sha},ensure_ascii=False))
