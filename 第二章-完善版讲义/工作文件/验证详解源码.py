from pathlib import Path
import hashlib, json, re, subprocess, tempfile, zipfile
import fitz

P = Path(__file__).resolve().parents[1]
NAME = '第二章-质点组力学讲义-完善版'
archive = P / '第二章-质点组力学-完善版LaTeX源码及图片.zip'
tmp = Path(tempfile.mkdtemp(prefix='mechanics-c2-final-portable-'))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    compile_inputs = {n: hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if "/资料核查/" not in n}
    z.extractall(tmp)
work = tmp / '第二章-质点组力学源码'
(P / '工作文件/独立编译位置.json').write_text(json.dumps({'directory': str(work)}, ensure_ascii=False, indent=2))
cmd = ['/Users/dongxingxi/.local/bin/latexmk', '-norc', '-xelatex', '-interaction=nonstopmode', '-halt-on-error', '-outdir=build', NAME + '.tex']
with (work / 'portable-build.log').open('w') as log:
    result = subprocess.run(cmd, cwd=work, stdout=log, stderr=subprocess.STDOUT)
assert result.returncode == 0
new_pdf = work / 'build' / (NAME + '.pdf')
final_pdf = P / (NAME + '.pdf')
qpdf_checks = {}
for label, pdf in [('portable', new_pdf), ('delivery', final_pdf)]:
    check = subprocess.run(['/opt/homebrew/bin/qpdf', '--check', str(pdf)], capture_output=True, text=True)
    qpdf_checks[label] = {'exit_code': check.returncode, 'output': check.stdout + check.stderr}
    assert check.returncode == 0, qpdf_checks[label]
warnings = [line for line in (work / 'build' / (NAME + '.log')).read_text().splitlines()
            if re.search(r'Warning|Overfull|Underfull|Missing character|^!', line)]
assert not warnings, warnings
a, b = fitz.open(final_pdf), fitz.open(new_pdf)
assert not a.is_repaired and not b.is_repaired
assert len(a) == len(b)
text_diffs, pixel_diffs = [], []
for i in range(len(a)):
    if a[i].get_text() != b[i].get_text(): text_diffs.append(i+1)
    fitz.TOOLS.store_shrink(100)
    first=a[i].get_pixmap(matrix=fitz.Matrix(.8,.8),alpha=False).digest
    fitz.TOOLS.store_shrink(100)
    second=b[i].get_pixmap(matrix=fitz.Matrix(.8,.8),alpha=False).digest
    if first != second: pixel_diffs.append(i+1)
assert not text_diffs and not pixel_diffs, (text_diffs, pixel_diffs)
source_hash_checks = []
for r in json.loads((P / '资料核查/原课件校验.json').read_text()):
    assert hashlib.sha256((P.parent / r['文件']).read_bytes()).hexdigest() == r['sha256']
    source_hash_checks.append(r['文件'])
report = {'status': 'passed', 'pdf_pages': len(a), 'all_page_texts_identical': True,
          'all_pages_pixel_identical_at_0_8x': True, 'warnings': warnings, 'qpdf_checks': qpdf_checks,
          'renderer_store_reset_between_pages': True,
          'source_ppts_unchanged': source_hash_checks,
          'pdf_sha256': hashlib.sha256(final_pdf.read_bytes()).hexdigest(),
          'source_archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
          'portable_directory': str(work), 'compile_input_hashes': compile_inputs}
(P / '资料核查/源码包独立编译检查.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps({k: v for k, v in report.items() if k not in ['qpdf_checks','compile_input_hashes']}, ensure_ascii=False))
