class Entry:
    """Uma classe privada utilizada para encapsular os pares chave/valor"""
    __slots__ = ( "key", "value" )
    def __init__( self, entryKey, entryValue ):
        self.key = entryKey
        self.value = entryValue
        
    def __str__( self ):
        return "(" + str( self.key ) + ", " + str( self.value ) + ")"
 
class ChainHashTable:
    def __init__(self, size=10):
        self.size = size
        # inicializa a tabela de dispersão com todos os elementos iguais a None
        self.table = list([] for i in range(self.size))


    def hash(self, key:int)->int:
        ''' Método que retorna a posição na tabela hashing conforme a chave.
            Método do hash modular
        '''
        return key % self.size

    def put(self, key:int, data:object)->int:
        '''Insere um par chave/valor na tabela hash.
           Retorna o slot em que o par chave/valor foi inserido'''
        slot = self.hash(key)
        print(f'key {key} at slot {slot}')

        # verifica se a chave está no list relativo ao slot
        if key in self.table[slot]:
            return -1
        else:
            self.table[slot].append(Entry(key,data))
            return slot

    def get(self, key:int):
        '''Obtem a carga associada à chave de busca.'''
        slot = self.hash(key)
        if key not in self.table[slot]:
            return -1
        else:            
            return self.table[slot]

   
    def __str__(self):
        info = ""
        for items in self.table:
            if items == None:
                continue
            for entry in items:
                info += str(entry)
        return info

    def __len__(self):
        return self.size
         

 
    def keys(self):
        """Retorna uma lista de chaves na hashTable fornecida.
       (Seria melhor retornar uma sequência, mas isso
         é muito avançado.)
        """
        result = []
        for lst in self.table:
            if lst != None:
                for entry in lst:
                    result.append( entry.key )
        return result

   
    def getr( hTable, key ):
        """Retorna o valor associado à chave dada em
       a tabela de hash fornecida.
           Pré-condição: contém (hTable, chave)
        """
        entry = _locate( hTable, key )
        return entry.value

    def locate( hTable, key ):
        """Encontre a entrada na tabela de hash para a chave fornecida.
       Se a chave não for encontrada, encontre o primeiro local não utilizado na tabela.
       (Isso é chamado de 'endereçamento aberto'.)
       Se a entrada para a chave for encontrada, essa entrada será retornada.
       Caso contrário, o índice int onde a chave iria na tabela é retornado.
       Finalmente, se a chave não for encontrada e nenhum local não utilizado for deixado,
            o int -1 é retornado.
       Esta função deve ser chamada apenas de dentro da hashtable.
       Os chamadores desta função devem estar preparados para
       lidar com resultados de dois tipos diferentes, a menos que
       tem certeza absoluta se a chave está na tabela
       ou não.
        """
        index = self.hash( key )

        if self.table[index] == None:
            return

        for i,entry in enumerate(self.table[index]):
             if entry.key == key:
                 return i

        return -1

    def contains( self, key ):
        """Retorna True se hTable tiver uma entrada com a chave fornecida."""
        entry = _locate( hTable, key )
        return isinstance( entry, _Entry )

    def displayTable(self):
        entrada = -1
        for items in self.table:
            entrada += 1
            print(f'Entrada {entrada:2d}: ', end='') 
            if len(items) == 0:
                print(' None')
                continue
            for entry in items:
                print(f'[ {entry.key},{entry.value} ] ',end='')
            print()
            
           
# main function
size = int(input("Enter the Size of the hash table : "))
table1 = ChainHashTable(size)
 
# storing elements in table
table1.put(12,'alex')
table1.displayTable()
input()

table1.put(12,'alex sandro')
table1.displayTable()
input()
table1.put(31,'nathan')
table1.put(90,'alice')

print('len',len(table1))

table1.put(28,'matheus')
table1.put(88,'duda')
table1.put(17,'jessika')
table1.put(22,'bruno')
table1.displayTable()
input()
print('get():', table1.get(12))
table1.displayTable()
 
