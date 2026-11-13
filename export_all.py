import glob, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _gen_articulo import convert

CORPUS = pathlib.Path('E:/projects/trainings/distill')
labels = {'01_defcon': 'DEF CON', '02_ekoparty': 'Ekoparty', '03_aipentest': 'IA & Pentesting',
          '04_unprompted': '[un]prompted', 'ai300-osai': 'AI300 — Offensive AI',
          'oscp-pen200': 'OSCP (PEN-200)', 'osep-pen300': 'OSEP (PEN-300)',
          '05_gentleai': 'Gentle AI', '06_aiecode': 'AIE CODE Summit', '07_broadcasts': 'Broadcasts'}
cids = {'01_defcon': 'defcon', '02_ekoparty': 'ekoparty', '03_aipentest': 'aipentest',
        '04_unprompted': 'unprompted', 'ai300-osai': 'ai300', 'oscp-pen200': 'oscp',
        'osep-pen300': 'osep', '05_gentleai': 'gentleai', '06_aiecode': 'aiecode', '07_broadcasts': 'broadcasts'}

n = 0
from collections import Counter
all_stems = Counter(pathlib.Path(p).stem for p in glob.glob(str(CORPUS / '*' / 'writeups' / '*.md')))
for p in sorted(glob.glob(str(CORPUS / '*' / 'writeups' / '*.md'))):
    parts = pathlib.Path(p).parts
    conf = parts[-3]
    stem = pathlib.Path(p).stem
    out_name = f'{cids[conf]}-{stem}.html' if all_stems[stem] > 1 else None
    convert(p, cids[conf], labels[conf], out_name)
    n += 1
print(f'FIN: {n} articulos exportados (determinista)', flush=True)
