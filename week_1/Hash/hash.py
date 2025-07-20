# Open Addressing

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



#  if the vlaue is delete and the its assigned None, a bug will occur during get()
#  solved by assigining self.DELETED to the index thats being deleted.
class HashTable:
    
    def __init__(self,size = 10):
        self.size = size
        self.table = [None] * size
        self.DELETED = object()
        
        
    def _hash(self,key):
        return hash(key) % self.size
        
    def insert(self,key,value):
        index = self._hash(key)
        original_index = index
        
        while self.table[index] is not None and self.table[index] != self.DELETED:
            k,v = self.table[index]
            if k == key:
                self.table[index] = (key,value)
                return 
            index = (index + 1) % self.size
            if index == original_index:
                return "hash table is  full"
        self.table[index]  = (key,value)
        
        
    def get(self,key):
        index = self._hash(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index] != self.DELETED:
                k,v = self.table[index]
                if k == key:
                    return v
                index = (index + 1) % self.size
                if index == original_index:
                    break
        return None
    
    def delete(self,key):
        index = self._hash(key)
        original_index = index
        
        while self.table[index] is not None:
            k,v = self.table[index]
            if k == key :
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
            if index == original_index:
                return False
                
                
    def display(self):
        for i , item in enumerate(self.table):
            print(f"{i}:{item}")
            
     

ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city","New york")
print(ht.get("name"))
print(ht.get("city"))
ht.delete("age")
ht.display()       
            
            
            
h = HashTable()
h.insert('name','don')
h.insert('age',20)
h.insert('city','ekm')
print(h.get('name'))
print(h.get('city'))
h.insert('city','kochi')
h.delete('age')
h.display()
        
        
        
        
        
        
        
        
        
                        
                
                
                
                
                
                
                
                
                
                
                
                
# Chaining


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






class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    
    def __init__(self,size=10):
        self.size = size
        self.table = [None] * size
        
    def _hash(self,key):
        return hash(key) % self.size
        
    def insert(self,key,value):
        index = self._hash(key)
        head = self.table[index]
        while head:
            if head.key == key:
                head.value = value
                return True
            head = head.next
        
        new_node = Node(key,value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        
        
    def get(self,key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
            
            
    def delete(self,key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False
        
    
    def display(self):
        for i,node in enumerate(self.table):
            print(f"{i}", end=" ")
            current = node
            while current:
                print(f"({current.key}:{current.value})", end =" ->")
                current =current.next
            print('None')
            
            
            
ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("gender", "female")
ht.insert("name", "Bob")  # Updates

print(ht.get("age"))      # 25
ht.delete("gender")
ht.display()

            