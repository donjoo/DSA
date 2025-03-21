class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->',end=" ")
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        print(self.head.data,'lllll')

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('x not preset')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print('linked is empty')
            return
        if self.head:
            if self.head.data == x:
                new_node = Node(data)
                new_node.ref = self.head
                self.head = new_node
                return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('no node found')
        else:
            new_node = Node(data)
            new_node.ref  = n.ref
            n.ref = new_node
        
     
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('ll is not empty')

    def delete_begin(self):
        if self.head is None:
            print('linked list is emptyy')
        else:
            self.head = self.head.ref

    
    def delete_end(self):
        if self.head is None:
            print('lll is empty')
            return
        if self.head.ref == None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None


    def delete_by_value(self,x):
        if self.head is None:
            print("linked l=empty")
            return 
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("value not found")
        else:
            n.ref = n.ref.ref

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

            


    def print_reverse_ll(self):
        def _print_reverse(node):
            if node is not None :
                _print_reverse(node.ref)
                print(node.data,'--->',end=" ")

        if self.head is None:
            print('ll is empty')
        else:
            _print_reverse(self.head)
            print('None')

    def find_middle(self):
        if self.head is None:
            print('None')
            return None
        else:
            slow = self.head
            fast = self.head
            while fast and fast.ref:
                slow = slow.ref
                fast = fast.ref.ref

            print(slow.data)
            return slow
    

    def has_cycle(self):
        if self.head is None:
            return False
        else:
            slow = self.head
            fast = self.head

            while fast and fast.ref:
                slow = slow.ref
                fast = fast.ref.ref

                if slow == fast:
                    return True
            return False
        
    def make_cycle(self):
        if self.head is None:
            print('lll is empty')
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = self.head

    
    def array_to_ll(arr):
        ll = LinkedList()
        for var in arr:
            ll.insert(var)



    
            



            