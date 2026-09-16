# Relatório de Desempenho dos Algoritmos de Ordenação

Os valores representam a **média aritmética de 3 execuções independentes** para cada configuração.

## Cenário: Entrada Aleatória

| Algoritmo | Tamanho (N) | Tempo Médio (s) | Comparações Médias | Trocas / Deslocamentos | Correto? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | 100 | 0.000486 | 4,895 | 2,506 | Sim |
| Selection Sort | 100 | 0.000325 | 4,950 | 98 | Sim |
| Insertion Sort | 100 | 0.000247 | 2,601 | 2,506 | Sim |
| Merge Sort | 100 | 0.000119 | 543 | 672 | Sim |
| Quick Sort | 100 | 0.000082 | 686 | 450 | Sim |
| Heap Sort | 100 | 0.000137 | 1,028 | 582 | Sim |
| Bubble Sort | 500 | 0.014757 | 123,760 | 60,394 | Sim |
| Selection Sort | 500 | 0.008176 | 124,750 | 496 | Sim |
| Insertion Sort | 500 | 0.005335 | 60,889 | 60,394 | Sim |
| Merge Sort | 500 | 0.000765 | 3,877 | 4,488 | Sim |
| Quick Sort | 500 | 0.000466 | 4,492 | 2,363 | Sim |
| Heap Sort | 500 | 0.000960 | 7,463 | 4,066 | Sim |
| Bubble Sort | 1,000 | 0.058573 | 499,035 | 253,536 | Sim |
| Selection Sort | 1,000 | 0.036986 | 499,500 | 988 | Sim |
| Insertion Sort | 1,000 | 0.022881 | 254,530 | 253,536 | Sim |
| Merge Sort | 1,000 | 0.001586 | 8,709 | 9,976 | Sim |
| Quick Sort | 1,000 | 0.001040 | 10,187 | 5,563 | Sim |
| Heap Sort | 1,000 | 0.002248 | 16,855 | 9,070 | Sim |
| Bubble Sort | 5,000 | 1.679035 | 12,496,597 | 6,359,272 | Sim |
| Selection Sort | 5,000 | 0.996834 | 12,497,500 | 4,991 | Sim |
| Insertion Sort | 5,000 | 0.742394 | 6,364,264 | 6,359,272 | Sim |
| Merge Sort | 5,000 | 0.013935 | 55,213 | 61,808 | Sim |
| Quick Sort | 5,000 | 0.010588 | 66,935 | 36,733 | Sim |
| Heap Sort | 5,000 | 0.016877 | 107,623 | 57,038 | Sim |
| Merge Sort | 10,000 | 0.021113 | 120,407 | 133,616 | Sim |
| Quick Sort | 10,000 | 0.017980 | 141,643 | 78,298 | Sim |
| Heap Sort | 10,000 | 0.043490 | 235,396 | 124,158 | Sim |
| Merge Sort | 50,000 | 0.147640 | 718,286 | 784,464 | Sim |
| Quick Sort | 50,000 | 0.105086 | 873,605 | 473,323 | Sim |
| Heap Sort | 50,000 | 0.239216 | 1,409,853 | 737,574 | Sim |
| Merge Sort | 100,000 | 0.329992 | 1,536,389 | 1,668,928 | Sim |
| Quick Sort | 100,000 | 0.226681 | 1,917,708 | 1,095,388 | Sim |
| Heap Sort | 100,000 | 0.562683 | 3,019,707 | 1,574,936 | Sim |

## Cenário: Entrada Já Ordenada

