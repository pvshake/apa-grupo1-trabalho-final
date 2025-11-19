#!/usr/bin/env python3
"""
Script para coletar métricas de desempenho de todas as implementações.

Gera dois arquivos:
1. results/performance_summary.json  -> dados brutos
2. results/performance_summary.md    -> resumo tabular
"""

from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path
from typing import Dict, List, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.backtracking import BacktrackingAlgorithm
from src.brute_force import BruteForceAlgorithm
from src.divide_and_conquer import DivideAndConquerAlgorithm
from src.dynamic_programming import DynamicProgrammingAlgorithm
from src.greedy import GreedyAlgorithm
from src.heuristics import HeuristicAlgorithm
from src.utils import generate_test_cases

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def format_float(value: float) -> float:
    """Arredonda números em segundos para 6 casas (para consistência)."""
    return round(value, 6)


def collect_metrics() -> Dict[str, Dict]:
    test_cases: List[Tuple[str, int]] = generate_test_cases()
    algorithms = [
        BruteForceAlgorithm(count_instructions=True),
        BacktrackingAlgorithm(count_instructions=True),
        DivideAndConquerAlgorithm(count_instructions=True),
        DynamicProgrammingAlgorithm(count_instructions=True),
        GreedyAlgorithm(count_instructions=True),
        HeuristicAlgorithm(count_instructions=True),
    ]

    metrics: Dict[str, Dict] = {}

    for algorithm in algorithms:
        algo_name = algorithm.name
        algo_metrics = {
            "cases": [],
            "average_time": 0.0,
            "average_instructions": 0.0,
            "max_length_observed": 0,
            "all_passed": True,
        }
        times: List[float] = []
        instructions: List[int] = []

        for input_str, expected_length in test_cases:
            result = algorithm.solve(input_str)
            times.append(result.execution_time or 0.0)
            instructions.append(result.instruction_count or 0)

            algo_metrics["cases"].append(
                {
                    "input_preview": input_str if len(input_str) <= 50 else input_str[:47] + "...",
                    "input_length": len(input_str),
                    "expected_length": expected_length,
                    "output_length": result.length,
                    "substring": result.substring if len(result.substring) <= 50 else result.substring[:47] + "...",
                    "execution_time": format_float(result.execution_time or 0.0),
                    "instruction_count": result.instruction_count,
                    "passed": result.length == expected_length,
                }
            )

            algo_metrics["max_length_observed"] = max(algo_metrics["max_length_observed"], result.length)
            if result.length != expected_length:
                algo_metrics["all_passed"] = False

        algo_metrics["average_time"] = format_float(statistics.mean(times))
        algo_metrics["average_instructions"] = int(statistics.mean(instructions))
        metrics[algo_name] = algo_metrics

    return metrics


def save_json(metrics: Dict[str, Dict]) -> Path:
    output_path = RESULTS_DIR / "performance_summary.json"
    with output_path.open("w", encoding="utf-8") as fp:
        json.dump(metrics, fp, indent=2, ensure_ascii=False)
    return output_path


def save_markdown(metrics: Dict[str, Dict]) -> Path:
    output_path = RESULTS_DIR / "performance_summary.md"
    header = "| Algoritmo | Tempo Médio (ms) | Instruções Médias | Maior Substring | Testes OK |\n"
    header += "|-----------|-----------------|-------------------|-----------------|-----------|\n"

    rows = []
    for name, data in metrics.items():
        rows.append(
            f"| {name} | {data['average_time'] * 1000:.3f} | "
            f"{data['average_instructions']:,} | {data['max_length_observed']} | "
            f"{'✅' if data['all_passed'] else '❌'} |"
        )

    ranking = sorted(metrics.items(), key=lambda item: item[1]["average_time"])
    ranking_lines = ["\n## Ranking por Tempo Médio (melhor → pior)\n"]
    for idx, (name, data) in enumerate(ranking, start=1):
        ranking_lines.append(f"{idx}. {name} — {data['average_time'] * 1000:.3f} ms")

    with output_path.open("w", encoding="utf-8") as fp:
        fp.write("# Resumo de Performance\n\n")
        fp.write(header)
        fp.write("\n".join(rows))
        fp.write("\n")
        fp.write("\n".join(ranking_lines))
        fp.write("\n")

    return output_path


def main():
    metrics = collect_metrics()
    json_path = save_json(metrics)
    md_path = save_markdown(metrics)
    print(f"✅ Resumo salvo em: {json_path}")
    print(f"✅ Tabela salva em: {md_path}")


if __name__ == "__main__":
    main()


