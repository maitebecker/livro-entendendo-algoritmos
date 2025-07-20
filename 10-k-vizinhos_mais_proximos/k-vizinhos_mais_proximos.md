# 📘 Capítulo 10 – K-Vizinhos Mais Próximos (KNN)

## Classificando laranjas vs toranjas

Imagine que você quer classificar uma fruta como **laranja** ou **toranja**.  
Uma abordagem simples seria verificar quem são as **frutas mais próximas** a ela.

Se a maioria dos vizinhos for **laranja**, então é bem provável que a fruta também seja uma **laranja**.

Essa é a ideia central do algoritmo dos **K-vizinhos mais próximos (KNN)**:  
> **Classificar algo com base em seus vizinhos mais próximos.**

---

## Sistema de Recomendação

Suponha que você seja o dono da **Netflix** e queira criar um sistema de recomendação de filmes.

Você pode:

1. **Agrupar usuários por similaridade**, ou seja, usuários com gostos parecidos ficam próximos uns dos outros.
2. Comparar as **notas que deram a certos filmes**.

### 🧮 Como medir a similaridade?

Você pode usar a fórmula:
> distância = √((x₁ - x₂)² + (y₁ - y₂)²)

No contexto da Netflix:

- `x₁`, `y₁` são as notas que um usuário deu a dois filmes.
- `x₂`, `y₂` são as notas de outro usuário para os mesmos filmes.

Quanto **menor** a distância, mais parecidos os usuários.

---

## Classificação vs Regressão

O algoritmo KNN pode ser usado para dois tipos de problemas:

### 🟦 Classificação
- Objetivo: **classificar** algo em grupos (ex: fruta é laranja ou toranja).
- Exemplo: prever se um e-mail é spam ou não.

### 🟨 Regressão
- Objetivo: **prever um valor numérico** (ex: nota de um filme, preço de uma casa).
- Como funciona? Pegamos os K vizinhos mais próximos e **calculamos a média**.

---


