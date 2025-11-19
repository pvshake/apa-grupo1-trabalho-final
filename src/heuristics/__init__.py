"""
Implementação de heurísticas para encontrar substrings sem repetição.

Exporta a classe `HeuristicAlgorithm`, que combina uma estratégia baseada em
saltos (jump heuristic) com uma verificação auxiliar para garantir a
corretude do resultado.
"""

from .heuristics import HeuristicAlgorithm

__all__ = ["HeuristicAlgorithm"]


