class Node:
    def __init__(self,data):
        self.data = data 
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->',end=" ")
                n = n.ref
    def add_node(self,data):
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
                print(node.data,'--->',end=" ",)
        if self.head is None:
            print("linked list is empty")
        else:
            _print_reverse(self.head)
        
ll = LinkedList()
ll.print_ll()
ll.add_node(7)
ll.add_node(8)
ll.add_node(9)
ll.add_node(10)
ll.print_ll()   




def reverse_string(s):
    if len(s) <=1 :
        
        return s
    else:
        return s[-1] + reverse_string(s[:-1])    
        
s = 'donjorois'
print(reverse_string(s))


def reverse_strinnn(s):
    if len(s) <=1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    


def list_sum(arr):
    if len(arr)== 0:
        return 0
    else:
        return arr[0] + list_sum(arr[1:])
    

arr =[1,2,3,4,5,6]
print(list_sum(arr))



def binary_search(arr,low,high,key):
    if low<=high:
        mid = (low+high)//2
        if  arr[mid]  == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr,mid+1,high,key)
        else:
            return binary_search(arr,low,mid-1,key)
    else:
        return-1



arr = [2,9,7,3,8,5,4,6,1,3]
arr.sort()
print(arr)
result = binary_search(arr,low=0,high=len(arr),key = 3)
if result != -1:
    print('heyyyy',result)
else:
    print('not found')





def recurssion_pal(str):
    print(str)
    if len(str)<=1:
        return True
    if str[0]==str[-1]:
        return recurssion_pal(str[1:-1])
    return False
    
s = "A man, a plan, a canal, Panama"
cleaned_s = ''.join(e.lower() for e in s if s.isalnum())
print(recurssion_pal(cleaned_s),'resurrsionPalll')