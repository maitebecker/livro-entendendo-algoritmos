# 📘 Capítulo 4 – QuickSort

## 🧠 Dividir para Conquistar

Para resolver um problema usando recursão, siga dois passos fundamentais:

1. **Descubra o caso base**, que deve ser o mais simples possível.
2. **Divida ou reduza o problema** até que ele se torne o caso base.

> 💡 Dica: quando escrevemos uma função recursiva para um array, o caso base geralmente será um array vazio ou com apenas um elemento.

Um exemplo disso pode ser visto no arquivo `soma.py`. A função analisa a lista e:

- Se estiver vazia, retorna zero;
- Caso contrário, retorna o primeiro número da lista somado à chamada da função para o restante da lista.

---

## ⚡ QuickSort

O QuickSort é um algoritmo de ordenação mais eficiente do que a ordenação por seleção.

Sua lógica se baseia em:

1. Criar um subarray com os elementos **menores** que o pivô;
2. Definir o **pivô**;
3. Criar outro subarray com os elementos **maiores** que o pivô.

Após essa separação, aplicamos o QuickSort recursivamente nos dois subarrays.

> 🔍 A performance do QuickSort depende bastante da escolha do pivô, que influencia diretamente na eficiência da ordenação.

---

