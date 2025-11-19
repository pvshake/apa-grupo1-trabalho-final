# Implementação: Programação Dinâmica (Dynamic Programming)

## Problema

Encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string.

**Exemplo:**
- Entrada: `"abcabcbb"` → Saída: `"abc"` (comprimento: 3)
- Entrada: `"bbbbb"` → Saída: `"b"` (comprimento: 1)

## Arquitetura

### `src/dynamic_programming/dynamic_programming.py`

**Classe `DynamicProgrammingAlgorithm`:**
- **Estratégia:** Mantém um vetor `dp[i]` com o tamanho da melhor substring terminando na posição `i` e utiliza um dicionário para registrar a última ocorrência de cada caractere.
- **Algoritmo:**
  1. Percorre a string uma única vez
  2. Atualiza o início válido sempre que encontra um caractere repetido
  3. Calcula `dp[i] = i - inicio_atual + 1`
  4. Mantém o melhor comprimento encontrado e sua posição inicial
- **Complexidade:**
  - **Tempo:** O(n)
  - **Espaço:** O(n) para o vetor `dp` e O(m) para o dicionário (`m` = alfabeto observado)
- **Extras:**
  - Medição de tempo de execução
  - Contagem opcional de instruções para fins acadêmicos

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

### Comandos para Testar

**1. Executar TODOS os testes da implementação de Programação Dinâmica:**
```bash
python3 -m pytest tests/test_dynamic_programming.py -v
```

**2. Mostrar detalhes de cada teste (entrada, tempo e instruções):**
```bash
python3 -m pytest tests/test_dynamic_programming.py -v -s
```

**3. Executar o programa principal com todas as implementações:**
```bash
python3 main.py
```

**4. Testar com uma string personalizada:**
```bash
python3 main.py "sua_string_aqui"
```

**5. Rodar um teste individual (exemplo):**
```bash
python3 -m pytest tests/test_dynamic_programming.py::TestDynamicProgrammingAlgorithm::test_string_extremamente_grande -v -s
```

**6. Gerar relatório de cobertura apenas desta implementação (opcional):**
```bash
pip3 install pytest-cov
python3 -m pytest --cov=src/dynamic_programming --cov-report=html
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

```
================================================================================
🧪 Executando: test_string_grande_todos_diferentes
================================================================================
📝 Testa com string muito grande onde todos os caracteres são diferentes.
   📥 Entrada: 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWx...' (tamanho: 100)
   📤 Resultado: 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ' (comprimento: 52)
   ⏱️  Tempo de execução: 0.000312s
✅ PASSOU: test_string_grande_todos_diferentes
   ⏱️  Tempo: 0.0003s
--------------------------------------------------------------------------------
============================= 15 passed in XX.XXs ==============================
```

## Exemplo de Uso em Código

```python
from src.dynamic_programming import DynamicProgrammingAlgorithm

algoritmo = DynamicProgrammingAlgorithm(count_instructions=True)
resultado = algoritmo.solve("pwwkew")

print(f"Substring: {resultado.substring}")
print(f"Comprimento: {resultado.length}")
print(f"Tempo: {resultado.execution_time:.6f}s")
print(f"Instruções: {resultado.instruction_count}")
```

## Observações Analíticas

- O vetor `dp` permite visualizar claramente como o tamanho ótimo evolui ao longo da string, útil para relatórios.
- A estratégia reutiliza informações anteriores e evita recomputações, servindo como ótimo contraponto teórico para Força Bruta e Backtracking.
- A contagem de instruções ilustra como o algoritmo cresce de forma linear com o tamanho da entrada.


