# TP2 – Graph Coloring with Local Search, SA, GA and DSATUR

Solução do **Trabalho Prático 2** de Fundamentos de Inteligência Artificial (UFMG). O objetivo é colorir grafos usando heurísticas de busca local, um algoritmo genético e a heurística determinística DSATUR, comparando desempenho em instâncias de referência.

## Estrutura do repositório

```
.
├── TP2_CSP_LocalSearch_GA.ipynb   # Notebook com todas as heurísticas e experimentos
├── data/
│   └── instances/                 # Instâncias adicionais do repositório COLOR
│       ├── myciel3.col
│       └── queen5_5.col
├── docs/
│   ├── TP_2_Fundamentos_IA_2025_2.pdf   # Enunciado
│   └── TP2_relatorio.pdf                # Relatório final
└── resultados/
    ├── runtime_grafo_exemplo.png
    ├── runtime_myciel3_(color).png
    └── runtime_queen5_5_(color).png     # Gráficos de runtime distribution (20 execuções)
```

## Instalação

O projeto utiliza Python 3.8+. Para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Conteúdo do notebook

1. **Implementação das heurísticas**
   - Random Walk (RW)
   - Best Improvement (BI)
   - First Improvement – Random Search (FI-RS)
   - First Improvement – Any Conflict (FI-AC)
   - Simulated Annealing (SA)
   - Algoritmo Genético (GA)
   - DSATUR

2. **Testes nas instâncias**
   - Grafo de exemplo do notebook (10 vértices).
   - Instâncias `myciel3.col` e `queen5_5.col` do repositório COLOR (<https://mat.tepper.cmu.edu/COLOR/instances.html>).

3. **Análise de runtime**
   - 20 execuções independentes de cada heurística para gerar as curvas `runtime_*.png`.

4. **Discussão dos resultados**
   - Comparação de robustez, tempo mediano e taxa de sucesso.

## Como executar

1. Abra `TP2_CSP_LocalSearch_GA.ipynb` em Jupyter, VS Code, Colab etc.
2. Execute as células na ordem:
   - As seções “Testando as heurísticas de Busca Local” e “Testando o algoritmo genético” mostram as execuções pontuais.
   - As seções seguintes automatizam experimentos, calculam estatísticas e salvam os gráficos em `resultados/`.
3. O relatório consolidado está em `docs/TP2_relatorio.pdf`.

## Resultados principais

- **Instâncias menores** (grafo exemplo e `myciel3`): todas as heurísticas encontraram soluções válidas rapidamente; DSATUR e FI-AC mantêm tempos < 1 ms.
- **Instância `queen5_5`**: heurísticas puramente aleatórias falham com frequência; SA obteve ~60% de sucesso, GA ~5%, enquanto DSATUR resolve determinística e praticamente instantaneamente (≈0,8 ms).
- Os gráficos de runtime deixam claro o contraste: curva do DSATUR aparece como degrau perto de 0 ms, enquanto métodos estocásticos exibem caudas longas.