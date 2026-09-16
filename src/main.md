# Arquitetura e Implementação dos Algoritmos

Os algoritmos de ordenação estão organizados em módulos independentes sob o diretório `src/`. Cada diretório possui código autocontido sem acoplamento direto ou classes base compartilhadas com os demais algoritmos, conforme a especificação do projeto.

---

## 1. Estrutura de Diretórios

```
src/
├── bubble/
│   ├── __init__.py
│   └── bubble_sort.py
├── heap/
│   ├── __init__.py
│   └── heap_sort.py
├── insertion/
│   ├── __init__.py
│   └── insertion_sort.py
├── merge/
│   ├── __init__.py
│   └── merge_sort.py
├── quick/
│   ├── __init__.py
│   └── quick_sort.py
├── selection/
│   ├── __init__.py
│   └── selection_sort.py
├── __init__.py
└── main.md
```

---

## 2. Padrão de Uso das Classes e Funções

Cada módulo expõe:
1. Uma classe de orquestração (ex: `BubbleSort`, `MergeSort`, etc.) que rastreia `comparisons`, `swaps` e `time_taken`.
2. Uma função auxiliar direta (ex: `bubble_sort(arr, key=None, in_place=True)`).

### Exemplo em Código Python

```python
from src.quick.quick_sort import quick_sort
from src.merge.merge_sort import merge_sort

# 1. Ordenação de lista simples de inteiros
numeros = [64, 25, 12, 22, 11]
resultado, metricas = quick_sort(numeros)
print("Ordenado:", resultado)
print("Métricas:", metricas)
# Saída: {'algorithm': 'Quick Sort', 'size': 5, 'comparisons': 8, 'swaps': 9, 'time_taken': 0.000012}

# 2. Ordenação de lista de objetos com chave customizada
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

alunos = [Aluno("Ana", 8.5), Aluno("Bruno", 6.0), Aluno("Carlos", 9.2)]
ordenados, _ = merge_sort(alunos, key=lambda a: a.nota)
for aluno in ordenados:
    print(aluno.nome, aluno.nota)
```

---

## 3. Características das Implementações

- **Bubble Sort (`src/bubble/bubble_sort.py`)**: Implementa parada antecipada com flag booleana quando nenhuma troca ocorre na passagem.
- **Selection Sort (`src/selection/selection_sort.py`)**: Realiza busca linear do elemento mínimo em cada partição e troca pontual na posição indexada.
- **Insertion Sort (`src/insertion/insertion_sort.py`)**: Desloca elementos maiores para a direita e insere o valor corrente no local correto.
- **Merge Sort (`src/merge/merge_sort.py`)**: Divisão e conquista estável garantindo $O(n \log n)$ com intercalação ordenada.
- **Quick Sort (`src/quick/quick_sort.py`)**: Otimizado com **Mediana de Três** e pilha iterativa para prevenir recursão profunda e degradação em arrays ordenados.
- **Heap Sort (`src/heap/heap_sort.py`)**: Constrói um Max-Heap *in-place* e ordena com trocas na raiz seguidas de `heapify`.
