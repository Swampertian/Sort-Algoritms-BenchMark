# Métricas de Desempenho e Análise de Complexidade

Este documento detalha as métricas coletadas durante os testes de benchmark dos algoritmos de ordenação, além de apresentar a fundamentação teórica de complexidade assintótica (tempo e espaço) e propriedades de estabilidade.

---

## 1. Métricas Coletadas

Para avaliar com precisão o comportamento dos algoritmos, o benchmark monitora as seguintes métricas de execução:

| Métrica | Descrição | Unidade |
| :--- | :--- | :--- |
| **Tempo de Execução (`time_taken`)** | Tempo real de CPU/relógio decorrido durante a ordenação medido com `time.perf_counter()`. | Segundos ($s$) |
| **Comparações (`comparisons`)** | Número total de operações relacionais entre elementos do array (ex: `A[i] > A[j]` ou `key(x) <= key(y)`). | Contagem inteira |
| **Trocas / Deslocamentos (`swaps`)** | Número total de mutações de posição de elementos (trocas de pares em Bubble/Selection/Quick/Heap ou deslocamentos/atribuições em Insertion/Merge). | Contagem inteira |
| **Corretude (`is_valid`)** | Validação pós-ordenação que verifica se $A[i] \le A[i+1]$ para todo $i$. | Booleano (`True`/`False`) |
| **Estabilidade** | Se elementos com chaves equivalentes mantêm sua ordem relativa inicial após a ordenação. | Propriedade teórica & testada |

---

## 2. Tabela de Complexidade Assintótica

A tabela a seguir sumariza as complexidades teóricas de tempo (Melhor Caso, Caso Médio e Pior Caso) e de espaço auxiliar para os 6 algoritmos implementados:

| Algoritmo | Melhor Caso (Tempo) | Caso Médio (Tempo) | Pior Caso (Tempo) | Espaço Auxiliar | Estável? | Método / Paradigma |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sim** | Trocas sucessivas adjacentes com parada antecipada |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Não** | Seleção do mínimo |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sim** | Inserção incremental |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **Sim** | Divisão e Conquista |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | **Não** | Divisão e Conquista com Particionamento (Mediana de 3) |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | **Não** | Estrutura de Heap Binário Máximo |

---

## 3. Explicação dos Casos por Algoritmo

### Bubble Sort
- **Melhor Caso ($O(n)$)**: Ocorre quando o array já se encontra totalmente ordenado. A flag `swapped` permanece `False` na primeira passagem e o algoritmo encerra com $n - 1$ comparações e 0 trocas.
- **Pior e Médio Casos ($O(n^2)$)**: Ocorre em dados aleatórios ou inversamente ordenados, executando $\approx \frac{n(n-1)}{2}$ comparações.

### Selection Sort
- **Todos os Casos ($O(n^2)$)**: O Selection Sort varre todo o subarray restante em busca do elemento mínimo independentemente da ordem inicial, resultando sempre em $\frac{n(n-1)}{2}$ comparações.
- **Vantagem em Trocas**: Realiza no máximo $O(n)$ trocas de elementos, sendo eficiente quando o custo de escrita em memória é muito superior ao de leitura.

### Insertion Sort
- **Melhor Caso ($O(n)$)**: Array já ordenado ou quase ordenado. Cada elemento é comparado apenas 1 vez com seu antecessor.
- **Pior Caso ($O(n^2)$)**: Array em ordem inversa. Cada novo elemento precisa ser deslocado por toda a extensão do subarray ordenado.

### Merge Sort
- **Consistência ($O(n \log n)$)**: Divide o array na metade recursivamente e intercala os subarrays ordenados. O tempo de execução é estritamente $O(n \log n)$ para qualquer padrão de entrada.
- **Custo de Memória ($O(n)$)**: Requer espaço de memória auxiliar para os arrays temporários de intercalação.

### Quick Sort
- **Caso Médio / Melhor ($O(n \log n)$)**: Partições balanceadas dividem o problema aproximadamente ao meio.
- **Otimizações Implementadas**: Utiliza a técnica de **Mediana de Três** (`first`, `mid`, `last`) para seleção de pivô e pilha iterativa, evitando a degradação para $O(n^2)$ em arrays já ordenados ou quase ordenados.

### Heap Sort
- **Garantia de Tempo ($O(n \log n)$) e Espaço ($O(1)$)**: Constrói um Max-Heap em $O(n)$ e extrai os $n$ elementos sucessivamente, cada extração custando $O(\log n)$ no `heapify`. Ordena *in-place* sem consumo extra de memória.
