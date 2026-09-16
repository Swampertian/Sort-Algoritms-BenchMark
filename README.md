## Algorithms Benchmark

Este repositório tem como objetivo implementar e comparar o desempenho dos seguintes algoritmos de ordenação:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

O projeto busca responder às seguintes [perguntas](docs/questions.md) e analisar as [métricas](docs/metrics.md).

### Estrutura do Repositório

`bench/`: contém os testes de benchmark e desempenho. Deve gerar a saída padrão, em arquivo, com os números e as estruturas de entrada (arrays simples ou objetos), além de produzir os gráficos.

`src/(algoritmo)`: contém o código relacionado a cada algoritmo. Cada diretório deve funcionar de forma independente, sem métodos ou classes compartilhados entre os algoritmos. Deve haver, no máximo, um orquestrador em um construtor ou classe principal.

`tests/`: contém testes unitários dos métodos presentes nos algoritmos (opcional).

### Testes

Os algoritmos deverão ser avaliados utilizando diferentes tamanhos de entrada. Sugere-se utilizar, por exemplo:

`n = 100`, `500`, `1.000`, `5.000`, `10.000`, `50.000` e `100.000`.

Os tamanhos podem ser ajustados de acordo com o desempenho dos algoritmos e os recursos computacionais disponíveis.
