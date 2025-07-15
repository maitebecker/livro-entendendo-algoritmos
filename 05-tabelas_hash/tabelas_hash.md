# 📘 Capítulo 5 – Tabelas Hash

## 🔑 Funções Hash

- Uma **função hash** mapeia consistentemente uma chave (como um nome) para o mesmo índice de um array.
- Ela tem conhecimento sobre o **tamanho do array** e sempre retorna **índices válidos**.
- Uma função hash, quando combinada com um array, forma uma **tabela hash**.
- Também são conhecidas como: **mapas hash**, **mapas**, **dicionários** ou **tabelas de dispersão**.
- Tabelas hash são extremamente **rápidas**.
- Elas armazenam dados em **pares chave-valor**, permitindo buscas rápidas por chave.

---

## 🧩 Utilização

- São amplamente utilizadas em **operações de pesquisa**.
- Muito úteis para **modelar relações** entre dois itens (ex: nome → telefone).
- Ajudam a **evitar duplicidades**, garantindo que cada chave seja única.

---

## 💥 Colisões
- Isso acontece quando duas chaves são indicadas para o mesmo endereço
- Pode ser utilizado uma lista encadeada para dois elementos ocuparem o mesmo espeço, porém isso pode diminuir o tempo de execução 

---

## 🚀 Desempenho

| Operação   | Arrays   | Listas Encadeadas | Tabelas Hash |
|------------|----------|-------------------|--------------|
| **Busca**  | `O(1)`   | `O(n)`            | `O(1)`       |
| **Inserção** | `O(n)` | `O(1)`            | `O(1)`       |
| **Remoção** | `O(n)`  | `O(1)`            | `O(1)`       |

> ℹ️ Obs: Tabelas hash oferecem desempenho constante (`O(1)`) na média, mas podem ter desempenho pior em casos de colisão.


