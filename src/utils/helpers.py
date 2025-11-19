"""
Funções auxiliares para o projeto.
"""

from typing import List, Tuple


def validate_string(s: str) -> bool:
    """
    Valida se a string de entrada é válida.
    
    Args:
        s: String a ser validada
        
    Returns:
        True se a string é válida, False caso contrário
    """
    return isinstance(s, str)


def generate_test_cases() -> List[Tuple[str, int]]:
    """
    Gera uma lista de casos de teste para validação dos algoritmos.
    
    Returns:
        Lista de tuplas (string, comprimento_esperado)
    """
    return [
        ("", 0),
        ("a", 1),
        ("aa", 1),
        ("ab", 2),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("abcdefghijklmnopqrstuvwxyz", 26),
        ("a" * 100, 1),
        ("abc" * 10, 3),
    ]

