def buscaTransposição(chave:int, array:list[int])->int:
    for i in range(len(array)):
        if array[i] == chave:
            if i != 0:
                array[i], array[i-1] == array[i-1], array[i]
            return i
    return -1

def buscar(chave:int, array:list[int]):
    chave = buscaTransposição(chave, array)
    if chave == -1:
        return'KeyError.'
    return chave

array:list = [2, 7, 80, 50, 70, 20]
print (buscar(50, array))