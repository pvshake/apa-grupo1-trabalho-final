#!/usr/bin/env python3
"""
Script principal para executar os algoritmos do projeto.

Este script permite testar e comparar diferentes algoritmos para
resolver o problema da substring de comprimento máximo.
"""

import sys
from typing import Iterable

from src.base.algorithm import Algorithm
from src.backtracking import BacktrackingAlgorithm
from src.brute_force import BruteForceAlgorithm
from src.divide_and_conquer import DivideAndConquerAlgorithm
from src.dynamic_programming import DynamicProgrammingAlgorithm
from src.greedy import GreedyAlgorithm
from src.heuristics import HeuristicAlgorithm
from src.utils import generate_test_cases


def _print_header():
    print("=" * 70)
    print("Trabalho Final de APA - String de Comprimento Máximo")
    print("=" * 70)
    print()


def _run_algorithm_suite(algorithms: Iterable[Algorithm], test_cases):
    for algorithm in algorithms:
        print(f"Testando algoritmo: {algorithm.name}")
        print("-" * 70)
        print(f"{'String de Entrada':<30} | {'Resultado':<20} | {'Tempo (s)':<12}")
        print("-" * 70)

        for test_string, expected_length in test_cases:
            display_string = test_string if len(test_string) <= 25 else test_string[:22] + "..."
            result = algorithm.solve(test_string)
            status = "✓" if result.length == expected_length else "✗"
            time_str = f"{result.execution_time:.6f}" if result.execution_time else "N/A"

            print(f"{display_string:<30} | {result.substring:<20} | {time_str:<12} {status}")
            if result.instruction_count is not None:
                print(f"  └─ Comprimento: {result.length} | Instruções: {result.instruction_count:,}")

        print("-" * 70)
        print()


def _run_custom_string(algorithms: Iterable[Algorithm], user_string: str):
    print(f"Testando string personalizada: '{user_string}'")
    for algorithm in algorithms:
        result = algorithm.solve(user_string)
        print(f"→ {algorithm.name}: {result}")
    print()


def main():
    """Função principal do programa."""
    _print_header()

    algorithms = [
        BruteForceAlgorithm(count_instructions=True),
        BacktrackingAlgorithm(count_instructions=True),
        DivideAndConquerAlgorithm(count_instructions=True),
        DynamicProgrammingAlgorithm(count_instructions=True),
        GreedyAlgorithm(count_instructions=True),
        HeuristicAlgorithm(count_instructions=True),
    ]
    test_cases = generate_test_cases()

    _run_algorithm_suite(algorithms, test_cases)

    if len(sys.argv) > 1:
        _run_custom_string(algorithms, sys.argv[1])

    print("Para testar uma string personalizada, execute:")
    print("  python main.py 'sua_string_aqui'")
    print()


if __name__ == "__main__":
    main()