| Algoritmo | Tamanho (N) | Tempo Médio (s) | Comparações Médias | Trocas / Deslocamentos | Correto? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | 100 | 0.000007 | 99 | 0 | Sim |
| Selection Sort | 100 | 0.000289 | 4,950 | 0 | Sim |
| Insertion Sort | 100 | 0.000009 | 99 | 0 | Sim |
| Merge Sort | 100 | 0.000100 | 356 | 672 | Sim |
| Quick Sort | 100 | 0.000069 | 606 | 345 | Sim |
| Heap Sort | 100 | 0.000170 | 1,081 | 640 | Sim |
| Bubble Sort | 500 | 0.000035 | 499 | 0 | Sim |
| Selection Sort | 500 | 0.010789 | 124,750 | 0 | Sim |
| Insertion Sort | 500 | 0.000050 | 499 | 0 | Sim |
| Merge Sort | 500 | 0.000680 | 2,272 | 4,488 | Sim |
| Quick Sort | 500 | 0.000387 | 4,008 | 2,232 | Sim |
| Heap Sort | 500 | 0.001006 | 7,756 | 4,354 | Sim |
| Bubble Sort | 1,000 | 0.000072 | 999 | 0 | Sim |
| Selection Sort | 1,000 | 0.040035 | 499,500 | 0 | Sim |
| Insertion Sort | 1,000 | 0.000161 | 999 | 0 | Sim |
| Merge Sort | 1,000 | 0.002051 | 5,044 | 9,976 | Sim |
| Quick Sort | 1,000 | 0.001235 | 9,009 | 4,960 | Sim |
| Heap Sort | 1,000 | 0.002377 | 17,583 | 9,708 | Sim |
| Bubble Sort | 5,000 | 0.000399 | 4,999 | 0 | Sim |
| Selection Sort | 5,000 | 0.960218 | 12,497,500 | 0 | Sim |
| Insertion Sort | 5,000 | 0.000595 | 4,999 | 0 | Sim |
| Merge Sort | 5,000 | 0.011453 | 32,004 | 61,808 | Sim |
| Quick Sort | 5,000 | 0.005741 | 57,726 | 30,713 | Sim |
| Heap Sort | 5,000 | 0.019360 | 112,126 | 60,932 | Sim |
| Bubble Sort | 10,000 | 0.001078 | 9,999 | 0 | Sim |
| Insertion Sort | 10,000 | 0.001130 | 9,999 | 0 | Sim |
| Merge Sort | 10,000 | 0.025384 | 69,008 | 133,616 | Sim |
| Quick Sort | 10,000 | 0.012638 | 125,439 | 66,421 | Sim |
| Heap Sort | 10,000 | 0.037808 | 244,460 | 131,956 | Sim |
| Bubble Sort | 50,000 | 0.005453 | 49,999 | 0 | Sim |
| Insertion Sort | 50,000 | 0.007173 | 49,999 | 0 | Sim |
| Merge Sort | 50,000 | 0.128837 | 401,952 | 784,464 | Sim |
| Quick Sort | 50,000 | 0.080097 | 750,015 | 398,052 | Sim |
| Heap Sort | 50,000 | 0.227234 | 1,455,438 | 773,304 | Sim |
| Bubble Sort | 100,000 | 0.009108 | 99,999 | 0 | Sim |
| Insertion Sort | 100,000 | 0.012498 | 99,999 | 0 | Sim |
| Merge Sort | 100,000 | 0.211996 | 853,904 | 1,668,928 | Sim |
| Quick Sort | 100,000 | 0.143710 | 1,600,016 | 846,100 | Sim |
| Heap Sort | 100,000 | 0.434111 | 3,112,517 | 1,650,854 | Sim |

## Cenário: Entrada Inversamente Ordenada

