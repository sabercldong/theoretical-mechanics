from pathlib import Path
import re, json, hashlib

P = Path(__file__).resolve().parents[1]
NAME = '第四章-转动参考系讲义-完善版'

def brace(s, i):
    assert s[i] == '{'
    d, j = 1, i + 1
    while d:
        if s[j] == '{' and s[j-1] != '\\': d += 1
        if s[j] == '}' and s[j-1] != '\\': d -= 1
        j += 1
    return s[i+1:j-1], j

MACROS = r'''
\makeatletter
\newcommand{\Needspace}[1]{\par\if@nobreak\else\penalty0\begingroup\dimen0=#1\relax\dimen2=\pagegoal\advance\dimen2 by-\pagetotal\ifdim\dimen0>\dimen2\newpage\fi\endgroup\fi}
\makeatother
\let\SavedSection\section
\renewcommand{\section}{\Needspace{8\baselineskip}\SavedSection}
\let\SavedSubsection\subsection
\renewcommand{\subsection}{\Needspace{6\baselineskip}\SavedSubsection}
\newsavebox{\TeachingBox}
\newcommand{\TeachingFigure}[2]{%
\par\addvspace{8pt}\noindent\begin{minipage}{\linewidth}\centering
\sbox{\TeachingBox}{\input{补充图/#1.tex}}%
\ifdim\wd\TeachingBox>.98\linewidth\resizebox{.98\linewidth}{!}{\usebox{\TeachingBox}}\else\usebox{\TeachingBox}\fi
\captionof{figure}{#2}\label{fig:lesson-#1}\end{minipage}\par\addvspace{8pt}}
\newcommand{\OriginalFigure}[3][6.2cm]{%
\par\addvspace{8pt}\noindent\begin{minipage}{\linewidth}\centering
\includegraphics[width=.94\linewidth,height=#1,keepaspectratio]{原图/#2}%
\captionof{figure}{#3}\label{fig:orig-#2}\end{minipage}\par\addvspace{8pt}}
'''

