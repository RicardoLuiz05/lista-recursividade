# Implemente uma função recursiva que,
# dados dois números inteiros x e n, calcula o
# valor de xn.

def multi(x, n):
    if n == 0:
        return 0

    return multi(x, n-1) + x

print(multi(9, 9))