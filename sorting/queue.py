"""

A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed. Think of it as a line of people waiting: the person who gets in line first is the first one to be served.

Operations

    Enqueue: Add an element to the end of the queue.
    Dequeue: Remove the front element from the queue.
    Front: View the front element without removing it.
    IsEmpty: Check if the queue is empty.


"""

class Queue:
    def __init__(self):
        self.items =[]
    
    def eneque(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    



gg = Queue()
gg.eneque(6)
gg.eneque(3)
gg.eneque(9)
print(gg.front())
print(gg.is_empty())