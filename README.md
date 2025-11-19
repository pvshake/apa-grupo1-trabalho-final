# Trabalho Final de APA - String de Comprimento Máximo

## 📋 Sobre o Projeto

Este repositório contém a implementação e análise de diferentes estratégias algorítmicas para resolver o problema **String de Comprimento Máximo**, desenvolvido como trabalho final da disciplina de Análise e Projeto de Algoritmos (APA).

## 🎯 Problema: String de Comprimento Máximo

O problema consiste em encontrar a **substring de comprimento máximo sem caracteres repetidos** em uma string dada.

### Definição

Dada uma string `s` de comprimento `n`, encontrar a substring `s[i:j]` tal que:
- Todos os caracteres em `s[i:j]` são únicos (não há repetição)
- O comprimento `j - i + 1` é máximo

### Exemplos

- **Entrada:** `"abcabcbb"` → **Saída:** `"abc"` (comprimento: 3)
- **Entrada:** `"bbbbb"` → **Saída:** `"b"` (comprimento: 1)
- **Entrada:** `"pwwkew"` → **Saída:** `"wke"` ou `"kew"` (comprimento: 3)

## 🛠️ Estratégias Implementadas

Este projeto implementa e compara as seguintes estratégias algorítmicas:

- ✅ **Força Bruta** (Brute Force)
- ✅ **Backtracking**
- ✅ **Divisão e Conquista** (Divide and Conquer)
- ✅ **Programação Dinâmica** (Dynamic Programming)
- ✅ **Algoritmos Gulosos** (Greedy Algorithms)
- ✅ **Algoritmos Aproximados ou Heurísticas**

## 📁 Estrutura do Projeto

```
.
├── README.md                 # Este arquivo (instruções principais)
├── requirements.txt         # Dependências do projeto (pytest, etc.)
├── setup.py                 # Configuração do pacote Python
├── pytest.ini              # Configuração dos testes
├── main.py                  # Script principal de execução
├── src/                     # Códigos-fonte das implementações
│   ├── __init__.py
│   ├── base/                # Classes base e interfaces
│   │   ├── __init__.py
│   │   └── algorithm.py     # Classe abstrata Algorithm
│   ├── brute_force/         # ✅ Implementado
│   │   ├── __init__.py
│   │   └── brute_force.py
│   ├── backtracking/        # ✅ Implementado
│   ├── divide_and_conquer/  # ✅ Implementado
│   ├── dynamic_programming/ # ✅ Implementado
│   ├── greedy/              # ✅ Implementado
│   ├── heuristics/          # ✅ Implementado
│   └── utils/               # Funções auxiliares
│       ├── __init__.py
│       └── helpers.py
├── tests/                   # Testes unitários
│   ├── __init__.py
│   ├── conftest.py          # Configuração do pytest (melhora exibição)
│   ├── test_brute_force.py
│   ├── test_backtracking.py
│   ├── test_divide_and_conquer.py
│   ├── test_dynamic_programming.py
│   ├── test_greedy.py
│   └── test_heuristics.py
├── docs/                    # Documentação do trabalho
│   ├── REQUISITOS.md        # Requisitos do trabalho final
│   ├── PLANO_DE_ACAO.md     # Plano de ação e divisão de tarefas
│   ├── implementations/     # Documentação das implementações
│   │   ├── BRUTE_FORCE.md
│   │   ├── BACKTRACKING.md
│   │   ├── DIVIDE_AND_CONQUER.md
│   │   ├── DYNAMIC_PROGRAMMING.md
│   │   ├── GREEDY.md
│   │   └── HEURISTICS.md
│   └── documentacao.pdf     # Documentação final em PDF (a ser criado)
└── results/                 # Resultados de performance e análises
```

## 🚀 Como Executar

### ⚙️ Requisitos do Sistema

**Versões necessárias:**
- **Python:** 3.8 ou superior (testado com Python 3.9.19)
- **pip3:** Gerenciador de pacotes Python
- **pytest:** 7.4.0 ou superior (será instalado automaticamente)

**Verificar versões instaladas:**
```bash
python3 --version    # Deve mostrar Python 3.8 ou superior
pip3 --version       # Deve mostrar pip instalado
```

### 📦 Instalação

**1. Instale as dependências:**
```bash
pip3 install -r requirements.txt
```

**2. Execute os testes:**
```bash
# Executar todos os testes
python3 -m pytest tests/ -v

# Executar testes com informações detalhadas
python3 -m pytest tests/ -v -s
```

**3. Executar todos os testes com um único comando:**
```bash
./scripts/run_all_tests.sh            # execução sequencial
./scripts/run_all_tests.sh --parallel # requer pytest-xdist
```

**4. Execute o programa principal:**
```bash
python3 main.py
```

### 📚 Instruções Detalhadas por Implementação

Para instruções específicas de cada algoritmo implementado, consulte:
- **Força Bruta:** [docs/implementations/BRUTE_FORCE.md](./docs/implementations/BRUTE_FORCE.md)
- **Backtracking:** [docs/implementations/BACKTRACKING.md](./docs/implementations/BACKTRACKING.md)
- **Divisão e Conquista:** [docs/implementations/DIVIDE_AND_CONQUER.md](./docs/implementations/DIVIDE_AND_CONQUER.md)
- **Programação Dinâmica:** [docs/implementations/DYNAMIC_PROGRAMMING.md](./docs/implementations/DYNAMIC_PROGRAMMING.md)
- **Algoritmos Gulosos:** [docs/implementations/GREEDY.md](./docs/implementations/GREEDY.md)
- **Heurísticas:** [docs/implementations/HEURISTICS.md](./docs/implementations/HEURISTICS.md)

