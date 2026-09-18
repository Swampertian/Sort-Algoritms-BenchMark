# Relatório de análise empírica

Documento principal: `relatorio.tex`, usando a classe local `uftex.cls`.
Este diretório é independente do restante do repositório para compilação: inclui gráficos, tabelas e dados.

## Antes da entrega

- Conferir a identifica??o j? preenchida em `identificacao.tex`.
- Ambiente registrado: Intel Core i9-14900F, 64 GB de RAM, CachyOS (Linux) e Python 3.13.
- O texto relata as limitações reais: uma medição por combinação, falta de cenário parcialmente ordenado, subcontagem de comparações do Quick e unidades diferentes de movimentação. A redação não substitui a correção dos experimentos.
- Não apresentar os valores como médias. Apenas 100, 1.000 e 10.000 elementos estão documentados.
- Se receber resultados corrigidos, atualizar dados, gráficos e discussão em conjunto. Não misturar as contagens antigas com gráficos novos.

## Compilação

Use pdfLaTeX, com a pasta `latex` como diretório de trabalho:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error relatorio.tex
pdflatex -interaction=nonstopmode -halt-on-error relatorio.tex
```

Nesta máquina, também é possível executar `powershell -ExecutionPolicy Bypass -File latex/compilar.ps1` a partir da raiz do projeto. O script usa o Tectonic local em `.tools/tectonic/tectonic.exe`, quando disponível, ou pdfLaTeX. O Tectonic baixa os pacotes necessários na primeira execução e pode exigir acesso à internet e ao cache do usuário.

Alternativamente, envie o conteúdo inteiro desta pasta para um projeto Overleaf, selecione `relatorio.tex` como documento principal e pdfLaTeX como compilador. A classe UFTex carrega vários pacotes; uma instalação TeX completa é recomendada. A capa foi adaptada para um grupo de trabalho, sem depender do arquivo `logouft`, ausente do repositório. Na classe, o driver `pdftex` deixou de ser fixado no carregamento de `hyperref`, permitindo a detecção automática para compatibilidade com Tectonic/XeTeX e pdfLaTeX.

## Rastreabilidade

- `dados/stdout_original.txt`: cópia exata do arquivo recebido do usuário, que tinha extensão CSV mas era uma tabela de texto.
- `dados/results.csv`: conversão para CSV, mantendo os 54 registros e os seis decimais dos tempos.
- `tabelas/*.tex`: tabelas com todas as métricas fornecidas, geradas por `python gerar_tabelas.py`.
- `figuras/*.png`: cópias dos dez gráficos da revisão `76413e7`.
- Referências bibliográficas incluídas no documento, sem depender de BibTeX.

O relatório não inclui a apresentação exigida separadamente pelo enunciado.
