"""
Testes unitários para o algoritmo de Força Bruta.
"""

import pytest
from src.brute_force import BruteForceAlgorithm


class TestBruteForceAlgorithm:
    """Classe de testes para o algoritmo de Força Bruta."""
    
    def setup_method(self):
        """Configura o ambiente de teste antes de cada método."""
        self.algorithm = BruteForceAlgorithm()
    
    def _print_test_result(self, test_name: str, input_str: str, result):
        """Exibe informações detalhadas sobre o resultado do teste."""
        display_input = input_str if len(input_str) <= 50 else input_str[:47] + "..."
        print(f"   📥 Entrada: '{display_input}' (tamanho: {len(input_str)})")
        print(f"   📤 Resultado: '{result.substring}' (comprimento: {result.length})")
        if result.execution_time is not None:
            print(f"   ⏱️  Tempo de execução: {result.execution_time:.6f}s")
        if result.instruction_count is not None:
            print(f"   🔢 Instruções executadas: {result.instruction_count:,}")
    
    def test_string_vazia(self):
        """Testa o comportamento com string vazia."""
        result = self.algorithm.solve("")
        self._print_test_result("test_string_vazia", "", result)
        assert result.substring == ""
        assert result.length == 0
    
    def test_string_unica_caractere(self):
        """Testa com string de um único caractere."""
        result = self.algorithm.solve("a")
        assert result.substring == "a"
        assert result.length == 1
    
    def test_string_todos_iguais(self):
        """Testa com string onde todos os caracteres são iguais."""
        result = self.algorithm.solve("aaaa")
        assert result.substring == "a"
        assert result.length == 1
    
    def test_string_todos_diferentes(self):
        """Testa com string onde todos os caracteres são diferentes."""
        result = self.algorithm.solve("abcde")
        assert result.substring == "abcde"
        assert result.length == 5
    
    def test_caso_geral_1(self):
        """Testa caso geral: 'abcabcbb'."""
        result = self.algorithm.solve("abcabcbb")
        self._print_test_result("test_caso_geral_1", "abcabcbb", result)
        assert result.length == 3
        # Pode ser "abc", "bca", ou "cab" - qualquer substring de 3 caracteres únicos
        assert len(result.substring) == 3
        assert len(set(result.substring)) == 3  # Verifica que não há repetição
    
    def test_caso_geral_2(self):
        """Testa caso geral: 'bbbbb'."""
        result = self.algorithm.solve("bbbbb")
        assert result.substring == "b"
        assert result.length == 1
    
    def test_caso_geral_3(self):
        """Testa caso geral: 'pwwkew'."""
        result = self.algorithm.solve("pwwkew")
        assert result.length == 3
        # Pode ser "wke" ou "kew"
        assert len(result.substring) == 3
        assert len(set(result.substring)) == 3
    
    def test_caso_complexo(self):
        """Testa caso mais complexo."""
        result = self.algorithm.solve("dvdf")
        assert result.length == 3
        assert len(set(result.substring)) == 3
    
    def test_string_com_espacos(self):
        """Testa com string contendo espaços."""
        result = self.algorithm.solve("a b c")
        # "a b c" tem espaços repetidos, então a substring máxima é "a b" ou "b c" (3 caracteres)
        assert result.length == 3
        assert len(set(result.substring)) == len(result.substring)
    
    def test_contagem_instrucoes(self):
        """Testa se a contagem de instruções funciona quando habilitada."""
        algorithm = BruteForceAlgorithm(count_instructions=True)
        result = algorithm.solve("abc")
        self._print_test_result("test_contagem_instrucoes", "abc", result)
        assert result.instruction_count is not None
        assert result.instruction_count > 0
    
    def test_tempo_execucao(self):
        """Testa se o tempo de execução é medido."""
        result = self.algorithm.solve("abcabcbb")
        assert result.execution_time is not None
        assert result.execution_time >= 0
    
    def test_string_grande_todos_diferentes(self):
        """Testa com string muito grande onde todos os caracteres são diferentes."""
        # String com 100 caracteres (52 únicos: a-z e A-Z)
        large_string = "".join(chr(ord('a') + i % 26) + chr(ord('A') + i % 26) for i in range(50))
        result = self.algorithm.solve(large_string)
        self._print_test_result("test_string_grande_todos_diferentes", large_string, result)
        # A substring máxima terá 52 caracteres (alfabeto minúsculo + maiúsculo)
        assert result.length == 52
        assert len(set(result.substring)) == 52
    
    def test_string_grande_repeticao(self):
        """Testa com string muito grande com muitas repetições."""
        # String de 500 caracteres com padrão repetitivo
        large_string = "abc" * 166 + "ab"  # 500 caracteres
        result = self.algorithm.solve(large_string)
        self._print_test_result("test_string_grande_repeticao", large_string, result)
        assert result.length == 3  # "abc" é a substring máxima
        assert len(set(result.substring)) == 3
    
    def test_string_muito_grande_alfabeto_completo(self):
        """Testa com string muito grande contendo todo o alfabeto repetido."""
        # String de 1000 caracteres: alfabeto completo repetido várias vezes
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        large_string = (alphabet * 38) + alphabet[:14]  # ~1000 caracteres
        result = self.algorithm.solve(large_string)
        self._print_test_result("test_string_muito_grande_alfabeto_completo", large_string, result)
        assert result.length == 26  # Alfabeto completo
        assert len(set(result.substring)) == 26
    
    def test_string_extremamente_grande(self):
        """Testa com string extremamente grande para análise de performance."""
        # String de 2000 caracteres com padrão complexo
        pattern = "abcdefghijklmnopqrstuvwxyz0123456789"
        large_string = (pattern * 51) + pattern[:44]  # ~2000 caracteres
        algorithm = BruteForceAlgorithm(count_instructions=True)
        result = algorithm.solve(large_string)
        self._print_test_result("test_string_extremamente_grande", large_string, result)
        # A substring máxima deve ter 36 caracteres (todos os caracteres do pattern são únicos)
        assert result.length == 36
        assert len(set(result.substring)) == 36
        # Verifica que o tempo foi medido
        assert result.execution_time is not None
        assert result.execution_time >= 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

