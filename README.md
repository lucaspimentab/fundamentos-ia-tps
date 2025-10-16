# TP2 – Graph Coloring with Local Search, SA, GA and DSATUR

Este repositório contém a solução do **Trabalho Prático 2** da disciplina Fundamentos de Inteligência Artificial (UFMG). O objetivo é resolver o problema de coloração de grafos utilizando diferentes heurísticas de busca local e um algoritmo genético, além da heurística clássica **DSATUR**, comparando o desempenho em instâncias de referência.

## Estrutura

```
.
├── TP2_CSP_LocalSearch_GA.ipynb     # Notebook principal com todas as implementações
├── data
│   └── instances
│       ├── myciel3.col
│       └── queen5_5.col             # Instâncias adicionais do repositório COLOR
├── docs
│   └── TP_2_Fundamentos_IA_2025_2.pdf   # Enunciado original do trabalho
└── outputs
    ├── runtime_grafo_exemplo.png
    ├── runtime_myciel3_(color).png
    └── runtime_queen5_5_(color).png     # Gráficos de runtime distribution
```

## Conteúdo do Notebook

O notebook está dividido em quatro partes principais, alinhadas às tarefas do enunciado:

1. **Implementação das heurísticas**  
   - Random Walk (RW)  
   - Best Improvement (BI)  
   - First Improvement – Random Search (FI-RS)  
   - First Improvement – Any Conflict (FI-AC)  
   - Simulated Annealing (SA)  
   - Algoritmo Genético (GA)  
   - DSATUR

2. **Testes nas instâncias**  
   - Grafo de exemplo fornecido no notebook.  
   - Instâncias `myciel3.col` e `queen5_5.col`, obtidas em <https://mat.tepper.cmu.edu/COLOR/instances.html>.

3. **Análise de runtime**  
   - Execução repetida das heurísticas para gerar os gráficos de **runtime distribution** (`outputs/runtime_*.png`).

4. **Discussão dos resultados**  
   - Comparação de robustez, tempo médio e taxa de sucesso das heurísticas.

## Requisitos

- Python 3.8+
- Bibliotecas utilizadas no notebook: `random`, `math`, `statistics`, `matplotlib`, `pathlib`, `time` (todas inclusas na biblioteca padrão, exceto `matplotlib`).

Para instalar o `matplotlib`, caso ainda não tenha:

```bash
pip install matplotlib
```

## Como executar

1. Abra o notebook `TP2_CSP_LocalSearch_GA.ipynb` em um ambiente compatível (Jupyter, VS Code, Colab etc.).
2. Execute as células sequencialmente.  
   - As seções “Testando as heurísticas de Busca Local” e “Testando o algoritmo genético” reproduzem os testes individuais iniciais.
   - As seções posteriores automatizam testes nas instâncias externas e geram os gráficos.

Os gráficos gerados serão salvos na pasta `outputs/`.

## Resultados principais

- Instâncias simples (`grafo exemplo` e `myciel3`): todas as heurísticas atingiram zero conflitos rapidamente.
- Instância `queen5_5`: heurísticas puramente locais (RW, FI-RS) raramente chegam à solução; SA e GA têm taxas de sucesso menores, porém positivas; DSATUR resolve determinística e instantaneamente.
- Os gráficos de runtime evidenciam a diferença de desempenho: curvas próximas da origem para casos fáceis e caudas longas/lentas para heurísticas menos robustas no `queen5_5`.