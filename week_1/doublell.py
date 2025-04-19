class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref =None

class doublell:
    def __init__(self):
        self.head = None 

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.nref

    def print_llreverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,'--->',end=" ")
                n = n.pref
    
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head 
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    
    def add_after(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("value not found")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("node was not found")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("deleted ,linked list empty now")
        else:
            self.head = self.head.nref
            self.head.pref = None
    
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("deleted,linked lidst is now empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    
    def delete_by_value(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print('value not present in list')
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:     
            if n.data == x:
                n.pref.nref = None
            else:
                print('value not present')

    def insertt(self,var):
        new_node = Node(var)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

def array_to_double(arr):
    ll = doublell()
    for var in arr:
        ll.insertt(var)
    ll.print_ll()
            

arr = [1,2,3,4,5,6]
array_to_double(arr)
dd = doublell()
# dd.insert_empty(100)
dd.add_begin(55)
dd.add_begin(66)
dd.add_end(12)
dd.add_begin(50)
dd.add_begin(45)
dd.add_end(29)
dd.add_after(33,29)
dd.add_before(77,45)
dd.delete_begin()
# dd.delete_end()
# dd.delete_end()
dd.delete_by_value(333)
dd.print_ll()
# dd.print_llreverse()


