from pathlib import Path
import fitz,re,json,hashlib
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1];N='第二章-质点组力学讲义-完善版'
src=P/'工作文件/详解编译'/(N+'.pdf');out=P/'工作文件/详解版待验收.pdf'
with fitz.open(src) as d:d.save(out,garbage=4,deflate=True)
d=fitz.open(out);O=P/'工作文件/详解终校';O.mkdir(exist_ok=True)
for old in O.glob('*.png'): old.unlink()
questions=[]
for i,page in enumerate(d):
 text=page.get_text()
 for m in re.finditer(r'(例|训练题)\s*(\d+)\s*题图',text):questions.append({'kind':'example' if m[1]=='例' else 'exercise','number':int(m[2]),'physical_page':i+1})
assert len(questions)==90,(len(questions),questions)
(P/'工作文件/逐题页码.json').write_text(json.dumps(questions,ensure_ascii=False,indent=2))
# Full-book contact sheets detect poor page breaks and retain the old theory within the visual review.
for j in range(0,len(d),12):
 im=Image.new('RGB',(1120,1500),'white');draw=ImageDraw.Draw(im)
 for k in range(12):
  i=j+k
  if i>=len(d):break
  p=d[i].get_pixmap(matrix=fitz.Matrix(.45,.45),alpha=False);a=Image.frombytes('RGB',[p.width,p.height],p.samples);a.thumbnail((270,350));x=(k%4)*280;y=(k//4)*500
  im.paste(a,(x,y+25));draw.text((x+8,y+5),str(i+1),fill='black')
 im.save(O/f'overview-{j//12+1:02}.png')
# First-page geometry plus subsequent solution pages around demanding examples.
example_samples=[1,2,7,11,18,21,22,25,29,31,32,35,37,38,39,40,41,43,44,45,46,48,49,50,52,53,56,57,58,59,60,61,62,64,65,66]
training_samples=[1,5,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24]
pages=set([1,2,3,len(d)])
for q in questions:
 if (q['kind']=='example' and q['number'] in example_samples) or (q['kind']=='exercise' and q['number'] in training_samples):
  pages.add(q['physical_page']);
  if q['physical_page']<len(d):pages.add(q['physical_page']+1)
for num in sorted(pages):d[num-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(O/f'page-{num:03}.png')
print(json.dumps({'pages':len(d),'questions':len(questions),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'full_pages_rendered':sorted(pages)},ensure_ascii=False))
