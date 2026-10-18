import fitz
from pathlib import Path
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1];D=P/'工作文件/整册校样';D.mkdir(exist_ok=True)
for old in D.glob('*.png'):old.unlink()
doc=fitz.open(P/'第五章-分析力学讲义-完善版.pdf')
for i,p in enumerate(doc):
 pix=p.get_pixmap(matrix=fitz.Matrix(1.1,1.1),alpha=False);pix.save(D/f'p{i+1:03}.png')
for start in range(0,len(doc),6):
 canvas=Image.new('RGB',(1830,1744),'#c5cbd0');draw=ImageDraw.Draw(canvas)
 for j in range(min(6,len(doc)-start)):
  im=Image.open(D/f'p{start+j+1:03}.png');im.thumbnail((590,835));x=(j%3)*610+10;y=(j//3)*872+27
  canvas.paste(im,(x+(590-im.width)//2,y));draw.text((x+5,y-19),f'PDF {start+j+1}',fill='black')
 canvas.save(D/f'sheet{start//6+1:02}.png')
print('Rendered',len(doc),'pages and',(len(doc)+5)//6,'contact sheets')
