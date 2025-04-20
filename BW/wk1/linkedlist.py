class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->', end=" ")
                n = n.ref
        

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node



    def add_after(self,data, x):
        n = self.head
        while n is not None:
            if n == x:
                break
            n = n.ref
        if n is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node



    def add_before(self,data,x):
        if self.head is None:
            print('ll is empty')
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
            print('node not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

        
    def insert_empty(self,data):
        if self.head is None:
            new_node = None(data)
            self.head = new_node

        else:
            print('ll is not empty')

    def delete_begine(self):
        if self.head:
            self.head = self.head.ref
        else:
            print('ll is empty')

    def delete_end(self):
        if self.head is None:
            print('ll is empty')
        if self.head.ref == None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

        
    def delete_by_value(self,x):
        if self.head is None:
            print('ll is empty')
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
            print('value not found')
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
            if node is not None:
                _print_reverse(node.ref)
                print(node.data,'--->', end=" ")

        if self.head is None:
            print('ll is empty')
        else:
            _print_reverse(self.head)
            print('None')




    def find_middle(self):
        if self.head is None:
            print(None)
            return
        else:
            slow = self.head
            fast = self.head
            while fast and fast.ref:
                slow = slow.ref
                fast = fast.ref.ref
            print(slow.data,'middle')
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

                if slow = fast:
                    return True
            return False            


    def make_cycle(self):
        if self.head is None:
            print('ll is empty')
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = self.head


    

    def sorted_merge(self, a, b):

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= n.data:
            result = a 
            result.ref = self.sorted_merge(a.ref,b)

        else:
            result = b
            result.ref = self.sorted_merge(a,b.ref)

        return result


    def merge_sort(self,head):
        if head is None or head.ref is None:
            return head
    

        middle = self.get_middle(head)
        next_to_middle = middle.ref


        middle.ref = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)


        sorted_list = self.sorted_merge(left,right)

        return sorted_list


    def sort(self):
        self.head = self.merge_sort(sef.head)










class DNode:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None


class Doublell:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->', end=" ")
                n = n.ref
            

    def print_llreve(self):
        if self.head is None:
            print('ll is empty')
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, '--->', end=" ")
                n = n.pref

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
            print("vaulue not found")
        else:
            new_node = DNode(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node



    def add_before(self,data,x):
        if self.head is None:
            print('ll is empty')
        else :
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print('node was not found')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node


    def delete_byvalue(self,x):
        if self.head is None:
            print('linked list is empty')
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head is None
            else :
                print('calue not preentin the list')
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
                print('value not found')

