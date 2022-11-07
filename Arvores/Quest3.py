from arvoreBi import Bi
from preordem import ClassPreordem

raiz = Bi('1')
raiz.insertLeft = Bi('2')
raiz.insertRight = Bi('3')

P1 = raiz.getLeftChild
P2 = raiz.getRightChild

P1.insertRight = Bi('4')

P2.insertLeft = Bi('5')
P2.insertRight = Bi('6')

arvore = ClassPreordem()
arvore.preordem(raiz)