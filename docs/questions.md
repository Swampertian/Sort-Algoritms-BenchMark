# Respostas às Questões Analíticas do Trabalho

Este documento analisa detalhadamente as questões propostas no trabalho prático da disciplina, correlacionando os dados empíricos observados nos experimentos com a teoria assintótica de complexidade.

---

### 1. Qual algoritmo apresentou melhor desempenho para entradas aleatórias?

**Resposta:**
Para entradas aleatórias, o **Quick Sort** apresentou o melhor desempenho geral em tempo de execução, especialmente para tamanhos médios e grandes ($N \ge 1.000$).
- **Justificativa Teórica e Prática:** O Quick Sort possui complexidade média de $O(n \log n)$ com um fator constante muito baixo. Sua localidade de referência espacial no particionamento *in-place* otimiza o uso da hierarquia de memória *cache* da CPU.
- **Merge Sort e Heap Sort:** Ambos também mantiveram crescimento estritamente $O(n \log n)$, com o Merge Sort ficando ligeiramente atrás do Quick Sort devido à sobrecarga de alocação de memória auxiliar e cópia de vetores, e o Heap Sort apresentando tempos superiores devido ao padrão de saltos não-lineares nos índices do heap (`2i+1`, `2i+2`).

---

### 2. Qual algoritmo apresentou pior desempenho?

**Resposta:**
O **Bubble Sort** apresentou o pior desempenho global em tempo de execução e número de operações para entradas aleatórias e invertidas.
- **Justificativa Teórica e Prática:** Embora Bubble Sort, Selection Sort e Insertion Sort compartilhem a complexidade assintótica $O(n^2)$ no caso médio e pior caso, o Bubble Sort realiza tanto um número quadrático de comparações ($\approx \frac{n^2}{2}$) quanto um número quadrático de trocas ($O(n^2)$).
- **Comparativo:** O Selection Sort, apesar de executar o mesmo número de comparações, realiza apenas $O(n)$ trocas; já o Insertion Sort realiza deslocamentos eficientes, superando o Bubble Sort por margens significativas de tempo.

---

### 3. O comportamento observado está de acordo com a complexidade teórica?

**Resposta:**
**Sim, com perfeita aderência.**
- Os algoritmos $O(n \log n)$ (Quick Sort, Merge Sort e Heap Sort) apresentaram curvas de tempo quase lineares em escala log-log, ordenando $100.000$ elementos em frações de segundo (entre $0,15$s e $0,50$s).
- Os algoritmos $O(n^2)$ (Bubble Sort, Selection Sort e Insertion Sort) apresentaram crescimento quadrático nítido, no qual multiplicar o tamanho da entrada por $10$ (de $1.000$ para $10.000$) resultou em um aumento de aproximadamente $100\times$ no tempo de execução e número de comparações.

---

### 4. Como o tipo de entrada influencia o desempenho dos algoritmos?

**Resposta:**
O tipo e o arranjo inicial dos dados alteram drasticamente o comportamento de algoritmos sensíveis ao estado da entrada:
- **Entrada Já Ordenada:**
  - *Insertion Sort* e *Bubble Sort* (com parada antecipada) atingem sua cota de **Melhor Caso $O(n)$**, executando em milissegundos mesmo para grandes $N$.
  - *Selection Sort* não se beneficia, permanecendo em $O(n^2)$ comparações.
  - *Quick Sort* (com mediana de 3) e *Merge/Heap Sort* mantêm $O(n \log n)$.
- **Entrada Inversamente Ordenada:**
  - Constitui o **Pior Caso $O(n^2)$** para o *Insertion Sort* e *Bubble Sort*, onde cada elemento deve percorrer toda a extensão da partição.
  - O *Selection Sort* realiza $O(n^2)$ comparações mas apenas $\frac{n}{2}$ trocas.
- **Entrada Parcialmente Ordenada (5% de desordem):**
  - O *Insertion Sort* destaca-se com desempenho quase linear ($O(n + d)$), sendo mais rápido até mesmo que os algoritmos $O(n \log n)$ para $N \le 5.000$.

---

### 5. Quais algoritmos são mais sensíveis ao fato de a entrada estar ordenada ou inversamente ordenada?

