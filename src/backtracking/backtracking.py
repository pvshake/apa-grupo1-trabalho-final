"""
Implementação do algoritmo de Backtracking para a substring de comprimento
máximo sem caracteres repetidos.

Complexidade Temporal: O(n²) nos piores casos devido às explorações
contíguas iniciadas em cada posição.
Complexidade Espacial: O(n) para a pilha de recursão e estrutura de apoio.
"""

import time
from typing import List, Set

from ..base.algorithm import Algorithm, AlgorithmResult


class BacktrackingAlgorithm(Algorithm):
    """
    Uso de backtracking para construir substrings contíguas únicas.

    Para cada posição inicial da string, o algoritmo tenta estender a
    substring atual enquanto não encontrar caracteres repetidos. Ao detectar
    uma repetição, ele retrocede (backtrack) para testar novas possibilidades.
    """

    def __init__(self, count_instructions: bool = False):
        """
        Args:
            count_instructions: ativa a contagem de instruções para análise.
        """
        super().__init__("Backtracking")
        self.count_instructions = count_instructions
        self._instruction_count = 0
        self._best_substring: str = ""

    def _update_best(self, current_chars: List[str]) -> None:
        """Mantém o registro do melhor resultado encontrado até o momento."""
        if not current_chars:
            return
        candidate = "".join(current_chars)
        if len(candidate) > len(self._best_substring):
            self._best_substring = candidate
            if self.count_instructions:
                self._instruction_count += 1  # Atualização do melhor valor

    def _explore(self, s: str, index: int, current_chars: List[str], used: Set[str]) -> None:
        """
        Explora recursivamente uma substring contígua a partir de `index`.

        Args:
            s: string original.
            index: posição atual a ser avaliada.
            current_chars: caracteres da substring construída até o momento.
            used: conjunto de caracteres já utilizados na substring atual.
        """
        if self.count_instructions:
            self._instruction_count += 1  # Chamada recursiva / verificação de limite

        if index >= len(s):
            self._update_best(current_chars)
            return

        char = s[index]
        if self.count_instructions:
            self._instruction_count += 1  # Leitura de caractere

        if char in used:
            if self.count_instructions:
                self._instruction_count += 1  # Detecção de repetição
            self._update_best(current_chars)
            return

        used.add(char)
        current_chars.append(char)
        if self.count_instructions:
            self._instruction_count += 2  # Inserções em estruturas auxiliares

        self._update_best(current_chars)
        self._explore(s, index + 1, current_chars, used)

        # Backtrack
        removed_char = current_chars.pop()
        used.remove(removed_char)
        if self.count_instructions:
            self._instruction_count += 2  # Remoções ao retroceder

    def solve(self, s: str) -> AlgorithmResult:
        """
        Resolve o problema utilizando backtracking.

        Args:
            s: string de entrada.

        Returns:
            AlgorithmResult com a melhor substring encontrada.
        """
        if not s:
            return AlgorithmResult(substring="", length=0)

        if self.count_instructions:
            self._instruction_count = 0
            self._instruction_count += 1  # Verificação da string vazia

        self._best_substring = ""
        start_time = time.time()

        for start_index in range(len(s)):
            if self.count_instructions:
                self._instruction_count += 1  # Iteração do laço externo
            self._explore(s, start_index, [], set())

        execution_time = time.time() - start_time
        result = AlgorithmResult(
            substring=self._best_substring,
            length=len(self._best_substring),
            execution_time=execution_time,
        )

        if self.count_instructions:
            result.instruction_count = self._instruction_count

        return result


