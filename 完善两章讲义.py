from pathlib import Path
import re,json,shutil

ROOT=Path(__file__).resolve().parent
CONFIG=[('第一章','质点力学',79),('第二章','质点组力学',66)]

MACROS=r'''
\usetikzlibrary{arrows.meta,calc,positioning,angles,quotes,patterns,decorations.pathmorphing}
\tikzset{every picture/.style={>=Stealth},every node/.style={font=\small},force/.style={->,thick,ink},guide/.style={dashed,muted}}
\newsavebox{\LessonFigureBox}
\newcommand{\TeachingFigure}[2]{%
\par\begin{center}\begin{minipage}{\linewidth}\centering
\sbox{\LessonFigureBox}{\input{补充图/#1.tex}}%
\ifdim\wd\LessonFigureBox>.98\linewidth
\resizebox{.98\linewidth}{!}{\usebox{\LessonFigureBox}}%
\else\usebox{\LessonFigureBox}\fi
\captionsetup{hypcap=false}\captionof{figure}{#2}\label{fig:lesson-#1}
\end{minipage}\end{center}\par}
'''

def build(chapter,topic,count):
    P=ROOT/(chapter+'-完善版讲义')
    baseline=(P/'工作文件/修订前主稿.tex').read_text();s=baseline
    items=json.loads((P/'工作文件/图示修订清单.json').read_text())
    # Every insertion is anchored to a unique unchanged passage of the reviewed text.
    for r in items:
        a=r['anchor'];assert s.count(a)==1,(r['key'],s.count(a))
        diagram=r'\TeachingFigure{'+r['key']+'}{'+r['caption']+'}'
        if r.get('discussion'):diagram+='\n\n'+r['discussion']
        s=s.replace(a,a+'\n\n'+diagram,1)
    fixes=P/'工作文件/正文完善修订.json'
    if fixes.exists():
        for f in json.loads(fixes.read_text()):
            assert s.count(f['old'])==1,(f['old'][:80],s.count(f['old']))
            s=s.replace(f['old'],f['new'],1)
    s=s.replace('xcolor,graphicx,booktabs','xcolor,graphicx,tikz,booktabs')
    s=s.replace(r'\begin{document}',MACROS+'\n'+r'\begin{document}',1)
    s=s.replace('原图版课程讲义','课程讲义').replace('（原图版）','（修订完善版）')
    s=s.replace('正文包含推导、完整例题和自测解答，配图取自原课件。','正文包含推导、完整例题和自测解答，配图说明模型、推导和结果之间的联系。')
    s=s.replace('插图沿用原课件标注；图题说明其与正文的符号对应。','课件原图沿用原有标注；图题说明其与正文的符号对应。定量图注明所取参数和适用范围。')
    s=s.replace('插图保留原有标注；当图中文字采用','课件原图保留原有标注；当图中文字采用')
    s=s.replace('插图来源索引','课件原图来源索引')
    if chapter=='第一章':
        s=s.replace(r'\newcommand{\OriginalFigure}[2]',r'\newcommand{\OriginalHeight}{6.5cm}'+'\n'+r'\newcommand{\OriginalFigure}[2]',1)
        s=s.replace('width=0.92\\linewidth,height=6.5cm','width=0.92\\linewidth,height=\\OriginalHeight',1)
        mercury=r'\OriginalFigure{mercury_precession}{水星近日点方向逐次变化的放大示意。}'
        assert s.count(mercury)==1
        s=s.replace(mercury,r'\begingroup\renewcommand{\OriginalHeight}{6.1cm}'+mercury+r'\endgroup',1)
    assert len(re.findall(r'\\example\{',s))==count
    for env in ['equation','align']:
        assert len(re.findall(r'\\begin\{'+env+r'\*?\}',s))>=len(re.findall(r'\\begin\{'+env+r'\*?\}',baseline))
    original_keys=re.findall(r'\\Original(?:Figure|Panel)\{([^}]+)\}',baseline)
    assert original_keys==re.findall(r'\\Original(?:Figure|Panel)\{([^}]+)\}',s)
    name=f'{chapter}-{topic}讲义-完善版'
    (P/(name+'.tex')).write_text(s)
    result={'new_figures':len(items),'original_assets':len(original_keys),'examples':count,'main':str(P/(name+'.tex'))}
    (P/'资料核查/正文与配图保留检查.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':
    for args in CONFIG:build(*args)
