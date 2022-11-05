from arvoreBi import Bi
from inordem import ClassIn

raiz = Bi('1')
raiz.__leftChild = Bi('2')
raiz.__rightChild = Bi('3')

p = raiz.__leftChild
q = raiz.__rightChild

p.__rightChild = Bi('4')
q.__leftChild = Bi('5')
q.__rightChild = Bi('6')


arvore = ClassIn()
arvore.inordem(raiz)

