from binary_tree_exception import BinaryTreeException
class Node:
    def __init__(self, dado= None):
        self.__dado = dado
        self.__esq = None
        self.__dir = None

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, novo):
        self.__dado = novo

    @property
    def esq(self):
        return self.__esq

    @esq.setter
    def esq(self, novo):
        if self.__esq != None:
            raise BinaryTreeException(('Nó esquerdo já existente'))
        self.__esq = novo

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, novo):
        if self.__dir != None:
            raise BinaryTreeException(('Nó direito já existente'))
        self.__dir = novo