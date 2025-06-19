class HashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self,key):
        return sum(ord(char) for char in str(key)) % self.size
        # return hash(key) % self.size

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












class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return






