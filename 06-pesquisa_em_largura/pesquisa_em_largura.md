# 📘 Capítulo 6 – Pesquisa em Largura

## 🔍 O que é a Pesquisa em Largura?

A **pesquisa em largura** (*Breadth-First Search – BFS*) é um algoritmo que permite:

1. Verificar **se existe um caminho** entre dois vértices em um grafo.
2. Encontrar o **caminho mais curto possível** entre dois pontos.


---

## 🔗 O que é um Grafo?

Um **grafo** é um modelo usado para representar conexões entre objetos. Ele é composto por:

- **Vértices (ou nós):** os elementos (ex: pessoas, cidades).
- **Arestas:** as conexões entre os vértices (ex: amizades, estradas).
- Um vértice pode estar conectado a **vários vizinhos**.

**Exemplo de grafo:**
```
Você → Alice, Bob, Claire
Bob → Anuj, Peggy
Claire → Thom, Jonny
```
---

## 🔁 Como funciona a Pesquisa em Largura?

- A pesquisa começa no **vértice inicial** e explora **todos os vizinhos imediatos** (conexões de primeiro grau).
- Depois, explora os vizinhos dos vizinhos (segundo grau), e assim por diante.
- Por isso, a estrutura ideal para armazenar os elementos a serem pesquisados é uma **fila** (FIFO – First In, First Out).

---

## 🧰 Estruturas usadas

- **Fila**: para armazenar os próximos nós a serem visitados.
- **Tabela hash**: para manter controle dos nós já verificados e evitar ciclos.

---

## 🧠 Resumo do algoritmo

1. Crie uma fila e adicione os vizinhos do ponto de partida.
2. Enquanto a fila não estiver vazia:
   - Retire a próxima pessoa da fila.
   - Verifique se é a que você procura.
   - Caso não seja, adicione seus vizinhos à fila.
3. Marque as pessoas já verificadas para evitar repetições.

---

## ✅ Anotações
- Garante encontrar o **caminho mais curto** em grafos não ponderados (caminhos não tem peso)
- Uma árvore é um tipo especial de grafo em que nenhuma aresta aponta de volta
