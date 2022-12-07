def crescente(list:list):
    if len(list) <= 1:
        return True
    elif list[0] <= list[1]:
        return crescente(list[1:])
    return False

print(crescente('54321'))