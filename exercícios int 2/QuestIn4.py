
# Defina a função media_digitos que recebe como argumento um número natural e devolve
# a média dos seus digitos.
def media_digitos(N:int) -> float:
    N = str(N)
    if N == '':
        return 0
    elif N :
        return (int(n[0]) + media_digitos(N[1:]))
    return N / len[n]

print(media_digitos(1234))