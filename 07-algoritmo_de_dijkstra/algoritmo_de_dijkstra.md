# 📘 Capítulo 7 – Algoritmo de Dijkstra

## ⚡ O que é o Algoritmo de Dijkstra?

O **Algoritmo de Dijkstra** é uma técnica usada para encontrar o **caminho mais rápido** (de menor custo) entre dois pontos em um grafo **ponderado**, ou seja, um grafo cujas conexões têm **pesos**.

---

## 🧠 Etapas do algoritmo

O algoritmo segue 4 passos principais:
1. Encontre o vértice mais barato. Esse é o vértice que você consegue chegar no menor tempo possível
2. Verifique se há um caminho mais barato para os vizinhos desse vértice. Caso exista, atualize os custos deles
3. Repita até que você tenha feito isso para cada vértice do grafo
4. Calcule o caminho final

---

## 📏 O que são pesos?

- Cada **aresta** do grafo tem um número associado a ela, chamado de **peso**.
- Esse peso pode representar **distância**, **tempo**, **custo**, etc.
- Um grafo que possui pesos é chamado de **grafo ponderado**.

---

## ⚠️ Limitação importante

> ❗ O algoritmo de Dijkstra **não funciona corretamente com arestas que têm pesos negativos**.  
Se houver caminhos com custo negativo, você deve usar outro algoritmo, como o **Bellman-Ford**.

---
