class HashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self,key):
        return sum(ord(char) for char in str(key)) % self.size


    def insert(self,key,value):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                self.table[index] = (key,value)
                return 
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("hash table is full")

        self.table[index] = (key, value)



    def get(self, key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            k, v = self.table[index]
            if k== key:
                return v
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

    def display(self):
        for i , item in enumerate(self.table):
            print(f"{i}: {item}")



ht = HashTable()

ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city","New york")

print(ht.get("name"))
print(ht.get("city"))

ht.delete("age")

ht.display()