## 📊 Coleta de Desempenho

Para gerar as métricas (tempo médio, contagem de instruções e ranking):

```bash
python3 scripts/collect_performance.py
```

Os resultados ficam disponíveis em:
- `results/performance_summary.json`
- `results/performance_summary.md`
- [docs/ANALISE_DESEMPENHO.md](./docs/ANALISE_DESEMPENHO.md) — interpretação completa dos dados

## 📈 Resumo dos Resultados

| Algoritmo | Complexidade | Tempo Médio (ms) | Instruções Médias |
|-----------|--------------|------------------|-------------------|
| Heurístico / Aproximação | ≈O(n) | 0.008 | 35 |
| Programação Dinâmica | O(n) | 0.010 | 67 |
| Algoritmo Guloso | O(n) | 0.010 | 51 |
| Divisão e Conquista | O(n log n) | 0.055 | 206 |
| Backtracking | O(n²) | 0.080 | 384 |
| Força Bruta | O(n³) | 0.697 | 33 921 |

> Fonte: `python3 scripts/collect_performance.py`. Veja detalhes e análise qualitativa em [docs/ANALISE_DESEMPENHO.md](./docs/ANALISE_DESEMPENHO.md).

### Exemplo de Uso

```python
from src.brute_force import BruteForceAlgorithm
from src.backtracking import BacktrackingAlgorithm
from src.divide_and_conquer import DivideAndConquerAlgorithm
from src.dynamic_programming import DynamicProgrammingAlgorithm
from src.greedy import GreedyAlgorithm
from src.heuristics import HeuristicAlgorithm

algorithms = [
    BruteForceAlgorithm(count_instructions=True),
    BacktrackingAlgorithm(count_instructions=True),
    DivideAndConquerAlgorithm(count_instructions=True),
    DynamicProgrammingAlgorithm(count_instructions=True),
    GreedyAlgorithm(count_instructions=True),
    HeuristicAlgorithm(count_instructions=True),
]

for algorithm in algorithms:
    result = algorithm.solve("abcabcbb")
    print(f"{algorithm.name} → Substring: {result.substring} | "
          f"Comprimento: {result.length} | Tempo: {result.execution_time:.6f}s | "
          f"Instruções: {result.instruction_count}")
```

Para mais exemplos e detalhes, consulte a documentação específica de cada implementação em `docs/implementations/`.

## 📊 Análise de Complexidade

[Análise de complexidade temporal e espacial será documentada aqui]

## 📈 Resultados

[Resultados comparativos das diferentes estratégias serão apresentados aqui]

## 📚 Referências

- T.H. Cormen, C.E. Leiserson, R.L. Rivest, and C. Stein. *Introduction to Algorithms.* The MIT Press/McGraw-Hill, 3rd edition, 2009.
- N. Ziviani. *Projeto de Algoritmos com implementações em Java e C++.* Cengage Learning (Thomson/Pioneira), São Paulo, 1st edition, 2006.

## 👥 Autores

[Adicionar nomes completos e números de matrícula dos integrantes do grupo]

## 📅 Prazos

- **Entrega do trabalho escrito:** 22/11/2025
- **Apresentação oral:** 24/11 ou 1/12/2025

## 📝 Documentação Adicional

- **Requisitos do trabalho:** [docs/REQUISITOS.md](./docs/REQUISITOS.md)
- **Plano de ação:** [docs/PLANO_DE_ACAO.md](./docs/PLANO_DE_ACAO.md)
- **Documentação da implementação Força Bruta:** [docs/implementations/BRUTE_FORCE.md](./docs/implementations/BRUTE_FORCE.md)
- **Documentação da implementação Backtracking:** [docs/implementations/BACKTRACKING.md](./docs/implementations/BACKTRACKING.md)
- **Documentação da implementação Divisão e Conquista:** [docs/implementations/DIVIDE_AND_CONQUER.md](./docs/implementations/DIVIDE_AND_CONQUER.md)
- **Documentação da implementação Programação Dinâmica:** [docs/implementations/DYNAMIC_PROGRAMMING.md](./docs/implementations/DYNAMIC_PROGRAMMING.md)
- **Documentação da implementação Algoritmo Guloso:** [docs/implementations/GREEDY.md](./docs/implementations/GREEDY.md)
- **Documentação da implementação Heurísticas:** [docs/implementations/HEURISTICS.md](./docs/implementations/HEURISTICS.md)
- **Análise consolidada de desempenho:** [docs/ANALISE_DESEMPENHO.md](./docs/ANALISE_DESEMPENHO.md)

## ❓ Solução de Problemas

**Erro: "No module named pytest"**
```bash
pip3 install -r requirements.txt
```

**Erro: "python3: command not found"**
- No Windows, use `python` ao invés de `python3`
- Certifique-se de que o Python está instalado e no PATH

**Testes não mostram informações detalhadas:**
- Use a flag `-s`: `python3 -m pytest tests/ -v -s`

**Verificar se tudo está instalado corretamente:**
```bash
python3 -m pytest --version
```
