#!/usr/bin/env python3
"""
Script principal para executar os algoritmos do projeto.

Este script permite testar e comparar diferentes algoritmos para
resolver o problema da substring de comprimento máximo.
"""

import sys
from src.brute_force import BruteForceAlgorithm
from src.utils import generate_test_cases


def main():
    """Função principal do programa."""
    print("=" * 70)
    print("Trabalho Final de APA - String de Comprimento Máximo")
    print("=" * 70)
    print()
    
    # Cria instância do algoritmo de força bruta
    brute_force = BruteForceAlgorithm(count_instructions=True)
    
    # Casos de teste
    test_cases = generate_test_cases()
    
    print(f"Testando algoritmo: {brute_force.name}")
    print("-" * 70)
    print(f"{'String de Entrada':<30} | {'Resultado':<20} | {'Tempo (s)':<12}")
    print("-" * 70)
    
    for test_string, expected_length in test_cases:
        # Limita a exibição de strings muito longas
        display_string = test_string if len(test_string) <= 25 else test_string[:22] + "..."
        
        result = brute_force.solve(test_string)
        
        # Verifica se o resultado está correto
        status = "✓" if result.length == expected_length else "✗"
        
        time_str = f"{result.execution_time:.6f}" if result.execution_time else "N/A"
        
        print(f"{display_string:<30} | {result.substring:<20} | {time_str:<12} {status}")
        if result.instruction_count:
            print(f"  └─ Comprimento: {result.length} | Instruções: {result.instruction_count}")
    
    print("-" * 70)
    print()
    
    # Permite teste interativo
    if len(sys.argv) > 1:
        user_string = sys.argv[1]
        print(f"Testando string personalizada: '{user_string}'")
        result = brute_force.solve(user_string)
        print(f"Resultado: {result}")
        print()
    
    print("Para testar uma string personalizada, execute:")
    print("  python main.py 'sua_string_aqui'")
    print()


if __name__ == "__main__":
    main()

