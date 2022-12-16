#O código abaixo corresponde à versão iterativa do algoritmo de ordenação por seleção. Modifique o
#código e apresente sua versão recursiva.
def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]

array = [2, 4, 5, 1]
def SSR(array):
    if i == len(array)-1:
        return 
    min = 0
    for j in range( len(array)):
        if(array[j] < array[min]):
            min = j
    array[min], array[i] = array[i], array[min]
    SSR(array)

v = [5, 9, 7, 21, 18, 3, 1]
print(v)
SSR( v )
print(v)