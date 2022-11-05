class Bi:
    def __init__(self, data):
        self.data = data
        self.__leftChild = None
        self.__rightChild = None

    def insertLeft(self, data):
        if self.__leftChild == None:
            self.__leftChild == Node(data)

    def insertRight(self, data):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def getRightChild(self):
        return self.__rightChild

    def getleftChild(self):
        return self.__leftChild

    def setValue(self, newValue):
        self.data = newValue

    def getValue(self):
        return self.data

