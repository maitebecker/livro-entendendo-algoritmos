# 📘 Capítulo 2 – Ordenação por Seleção

## 🧠 Como funciona a memória
- Cada vez que quer armazenar um item na memória, você pede ao computador um pouco de espaço e ele te dá um endereço no qual você pode armazenar o seu item
- Se quiser armazenar múltiplos itens, existem duas maneiras: arrays e listas

### 📦 Arrays (Vetores)
- Os elementos são armazenados **em posições contíguas** na memória (lado a lado).
- Você **reserva previamente** o espaço necessário, o que pode gerar **desperdício de memória**.
- Como os itens estão em ordem, você pode **acessar diretamente qualquer posição** (acesso aleatório rápido).

### 🔗 Listas Encadeadas
- Os elementos **podem estar espalhados pela memória**.
- Cada item contém o **endereço do próximo item**, formando uma cadeia.
- São **melhores para inserções e deleções**, especialmente no meio da lista.
- Não são boas para acesso aleatório, pois é necessário percorrer a lista item por item.

### ⏱️ Tempo de execução
| Operação    | Arrays                     | Listas                        |
|--------------|--------------------------|----------------------------------|
|  LEITURA   | `O(1)`          | `O(n)`          | 
|  INSERÇÃO   | `O(n)`          | `O(1)`          | 
|  ELIMINAÇÃO   | `O(n)`          | `O(1)`          | 
> `O(1)` significa que a operação leva tempo constante – como acessar o item diretamente.  
> `O(n)` significa que a operação depende do número de elementos.

------
## 🔢 Ordenação por Seleção

- A **ordenação por seleção** (selection sort) é um algoritmo simples de ordenação.
- Embora seja fácil de entender, **não é eficiente para listas grandes**.
- Seu tempo de execução é `O(n²)` — ou seja, **lento em grandes volumes** de dados.
- O **QuickSort** é uma alternativa mais eficiente, com tempo médio `O(n log n)`.