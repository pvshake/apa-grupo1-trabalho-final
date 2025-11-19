# Implementação: Algoritmo Guloso (Greedy)

## Problema

Encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string.

**Exemplo:**
- Entrada: `"abcabcbb"` → Saída: `"abc"` (comprimento: 3)
- Entrada: `"bbbbb"` → Saída: `"b"` (comprimento: 1)

## Arquitetura

### `src/greedy/greedy.py`

**Classe `GreedyAlgorithm`:**
- **Estratégia:** Usa uma janela deslizante que é expandida enquanto encontra caracteres inéditos e encolhida de forma gulosa (removendo um caractere por vez) quando detecta repetição.
- **Algoritmo:**
  1. Mantém um conjunto com os caracteres da janela atual
  2. Avança o ponteiro direito (`right`) e adiciona novos caracteres
  3. Ao detectar repetição, remove os caracteres do início (`left`) até eliminar o duplicado
  4. Atualiza o melhor resultado sempre que a janela cresce
- **Complexidade:**
  - **Tempo:** O(n) – cada caractere é inserido e removido no máximo uma vez
  - **Espaço:** O(min(n, m)) para o conjunto de caracteres (`m` = alfabeto)
- **Recursos extras:**
  - Medição de tempo
  - Contagem de instruções para análise empírica

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

**1. Rodar todos os testes do algoritmo guloso:**
```bash
python3 -m pytest tests/test_greedy.py -v
```

**2. Rodar testes com saída detalhada:**
```bash
python3 -m pytest tests/test_greedy.py -v -s
```

**3. Executar o programa principal com todas as estratégias:**
```bash
python3 main.py
```

**4. Testar com uma string personalizada:**
```bash
python3 main.py "sua_string_aqui"
```

**5. Executar teste específico (exemplo):**
```bash
python3 -m pytest tests/test_greedy.py::TestGreedyAlgorithm::test_string_extremamente_grande -v -s
```

**6. Cobertura dedicada (opcional):**
```bash
pip3 install pytest-cov
python3 -m pytest --cov=src/greedy --cov-report=html
```

### Saída Esperada

```
================================================================================
🧪 Executando: test_string_extremamente_grande
================================================================================
📝 Testa com string extremamente grande para análise de performance.
   📥 Entrada: 'abcdefghijklmnopqrstuvwxyz0123456789abcd...' (tamanho: 1872)
   📤 Resultado: 'abcdefghijklmnopqrstuvwxyz0123456789' (comprimento: 36)
   ⏱️  Tempo de execução: 0.006230s
✅ PASSOU: test_string_extremamente_grande
   ⏱️  Tempo: 0.0062s
--------------------------------------------------------------------------------
============================= 15 passed in XX.XXs ==============================
```

## Exemplo de Uso em Código

```python
from src.greedy import GreedyAlgorithm

algoritmo = GreedyAlgorithm(count_instructions=True)
resultado = algoritmo.solve("dvdf")

print(f"Substring: {resultado.substring}")
print(f"Comprimento: {resultado.length}")
print(f"Tempo: {resultado.execution_time:.6f}s")
print(f"Instruções: {resultado.instruction_count}")
```

## Observações Analíticas

- A estratégia gulosa evidencia como decisões locais (remover apenas o primeiro caractere repetido) produzem soluções globais corretas.
- Serve como ponte entre a simplicidade do brute force e a sofisticação de Programação Dinâmica/Heurísticas.
- Por operar estritamente em tempo linear, é excelente para coletar métricas e comparar com as demais abordagens implementadas no trabalho.


