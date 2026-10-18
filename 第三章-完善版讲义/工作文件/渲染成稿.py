from pathlib import Path
import re,json,hashlib,sys
import fitz
from PIL import Image,ImageDraw

P=Path(__file__).resolve().parents[1]
name='第三章-刚体力学讲义-完善版'
pdf=P/'工作文件/编译'/(name+'.pdf')
d=fitz.open(pdf);aux=(P/'工作文件/编译'/(name+'.aux')).read_text()
body=next(x[2] for x in d.get_toc() if x[1]=='刚体模型与运动分解')
labels={m[1]:{'number':m[2],'page':int(m[3])+body-1} for m in re.finditer(r'\\newlabel\{(fig:(?:lesson|orig)-[^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
out=P/'工作文件/成稿预览';out.mkdir(exist_ok=True)
selected=set(map(int,sys.argv[1:])) if len(sys.argv)>1 else set(range(1,len(d)+1))
for i in sorted(selected):
    d[i-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).save(out/f'p{i:03}.png')
for start in range(0,len(d),8):
    if not any(i in selected for i in range(start+1,min(start+8,len(d))+1)):continue
    im=Image.new('RGB',(1560,1135),'#dddddd');draw=ImageDraw.Draw(im)
    for j in range(8):
        if start+j>=len(d):break
        thumb=Image.open(out/f'p{start+j+1:03}.png');thumb.thumbnail((380,538))
        x=(j%4)*390+5;y=(j//4)*565+22;im.paste(thumb,(x,y));draw.text((x,y-18),str(start+j+1),fill='black')
    im.save(out/f'sheet-{start+1:03}-{min(start+8,len(d)):03}.jpg',quality=88)
(P/'工作文件/图示页码.json').write_text(json.dumps({'pages':len(d),'body_start':body,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'figures':labels},ensure_ascii=False,indent=2))
print(f'{len(d)} pages; {len(labels)} numbered figures; {len(selected)} pages rendered.',flush=True)
