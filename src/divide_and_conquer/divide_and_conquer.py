"""
Estratégia de Divisão e Conquista para encontrar a substring de comprimento
máximo sem repetição.

Complexidade Temporal: O(n log n) graças à divisão recursiva da string e à
combinação linear nos passos de junção.
Complexidade Espacial: O(log n) devido à pilha de recursão (sem contar as
strings resultantes utilizadas para comparação).
"""

import time
from typing import Dict, Tuple

from ..base.algorithm import Algorithm, AlgorithmResult


class DivideAndConquerAlgorithm(Algorithm):
    """
    Divide a string em duas metades, resolve o problema em cada parte e
    combina os resultados considerando substrings que atravessam o ponto
    médio.
    """

    def __init__(self, count_instructions: bool = False):
        super().__init__("Divisão e Conquista (Divide and Conquer)")
        self.count_instructions = count_instructions
        self._instruction_count = 0

    def _max_crossing_substring(self, segment: str, mid: int) -> Tuple[str, int]:
        """Calcula a melhor substring que cruza o ponto médio."""
        if mid == 0 or mid == len(segment):
            return "", 0

        last_seen: Dict[str, int] = {}
        left_ptr = 0
        best_length = 0
        best_substring = ""

        for right_ptr, char in enumerate(segment):
            if self.count_instructions:
                self._instruction_count += 1  # Iteração do loop cruzado

            if char in last_seen and last_seen[char] >= left_ptr:
                left_ptr = last_seen[char] + 1
                if self.count_instructions:
                    self._instruction_count += 1  # Ajuste do ponteiro esquerdo

            last_seen[char] = right_ptr

            if left_ptr <= mid - 1 <= right_ptr:
                current_length = right_ptr - left_ptr + 1
                if current_length > best_length:
                    best_length = current_length
                    best_substring = segment[left_ptr : right_ptr + 1]
                    if self.count_instructions:
                        self._instruction_count += 1  # Atualização do melhor cruzamento

            if left_ptr > mid - 1:
                # Não é mais possível formar substrings cruzando o meio
                break

        return best_substring, best_length

    def _solve_recursive(self, segment: str) -> Tuple[str, int]:
        """Resolve recursivamente o problema para um segmento."""
        if self.count_instructions:
            self._instruction_count += 1  # Chamada recursiva

        n = len(segment)
        if n <= 1:
            return segment, n

        mid = n // 2
        left_substring, left_length = self._solve_recursive(segment[:mid])
        right_substring, right_length = self._solve_recursive(segment[mid:])
        cross_substring, cross_length = self._max_crossing_substring(segment, mid)

        if self.count_instructions:
            self._instruction_count += 3  # Comparações de comprimento

        if left_length >= right_length and left_length >= cross_length:
            return left_substring, left_length
        if right_length >= left_length and right_length >= cross_length:
            return right_substring, right_length
        return cross_substring, cross_length

    def solve(self, s: str) -> AlgorithmResult:
        """
        Executa a estratégia de divisão e conquista sobre a string informada.
        """
        if not s:
            return AlgorithmResult(substring="", length=0)

        if self.count_instructions:
            self._instruction_count = 0
            self._instruction_count += 1  # Verificação de string vazia

        start_time = time.time()
        best_substring, best_length = self._solve_recursive(s)
        execution_time = time.time() - start_time

        result = AlgorithmResult(
            substring=best_substring,
            length=best_length,
            execution_time=execution_time,
        )

        if self.count_instructions:
            result.instruction_count = self._instruction_count

        return result


