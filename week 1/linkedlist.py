class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->',end=" ")
                n = n.ref
                
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head 
        self.head = new_node
        print(self.head.data,'llll')
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n  = self.head
            while n.ref is not None:
                n  =  n.ref
            n.ref = new_node
            
    def add_after(self,data,x):
        n =self.head
        while n is not None:
            if x == n.data:
                break
            n=n.ref
        if n is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def add_before(self,data,x):
        if self.head is None:
            print('linkedlist is empty')
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
            print('node node found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
        if self.head.ref == None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref
        if n.ref is None:
            print('value not found')
        else:
            n.ref = n.ref.ref

    def insertt(self,var):
        new_node = Node(var)
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
                print(node.data, '--->lll', end=" ")
        
        if self.head is None:
            print("Linked list is empty")
        else:
            _print_reverse(self.head)
            print("None")


    def find_middle(self):
        if self.head is None:
            print(None)
            return None
        else:
            slow = self.head
            fast = self.head
            while fast and fast.ref:
                slow  = slow.ref
                fast = fast.ref.ref
            print('\n',slow.data,'middle')
            return slow

            # self.next = next



# cycle in linkedlist
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
            print('ll is empty')
        else:
            n = self.head
            while n.ref is not None:
                n=n.ref
            n.ref = self.head




    def sorted_merge(self,a,b):

        if a is None:
            return b
        if b is None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.ref,b)
        else:
            result = b
            result.ref = self.sorted_merge(a,b.next)

        return result


    def get_middle(self,head):
        if head is None:
            return head
        
        slow = head 
        fast = head

        while fast.ref and fast.ref.ref:
            slow = slow.ref 
            fast = fast.ref.ref

        return slow
    


    def merge_sort(self,head):

        if head is None or head.ref is None:
            return head
        
        middle = self.get_middle(head)
        next_to_middle = middle.ref


        middle.ref = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)


        sorted_list = self.sorted_merge(left, right)

        return sorted_list
    

    def sort(self):
        self.head = self.merge_sort(self.head)






    
def array_to_linked(arr):
    LinkedListtt = LinkedList()
    for var in arr:
        LinkedListtt.insertt(var)
    LinkedListtt.print_ll()
    LinkedListtt.print_reverse_ll()
    LinkedListtt.print_ll()


arr = [1,3,2,4,2,5,3,6]
array_to_linked(arr)     

ll = LinkedList()
ll.add_end(200000)
ll.add_begin(10)
ll.add_end(100)
ll.add_begin(30)
ll.add_after(50,300)
ll.add_before(11,30)
ll.add_before(99,10)
ll.add_before(111111,100)
ll.insert_empty(44)
ll.insert_empty(455)
ll.delete_begin()
ll.delete_by_value(100)
ll.print_ll()
ll.find_middle()
ll.make_cycle()

result = ll.has_cycle()
if result:
    print('has cycle')
else:
    print('no cycle')