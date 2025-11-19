# Implementação: Força Bruta (Brute Force)

## Problema

Encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string.

**Exemplo:**
- Entrada: `"abcabcbb"` → Saída: `"abc"` (comprimento: 3)
- Entrada: `"bbbbb"` → Saída: `"b"` (comprimento: 1)

## Arquitetura

### `src/base/algorithm.py`

**Classe `Algorithm` (Abstrata):**
- Interface base para todos os algoritmos
- Define o método `solve(s: str) -> AlgorithmResult`
- Garante consistência entre implementações

**Classe `AlgorithmResult`:**
- Armazena o resultado: substring, comprimento, tempo de execução, contagem de instruções
- Permite comparação entre algoritmos

### `src/brute_force/brute_force.py`

**Classe `BruteForceAlgorithm`:**
- **Estratégia:** Testa todas as substrings possíveis
- **Algoritmo:**
  1. Para cada posição inicial `i`
  2. Para cada posição final `j >= i`
  3. Verifica se `s[i:j+1]` tem caracteres únicos
  4. Mantém a maior substring válida

**Complexidade:**
- **Tempo:** O(n³) - três loops aninhados
- **Espaço:** O(min(n, m)) - onde m é o tamanho do alfabeto

**Funcionalidades:**
- Medição de tempo de execução
- Contagem opcional de instruções (para análise de complexidade)

## Instruções de Execução

### Pré-requisitos

**Versões necessárias:**
- **Python:** 3.8 ou superior (testado com Python 3.9.19)
- **pip3:** Gerenciador de pacotes Python
- **pytest:** 7.4.0 ou superior

**Instalação das dependências:**
```bash
pip3 install -r requirements.txt
```

Isso instalará automaticamente o `pytest` e outras dependências necessárias.

### Comandos para Testar

**1. Executar TODOS os testes (recomendado para o professor):**
```bash
python3 -m pytest tests/test_brute_force.py -v
```

**2. Executar testes com informações detalhadas (mostra entrada, resultado, tempo):**
```bash
python3 -m pytest tests/test_brute_force.py -v -s
```

**3. Executar o programa principal com casos de teste padrão:**
```bash
python3 main.py
```

**4. Testar com uma string personalizada:**
```bash
python3 main.py "sua_string_aqui"
```

**5. Executar um teste específico:**
```bash
python3 -m pytest tests/test_brute_force.py::TestBruteForceAlgorithm::test_caso_geral_1 -v -s
```

**6. Executar testes com cobertura (opcional, requer pytest-cov):**
```bash
pip3 install pytest-cov
python3 -m pytest --cov=src --cov-report=html
```

**Extra — Executar toda a suíte do projeto:**
```bash
./scripts/run_all_tests.sh            # sequencial
./scripts/run_all_tests.sh --parallel # requer pytest-xdist
```

**Extra — Gerar relatório comparativo de desempenho:**
```bash
python3 scripts/collect_performance.py
```
Consulte `results/performance_summary.md` e [docs/ANALISE_DESEMPENHO.md](../ANALISE_DESEMPENHO.md).

### Saída Esperada

Ao executar os testes, você verá informações detalhadas para cada teste:

```
================================================================================
🧪 Executando: test_string_grande_repeticao
================================================================================
📝 Testa com string muito grande com muitas repetições.
   📥 Entrada: 'abcabcabc...' (tamanho: 500)
   📤 Resultado: 'abc' (comprimento: 3)
   ⏱️  Tempo de execução: 0.289740s
PASSED✅ PASSOU: test_string_grande_repeticao
   ⏱️  Tempo: 0.2900s
```

**Resultado final esperado:**
```
============================= 15 passed in XX.XXs ==============================
```

## Exemplo de Uso em Código

```python
from src.brute_force import BruteForceAlgorithm

# Criar instância
algoritmo = BruteForceAlgorithm(count_instructions=True)

# Resolver
resultado = algoritmo.solve("abcabcbb")

print(f"Substring: {resultado.substring}")
print(f"Comprimento: {resultado.length}")
print(f"Tempo: {resultado.execution_time:.6f}s")
print(f"Instruções: {resultado.instruction_count}")
```

