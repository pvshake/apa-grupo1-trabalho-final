"""
Implementação de um algoritmo guloso (Greedy) para encontrar a substring de
comprimento máximo sem caracteres repetidos.

Complexidade Temporal: O(n) no pior caso, mas com possíveis incrementos
locais devido à remoção caracter a caracter da janela.
Complexidade Espacial: O(min(n, m)) para armazenar os caracteres da janela.
"""

import time
from typing import Set

from ..base.algorithm import Algorithm, AlgorithmResult


class GreedyAlgorithm(Algorithm):
    """
    Mantém uma janela deslizante que é expandida ao encontrar caracteres
    inéditos e encolhida de forma gulosa (um caractere por vez) quando ocorre
    repetição. Essa estratégia prioriza decisões locais rápidas que levam a
    uma solução global ótima.
    """

    def __init__(self, count_instructions: bool = False):
        super().__init__("Algoritmo Guloso (Greedy)")
        self.count_instructions = count_instructions
        self._instruction_count = 0

    def solve(self, s: str) -> AlgorithmResult:
        if not s:
            return AlgorithmResult(substring="", length=0)

        if self.count_instructions:
            self._instruction_count = 0
            self._instruction_count += 1  # Verificação de string vazia

        start_time = time.time()

        window_chars: Set[str] = set()
        left = 0
        best_length = 0
        best_start = 0

        for right, char in enumerate(s):
            if self.count_instructions:
                self._instruction_count += 1  # Iteração principal

            while char in window_chars:
                if self.count_instructions:
                    self._instruction_count += 1  # Remoção gulosa
                window_chars.remove(s[left])
                left += 1

            window_chars.add(char)
            if self.count_instructions:
                self._instruction_count += 1  # Inserção na janela

            current_length = right - left + 1
            if current_length > best_length:
                best_length = current_length
                best_start = left
                if self.count_instructions:
                    self._instruction_count += 1  # Atualização do melhor valor

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


