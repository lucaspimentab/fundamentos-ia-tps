# TP2 - Graph Coloring (Local Search, SA, GA e DSATUR)

Solucao do Trabalho Pratico 2 de Fundamentos de IA (UFMG). O objetivo e colorir grafos com heuristicas de busca local, simulated annealing, algoritmo genetico e a heuristica deterministica DSATUR, comparando desempenho em instancias de referencia.

## Estrutura
- `notebooks/TP2_CSP_LocalSearch_GA.ipynb`: notebook com implementacao e experimentos.
- `data/instances/`: instancias `myciel3.col` e `queen5_5.col`.
- `docs/TP_2_Fundamentos_IA_2025_2.pdf`: enunciado original.
- `docs/TP2_relatorio.pdf`: relatorio final.
- `results/`: graficos `runtime_*.png` gerados pelo notebook.
- `requirements.txt`: dependencias (matplotlib >= 3.9).

## Como rodar
1. Crie um ambiente com Python 3.9+.
2. Instale dependencias: `pip install -r requirements.txt`.
3. Abra `notebooks/TP2_CSP_LocalSearch_GA.ipynb` em Jupyter, VS Code ou Colab.
4. Execute as celulas na ordem; os graficos sao salvos em `results/`.

## Heuristicas implementadas
- Random Walk
- Best Improvement
- First Improvement - Random Search
- First Improvement - Any Conflict
- Simulated Annealing
- Algoritmo genetico
- DSATUR
