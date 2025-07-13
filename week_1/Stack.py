'''
🧱 What is a Stack?

    A Stack is a linear data structure that follows the LIFO (Last-In, First-Out) principle.

Think of a stack of plates: the last plate you put on top is the first one you take off.



'''



class ArrayStack:
    
    def __init__(self,size):
        self.stack = [None] * size
        self.top = -1
        self.size = size
        
    def push(self,value):
        if slef.top == self.size - 1:
            return Exception('stack overflow')
        self.top += 1
        self.stack[self.top] = value
        
        
    def pop(self):
        if self.top == -1:
            return Exception('stack underflow')
        value = self.stack[self.top]
        self.top -= 1 
        return value
        
        
        




class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
        
class LinkedStack:
    def __init__(self,value):
        self.top = None
        
        
    def push(self,value):
        node = Node(vlaue)
        node.next = self.top
        self.top = node
        
    def pop(self):
        if self.top is None:
            raise Exception("Stack Underflow")
        value = self.top.value
        self.top = self.top.next
        return value
        