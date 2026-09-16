# Algorithms Benchmark

Este repositório implementa e compara o desempenho dos seguintes algoritmos de ordenação:

- **Bubble Sort** (com parada antecipada)
- **Selection Sort**
- **Insertion Sort**
- **Merge Sort** (divisão e conquista recursiva estável)
- **Quick Sort** (otimizado com pivô por Mediana de Três e partição iterativa)
- **Heap Sort** (max-heap *in-place*)

O projeto responde às perguntas teóricas e práticas em [docs/questions.md](docs/questions.md) e analisa as métricas de tempo, comparações, trocas e estabilidade em [docs/metrics.md](docs/metrics.md).

---

## 📁 Estrutura do Repositório

```
.
├── bench/                  # Testes de benchmark e geração de métricas/gráficos
│   ├── charts/             # Gráficos de desempenho gerados em PNG
│   ├── results/            # Resultados exportados (JSON, CSV e Markdown)
│   ├── main.py             # Script principal executor do benchmark
│   ├── utils.py            # Geradores de dados e utilitários
│   └── utilts.py           # Módulo base de utilitários
├── docs/                   # Documentação conceitual e teórica
│   ├── metrics.md          # Definição das métricas, complexidades assintóticas e estabilidade
│   └── questions.md        # Respostas detalhadas às perguntas de análise de desempenho
├── src/                    # Implementações modulares e desacopladas dos algoritmos
│   ├── bubble/             # Implementação do Bubble Sort
│   ├── heap/               # Implementação do Heap Sort
│   ├── insertion/          # Implementação do Insertion Sort
│   ├── merge/              # Implementação do Merge Sort
│   ├── quick/              # Implementação do Quick Sort
│   ├── selection/          # Implementação do Selection Sort
│   └── main.md             # Guia de arquitetura e exemplos de uso
├── tests/                  # Testes unitários com unittest
│   └── tests.py            # Testes com arrays vazios, unitários, invertidos, duplicados e objetos
└── README.md
```

---

## 📊 Resumo de Complexidade Assintótica

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso | Espaço Auxiliar | Estável? | Paradigma |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sim** | Trocas adjacentes |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Não** | Seleção do mínimo |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sim** | Inserção incremental |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **Sim** | Divisão e Conquista |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | **Não** | Particionamento (Mediana de 3) |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | **Não** | Heap Binário Máximo |

---

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python 3.10+ e as dependências instaladas:
```bash
pip install matplotlib
```

### 2. Executar os Testes Unitários
Para validar a corretude de todos os algoritmos (incluindo testes de ordenação de inteiros, floats, negativos, objetos e estabilidade):
```bash
python -m unittest tests/tests.py -v
```

### 3. Executar o Benchmark Completo
Para rodar a bateria de testes de desempenho para todos os tamanhos ($N = 100, 500, 1.000, 5.000, 10.000, 50.000, 100.000$), gerar os arquivos de dados (JSON/CSV) e os gráficos de comparação:
```bash
python -u -m bench.main
```

---

## 📈 Resultados e Gráficos Gerados

Os testes geram automaticamente gráficos comparativos em alta resolução no diretório `bench/charts/`:

- **Tempo de Execução (Aleatório)**: `bench/charts/time_comparison_random.png`
- **Tempo de Execução (Já Ordenado)**: `bench/charts/time_comparison_sorted.png`
- **Tempo de Execução (Invertido)**: `bench/charts/time_comparison_reverse.png`
- **Tempo de Execução (Quase Ordenado - 5% swaps)**: `bench/charts/time_comparison_nearly_sorted.png`
- **Comparações vs Tamanho**: `bench/charts/comparisons_vs_size.png`
- **Trocas / Deslocamentos vs Tamanho**: `bench/charts/swaps_vs_size.png`
- **Tipos Primitivos vs Objetos Customizados**: `bench/charts/primitives_vs_objects.png`
- **Comparativo Geral em Barra ($N=5.000$)**: `bench/charts/overall_comparison_bar.png`

Os dados numéricos detalhados encontram-se salvos em [bench/results/summary.md](bench/results/summary.md), [bench/results/benchmark_results.json](bench/results/benchmark_results.json) e [bench/results/benchmark_results.csv](bench/results/benchmark_results.csv).
