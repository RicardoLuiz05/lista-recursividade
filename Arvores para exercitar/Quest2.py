from arvoreBi import Bi
from inordem import ClassIn

raiz = Bi('1')
raiz.insertLeft = Bi('2')
raiz.insertRight = Bi('3')

p = raiz.getLeftChild
q = raiz.getRightChild

p.insertRight = Bi('4')
q.insertLeft = Bi('5')
q.insertRight = Bi('6')


arvore = ClassIn()
arvore.inordem(raiz)

