from pathlib import Path
import json,hashlib,fitz

P=Path(__file__).resolve().parents[1]
rows=[]
for x in 'abc':rows+=json.loads((P/f'工作文件/原图清单-{x}.json').read_text())
bykey={r['key']:r for r in rows};overrides={}
captions={
'c3-2-p007-couple':r'等大反向的非共线二力构成力偶；图中为顺时针力偶，例~\ref{ex:c3-16} 取两力反向后的逆时针情形',
'c3-4-p009-tipping-cube':r'立方体绕地面棱转动的截面；图中 $\alpha$ 对应正文倾角 $\theta$，释放时为 $\theta_0$',
'c3-5-p033-wheel-left-acceleration':r'轮缘左侧点的相对切向与法向加速度；图中浅色 $\omega$ 为角速度，$\varepsilon$ 对应正文角加速度 $\alpha$',
'c3-5-p028-two-wheel-forces':r'双轮和悬挂物的受力；$T,T^{\prime}$ 大小相等，悬挂段张力为 $S$。原图 $\varepsilon_1,\varepsilon_2$ 分别以各轮提升重物时的转向为正，正文两轮统一取逆时针为正',
'c3-6-p021-nutation-tracks':r'单位球面上的重陀螺轴迹：单向、回环与尖点；原图上、下边界分别为 $\theta_2=\theta_{\min}$、$\theta_1=\theta_{\max}$'
}
for key,caption in captions.items():overrides.setdefault(key,{})['caption']=caption
clean=P/'工作文件/模板背景剥离'
source_map={
str(P/'工作文件/源课件PDF/理论力学-c3-3.pdf'):clean/'c3-3-source-figures.pdf',
str(P/'工作文件/源课件PDF/理论力学-c3-4.pdf'):clean/'c3-4-source-figures.pdf',
str(P/'工作文件/原图核查-b/c3-3-original-labels.pdf'):clean/'c3-3-labels-figures.pdf',
str(P/'工作文件/原图核查-b/c3-4-original-labels.pdf'):clean/'c3-4-labels-figures.pdf'
}
changed=[]
def extract(row,source,rect):
    doc=fitz.open(source);clip=fitz.Rect(rect);out=fitz.open();page=out.new_page(width=clip.width,height=clip.height)
    page.show_pdf_page(page.rect,doc,row['page']-1,clip=clip)
    pdf=P/'原图'/(row['key']+'.pdf');png=P/'原图'/(row['key']+'.png')
    out.save(pdf,garbage=4,deflate=True);page.get_pixmap(matrix=fitz.Matrix(3,3),alpha=False).save(png)
    return hashlib.sha256(pdf.read_bytes()).hexdigest()
for r in json.loads((P/'工作文件/原图清单-b.json').read_text()):
    if not r.get('crop_rect_pt'):continue  # Direct embedded media have no slide background.
    rect=list(r['crop_rect_pt'])
    if r['key']=='c3-4-p018-tilted-disk':rect[1]=164
    src=source_map[r['source_pdf']];sha=extract(r,src,rect)
    note=r.get('notes','')+' 终校从仅将母版背景设为白色的工作副本提取，幻灯片对象XML及媒体字节不变；去掉与图形无关的模板色条。'
    overrides.setdefault(r['key'],{}).update(source_pdf=str(src),notes=note,sha256=sha)
    if r['key']=='c3-4-p018-tilted-disk':
        overrides[r['key']].update(crop_rect_pt=rect,notes=note+' 上裁界由163收至164pt，移除上方题干底边，保留完整坐标标签。')
    changed.append(r['key'])
key='c3-6-p018-heavy-top';r=bykey[key];rect=list(r['crop_rect_pt']);rect[1]=234.25
sha=extract(r,Path(r['source_pdf']),rect)
overrides.setdefault(key,{}).update(crop_rect_pt=rect,sha256=sha,notes=r.get('notes','')+' 终校将上裁界由233调至234.25pt，去除相邻公式底边，保留竖直轴端点。')
changed.append(key)
(P/'工作文件/原图终校修订.json').write_text(json.dumps(overrides,ensure_ascii=False,indent=2))
(P/'资料核查/终校修订记录.json').write_text(json.dumps({'changed_assets':changed,'caption_changes':captions,'pre_change_pdf_sha256':'e6ef58f086c98636188419333db3753e37dc7e3ca74b725d1537c7657971b4a2','source_background_validation':json.loads((clean/'母版背景处理核验.json').read_text())},ensure_ascii=False,indent=2))
print(f'Re-extracted {len(changed)} assets; clarified {len(captions)} captions.')
