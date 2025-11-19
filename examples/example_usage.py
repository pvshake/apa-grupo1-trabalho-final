#!/usr/bin/env python3
"""
Exemplo de uso dos algoritmos do projeto.

Este arquivo demonstra como usar os diferentes algoritmos implementados
para resolver o problema da substring de comprimento máximo.
"""

from src.brute_force import BruteForceAlgorithm


def exemplo_basico():
    """Exemplo básico de uso do algoritmo de força bruta."""
    print("=" * 70)
    print("Exemplo Básico - Algoritmo de Força Bruta")
    print("=" * 70)
    
    # Cria instância do algoritmo
    algoritmo = BruteForceAlgorithm(count_instructions=True)
    
    # Casos de teste
    casos_teste = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "dvdf",
        "abcdefghijklmnopqrstuvwxyz",
    ]
    
    for caso in casos_teste:
        resultado = algoritmo.solve(caso)
        print(f"\nEntrada: '{caso}'")
        print(f"  Substring encontrada: '{resultado.substring}'")
        print(f"  Comprimento: {resultado.length}")
        print(f"  Tempo de execução: {resultado.execution_time:.6f}s")
        if resultado.instruction_count:
            print(f"  Instruções executadas: {resultado.instruction_count}")
    
    print("\n" + "=" * 70)


def exemplo_comparacao():
    """Exemplo comparando diferentes configurações."""
    print("\n" + "=" * 70)
    print("Exemplo de Comparação - Com e Sem Contagem de Instruções")
    print("=" * 70)
    
    string_teste = "abcabcbb"
    
    # Sem contagem de instruções (mais rápido)
    algo_sem_contagem = BruteForceAlgorithm(count_instructions=False)
    resultado_sem = algo_sem_contagem.solve(string_teste)
    
    # Com contagem de instruções (mais lento, mas com métricas)
    algo_com_contagem = BruteForceAlgorithm(count_instructions=True)
    resultado_com = algo_com_contagem.solve(string_teste)
    
    print(f"\nString de teste: '{string_teste}'")
    print(f"\nSem contagem de instruções:")
    print(f"  Tempo: {resultado_sem.execution_time:.6f}s")
    print(f"  Instruções: N/A")
    
    print(f"\nCom contagem de instruções:")
    print(f"  Tempo: {resultado_com.execution_time:.6f}s")
    print(f"  Instruções: {resultado_com.instruction_count}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    exemplo_basico()
    exemplo_comparacao()

