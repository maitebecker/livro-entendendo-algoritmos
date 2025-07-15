def regressiva(i):
    print(i)
    if i<=1: #caso base
        return
    else:
        regressiva(i-1) #caso recursivo

regressiva(10) # retorno 10, 9, 8, 7...


def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)
    
print(fatorial(3)) # retorno 6