| Algoritmo | Tamanho (N) | Tempo Médio (s) | Comparações Médias | Trocas / Deslocamentos | Correto? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | 100 | 0.000624 | 4,950 | 4,950 | Sim |
| Selection Sort | 100 | 0.000303 | 4,950 | 50 | Sim |
| Insertion Sort | 100 | 0.000436 | 4,950 | 4,950 | Sim |
| Merge Sort | 100 | 0.000091 | 316 | 672 | Sim |
| Quick Sort | 100 | 0.000080 | 796 | 496 | Sim |
| Heap Sort | 100 | 0.000121 | 944 | 516 | Sim |
| Bubble Sort | 500 | 0.014581 | 124,750 | 124,750 | Sim |
| Selection Sort | 500 | 0.008545 | 124,750 | 250 | Sim |
| Insertion Sort | 500 | 0.014625 | 124,750 | 124,750 | Sim |
| Merge Sort | 500 | 0.000590 | 2,216 | 4,488 | Sim |
| Quick Sort | 500 | 0.000619 | 6,568 | 4,040 | Sim |
| Heap Sort | 500 | 0.000863 | 7,010 | 3,676 | Sim |
| Bubble Sort | 1,000 | 0.074323 | 499,500 | 499,500 | Sim |
| Selection Sort | 1,000 | 0.035512 | 499,500 | 500 | Sim |
| Insertion Sort | 1,000 | 0.049014 | 499,500 | 499,500 | Sim |
| Merge Sort | 1,000 | 0.002048 | 4,932 | 9,976 | Sim |
| Quick Sort | 1,000 | 0.001959 | 15,456 | 9,464 | Sim |
| Heap Sort | 1,000 | 0.002062 | 15,965 | 8,316 | Sim |
| Bubble Sort | 5,000 | 1.675500 | 12,497,500 | 12,497,500 | Sim |
| Selection Sort | 5,000 | 0.992630 | 12,497,500 | 2,500 | Sim |
| Insertion Sort | 5,000 | 1.350947 | 12,497,500 | 12,497,500 | Sim |
| Merge Sort | 5,000 | 0.010234 | 29,804 | 61,808 | Sim |
| Quick Sort | 5,000 | 0.011925 | 105,744 | 64,520 | Sim |
| Heap Sort | 5,000 | 0.017507 | 103,227 | 53,436 | Sim |
| Merge Sort | 10,000 | 0.021589 | 64,608 | 133,616 | Sim |
| Quick Sort | 10,000 | 0.026734 | 236,628 | 144,252 | Sim |
| Heap Sort | 10,000 | 0.035188 | 226,682 | 116,696 | Sim |
| Merge Sort | 50,000 | 0.111303 | 382,512 | 784,464 | Sim |
| Quick Sort | 50,000 | 0.146497 | 1,476,076 | 896,636 | Sim |
| Heap Sort | 50,000 | 0.211375 | 1,366,047 | 698,892 | Sim |
| Merge Sort | 100,000 | 0.237760 | 815,024 | 1,668,928 | Sim |
| Quick Sort | 100,000 | 0.317048 | 3,202,028 | 1,943,196 | Sim |
| Heap Sort | 100,000 | 0.481839 | 2,926,640 | 1,497,434 | Sim |

## Cenário: Entrada Parcialmente Ordenada

