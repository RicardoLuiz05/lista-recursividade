def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]

# main
v = [5, 9, 7, 21, 18, 3, 1]
print(v)
selectionSort( v )
print(v)