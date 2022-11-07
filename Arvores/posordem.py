class ClassPosordem:
    def posordem(self, Node):
        if Node == None:
            return None
        self.posordem(Node.getLeftChild)
        self.posordem(Node.getRightChild)
        print(Node.data)