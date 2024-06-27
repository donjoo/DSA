"""
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
This means that the last element added to the stack will be the first one to be removed. 
Think of it as a stack of plates: you can only take the top plate off first.
Operations

    Push: Add an element to the top of the stack.
    Pop: Remove the top element from the stack.
    Peek/Top: View the top element without removing it.
    IsEmpty: Check if the stack is empty.

"""

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "emptyyyy"
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'emptyyy'
        
    def is_empty(self):
        return len(self.items) == 0
    def print(self):
        for item in reversed(self.items):
            print(item)

ll=Stack()
ll.push(2)
ll.push(6)
ll.push(5)
ll.print()
ll.peek()
ll.pop()
ll.print()