def build():
    baseline = (P/'工作文件/修订前主稿.tex').read_text()
    s = baseline
    manifests = [P/f'工作文件/原图清单-{x}.json' for x in 'ab']
    originals = []
    for f in manifests:
        if f.exists():
            data = json.loads(f.read_text())
            if isinstance(data, dict): data = data.get('figures', data.get('items', []))
            originals.extend(data)
    final_adjustments=P/'工作文件/原图终校修订.json'
    if final_adjustments.exists():
        overrides=json.loads(final_adjustments.read_text())
        for row in originals:
            row.update(overrides.get(row['key'],{}))
    layout_adjustments=P/'工作文件/排版位置调整.json'
    if layout_adjustments.exists():
        overrides=json.loads(layout_adjustments.read_text())
        for row in originals:
            if row['key'] in overrides:
                row['insert_after']=overrides[row['key']]['insert_after']
                row['layout_note']=overrides[row['key']]['reason']
    assert len({r['key'] for r in originals}) == len(originals)
    patches = P/'工作文件/正文适配修订.json'
    patch_rows = json.loads(patches.read_text()) if patches.exists() else []
    # Source image placements are applied against a frozen, fully detailed manuscript.
    groups = {}
    for row in originals:
        key = row['key']
        assert (P/'原图'/(key+'.pdf')).exists(), key
        anchor = row.get('insert_after', row.get('anchor_text'))
        row['insert_after'] = anchor
        assert baseline.count(anchor) == 1, (key, 'anchor count', baseline.count(anchor))
        pos=baseline.index(anchor)+len(anchor)
        prefix=re.sub(r'(?m)(?<!\\)%[^\n]*','',baseline[:pos])
        depth=len(re.findall(r'(?<!\\)\{',prefix))-len(re.findall(r'(?<!\\)\}',prefix))
        assert depth==0,(key,'anchor inside a command argument',depth)
        stack=[]
        for env in re.finditer(r'\\(begin|end)\{([^}]+)\}',prefix):
            if env[1]=='begin':stack.append(env[2])
            else:
                assert stack and stack[-1]==env[2],(key,'unbalanced environment',env[2])
                stack.pop()
        assert stack==['document'],(key,'anchor inside an environment',stack)
        assert len(re.findall(r'(?<!\\)\\\[',prefix))==len(re.findall(r'(?<!\\)\\\]',prefix)),(key,'anchor inside display math')
        groups.setdefault(anchor, []).append(row)
    additions = []
    for anchor, rows in groups.items():
        text = '\n% BEGIN ORIGINAL FIGURES\n'
        for row in sorted(rows, key=lambda r:(r['deck'], r['page'], r['key'])):
            size = row.get('max_height_cm', 6.2)
            text += r'\OriginalFigure['+str(size)+'cm]{'+row['key']+'}{'+row['caption']+'}\n'
        text += '% END ORIGINAL FIGURES\n'
        additions.append((baseline.index(anchor)+len(anchor), text))
    for pos, text in sorted(additions, reverse=True): s = s[:pos]+text+s[pos:]
    # Move every existing model drawing into its own editable file, without rewriting it.
    model_patch_path=P/'工作文件/模型排版修订.json'
    model_patches=json.loads(model_patch_path.read_text()) if model_patch_path.exists() else {}
    models, spans = [], []
    for idx, m in enumerate(re.finditer(r'\\figstart\s*\n', s), 1):
        j = s.index(r'\figend{', m.end())
        caption, end = brace(s, j+len(r'\figend'))
        code = s[m.end():j].strip()+'\n'
        assert '% BEGIN ORIGINAL FIGURES' not in code, ('anchor placed inside model figure', idx)
        key = f'c4-diagram-{idx:02d}'
        original_model_sha256=hashlib.sha256(code.encode()).hexdigest()
        for patch in model_patches.get(key,[]):
            assert code.count(patch['old'])==1,(key,patch)
            code=code.replace(patch['old'],patch['new'],1)
        f = P/'补充图'/(key+'.tex')
        f.write_text(code)
        models.append({'key':key,'original_index':idx,'caption':caption,'file':str(f.relative_to(P)),
                       'sha256':hashlib.sha256(code.encode()).hexdigest(),
                       'baseline_model_sha256':original_model_sha256,'layout_patches':model_patches.get(key,[]),
                       'source':'项目既有第四章详细讲义中的模型图；保留2026-10-13图形核查修订。'})
        spans.append((m.start(), end, r'\TeachingFigure{'+key+'}{'+caption+'}', s[m.start():end]))
    assert len(models) == 47
    for start, end, replacement, _ in reversed(spans): s = s[:start]+replacement+s[end:]
    # Prove that extraction and insertion have not removed any pre-existing text.
    restored = s
    for _, _, replacement, original in spans: restored = restored.replace(replacement, original, 1)
    restored = re.sub(r'\n% BEGIN ORIGINAL FIGURES\n.*?% END ORIGINAL FIGURES\n', '', restored, flags=re.S)
    assert restored == baseline, 'Source text changed during figure integration'
    for row in patch_rows:
        assert s.count(row['old']) == 1, row['old'][:100]
        s = s.replace(row['old'], row['new'], 1)
    s = s.replace('% 第四章转动参考系讲义。\n% 单文件文档；使用当前编辑器的内置编译器。',
                  '% !TEX program = xelatex\n% 第四章完善版；主文件、原图与补充图目录须一起保存。')
    s = s.replace('xcolor,tikz,booktabs', 'xcolor,graphicx,tikz,booktabs')
    s = s.replace('pdftitle={理论力学讲义：第四章 转动参考系}',
                  'pdftitle={理论力学讲义：第四章 转动参考系（完善版）}')
    s = s.replace(r'\refstepcounter{example}\subsubsection*', r'\Needspace{5\baselineskip}\refstepcounter{example}\subsubsection*')
    s = s.replace(r'\refstepcounter{exercise}\subsubsection*', r'\Needspace{5\baselineskip}\refstepcounter{exercise}\subsubsection*')
    s = s.replace(r'\begin{document}', MACROS+'\n'+r'\begin{document}', 1)
    # Stable source-page and figure references survive pagination changes.
    sec = sub = example = exercise = 0
    anchors, pieces, last = [], [], 0
    for m in re.finditer(r'\\(section|subsection|example|exercise)\{', s):
        title, end = brace(s, m.end()-1); kind = m[1]
        if kind == 'section': sec += 1; sub = 0; key = f'sec:c4-{sec}'
        elif kind == 'subsection': sub += 1; key = f'sub:c4-{sec}.{sub}'
        elif kind == 'example': example += 1; key = f'ex:c4-{example}'
        else: exercise += 1; key = f'test:c4-{exercise}'
        pieces += [s[last:end], r'\label{'+key+'}']; last = end
        anchors.append({'key':key,'title':title,'kind':kind})
    pieces.append(s[last:]); s = ''.join(pieces)
    appendix = r'''
\clearpage
\section*{原课件作业题号}\label{appendix:coursework}
\addcontentsline{toc}{section}{原课件作业题号}
以下保留课件给出的教材作业题号。仅列题号的条目须结合原教材使用；
课件中给出完整题干的旋转滑珠、偏置单摆与傅科摆等题目，已在正文中逐步求解。
讲义中的例题和自测另行连续编号。
\begin{center}\begin{tabular}{@{}lll@{}}\toprule
课件&原页码&教材作业题号\\\midrule
c4-1&29&4.1、4.2、4.3\\
c4-2&26&4.7、4.10、4.12\\\bottomrule
\end{tabular}\end{center}
\subsection*{学习与复习建议}\label{appendix:study}
理解力学规律需要接触和分析具体问题，不能只记结论。
可按“听课理解、复习课件、独立做题、思考总结”的顺序反复练习，
每次用参考系选择、受力分析、计算结果及其极限检查来检验自己的理解。
\section*{课件原图来源索引}\label{appendix:originals}
\addcontentsline{toc}{section}{课件原图来源索引}
下表按讲义中的出现顺序列出课件原图。页码按各份课件从第一页起连续计数；
相同图形的重复出现合并处理。与原图并列的模型图用于展开坐标、受力或计算关系。
逐页内容定位与图像来源的详细记录见源码包中的资料核查文件。
\small
\begin{longtable}{@{}p{1.4cm}p{8.1cm}p{4.8cm}@{}}
\toprule 图号&内容&原课件位置\\\midrule\endhead
'''
    order = re.findall(r'\\OriginalFigure(?:\[[^\]]+\])?\{([^}]+)\}', s)
    bykey = {r['key']:r for r in originals}
    for key in order:
        r = bykey[key]
        appendix += r'\ref{fig:orig-'+key+'}&'+r['topic'].replace('_',r'\_')+'&'+r['deck']+f'，第 {r["page"]} 页'+r'\\'+'\n'
    appendix += r'\bottomrule\end{longtable}\normalsize'+'\n'
    s = s.replace(r'\end{document}', appendix+r'\end{document}')
    for token, n in [(r'\example{',47),(r'\exercise{',24),(r'\TeachingFigure{',47),(r'\section{',12)]:
        assert s.count(token) == n, (token, s.count(token), n)
    assert '补充绘制' not in s
    (P/(NAME+'.tex')).write_text(s)
    (P/'工作文件/正文定位标记.json').write_text(json.dumps(anchors,ensure_ascii=False,indent=2))
    (P/'资料核查/模型图来源与核对.json').write_text(json.dumps(models,ensure_ascii=False,indent=2))
    (P/'工作文件/整合原图清单.json').write_text(json.dumps([bykey[k] for k in order],ensure_ascii=False,indent=2))
    report = {'baseline_sha256':hashlib.sha256(baseline.encode()).hexdigest(),
              'all_preexisting_text_preserved_before_listed_patches':True,
              'existing_model_figures_preserved':len(models),'examples':47,'selftests':24,
              'original_assets_added':len(originals),'documented_text_patches':patch_rows,
              'heading_pagination':'先以零惩罚触发页面构建，再判断实际剩余高度；避免沿用前页高度导致尾段单独成页；正文及数学内容不改。',
              'documented_model_layout_patches':model_patches,
              'numbered_equation_environments_before':baseline.count(r'\begin{equation}'),
              'numbered_equation_environments_after':s.count(r'\begin{equation}')}
    (P/'资料核查/正文与配图保留检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k != 'documented_text_patches'},ensure_ascii=False))

if __name__ == '__main__': build()
