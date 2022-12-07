# Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma
# seria igual a 1 + 2 + 3 = 6

def soma(n):
    if n == 0:
        return n
    return soma(n-1) + n

print(soma(3))