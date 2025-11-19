# Análise de Desempenho e Comparação das Estratégias

Este documento consolida as medições de tempo e a contagem de instruções de todas as implementações desenvolvidas para o problema da **Substring de Comprimento Máximo sem Repetição**.

Os dados foram coletados com o script `python3 scripts/collect_performance.py`, que executa cada algoritmo com os casos de teste definidos em `src/utils/generate_test_cases()`. Todos os algoritmos foram instanciados com `count_instructions=True` para permitir a comparação direta.

## Resumo Global

| Algoritmo | Tempo Médio (ms) | Instruções Médias | Maior Substring | Testes OK |
|-----------|-----------------|-------------------|-----------------|-----------|
| Força Bruta (Brute Force) | 0.697 | 33,921 | 26 | ✅ |
| Backtracking | 0.080 | 384 | 26 | ✅ |
| Divisão e Conquista (Divide and Conquer) | 0.055 | 206 | 26 | ✅ |
| Programação Dinâmica (Dynamic Programming) | 0.010 | 67 | 26 | ✅ |
| Algoritmo Guloso (Greedy) | 0.010 | 51 | 26 | ✅ |
| Heurístico / Aproximação | 0.008 | 35 | 26 | ✅ |

**Ranking por tempo médio:**
1. Heurístico / Aproximação — 0.008 ms  
2. Programação Dinâmica — 0.010 ms  
3. Algoritmo Guloso — 0.010 ms  
4. Divisão e Conquista — 0.055 ms  
5. Backtracking — 0.080 ms  
6. Força Bruta — 0.697 ms  

> Os arquivos completos se encontram em `results/performance_summary.json` e `results/performance_summary.md`.

## Interpretação por Estratégia

- **Força Bruta (O(n³)):** Apresenta o pior desempenho, com média de ~0,7 ms e mais de 30 mil instruções, refletindo o custo cúbico da exploração exaustiva. Serve como baseline conceitual, mas é inviável para strings maiores.

- **Backtracking (O(n²)):** Reduz drasticamente a contagem de instruções (média ~384) e melhora o tempo (0,08 ms), porém ainda precisa reinicializar a busca a cada posição inicial, o que o torna inferior às abordagens mais modernas.

- **Divisão e Conquista (O(n log n)):** Obtém 0,055 ms em média graças à combinação linear feita no passo de junção. É vantajosa quando se deseja uma alternativa recursiva determinística com garantias formais.

- **Programação Dinâmica (O(n)):** Aproveita o histórico de estados para operar em tempo linear e mantém a contagem média em 67 instruções. É estável e previsível, sendo uma das melhores opções quando se prioriza clareza matemática e performance.

- **Algoritmo Guloso (O(n)):** Similar ao DP em tempo (0,010 ms) e ainda mais enxuto em instruções (51). O uso de janela deslizante direta o torna perfeito para aplicações em streaming.

- **Heurístico / Aproximação (≈O(n)):** Entrega o melhor tempo médio (0,008 ms) e a menor contagem (35) graças às heurísticas de salto e parada antecipada. Apesar de heurístico, os saltos foram implementados de forma segura, garantindo os mesmos resultados das abordagens determinísticas nesta classe de problemas.

## Conclusões

- **Melhor estratégia (tempo/instruções):** a abordagem **Heurística** ficou ligeiramente à frente, seguida de perto por **Programação Dinâmica** e **Greedy**. Todas operam em tempo linear, mas o heurístico aproveita saltos maiores para reduzir o número de passos efetivos.

- **Pior estratégia:** **Força Bruta**, tanto em tempo quanto em contagem de instruções. Ela permanece útil apenas como referência didática.

- **Trade-offs práticos:**
  - **Heurístico** é ideal quando se busca o menor tempo possível mantendo simplicidade de uso.
  - **Programação Dinâmica** oferece o melhor equilíbrio entre clareza formal e performance.
  - **Divisão e Conquista** e **Backtracking** são úteis em relatórios acadêmicos para mostrar abordagens recursivas, mas não são competitivas em escala.

## Como Reproduzir as Métricas

```bash
python3 scripts/collect_performance.py
```

O comando acima atualiza os arquivos em `results/` e permite rastrear regressões de performance durante o desenvolvimento.


