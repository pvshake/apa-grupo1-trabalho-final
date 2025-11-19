# Implementação: Algoritmos Aproximados / Heurísticas

## Problema

Encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string.

**Exemplo:**
- Entrada: `"abcabcbb"` → Saída: `"abc"` (comprimento: 3)
- Entrada: `"bbbbb"` → Saída: `"b"` (comprimento: 1)

## Arquitetura

### `src/heuristics/heuristics.py`

**Classe `HeuristicAlgorithm`:**
- **Estratégia:** Combina duas heurísticas complementares:
  1. **Jump heuristic:** ao detectar um caractere repetido, salta diretamente para a posição seguinte à última ocorrência, evitando remoções passo a passo.
  2. **Early stopping:** interrompe a busca quando o trecho restante da string não pode mais superar o melhor resultado atual.
- **Complexidade:**
  - **Tempo:** O(n) em média, com loops curtos adicionais apenas quando necessário
  - **Espaço:** O(min(n, m)) para mapear últimas ocorrências
- **Funcionalidades:**
  - Medição de tempo de execução
  - Contagem opcional de instruções, útil para comparar com as demais abordagens

## Instruções de Execução

### Pré-requisitos

- **Python:** 3.8 ou superior (testado com Python 3.9.19)
- **pip3:** Gerenciador de pacotes Python
- **pytest:** 7.4.0 ou superior

**Instalação das dependências:**
```bash
pip3 install -r requirements.txt
```

### Comandos para Testar

**1. Executar todos os testes de heurísticas:**
```bash
python3 -m pytest tests/test_heuristics.py -v
```

**2. Visualizar detalhes completos em cada teste:**
```bash
python3 -m pytest tests/test_heuristics.py -v -s
```

**3. Rodar o programa principal (compare todas as estratégias lado a lado):**
```bash
python3 main.py
```

**4. Testar com uma string informada manualmente:**
```bash
python3 main.py "sua_string_aqui"
```

**5. Executar um teste específico (exemplo):**
```bash
python3 -m pytest tests/test_heuristics.py::TestHeuristicAlgorithm::test_string_muito_grande_alfabeto_completo -v -s
```

**6. Geração de cobertura exclusiva (opcional):**
```bash
pip3 install pytest-cov
python3 -m pytest --cov=src/heuristics --cov-report=html
```

### Saída Esperada

```
================================================================================
🧪 Executando: test_string_grande_repeticao
================================================================================
📝 Testa com string muito grande com muitas repetições.
   📥 Entrada: 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcab...' (tamanho: 500)
   📤 Resultado: 'abc' (comprimento: 3)
   ⏱️  Tempo de execução: 0.000812s
✅ PASSOU: test_string_grande_repeticao
   ⏱️  Tempo: 0.0008s
--------------------------------------------------------------------------------
============================= 15 passed in XX.XXs ==============================
```

## Exemplo de Uso em Código

```python
from src.heuristics import HeuristicAlgorithm

algoritmo = HeuristicAlgorithm(count_instructions=True)
resultado = algoritmo.solve("abcabcbb")

print(f"Substring: {resultado.substring}")
print(f"Comprimento: {resultado.length}")
print(f"Tempo: {resultado.execution_time:.6f}s")
print(f"Instruções: {resultado.instruction_count}")
```

## Observações Analíticas

- As heurísticas ilustram como otimizações baseadas em saltos e limites superiores reduzem significativamente o número de operações necessárias.
- Mesmo sendo classificadas como heurísticas, as duas técnicas combinadas preservam a corretude, garantindo os mesmos resultados que as abordagens determinísticas.
- Ótima opção para comparar ganhos práticos de desempenho frente ao algoritmo guloso tradicional.


