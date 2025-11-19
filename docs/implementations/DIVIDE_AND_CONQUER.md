# Implementação: Divisão e Conquista (Divide and Conquer)

## Problema

Encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string.

**Exemplo:**
- Entrada: `"abcabcbb"` → Saída: `"abc"` (comprimento: 3)
- Entrada: `"bbbbb"` → Saída: `"b"` (comprimento: 1)

## Arquitetura

### `src/divide_and_conquer/divide_and_conquer.py`

**Classe `DivideAndConquerAlgorithm`:**
- **Estratégia:** Divide a string ao meio, resolve o problema em cada metade e combina os resultados calculando uma substring que cruza o ponto médio.
- **Algoritmo:**
  1. Divide a string em duas partes (`esquerda`, `direita`)
  2. Resolve recursivamente cada metade
  3. Calcula a melhor substring que cruza o ponto médio garantindo unicidade
  4. Retorna o melhor resultado entre `esquerda`, `direita` e `cruzado`
- **Complexidade:**
  - **Tempo:** O(n log n) – cada nível da recursão analisa a string linearmente
  - **Espaço:** O(log n) – devido à profundidade da pilha de recursão
- **Funcionalidades adicionais:**
  - Medição de tempo de execução
  - Contagem opcional de instruções para análise de eficiência

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

**1. Executar TODOS os testes da implementação Divide and Conquer:**
```bash
python3 -m pytest tests/test_divide_and_conquer.py -v
```

**2. Executar testes com informações detalhadas (entrada, tempo, instruções):**
```bash
python3 -m pytest tests/test_divide_and_conquer.py -v -s
```

**3. Executar o programa principal e conferir os três algoritmos lado a lado:**
```bash
python3 main.py
```

**4. Testar com uma string personalizada diretamente pelo programa:**
```bash
python3 main.py "sua_string_aqui"
```

**5. Executar um teste específico (exemplo):**
```bash
python3 -m pytest tests/test_divide_and_conquer.py::TestDivideAndConquerAlgorithm::test_string_extremamente_grande -v -s
```

**6. Executar testes com cobertura (opcional, requer pytest-cov):**
```bash
pip3 install pytest-cov
python3 -m pytest --cov=src/divide_and_conquer --cov-report=html
```

### Saída Esperada

```
================================================================================
🧪 Executando: test_string_muito_grande_alfabeto_completo
================================================================================
📝 Testa com string muito grande contendo todo o alfabeto repetido.
   📥 Entrada: 'abcdefghijklmnopqrstuvwxyzabcd...' (tamanho: 988)
   📤 Resultado: 'abcdefghijklmnopqrstuvwxyz' (comprimento: 26)
   ⏱️  Tempo de execução: 0.007820s
✅ PASSOU: test_string_muito_grande_alfabeto_completo
   ⏱️  Tempo: 0.0078s
--------------------------------------------------------------------------------
============================= 15 passed in XX.XXs ==============================
```

## Exemplo de Uso em Código

```python
from src.divide_and_conquer import DivideAndConquerAlgorithm

algoritmo = DivideAndConquerAlgorithm(count_instructions=True)
resultado = algoritmo.solve("dvdf")

print(f"Substring: {resultado.substring}")
print(f"Comprimento: {resultado.length}")
print(f"Tempo: {resultado.execution_time:.6f}s")
print(f"Instruções: {resultado.instruction_count}")
```

## Observações Analíticas

- A abordagem divide a string em problemas menores e preserva o contexto de unicidade através do cálculo da substring cruzada.
- A estratégia apresenta melhora de desempenho em strings grandes quando comparada à Força Bruta, especialmente quando a substring ótima atravessa o ponto médio.
- A contagem de instruções permite observar o crescimento O(n log n) ao variar o comprimento da entrada.


