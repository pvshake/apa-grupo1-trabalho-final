"""
Classe base abstrata para todos os algoritmos do projeto.

Define a interface comum que todos os algoritmos devem implementar,
garantindo consistência e facilitando a comparação entre diferentes estratégias.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class AlgorithmResult:
    """
    Classe para armazenar o resultado de um algoritmo.
    
    Attributes:
        substring: A substring de comprimento máximo encontrada
        length: O comprimento da substring encontrada
        execution_time: Tempo de execução em segundos (opcional)
        instruction_count: Número de instruções executadas (opcional)
    """
    substring: str
    length: int
    execution_time: Optional[float] = None
    instruction_count: Optional[int] = None
    
    def __str__(self) -> str:
        """Representação em string do resultado."""
        result = f"Substring: '{self.substring}' | Comprimento: {self.length}"
        if self.execution_time is not None:
            result += f" | Tempo: {self.execution_time:.6f}s"
        if self.instruction_count is not None:
            result += f" | Instruções: {self.instruction_count}"
        return result


class Algorithm(ABC):
    """
    Classe abstrata base para todos os algoritmos.
    
    Todos os algoritmos (Força Bruta, Backtracking, etc.) devem herdar
    desta classe e implementar o método solve().
    """
    
    def __init__(self, name: str):
        """
        Inicializa o algoritmo.
        
        Args:
            name: Nome descritivo do algoritmo
        """
        self.name = name
    
    @abstractmethod
    def solve(self, s: str) -> AlgorithmResult:
        """
        Resolve o problema da substring de comprimento máximo.
        
        O problema consiste em encontrar a substring de comprimento máximo
        sem caracteres repetidos em uma string dada.
        
        Args:
            s: String de entrada
            
        Returns:
            AlgorithmResult contendo a substring encontrada e seu comprimento
        """
        pass
    
    def __str__(self) -> str:
        """Representação em string do algoritmo."""
        return f"{self.name}"

