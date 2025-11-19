# Implementação: Backtracking

## Problema

Encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string.

**Exemplo:**
- Entrada: `"abcabcbb"` → Saída: `"abc"` (comprimento: 3)
- Entrada: `"bbbbb"` → Saída: `"b"` (comprimento: 1)

## Arquitetura

### `src/backtracking/backtracking.py`

**Classe `BacktrackingAlgorithm`:**
- **Estratégia:** Explora substrings contíguas utilizando recursão com retrocesso
- **Algoritmo:**
  1. Define um ponto inicial `i`
  2. Avança caractere a caractere enquanto não houver repetição
  3. Ao encontrar um caractere repetido, realiza o backtrack removendo o último caractere inserido e volta ao próximo ponto inicial
  4. Mantém a substring mais longa encontrada durante o processo
- **Recursos adicionais:**
  - Medição de tempo de execução
  - Contagem opcional de instruções para análise de complexidade

**Complexidade:**
- **Tempo:** O(n²) – cada ponto inicial gera uma exploração contígua até encontrar repetição
- **Espaço:** O(n) – pilha de recursão + estrutura para caracteres únicos

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

**1. Executar TODOS os testes da implementação Backtracking:**
```bash
python3 -m pytest tests/test_backtracking.py -v
```

**2. Executar testes com informações detalhadas (entrada, tempo, instruções):**
```bash
python3 -m pytest tests/test_backtracking.py -v -s
```

**3. Executar o programa principal e ver a comparação entre algoritmos:**
```bash
python3 main.py
```

**4. Testar com uma string personalizada diretamente pelo programa:**
```bash
python3 main.py "sua_string_aqui"
```

**5. Executar um teste específico (exemplo):**
```bash
python3 -m pytest tests/test_backtracking.py::TestBacktrackingAlgorithm::test_string_grande_todos_diferentes -v -s
```

**6. Executar testes com cobertura (opcional, requer pytest-cov):**
```bash
pip3 install pytest-cov
python3 -m pytest --cov=src/backtracking --cov-report=html
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

Ao executar os testes com `-s`, você verá informações detalhadas:

```
================================================================================
🧪 Executando: test_string_grande_todos_diferentes
================================================================================
📝 Testa com string muito grande onde todos os caracteres são diferentes.
   📥 Entrada: 'abcABCabcABC...' (tamanho: 100)
   📤 Resultado: 'abcABC...' (comprimento: 52)
   ⏱️  Tempo de execução: 0.012345s
✅ PASSOU: test_string_grande_todos_diferentes
   ⏱️  Tempo: 0.0123s
--------------------------------------------------------------------------------
```

**Resultado final esperado:**
```
============================= 15 passed in XX.XXs ==============================
```

## Exemplo de Uso em Código

```python
from src.backtracking import BacktrackingAlgorithm

algoritmo = BacktrackingAlgorithm(count_instructions=True)
resultado = algoritmo.solve("pwwkew")

print(f"Substring: {resultado.substring}")
print(f"Comprimento: {resultado.length}")
print(f"Tempo: {resultado.execution_time:.6f}s")
print(f"Instruções: {resultado.instruction_count}")
```

## Observações Analíticas

- O backtracking garante análise completa das substrings contíguas, mantendo simplicidade de implementação.
- Como a recursão é reiniciada a cada ponto inicial, o algoritmo oferece boa visualização de estados intermediários, ideal para documentação e ensino.
- A contagem de instruções disponível nos testes auxilia na comparação direta com Força Bruta e Divisão e Conquista.


