#Exemplo que evita duplicidades:
votaram = {}
def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = True
        print("Deixe votar!")

verifica_eleitor("tom") # Deixe votar!
verifica_eleitor("mike") # Deixe votar!
verifica_eleitor("mike") # Mande embora!