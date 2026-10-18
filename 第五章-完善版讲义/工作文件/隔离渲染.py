import sys,json,hashlib,fitz
from pathlib import Path
from PIL import Image
cfg=json.loads(sys.argv[1]);doc=fitz.open(cfg['pdf']);pg=doc[cfg.get('page',1)-1]
clip=fitz.Rect(cfg['rect']) if cfg.get('rect') else None
scale=cfg.get('scale',1)
pix=pg.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
if clip:
 # Some source drawings have inaccurate PDF bounds. Render the whole slide
 # before taking the pixel rectangle so faint original marks are preserved.
 im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
 im=im.crop(tuple(round(v*scale) for v in clip))
 if cfg.get('png'):im.save(cfg['png'])
 print(hashlib.sha256(im.tobytes()).hexdigest())
else:
 if cfg.get('png'):pix.save(cfg['png'])
 print(hashlib.sha256(pix.samples).hexdigest())
