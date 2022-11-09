class ClassPreordem:
    def preordem(self, Node):
        if Node != None:
            print (f'{Node.data}, ', end='')
            self.preordem(Node.getLeftChild)
            self.preordem(Node.getRightChild)