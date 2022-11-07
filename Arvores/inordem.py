class ClassIn:
    def inordem(self, Node):
        if Node == None:
            return None
        self.inordem(Node.getLeftChild)
        print(f' {Node.data}, ', end ='')
        self.inordem(Node.getRightChild)