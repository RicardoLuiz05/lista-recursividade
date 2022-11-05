from arvoreBi import Bi
class ClassIn:
    def inordem(self, Node):
        if Node == None:
            return None
        inordem(Node.__leftChild)
        print(f'{Node}, ')
        inordem(Node.__rightChild)