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

- ✅ **Força Bruta** (Brute Force) - Implementado
- ⏳ **Backtracking** - Em desenvolvimento
- ⏳ **Divisão e Conquista** (Divide and Conquer) - Em desenvolvimento
- ⏳ **Programação Dinâmica** (Dynamic Programming) - Em desenvolvimento
- ⏳ **Algoritmos Gulosos** (Greedy Algorithms) - Em desenvolvimento
- ⏳ **Algoritmos Aproximados ou Heurísticas** - Em desenvolvimento

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
│   ├── backtracking/        # ⏳ Em desenvolvimento
│   ├── divide_and_conquer/  # ⏳ Em desenvolvimento
│   ├── dynamic_programming/ # ⏳ Em desenvolvimento
│   ├── greedy/              # ⏳ Em desenvolvimento
│   ├── heuristics/          # ⏳ Em desenvolvimento
│   └── utils/               # Funções auxiliares
│       ├── __init__.py
│       └── helpers.py
├── tests/                   # Testes unitários
│   ├── __init__.py
│   ├── conftest.py          # Configuração do pytest (melhora exibição)
│   └── test_brute_force.py   # Testes do algoritmo de Força Bruta
├── docs/                    # Documentação do trabalho
│   ├── REQUISITOS.md        # Requisitos do trabalho final
│   ├── PLANO_DE_ACAO.md     # Plano de ação e divisão de tarefas
│   ├── implementations/     # Documentação das implementações
│   │   └── BRUTE_FORCE.md   # Documentação detalhada da Força Bruta
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

**3. Execute o programa principal:**
```bash
python3 main.py
```

### 📚 Instruções Detalhadas por Implementação

Para instruções específicas de cada algoritmo implementado, consulte:
- **Força Bruta:** [docs/implementations/BRUTE_FORCE.md](./docs/implementations/BRUTE_FORCE.md)
- **Backtracking:** (em desenvolvimento)
- **Divisão e Conquista:** (em desenvolvimento)
- **Programação Dinâmica:** (em desenvolvimento)
- **Algoritmos Gulosos:** (em desenvolvimento)
- **Heurísticas:** (em desenvolvimento)

### Exemplo de Uso

```python
from src.brute_force import BruteForceAlgorithm

# Cria instância do algoritmo
algorithm = BruteForceAlgorithm(count_instructions=True)

# Resolve o problema
result = algorithm.solve("abcabcbb")

print(f"Substring: {result.substring}")
print(f"Comprimento: {result.length}")
print(f"Tempo: {result.execution_time:.6f}s")
print(f"Instruções: {result.instruction_count}")
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
