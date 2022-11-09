def menores_rec(lista , key):
    if lista == '':
        return ''

    elif lista[0] < key:
        return menores_rec(lista[-1], key) + 1

    else:
        return menores_rec(lista[-1], key)

print(menores_rec('30, 40, 80, 90', '30'))
    