"""
Implementação do algoritmo de Força Bruta para encontrar a substring
de comprimento máximo sem caracteres repetidos.

Complexidade Temporal: O(n³) onde n é o comprimento da string
Complexidade Espacial: O(min(n, m)) onde m é o tamanho do alfabeto
"""

import time
from typing import Set
from ..base.algorithm import Algorithm, AlgorithmResult


class BruteForceAlgorithm(Algorithm):
    """
    Algoritmo de Força Bruta para encontrar a substring de comprimento máximo.
    
    Este algoritmo testa todas as possíveis substrings da string de entrada,
    verificando qual delas tem o maior comprimento sem caracteres repetidos.
    
    Estratégia:
    1. Para cada posição inicial i na string
    2. Para cada posição final j >= i na string
    3. Verifica se a substring s[i:j+1] não contém caracteres repetidos
    4. Mantém registro da maior substring válida encontrada
    """
    
    def __init__(self, count_instructions: bool = False):
        """
        Inicializa o algoritmo de força bruta.
        
        Args:
            count_instructions: Se True, conta o número de instruções executadas
        """
        super().__init__("Força Bruta (Brute Force)")
        self.count_instructions = count_instructions
        self._instruction_count = 0
    
    def _has_unique_characters(self, substring: str) -> bool:
        """
        Verifica se uma substring contém apenas caracteres únicos.
        
        Args:
            substring: A substring a ser verificada
            
        Returns:
            True se todos os caracteres são únicos, False caso contrário
        """
        if self.count_instructions:
            self._instruction_count += 1  # Comparação de tamanho
        
        # Se o tamanho da substring é maior que o número de caracteres únicos,
        # então há repetição
        if len(substring) > len(set(substring)):
            if self.count_instructions:
                self._instruction_count += len(substring)  # Criação do set
            return False
        
        if self.count_instructions:
            self._instruction_count += len(substring)  # Criação do set
        return True
    
    def solve(self, s: str) -> AlgorithmResult:
        """
        Resolve o problema usando força bruta.
        
        Testa todas as possíveis substrings e retorna a de maior comprimento
        que não contém caracteres repetidos.
        
        Args:
            s: String de entrada
            
        Returns:
            AlgorithmResult contendo a substring de comprimento máximo e
            informações sobre a execução
        """
        if not s:
            return AlgorithmResult(substring="", length=0)
        
        # Inicializa contador de instruções se necessário
        if self.count_instructions:
            self._instruction_count = 0
            self._instruction_count += 1  # Verificação de string vazia
        
        start_time = time.time()
        
        max_length = 0
        max_substring = ""
        
        # Itera sobre todas as posições iniciais possíveis
        # Complexidade: O(n) onde n = len(s)
        for i in range(len(s)):
            if self.count_instructions:
                self._instruction_count += 1  # Incremento do loop externo
            
            # Itera sobre todas as posições finais possíveis a partir de i
            # Complexidade: O(n) para cada i
            for j in range(i, len(s)):
                if self.count_instructions:
                    self._instruction_count += 1  # Incremento do loop interno
                
                # Extrai a substring atual
                current_substring = s[i:j+1]
                if self.count_instructions:
                    self._instruction_count += (j - i + 1)  # Operação de slice
                
                # Verifica se a substring atual é válida (sem repetições)
                # e se é maior que a máxima encontrada até agora
                if self._has_unique_characters(current_substring):
                    if self.count_instructions:
                        self._instruction_count += 1  # Comparação de comprimento
                    
                    if len(current_substring) > max_length:
                        max_length = len(current_substring)
                        max_substring = current_substring
                        if self.count_instructions:
                            self._instruction_count += 2  # Atribuições
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        result = AlgorithmResult(
            substring=max_substring,
            length=max_length,
            execution_time=execution_time
        )
        
        if self.count_instructions:
            result.instruction_count = self._instruction_count
        
        return result

