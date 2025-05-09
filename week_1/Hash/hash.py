class HashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self,key):
        return hash(key) % self.size


    def insert(self,key,value):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                self.table[index] = (key,value)
                return
                 
