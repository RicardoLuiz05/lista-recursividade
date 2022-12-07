def quickSort(array):
    quickSortRun(array,0,len(array)-1)

def quickSortRun(array,low,high): 
    if low < high:  
        pi = partition(array,low,high) 
        quickSortRun(array, low, pi-1) 
        quickSortRun(array, pi+1, high) 
	

def partition(array,low,high):
    pivot = array[low]
    a = low + 1
    b = high
    

    while(True):
        while( a <= high  and array[a] <= pivot ):
            a+=1

        while( array[b] > pivot):
            b-=1

        if ( a < b ):
            array[a],array[b] = array[b],array[a]
            a+=1
            b-=1
			
        if( a > b):
            break

    array[low] = array[b]
    array[b] = pivot

    return ( b )   
    	
print('Algoritmo de Ordenação - QuickSort')
print('*' * 45)
array = [20,5,15,4,2,9,11]
print(' Array Original:',array)
quickSort(array)
print(' Array Ordenada:', array)