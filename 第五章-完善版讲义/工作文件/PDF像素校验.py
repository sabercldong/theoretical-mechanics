import sys,fitz,json,hashlib
from PIL import Image
d=fitz.open(sys.argv[1]);out=[]
for p in d:
 pix=p.get_pixmap(matrix=fitz.Matrix(.8,.8),alpha=False)
 im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 content=im.crop((0,0,pix.width,pix.height-40))
 out.append({'text':hashlib.sha256(p.get_text().encode()).hexdigest(),'pixels':hashlib.sha256(pix.samples).hexdigest(),'content_pixels_without_footer':hashlib.sha256(content.tobytes()).hexdigest(),'size':[pix.width,pix.height]})
print(json.dumps(out))
