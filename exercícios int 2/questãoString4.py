#Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário

def invertString(s):
    if s == "":
        return s
    else:
        return invertString(s[1:]) + s[0]

print(invertString('amoR'))