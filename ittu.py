def insertionSortRecursive(arr,n):
    if n<=1:
        return
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1]= last
    print('last:', last,'array:',arr)

# Main program to test insertion sort
array = [12,3,13,5,6,8,14]
size = len(array)
insertionSortRecursive(array, size)