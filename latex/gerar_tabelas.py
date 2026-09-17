"""Converte o stdout recebido e gera tabelas sem alterar os resultados."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
pattern = re.compile(r'^(random|sorted|reverse_sorted)\s+(.+? Sort)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\.\d+)\s*$')
rows = []
for line in (ROOT / 'dados/stdout_original.txt').read_text(encoding='utf-8-sig').splitlines():
    match = pattern.fullmatch(line)
    if match:
        case, algorithm, size, comparisons, swaps, elapsed = match.groups()
        rows.append(dict(case=case, algorithm=algorithm, size=int(size), comparisons=int(comparisons), swaps=int(swaps), time_taken=elapsed))
assert len(rows) == 54, 'Esperados 54 registros da execução fornecida.'
assert len({(r['case'], r['algorithm'], r['size']) for r in rows}) == 54
with (ROOT / 'dados/results.csv').open('w', encoding='utf-8', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

def number(value):
    return f'{value:,}'.replace(',', r'\,')

for case, title in [('random', 'aleatória'), ('sorted', 'ordenada'), ('reverse_sorted', 'inversamente ordenada')]:
    lines = [r'\begin{table}[htbp]', r'\centering', r'\small',
             r'\caption{Resultados completos para entrada ' + title + '. Tempos em segundos.}',
             r'\label{tab:' + case + '}', r'\begin{tabular}{lrrrr}', r'\toprule',
             r'Algoritmo & $n$ & Comparações & Contador $M$ & Tempo (s) \\', r'\midrule']
    subset = [r for r in rows if r['case'] == case]
    for index, row in enumerate(subset):
        if index and index % 6 == 0:
            lines.append(r'\midrule')
        lines.append(' & '.join([row['algorithm'], number(row['size']), number(row['comparisons']), number(row['swaps']), row['time_taken'].replace('.', ',')]) + r' \\')
    lines += [r'\bottomrule', r'\end{tabular}', r'\par\smallskip\footnotesize Fonte: saída fornecida pelo grupo. $M$ segue as convenções da Seção~\ref{sec:metricas}; as comparações do Quick Sort estão subcontadas.', r'\end{table}']
    (ROOT / f'tabelas/{case}.tex').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('54 registros preservados; CSV e três tabelas gerados.')
