# Defina a função prim_alg que recebe como argumento um número natural e
# devolve o primeiro algarismo (o mais significativo) na representação decimal de  n .

def prim_alg(n):
    n = str(n)
    if len(n) == 1:
        return n
    return prim_alg(n[:-1])

#return n if len(n) == 1 else return prim_alg(n[:-1])

print(prim_alg(10023))