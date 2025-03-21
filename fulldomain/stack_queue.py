class Stack:
    def __init__(self):
        self.items =[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "emptyy"
        

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "empty"
        

    def is_empty(self):
        return  len(self.items) == 0
    
    def print(self):
        for item in reversed(self.items):
            print(item)







class Queue:
    def __init__(self):
        self.items =[]

    def eneque(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "emptyy"


    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0