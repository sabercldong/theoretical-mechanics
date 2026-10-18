from pathlib import Path
import re,json,sys
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
for ch,topic,first in [('第一章','质点力学','运动描述与直角坐标'),('第二章','质点组力学','质点组的运动学与质心')]:
    if len(sys.argv)>1 and ch not in sys.argv[1:]:continue
    p=ROOT/(ch+'-完善版讲义');name=f'{ch}-{topic}讲义-完善版'
    d=fitz.open(p/'工作文件/编译'/(name+'.pdf'));aux=(p/'工作文件/编译'/(name+'.aux')).read_text()
    body=next(row[2] for row in d.get_toc() if row[1]==first)
    labels={m[1]:int(m[3])+body-1 for m in re.finditer(r'\\newlabel\{(fig:lesson-[^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
    out=p/'工作文件/成稿预览';out.mkdir(exist_ok=True)
    for i,page in enumerate(d):page.get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).save(out/f'p{i+1:03}.png')
    for start in range(0,len(d),8):
        im=Image.new('RGB',(1560,1135),'#dddddd');draw=ImageDraw.Draw(im)
        for j in range(8):
            if start+j>=len(d):break
            thumb=Image.open(out/f'p{start+j+1:03}.png');thumb.thumbnail((380,538))
            x=(j%4)*390+5;y=(j//4)*565+22;im.paste(thumb,(x,y));draw.text((x,y-18),str(start+j+1),fill='black')
        im.save(out/f'sheet-{start+1:03}-{min(start+8,len(d)):03}.jpg',quality=88)
    (p/'工作文件/新增图页码.json').write_text(json.dumps({'pages':len(d),'body_start':body,'figures':labels},ensure_ascii=False,indent=2))
    print(ch,len(d),labels,flush=True)
