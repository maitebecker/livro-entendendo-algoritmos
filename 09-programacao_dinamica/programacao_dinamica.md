# 📘 Capítulo 9 – Programação Dinâmica

## 🧠 O que é Programação Dinâmica?

A **programação dinâmica (PD)** é uma técnica usada para resolver problemas complexos dividindo-os em **subproblemas menores** e armazenando os resultados já calculados em uma **tabela (matriz)** para evitar cálculos repetidos.

---

## 🎒 Exemplo Clássico – Problema da Mochila

Imagine que você é um **ladrão** com uma mochila que suporta até **4 kg** e quer levar os itens com o **maior valor possível**.

### Itens disponíveis:

- **Rádio**: R$3000 – 4kg  
- **Notebook**: R$2000 – 3kg  
- **Violão**: R$1500 – 1kg  

### Tabela de valores (peso máximo da mochila nas colunas):

| Item \ Peso | 1kg  | 2kg  | 3kg  | 4kg   |
|-------------|------|------|------|--------|
| Violão      | 1k5  | 1k5  | 1k5  | 1k5    |
| Rádio       | 1k5  | 1k5  | 1k5  | 3k     |
| Notebook    | 1k5  | 1k5  | 2k   | **3k5** |

✅ **Melhor combinação**: **Violão + Notebook** (1kg + 3kg = 4kg → R$1500 + R$2000 = R$3500)

---

### 🧮 Fórmula usada para preencher a tabela:

Cada célula `CELULA[i][j]` representa o **valor máximo** que pode ser obtido considerando os `i` primeiros itens e `j` quilos disponíveis na mochila.

```text
CELULA[i][j] = máximo entre:
1. O máximo anterior(valor da cédula [i-1][j]) 
2. Valor do item atual + valor do espaço restante (CELULA[i-1][j-PESO DO ITEM])
```

## 🔍 Maior Substring Comum (Substring Contínua)

Exemplo: O usuário digitou `"HISH"`. Qual palavra ele queria digitar? `"FISH"` ou `"VISTA"`?

Construímos uma tabela comparando letra por letra:

|     | H | I | S | H |
|-----|---|---|---|---|
| F   | 0 | 0 | 0 | 0 |
| I   | 0 | 1 | 0 | 0 |
| S   | 0 | 0 | 2 | 0 |
| H   | 1 | 0 | 0 | **3** |

📌 **Regra**:
- Se as letras **combinam**, somamos **1 ao valor da diagonal superior esquerda**.
- O **maior número da tabela** indica o **tamanho da maior substring comum**.

✅ Neste caso, `"ISH"` aparece tanto em `"HISH"` quanto em `"FISH"` → **tamanho 3**.

---

## 🧬 Maior Subsequência Comum (Subsequência Não Contínua)

Exemplo: O usuário digitou `"FOSH"`. Ele queria digitar `"FISH"` ou `"FORT"`?

Tabela de comparação:

|     | F | O | S | H |
|-----|---|---|---|---|
| F   | 1 | 1 | 1 | 1 |
| I   | 1 | 1 | 1 | 1 |
| S   | 1 | 1 | 2 | 2 |
| H   | 1 | 1 | 2 | **3** |

📌 **Regras**:
- Se as letras **combinam**, somamos **1 ao valor da diagonal superior esquerda**.
- Se **não combinam**, usamos o **maior valor entre o de cima ou o da esquerda**.

✅ Neste caso, a subsequência `"FSH"` está presente em `"FOSH"` e `"FISH"` → **tamanho 3**.

---