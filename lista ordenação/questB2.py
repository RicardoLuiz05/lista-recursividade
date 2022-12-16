def getIndiceDuplicatas(chave:int, array:list[int])->tuple:
    armaz = []
    for i in range(len(array)):
        if array[i] == chave:
            armaz.append(i)
    return armaz

array:list = [2, 7, 80, 50, 70, 20, 2, 4, 2, 70, 30]
print(getIndiceDuplicatas(2, array))