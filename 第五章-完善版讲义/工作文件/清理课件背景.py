from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import re,json,subprocess,hashlib
P=Path(__file__).resolve().parents[1];W=P/'工作文件/白底课件';W.mkdir(exist_ok=True)
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
tag=lambda s:'{'+ns[s.split(':')[0]]+'}'+s.split(':')[1]
checks=[]
for src in sorted(P.parent.glob('理论力学-c5-*.pptx')):
 out=W/src.name
 with ZipFile(src) as zi,ZipFile(out,'w',ZIP_DEFLATED) as zo:
  unchanged=0
  for item in zi.infolist():
   b=zi.read(item.filename)
   if re.fullmatch(r'ppt/slides/slide\d+\.xml',item.filename):
    x=E.fromstring(b);tree=E.tostring(x.find('p:cSld/p:spTree',ns));x.set('showMasterSp','0');c=x.find('p:cSld',ns);bg=c.find('p:bg',ns)
    if bg is not None:c.remove(bg)
    bg=E.Element(tag('p:bg'));pr=E.SubElement(bg,tag('p:bgPr'));sf=E.SubElement(pr,tag('a:solidFill'));E.SubElement(sf,tag('a:srgbClr'),val='FFFFFF');E.SubElement(pr,tag('a:effectLst'));c.insert(0,bg)
    assert E.tostring(x.find('p:cSld/p:spTree',ns))==tree;unchanged+=1
    b=E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
   zo.writestr(item,b)
 checks.append({'source':src.name,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'unchanged_slide_object_trees':unchanged})
(W/'背景处理核验.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
cmd=['/Applications/LibreOffice.app/Contents/MacOS/soffice','-env:UserInstallation=file:///tmp/codex-c5-white-export','--headless','--convert-to','pdf','--outdir',str(W)]+[str(p) for p in W.glob('*.pptx')]
subprocess.run(cmd,check=True)
