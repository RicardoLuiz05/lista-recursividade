def particiona(array, inicio, fim):
    pivot = array[fim] # pivot
    i = ( inicio - 1 ) # indice do menor elemento

    for j in range(inicio , fim):
    # Se o elemento corrente é menor ou igual ao pivo, efetua a troca
        if array[j] <= pivot:
        # incrementa o indice do menor elemento
            i = i+1
            array[i],array[j] = array[j],array[i]

    array[i+1],array[fim] = array[fim],array[i+1]
    return ( i+1 )
def quickSort(array,inicio,fim):
    if inicio < fim:
    # pi é o indice de particionamento, correspondente ao posicionamento do pivot.
    # Assim, o pivot está na sua devida posição
        ip = particiona(array,inicio,fim)
        print(array)
        # Separadamente, aplica o método de ordenação antes e depois do ponto
        # de particionamento
        quickSort(array, inicio, ip-1)
        quickSort(array, ip+1, fim)
array = [54,28,61,12,7,85,97,2,71,44]
print('Array Inicial:',array)
quickSort(array,0,len(array)-1)
print('Array Ordenado:',array)