**Resposta:**
Os algoritmos mais sensíveis à ordenação prévia da entrada são:
1. **Insertion Sort:** É o mais sensível de todos. Varia de $O(n)$ ($0,00001$s para $N=1.000$) no caso ordenado para $O(n^2)$ ($0,057$s para $N=1.000$) no caso invertido — uma variação de mais de $5.000\times$.
2. **Bubble Sort:** Graças à otimização da flag `swapped`, reduz de $O(n^2)$ para $O(n)$ no caso já ordenado.
3. **Selection Sort:** É totalmente **insensível** ao estado da entrada; seu número de comparações é rigidamente fixo em $\frac{n(n-1)}{2}$ em todos os cenários.
4. **Merge Sort e Heap Sort:** Praticamente **insensíveis** em tempo de execução, com variação mínima dentro do limite de $O(n \log n)$.

---

### 6. Em quais situações um algoritmo $O(n^2)$ pode apresentar desempenho competitivo?

**Resposta:**
Um algoritmo $O(n^2)$ (em especial o **Insertion Sort**) é altamente competitivo e preferível nas seguintes situações:
1. **Arrays Pequenos ($N < 50$ ou $N \le 100$):** Devido à baixíssima sobrecarga constante (ausência de recursão, alocação de pilhas/vetores auxiliares e chamadas de função), o Insertion Sort é mais rápido que Quick Sort e Merge Sort. Por isso, algoritmos híbridos de produção como o *Timsort* (padrão em Python e Java) e *Introsort* (C++ STL) utilizam Insertion Sort para pequenos blocos.
2. **Vetores Quase Totalmente Ordenados:** Quando apenas uma pequena fração dos elementos está fora de posição ou novos elementos são inseridos em um vetor previamente ordenado em tempo real (*online sorting*).

---

### 7. O comportamento observado do Quick Sort está de acordo com o esperado?

**Resposta:**
**Sim.**
- Uma implementação ingênua do Quick Sort (escolhendo sempre o primeiro elemento como pivô) degeneraria para $O(n^2)$ e causaria estouro de pilha recursiva em entradas já ordenadas ou invertidas.
- Com a técnica de **Mediana de Três** (`first`, `mid`, `last`) implementada no projeto, o pivô escolhido dividiu os dados de forma equilibrada em todos os cenários (aleatório, ordenado, invertido e quase ordenado), garantindo tempo médio de $O(n \log n)$ consistente e ausência de estouro de pilha.

---

### 8. Quais fatores podem explicar diferenças entre o desempenho teórico e o experimental?

**Resposta:**
Vários fatores da arquitetura computacional real explicam as divergências pontuais em relação ao modelo abstrato de contagem de operações:
1. **Constantes Ocultas e Sobrecarga de Instruções:** Operações elementares possuem pesos diferentes. Uma troca de elementos em memória consome mais ciclos do que uma comparação entre inteiros.
2. **Hierarquia de Memória e Acesso a Cache:** Algoritmos com varredura contígua de memória (Quick Sort e Insertion Sort) aproveitam o *cache L1/L2/L3* muito melhor do que o Heap Sort (que realiza saltos de índices) e o Merge Sort (que aloca buffers externos).
3. **Sobrecarga do Interpretador (Python Bytecode):** A chamada de funções extratoras de chave para objetos (`key=lambda x: x.val`) introduz uma sobrecarga considerável por comparação quando comparada à comparação direta de tipos primitivos em registradores C.
4. **Alocação Dinâmica de Memória:** O Merge Sort demanda criação de fatias (*slices*) e cópia de listas, impactando o tempo de relógio pela atividade do gerenciador de memória do Python.

---

### 9. Qual algoritmo seria mais indicado para cada cenário analisado?

| Cenário Analisado | Algoritmo Mais Indicado | Justificativa |
| :--- | :--- | :--- |
| **Entrada Aleatória Grande ($N > 1.000$)** | **Quick Sort** | Menor tempo médio de execução e excelente eficiência de cache. |
| **Entrada Já Ordenada ou Quase Ordenada** | **Insertion Sort** | Complexidade linear $O(n)$, sem sobrecarga de estruturas auxiliares. |
| **Garantia Estrita de Pior Caso $O(n \log n)$ com Estabilidade** | **Merge Sort** | Preserva a ordem original de chaves iguais e não sofre degradação em nenhum cenário. |
| **Garantia de $O(n \log n)$ com Memória Estrita $O(1)$** | **Heap Sort** | Não aloca memória extra e não depende de chamadas recursivas profundas. |
| **Tamanhos Muito Pequenos ($N < 50$)** | **Insertion Sort** | Simplicidade, zero sobrecarga operacional e execução *in-place*. |
| **Minimização do Número de Escritas em Memória** | **Selection Sort** | Executa no máximo $n - 1$ trocas, útil quando a escrita em memória Flash/EEPROM é custosa. |
