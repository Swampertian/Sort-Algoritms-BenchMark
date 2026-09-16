"""
Sorting Algorithms Benchmark Suite
Executes performance tests with multiple runs per scenario, averages metrics,
exports datasets, and creates visualization charts.
"""
import copy
import os
import sys
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

import matplotlib.pyplot as plt

# Ensure root workspace directory is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.bubble.bubble_sort import bubble_sort
from src.selection.selection_sort import selection_sort
from src.insertion.insertion_sort import insertion_sort
from src.merge.merge_sort import merge_sort
from src.quick.quick_sort import quick_sort
from src.heap.heap_sort import heap_sort

from bench.utilts import (
    BenchmarkItem,
    generate_random_integers,
    generate_sorted_integers,
    generate_reverse_sorted_integers,
    generate_nearly_sorted_integers,
    generate_duplicate_integers,
    generate_custom_objects,
    verify_sorted,
    save_results_to_json,
    save_results_to_csv,
)

ALGORITHMS = [
    ("Bubble Sort", bubble_sort, "O(n^2)"),
    ("Selection Sort", selection_sort, "O(n^2)"),
    ("Insertion Sort", insertion_sort, "O(n^2)"),
    ("Merge Sort", merge_sort, "O(n log n)"),
    ("Quick Sort", quick_sort, "O(n log n)"),
    ("Heap Sort", heap_sort, "O(n log n)"),
]

SIZES = [100, 500, 1000, 5000, 10000, 50000, 100000]
QUADRATIC_MAX_SIZE = 5000
NUM_RUNS = 3  # Multiple executions per experiment for statistical robustness


def run_benchmark_with_averaging(
    name: str,
    sort_fn: Callable,
    data_generator: Callable[[], List[Any]],
    runs: int = NUM_RUNS,
    key: Optional[Callable[[Any], Any]] = None,
) -> Dict[str, Any]:
    """Runs an experiment multiple times and returns the average metrics."""
    times = []
    comparisons_list = []
    swaps_list = []
    is_valid_all = True

    for _ in range(runs):
        data = data_generator()
        data_copy = list(data)
        sorted_res, metrics = sort_fn(data_copy, key=key, in_place=True)
        if not verify_sorted(sorted_res, key=key):
            is_valid_all = False
        times.append(metrics["time_taken"])
        comparisons_list.append(metrics["comparisons"])
        swaps_list.append(metrics["swaps"])

    avg_time = sum(times) / len(times)
    avg_comps = int(sum(comparisons_list) / len(comparisons_list))
    avg_swaps = int(sum(swaps_list) / len(swaps_list))

    return {
        "time_taken": avg_time,
        "comparisons": avg_comps,
        "swaps": avg_swaps,
        "is_valid": is_valid_all,
        "runs": runs,
    }


def run_benchmarks() -> List[Dict[str, Any]]:
    """Runs the complete benchmark suite across distributions and sizes."""
    all_results = []
    print("=" * 80, flush=True)
    print(f"  SORTING ALGORITHMS BENCHMARK SUITE ({NUM_RUNS} EXECUÇÕES POR TESTE)", flush=True)
    print("=" * 80, flush=True)

    scenarios = [
        ("Entrada Aleatória", "Random Numbers", lambda n: generate_random_integers(n, seed=42 + n)),
        ("Entrada Já Ordenada", "Already Sorted", lambda n: generate_sorted_integers(n)),
        ("Entrada Inversamente Ordenada", "Reverse Sorted", lambda n: generate_reverse_sorted_integers(n)),
        ("Entrada Parcialmente Ordenada", "Nearly Sorted", lambda n: generate_nearly_sorted_integers(n, swap_ratio=0.05, seed=100 + n)),
    ]

    for scenario_label, itype, gen_fn in scenarios:
        print(f"\n--- Cenário: {scenario_label} ---", flush=True)
        for n in SIZES:
            for name, fn, comp_class in ALGORITHMS:
                # Limit quadratic algorithms on large inputs to avoid excessive delay
                if comp_class == "O(n^2)" and n > QUADRATIC_MAX_SIZE:
                    if not (itype == "Already Sorted" and (name == "Insertion Sort" or name == "Bubble Sort")):
                        continue

                metrics = run_benchmark_with_averaging(
                    name=name,
                    sort_fn=fn,
                    data_generator=lambda: gen_fn(n),
                    runs=NUM_RUNS,
                )

                entry = {
                    "algorithm": name,
                    "scenario": scenario_label,
                    "input_type": itype,
                    "size": n,
                    "time_seconds": round(metrics["time_taken"], 6),
                    "comparisons": metrics["comparisons"],
                    "swaps": metrics["swaps"],
                    "runs": metrics["runs"],
                    "is_valid": metrics["is_valid"],
                }
                all_results.append(entry)
                print(f"[{entry['algorithm']:<14}] {scenario_label:<28} (n={n:<6}): "
                      f"Tempo Médio: {entry['time_seconds']:>8.5f}s | "
                      f"Comps: {entry['comparisons']:>10} | Swaps: {entry['swaps']:>10}", flush=True)

    # Custom Objects Benchmark
    print("\n--- Cenário Especial: Objetos Customizados (Entrada Aleatória) ---", flush=True)
    for n in [100, 500, 1000, 5000]:
        for name, fn, comp_class in ALGORITHMS:
            metrics = run_benchmark_with_averaging(
                name=name,
                sort_fn=fn,
                data_generator=lambda: generate_custom_objects(n, seed=300 + n),
                runs=NUM_RUNS,
                key=lambda obj: obj.val,
            )
            entry = {
                "algorithm": name,
                "scenario": "Objetos Customizados",
                "input_type": "Custom Objects",
                "size": n,
                "time_seconds": round(metrics["time_taken"], 6),
                "comparisons": metrics["comparisons"],
                "swaps": metrics["swaps"],
                "runs": metrics["runs"],
                "is_valid": metrics["is_valid"],
            }
            all_results.append(entry)
            print(f"[{entry['algorithm']:<14}] Objetos Customizados (n={n:<6}): "
                  f"Tempo Médio: {entry['time_seconds']:>8.5f}s | "
                  f"Comps: {entry['comparisons']:>10} | Swaps: {entry['swaps']:>10}", flush=True)

    return all_results


