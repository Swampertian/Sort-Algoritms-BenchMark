### Classe para plotar a saida

from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

CHARTS_DIR = Path(__file__).resolve().parent / "charts"


class GraphPlotter:

    def __init__(self, results: List[Dict[str, Any]], output_dir: Path = CHARTS_DIR):
        self.results = results
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._by_case: Dict[str, Dict[str, Dict[int, Dict[str, Any]]]] = defaultdict(
            lambda: defaultdict(dict)
        )
        for r in results:
            self._by_case[r["case"]][r["algorithm"]][r["size"]] = r

    def _cases(self) -> List[str]:
        return sorted(self._by_case.keys())

    def _line_chart(self, case: str, metric: str, ylabel: str, filename: str) -> Path:
        fig, ax = plt.subplots(figsize=(8, 5))
        for algorithm, by_size in sorted(self._by_case[case].items()):
            sizes = sorted(by_size.keys())
            values = [by_size[s][metric] for s in sizes]
            ax.plot(sizes, values, marker="o", label=algorithm)

        ax.set_title(f"{ylabel} vs. tamanho da entrada ({case})")
        ax.set_xlabel("Tamanho da entrada (n)")
        ax.set_ylabel(ylabel)
        ax.legend()
        ax.grid(True, alpha=0.3)

        path = self.output_dir / filename
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        return path

    def plot_time_vs_size(self, case: str) -> Path:
        return self._line_chart(case, "time_taken", "Tempo (s)", f"time_comparison_{case}.png")

    def plot_comparisons_vs_size(self, case: str) -> Path:
        return self._line_chart(case, "comparisons", "Comparações", f"comparisons_vs_size_{case}.png")

    def plot_swaps_vs_size(self, case: str) -> Path:
        return self._line_chart(case, "swaps", "Trocas/atribuições", f"swaps_vs_size_{case}.png")

    def plot_overall_bar(self, size: int) -> Path:
        """Bar chart comparing every algorithm's time_taken at a single size, across cases."""
        cases = self._cases()
        algorithms = sorted({r["algorithm"] for r in self.results})

        fig, ax = plt.subplots(figsize=(10, 6))
        bar_width = 0.8 / max(len(cases), 1)
        x = range(len(algorithms))

        for i, case in enumerate(cases):
            values = [self._by_case[case].get(algo, {}).get(size, {}).get("time_taken", 0.0) for algo in algorithms]
            offsets = [xi + i * bar_width for xi in x]
            ax.bar(offsets, values, width=bar_width, label=case)

        ax.set_title(f"Comparação geral de tempo (n = {size})")
        ax.set_xlabel("Algoritmo")
        ax.set_ylabel("Tempo (s)")
        ax.set_xticks([xi + bar_width * (len(cases) - 1) / 2 for xi in x])
        ax.set_xticklabels(algorithms, rotation=30, ha="right")
        ax.legend(title="Caso")
        ax.grid(True, axis="y", alpha=0.3)

        path = self.output_dir / "overall_comparison_bar.png"
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        return path

    def plot_all(self) -> List[Path]:
        """Generates the full set of charts for every case present in the results."""
        paths = []
        for case in self._cases():
            paths.append(self.plot_time_vs_size(case))
            paths.append(self.plot_comparisons_vs_size(case))
            paths.append(self.plot_swaps_vs_size(case))

        all_sizes = sorted({r["size"] for r in self.results})
        if all_sizes:
            paths.append(self.plot_overall_bar(all_sizes[-1]))

        return paths
