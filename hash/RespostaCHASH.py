while(True): 
                if i >= 10 and i%2 == 0:
                    # get rerash index
                    irh = self.__rh( i1, i2,i) + 1
  
                # if no collision occurs, store the key 
                    if (self.table[irh] == None):
                        self.table[irh] = key
                        break
                    i += 1

                # get rerash index
                irh = self.__rh( i1, i2,i)
  
                # if no collision occurs, store the key 
                if (self.table[irh] == None):
                    self.table[irh] = key
                    break 
                i += 1 