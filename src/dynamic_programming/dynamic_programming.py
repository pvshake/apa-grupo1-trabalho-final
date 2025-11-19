"""
Implementação baseada em Programação Dinâmica para encontrar a substring de
comprimento máximo sem caracteres repetidos.

Complexidade Temporal: O(n) graças ao reaproveitamento de resultados
intermediários (estados dp) e mapeamento das últimas ocorrências.
Complexidade Espacial: O(n) para o vetor de estados e O(m) para o dicionário
de ocorrências (m = tamanho do alfabeto observado).
"""

import time
from typing import Dict, List

from ..base.algorithm import Algorithm, AlgorithmResult


class DynamicProgrammingAlgorithm(Algorithm):
    """
    Utiliza um vetor de estados `dp[i]` que representa o comprimento da maior
    substring válida terminando na posição `i`. O algoritmo compara o estado
    anterior com a distância até a última ocorrência do caractere atual, o que
    permite decidir rapidamente o novo comprimento máximo.
    """

    def __init__(self, count_instructions: bool = False):
        super().__init__("Programação Dinâmica (Dynamic Programming)")
        self.count_instructions = count_instructions
        self._instruction_count = 0

    def solve(self, s: str) -> AlgorithmResult:
        """
        Resolve o problema utilizando programação dinâmica.
        """
        if not s:
            return AlgorithmResult(substring="", length=0)

        if self.count_instructions:
            self._instruction_count = 0
            self._instruction_count += 1  # Verificação de string vazia

        start_time = time.time()

        last_seen: Dict[str, int] = {}
        dp: List[int] = [0] * len(s)
        best_length = 0
        best_start = 0
        current_start = 0

        for i, char in enumerate(s):
            if self.count_instructions:
                self._instruction_count += 1  # Iteração principal

            prev_index = last_seen.get(char, -1)
            if prev_index >= current_start:
                current_start = prev_index + 1
                if self.count_instructions:
                    self._instruction_count += 1  # Ajuste do início

            dp[i] = i - current_start + 1
            last_seen[char] = i
            if self.count_instructions:
                self._instruction_count += 2  # Escritas em dp e last_seen

            if dp[i] > best_length:
                best_length = dp[i]
                best_start = current_start
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


