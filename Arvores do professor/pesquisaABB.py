def search(self, chave):
    if(self.__root != None):
        return self.__serchData(chave, self.__root)
    else:
        return None

def __serchData(self, chave, node):
    if(chave == node.data):
        return node

    elif (chave < node.data and node.left != None):
        return self.__serchData(chave, node.left)
    
    elif (chave > node.data and node.right != None):
        return self.__serchData(chave, Node.right)

    else:
        return None