def generate_markdown_summary(results: List[Dict[str, Any]], filepath: str) -> None:
    """Generates a structured markdown summary report."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# Relatório de Desempenho dos Algoritmos de Ordenação\n\n")
        f.write(f"Os valores representam a **média aritmética de {NUM_RUNS} execuções independentes** para cada configuração.\n\n")

        scenarios = ["Entrada Aleatória", "Entrada Já Ordenada", "Entrada Inversamente Ordenada", "Entrada Parcialmente Ordenada", "Objetos Customizados"]
        for scen in scenarios:
            sub_results = [r for r in results if r["scenario"] == scen]
            if not sub_results:
                continue
            f.write(f"## Cenário: {scen}\n\n")
            f.write("| Algoritmo | Tamanho (N) | Tempo Médio (s) | Comparações Médias | Trocas / Deslocamentos | Correto? |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            for r in sub_results:
                f.write(f"| {r['algorithm']} | {r['size']:,} | {r['time_seconds']:.6f} | {r['comparisons']:,} | {r['swaps']:,} | {'Sim' if r['is_valid'] else 'Não'} |\n")
            f.write("\n")


def generate_charts(results: List[Dict[str, Any]], charts_dir: str) -> None:
    """Generates analytical charts and saves them as high resolution PNGs."""
    os.makedirs(charts_dir, exist_ok=True)

    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    colors = {
        "Bubble Sort": "#E63946",
        "Selection Sort": "#F4A261",
        "Insertion Sort": "#E76F51",
        "Merge Sort": "#2A9D8F",
        "Quick Sort": "#1D3557",
        "Heap Sort": "#457B9D",
    }

    def plot_time_curve(scenario: str, filename: str, title: str):
        plt.figure(figsize=(10, 6), dpi=300)
        data_type_results = [r for r in results if r["scenario"] == scenario]

        for alg_name in colors.keys():
            alg_data = [r for r in data_type_results if r["algorithm"] == alg_name]
            if not alg_data:
                continue
            sizes = [r["size"] for r in alg_data]
            times = [r["time_seconds"] for r in alg_data]
            plt.plot(sizes, times, marker="o", label=alg_name, color=colors[alg_name], linewidth=2.2, markersize=5.5)

        plt.title(title, fontsize=14, fontweight="bold", pad=15)
        plt.xlabel("Tamanho da Entrada (N)", fontsize=12)
        plt.ylabel("Tempo Médio de Execução (s - Escala Logarítmica)", fontsize=12)
        plt.yscale("log")
        plt.legend(frameon=True, fontsize=10, loc="upper left")
        plt.tight_layout()
        plt.savefig(os.path.join(charts_dir, filename))
        plt.close()

    # 1. Random Numbers Time Curve
    plot_time_curve("Entrada Aleatória", "time_comparison_random.png", "Tempo de Execução vs Tamanho (Entrada Aleatória)")

    # 2. Already Sorted Time Curve
    plot_time_curve("Entrada Já Ordenada", "time_comparison_sorted.png", "Tempo de Execução vs Tamanho (Entrada Já Ordenada)")

    # 3. Reverse Sorted Time Curve
    plot_time_curve("Entrada Inversamente Ordenada", "time_comparison_reverse.png", "Tempo de Execução vs Tamanho (Entrada Invertida)")

    # 4. Nearly Sorted Time Curve
    plot_time_curve("Entrada Parcialmente Ordenada", "time_comparison_nearly_sorted.png", "Tempo de Execução vs Tamanho (Entrada Parcialmente Ordenada - 5% swaps)")

    # 5. Comparisons vs Size (Random Numbers)
    plt.figure(figsize=(10, 6), dpi=300)
    for alg_name in colors.keys():
        alg_data = [r for r in results if r["scenario"] == "Entrada Aleatória" and r["algorithm"] == alg_name]
        if not alg_data:
            continue
        sizes = [r["size"] for r in alg_data]
        comps = [r["comparisons"] for r in alg_data]
        plt.plot(sizes, comps, marker="s", label=alg_name, color=colors[alg_name], linewidth=2, markersize=5)

    plt.yscale("log")
    plt.title("Número de Comparações vs Tamanho da Entrada (Aleatória)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Tamanho da Entrada (N)", fontsize=12)
    plt.ylabel("Comparações Médias (Escala Logarítmica)", fontsize=12)
    plt.legend(frameon=True, fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "comparisons_vs_size.png"))
    plt.close()

    # 6. Swaps vs Size (Random Numbers)
    plt.figure(figsize=(10, 6), dpi=300)
    for alg_name in colors.keys():
        alg_data = [r for r in results if r["scenario"] == "Entrada Aleatória" and r["algorithm"] == alg_name]
        if not alg_data:
            continue
        sizes = [r["size"] for r in alg_data]
        swaps = [r["swaps"] for r in alg_data]
        plt.plot(sizes, swaps, marker="^", label=alg_name, color=colors[alg_name], linewidth=2, markersize=5)

    plt.yscale("log")
    plt.title("Número de Trocas / Movimentações vs Tamanho da Entrada (Aleatória)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Tamanho da Entrada (N)", fontsize=12)
    plt.ylabel("Trocas / Movimentações Médias (Escala Logarítmica)", fontsize=12)
    plt.legend(frameon=True, fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "swaps_vs_size.png"))
    plt.close()

    # 7. Primitives vs Custom Objects Comparison (N=5,000)
    plt.figure(figsize=(11, 6), dpi=300)
    algs = list(colors.keys())
    x = range(len(algs))
    width = 0.35

    prim_times = []
    obj_times = []
    for alg in algs:
        p = next((r["time_seconds"] for r in results if r["algorithm"] == alg and r["scenario"] == "Entrada Aleatória" and r["size"] == 5000), 0)
        o = next((r["time_seconds"] for r in results if r["algorithm"] == alg and r["scenario"] == "Objetos Customizados" and r["size"] == 5000), 0)
        prim_times.append(p)
        obj_times.append(o)

    plt.bar([i - width/2 for i in x], prim_times, width=width, label="Array de Inteiros (N=5.000)", color="#457B9D")
    plt.bar([i + width/2 for i in x], obj_times, width=width, label="Array de Objetos (N=5.000)", color="#E76F51")
    plt.title("Comparativo de Desempenho: Inteiros vs Objetos Customizados (N=5.000)", fontsize=13, fontweight="bold", pad=15)
    plt.xticks(x, algs, rotation=15, ha="right", fontsize=10)
    plt.ylabel("Tempo Médio de Execução (s)", fontsize=12)
    plt.legend(frameon=True, fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "primitives_vs_objects.png"))
    plt.close()

    # 8. Overall Grouped Bar Comparison for N=5,000
    plt.figure(figsize=(12, 6), dpi=300)
    n5k_data = [r for r in results if r["size"] == 5000 and r["scenario"] == "Entrada Aleatória"]
    if n5k_data:
        names = [r["algorithm"] for r in n5k_data]
        times = [r["time_seconds"] for r in n5k_data]
        bar_colors = [colors.get(name, "#333333") for name in names]
        bars = plt.bar(names, times, color=bar_colors, width=0.55)
        plt.title("Tempo Médio de Execução para N = 5.000 Elementos Aleatórios (3 execuções)", fontsize=14, fontweight="bold", pad=15)
        plt.ylabel("Tempo Médio (segundos)", fontsize=12)
        plt.xticks(rotation=15, ha="right", fontsize=11)
        for bar, t in zip(bars, times):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (max(times)*0.01), f"{t:.4f}s", ha='center', va='bottom', fontsize=9, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(charts_dir, "overall_comparison_bar.png"))
        plt.close()


def main():
    results = run_benchmarks()

    res_dir = os.path.join(BASE_DIR, "bench", "results")
    json_path = os.path.join(res_dir, "benchmark_results.json")
    csv_path = os.path.join(res_dir, "benchmark_results.csv")
    summary_path = os.path.join(res_dir, "summary.md")
    charts_dir = os.path.join(BASE_DIR, "bench", "charts")

    print(f"\nSalvando resultados em JSON: {json_path}", flush=True)
    save_results_to_json(results, json_path)

    print(f"Salvando resultados em CSV: {csv_path}", flush=True)
    save_results_to_csv(results, csv_path)

    print(f"Gerando relatório Markdown: {summary_path}", flush=True)
    generate_markdown_summary(results, summary_path)

    print(f"Gerando gráficos em: {charts_dir}", flush=True)
    generate_charts(results, charts_dir)

    print("\n[SUCESSO] Benchmark multi-execuções finalizado com sucesso!", flush=True)


if __name__ == "__main__":
    main()
