"""
Implementação heurística/aproximada para encontrar a substring de comprimento
máximo sem caracteres repetidos.

Complexidade Temporal: O(n) em média, graças a heurísticas de salto e parada
antecipada.
Complexidade Espacial: O(min(n, m)) para armazenar últimas ocorrências.
"""

import time
from typing import Dict

from ..base.algorithm import Algorithm, AlgorithmResult


class HeuristicAlgorithm(Algorithm):
    """
    Aplica duas heurísticas principais:
      1. **Jump heuristic**: ao detectar um caractere repetido, pula
         diretamente para a posição seguinte à sua última ocorrência.
      2. **Early stopping**: encerra a busca quando o tamanho restante da
         string não é suficiente para superar o melhor resultado atual.
    O algoritmo mantém a corretude, mas favorece saltos maiores e saídas
    antecipadas para acelerar execuções em strings longas.
    """

    def __init__(self, count_instructions: bool = False):
        super().__init__("Heurístico / Aproximação")
        self.count_instructions = count_instructions
        self._instruction_count = 0

    def solve(self, s: str) -> AlgorithmResult:
        if not s:
            return AlgorithmResult(substring="", length=0)

        if self.count_instructions:
            self._instruction_count = 0
            self._instruction_count += 1  # Verificação de string vazia

        start_time = time.time()

        last_seen: Dict[str, int] = {}
        left = 0
        best_length = 0
        best_start = 0

        for right, char in enumerate(s):
            if self.count_instructions:
                self._instruction_count += 1  # Iteração principal

            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
                if self.count_instructions:
                    self._instruction_count += 1  # Salto heurístico

            last_seen[char] = right

            current_length = right - left + 1
            if current_length > best_length:
                best_length = current_length
                best_start = left
                if self.count_instructions:
                    self._instruction_count += 1  # Atualização do melhor valor

            remaining = len(s) - left
            if remaining <= best_length:
                if self.count_instructions:
                    self._instruction_count += 1  # Avaliação de parada
                break

        best_substring = s[best_start : best_start + best_length]
        execution_time = time.time() - start_time

        result = AlgorithmResult(
            substring=best_substring,
            length=best_length,
            execution_time=execution_time,
        )

        if self.count_instructions:
            result.instruction_count = self._instruction_count

        return result


