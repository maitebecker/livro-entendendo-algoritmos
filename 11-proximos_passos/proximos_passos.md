# 📘 Capítulo 11 – Próximos Passos

Neste capítulo, o autor apresenta um resumo de conceitos e algoritmos importantes que **não foram explorados a fundo** no livro, mas que são amplamente utilizados na prática.

---

## 🌳 Árvores

- Quando um usuário acessa o Facebook, o sistema precisa verificar se esse usuário realmente existe.
- Isso **poderia** ser feito com uma **busca binária**, mas se novos usuários forem adicionados, o array precisaria ser reordenado — o que é ineficiente.
- A **árvore binária de busca** resolve isso ao inserir novos usuários diretamente no local correto, sem a necessidade de reordenação.
- Em uma árvore binária:
  - Nós à **esquerda** são **menores** que o nó atual.
  - Nós à **direita** são **maiores**.
- **Desvantagem:** não permite acesso aleatório como arrays.
- Para garantir boa performance, as árvores devem ser **balanceadas**.

---


## 🧩 Índices Invertidos

- Imagine uma tabela hash onde:
  - As **chaves** são palavras.
  - Os **valores** são as páginas onde essas palavras aparecem.
- Isso é um **índice invertido**, estrutura usada para **mapear palavras para os locais onde ocorrem**.
- Muito útil em **ferramentas de busca** como o Google.

---


## 🎵 Transformada de Fourier

- Dado um **smoothie**, a transformada de Fourier determina os **ingredientes** dele.
- Dada uma **música**, ela separa a composição nas **frequências individuais**.
- Usada no formato **MP3** para eliminar sons que não são perceptíveis ao ouvido humano.
- Permite **compressão eficiente** de dados de áudio.

---


## 🧠 Algoritmos Paralelos

- Existem versões paralelas de algoritmos como o **Quicksort**, que podem ordenar arrays em tempo **O(n)**.
- São extremamente eficientes, mas **difíceis de projetar e implementar** corretamente.

---

## 🗺️ MapReduce

- O **MapReduce** é um algoritmo **distribuído popular**, usado em frameworks como o **Apache Hadoop**.
- Baseado em duas operações simples:
  1. **Map**
  2. **Reduce**

### 🔹 Função map

- Aplica uma função a **cada item de um array**.
  
```python
arr1 = [1, 2, 3]
arr2 = map(lambda x: 2 * x, arr1)  # retorna [2, 4, 6]
```

### 🔹 Função reduce

Reduz um array a um único valor.

```python
from functools import reduce

arr1 = [1, 2, 3, 5, 5]
total = reduce(lambda x, y: x + y, arr1)  # retorna 16
```
---
## 🧪 Filtros de Bloom e HyperLogLog
Quando se tem um conjunto muito grande e você quer verificar se um item pertence a ele, usar tabelas hash pode ser inviável devido ao tamanho.

### 🔸 Filtros de Bloom
- Estrutura de dados probabilística.
- Responde se um item possivelmente está presente (pode haver falso positivo, mas nunca falso negativo).
- Muito eficientes em termos de espaço e velocidade.

### 🔸 HyperLogLog
- Estima quantos elementos únicos existem em um conjunto.
- Também fornece uma resposta aproximada, com baixo consumo de memória.
- Ideal para análise de grandes volumes de dados.

---

## 🔐 Algoritmos SHA
- SHA (Secure Hash Algorithm) é um algoritmo que gera um resumo digital (hash) de uma string.
- Cada string de entrada gera uma hash única.
- É irreversível: não é possível obter a string original a partir da hash.
- Aplicações: Verificar se dois arquivos são iguais, armazenar senhas de forma segura.

 ---

## 🔑 Troca de Chaves de Diffie-Hellman
- Como você encriptaria uma mensagem para que ela pudesse ser lida apenas pelo destinatário?
- A troca de chaves Diffie-Hellman contém duas chaves: uma pública e uma chave primária
- Uma chave encriptada pode ser decotificada apenas com a utilização de uma chave privada. Assim, enquanto você for a única pessoa com a chave privada, somente você será capaz de decodificar as mensagens 