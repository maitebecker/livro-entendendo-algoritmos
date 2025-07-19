# 📘 Capítulo 8 – Algoritmos Gulosos

## 🧠 O que são Algoritmos Gulosos?

Um **algoritmo guloso** toma a melhor decisão possível em **cada etapa**, com a esperança de que isso levará a uma **solução global ideal**.

⚠️ Nem sempre os algoritmos gulosos garantem a **melhor solução possível**, mas geralmente chegam **bem perto**, de forma eficiente.

---

### 🎓 Exemplo Clássico

> Tenho apenas **uma sala de aula** e quero agendar o **máximo de aulas possíveis**.  
> A estratégia gulosa é escolher **sempre a aula que termina mais cedo**, ocupando o espaço restante com as próximas aulas compatíveis.

---

## 🧩 Cobertura de Conjuntos

Quando é necessário **muito tempo computacional** para calcular a **solução exata**, usamos um **algoritmo de aproximação**.

🧪 **Algoritmos de aproximação** são avaliados por:

1. ✅ Sua **velocidade**
2. 🎯 O quão **próxima** está sua resposta da **solução ideal**

- Você tem um **conjunto de elementos** que deseja cobrir (ex: cidades).
- Tem também vários **subconjuntos**, cada um cobrindo parte desses elementos (ex: rádios que cobrem cidades).
- O objetivo é escolher o **menor número de subconjuntos** que, juntos, cubram **todos os elementos**.
> 📁 No arquivo `algoritmos_gulosos.py`, há um exemplo prático de **cobertura de conjuntos usando algoritmo guloso**.

---

## Conjunto
- União significa combinar os dois conjuntos -> Lógica **OU**
- Intersecção, significa encontrar os itens que aparecem nos dois conjuntos -> Lógica **E**
- Diferença, significa subtrair os itens de um conjunto dos itens de outro conjunto

---
## 🧩 Problemas NP-Completos
- São problemas difíceis de resolver com algoritmos exatos (levam muito tempo conforme crescem).
- Por isso, usamos algoritmos de aproximação quando estamos tentando resolver um problema de NP-completo
- Algoritmos gulosos são bons algoritmos de aproximação 