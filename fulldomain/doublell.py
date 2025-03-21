class Node:
    def __Init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None


class doubleell:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->", end = "")

    def print_llreverse(self):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n = n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("not empty")

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
                self.head  = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n


    def add_after(self,data,x):
        if self.head is None:
            print("em")
            return
        
        n =self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("not found")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node
            
    
    def add_before(self,data,x):
        if self.head is None:
            print("lll is emptyyyy")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("not found")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref 
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node

    
