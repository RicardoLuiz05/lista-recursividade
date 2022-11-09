# Usando recursividade, calcule a soma de
# todos os valores de um array de reais.

def reais(n):
    
    if n == []:
        return 0

    return reais(n[1:]) + n[0]

print(reais([1, 2, 3]))