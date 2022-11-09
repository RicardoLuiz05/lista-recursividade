
class Bi:
    def __init__(self, data= None):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, novo):
        self.__data = novo

    @property
    def getLeftChild(self):
        return self.__leftChild

    @getLeftChild.setter
    def insertLeft(self, novo):
        if self.__leftChild == None:
            self.__leftChild = novo

    @property
    def getRightChild(self):
        return self.__rightChild

    @getRightChild.setter
    def insertRight(self, novo):
        if self.__rightChild == None:
            self.__rightChild = novo

    # def setValue(self, newValue):
    #     self.data = newValue

    # def getValue(self):
    #     return self.data