| Algoritmo | Tamanho (N) | Tempo Médio (s) | Comparações Médias | Trocas / Deslocamentos | Correto? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | 100 | 0.000421 | 4,884 | 337 | Sim |
| Selection Sort | 100 | 0.000302 | 4,950 | 5 | Sim |
| Insertion Sort | 100 | 0.000039 | 436 | 337 | Sim |
| Merge Sort | 100 | 0.000099 | 455 | 672 | Sim |
| Quick Sort | 100 | 0.000092 | 954 | 280 | Sim |
| Heap Sort | 100 | 0.000147 | 1,083 | 635 | Sim |
| Bubble Sort | 500 | 0.009186 | 124,579 | 9,341 | Sim |
| Selection Sort | 500 | 0.008061 | 124,750 | 25 | Sim |
| Insertion Sort | 500 | 0.000994 | 9,836 | 9,341 | Sim |
| Merge Sort | 500 | 0.000669 | 3,354 | 4,488 | Sim |
| Quick Sort | 500 | 0.000905 | 14,341 | 2,208 | Sim |
| Heap Sort | 500 | 0.001049 | 7,694 | 4,287 | Sim |
| Bubble Sort | 1,000 | 0.041172 | 496,419 | 31,076 | Sim |
| Selection Sort | 1,000 | 0.041205 | 499,500 | 50 | Sim |
| Insertion Sort | 1,000 | 0.002978 | 32,075 | 31,076 | Sim |
| Merge Sort | 1,000 | 0.001475 | 7,505 | 9,976 | Sim |
| Quick Sort | 1,000 | 0.001391 | 19,597 | 4,249 | Sim |
| Heap Sort | 1,000 | 0.002778 | 17,485 | 9,668 | Sim |
| Bubble Sort | 5,000 | 1.083842 | 12,452,650 | 754,256 | Sim |
| Selection Sort | 5,000 | 0.851214 | 12,497,500 | 250 | Sim |
| Insertion Sort | 5,000 | 0.080628 | 759,255 | 754,256 | Sim |
| Merge Sort | 5,000 | 0.009066 | 50,648 | 61,808 | Sim |
| Quick Sort | 5,000 | 0.006498 | 79,519 | 28,680 | Sim |
| Heap Sort | 5,000 | 0.015821 | 111,693 | 60,416 | Sim |
| Merge Sort | 10,000 | 0.020170 | 112,004 | 133,616 | Sim |
| Quick Sort | 10,000 | 0.017719 | 242,978 | 66,402 | Sim |
| Heap Sort | 10,000 | 0.032352 | 243,445 | 130,720 | Sim |
| Merge Sort | 50,000 | 0.127651 | 672,211 | 784,464 | Sim |
| Quick Sort | 50,000 | 0.086412 | 1,155,850 | 372,239 | Sim |
| Heap Sort | 50,000 | 0.196065 | 1,451,216 | 771,036 | Sim |
| Merge Sort | 100,000 | 0.249670 | 1,449,138 | 1,668,928 | Sim |
| Quick Sort | 100,000 | 0.192901 | 2,665,471 | 789,981 | Sim |
| Heap Sort | 100,000 | 0.426304 | 3,103,938 | 1,642,712 | Sim |

## Cenário: Objetos Customizados

| Algoritmo | Tamanho (N) | Tempo Médio (s) | Comparações Médias | Trocas / Deslocamentos | Correto? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | 100 | 0.000508 | 4,740 | 2,225 | Sim |
| Selection Sort | 100 | 0.000340 | 4,950 | 93 | Sim |
| Insertion Sort | 100 | 0.000249 | 2,320 | 2,225 | Sim |
| Merge Sort | 100 | 0.000114 | 534 | 672 | Sim |
| Quick Sort | 100 | 0.000078 | 645 | 408 | Sim |
| Heap Sort | 100 | 0.000150 | 1,031 | 587 | Sim |
| Bubble Sort | 500 | 0.012596 | 123,475 | 60,397 | Sim |
| Selection Sort | 500 | 0.008387 | 124,750 | 493 | Sim |
| Insertion Sort | 500 | 0.005660 | 60,891 | 60,397 | Sim |
| Merge Sort | 500 | 0.000750 | 3,851 | 4,488 | Sim |
| Quick Sort | 500 | 0.000480 | 4,563 | 2,409 | Sim |
| Heap Sort | 500 | 0.001012 | 7,451 | 4,062 | Sim |
| Bubble Sort | 1,000 | 0.055609 | 498,834 | 253,593 | Sim |
| Selection Sort | 1,000 | 0.033665 | 499,500 | 991 | Sim |
| Insertion Sort | 1,000 | 0.023231 | 254,587 | 253,593 | Sim |
| Merge Sort | 1,000 | 0.001612 | 8,707 | 9,976 | Sim |
| Quick Sort | 1,000 | 0.001043 | 10,163 | 5,594 | Sim |
| Heap Sort | 1,000 | 0.002282 | 16,834 | 9,059 | Sim |
| Bubble Sort | 5,000 | 1.405312 | 12,478,779 | 6,298,597 | Sim |
| Selection Sort | 5,000 | 0.866013 | 12,497,500 | 4,994 | Sim |
| Insertion Sort | 5,000 | 0.596708 | 6,303,588 | 6,298,597 | Sim |
| Merge Sort | 5,000 | 0.011839 | 55,273 | 61,808 | Sim |
| Quick Sort | 5,000 | 0.009195 | 65,138 | 32,575 | Sim |
| Heap Sort | 5,000 | 0.016073 | 107,652 | 57,089 | Sim |

