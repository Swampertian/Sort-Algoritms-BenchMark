import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.main import build_algorithms

from bench.random import generate_input as random_input
from bench.sorted import generate_input as sorted_input
from bench.reverse_sorted import generate_input as reverse_sorted_input

INPUT_SIZES = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]

INPUT_CASES: Dict[str, Callable[[int], List[int]]] = {
    "random": random_input,
    "sorted": sorted_input,
    "reverse_sorted": reverse_sorted_input,
}


def run_benchmarks(
    sizes: List[int] = INPUT_SIZES,
    cases: Dict[str, Callable[[int], List[int]]] = INPUT_CASES,
) -> List[Dict[str, Any]]:
    results = []
    for case_name, generator in cases.items():
        for size in sizes:
            base_input = generator(size)
            algorithms = build_algorithms()
            for algo_name, instance in algorithms.items():
                _, metrics = instance.sort(list(base_input), in_place=True)
                metrics["name"] = algo_name
                metrics["case"] = case_name
                results.append(metrics)
    return results


def _prompt_menu(title: str, options: List[Any], prompt_text: str) -> List[int]:
    print(title)
    for idx, option in enumerate(options, start=1):
        print(f"  [{idx}] {option}")
    print("  [0] todos")

    while True:
        raw = input(prompt_text).strip()
        if not raw:
            print("Entrada vazia. Tente novamente.")
            continue

        if raw == "0":
            return list(range(1, len(options) + 1))

        try:
            indices = {int(token) for token in raw.split(",")}
        except ValueError:
            print("Entrada inválida. Use apenas números separados por vírgula.")
            continue

        if not indices.issubset(range(1, len(options) + 1)):
            print(f"Escolha valores entre 1 e {len(options)} (ou 0 para todos).")
            continue

        return sorted(indices)


def input_selection(
    cases: Dict[str, Callable[[int], List[int]]] = INPUT_CASES,
    sizes: List[int] = INPUT_SIZES,
) -> Tuple[Dict[str, Callable[[int], List[int]]], List[int]]:
    """Interactive terminal menus to pick which input cases and sizes to benchmark."""
    case_names = list(cases.keys())
    case_indices = _prompt_menu(
        "Selecione os casos de entrada a testar:",
        case_names,
        "Digite os números separados por vírgula (ex: 1,3) ou 0: ",
    )
    selected_cases = {case_names[i - 1]: cases[case_names[i - 1]] for i in case_indices}

    size_indices = _prompt_menu(
        "Selecione o tamanho da entrada a testar:",
        sizes,
        "Digite os números separados por vírgula (ex: 1,3) ou 0: ",
    )
    selected_sizes = [sizes[i - 1] for i in size_indices]

    return selected_cases, selected_sizes

def print_results(results: List[Dict[str, Any]]) -> None:
    header = f"{'case':<16}{'algorithm':<15}{'size':>10}{'comparisons':>15}{'swaps':>15}{'time_taken':>15}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(
            f"{r['case']:<16}{r['algorithm']:<15}{r['size']:>10}"
            f"{r['comparisons']:>15}{r['swaps']:>15}{r['time_taken']:>15.6f}"
        )

if __name__ == "__main__":
    from bench.plot import GraphPlotter

    selected_cases, selected_sizes = input_selection()
    results = run_benchmarks(sizes=selected_sizes, cases=selected_cases)
    print_results(results)

    plotter = GraphPlotter(results)
    for path in plotter.plot_all():
        print(f"gerado: {path}")
