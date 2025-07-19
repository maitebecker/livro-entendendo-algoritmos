# Maior substring comum
def maior_substring_comum(a, b):
    linhas = len(a) + 1
    colunas = len(b) + 1
    tabela = [[0] * colunas for _ in range(linhas)]
    maior_valor = 0
    fim_substring = 0  # para saber onde termina a substring

    for i in range(1, linhas):
        for j in range(1, colunas):
            if a[i - 1] == b[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
                if tabela[i][j] > maior_valor:
                    maior_valor = tabela[i][j]
                    fim_substring = i
            else:
                tabela[i][j] = 0

    substring = a[fim_substring - maior_valor: fim_substring]
    return maior_valor, substring


# Exemplo
a = "HISH"
b = "FISH"
tamanho, substring = maior_substring_comum(a, b)
print(f"Maior substring comum: '{substring}' com tamanho {tamanho}") #Maior substring comum: 'ISH' com tamanho 3

# Maior subsequencia comum
def maior_subsequencia_comum(a, b):
    linhas = len(a) + 1
    colunas = len(b) + 1
    tabela = [[0] * colunas for _ in range(linhas)]

    for i in range(1, linhas):
        for j in range(1, colunas):
            if a[i - 1] == b[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])

    # Reconstruindo a subsequência
    subsequencia = ""
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            subsequencia = a[i - 1] + subsequencia
            i -= 1
            j -= 1
        elif tabela[i - 1][j] >= tabela[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return tabela[-1][-1], subsequencia


# Exemplo
a = "FOSH"
b = "FISH"
tamanho, subsequencia = maior_subsequencia_comum(a, b)
print(f"Maior subsequência comum: '{subsequencia}' com tamanho {tamanho}") #Maior subsequência comum: 'FSH' com tamanho 3
