''' 

1. 🧩 What is a Deque?

A Deque (pronounced deck) is a linear data structure that allows insertion and deletion from both front and rear ends.

    Also known as: Double Ended Queue

    Unlike queues (FIFO) or stacks (LIFO), it offers flexibility.

2. 🔄 Types of Deques
✅ Input Restricted Deque

    Insertion allowed only at one end (usually rear)

    Deletion allowed at both ends

✅ Output Restricted Deque

    Deletion allowed only at one end (usually front)

    Insertion allowed at both ends




5. 🛠️ Applications of Deque

    Sliding Window Maximum (e.g. in Leetcode)

    Palindrome Checker

    Undo functionality in editors

    Job scheduling (allowing insertion/removal from both ends)

    Browser history (back and forward navigation)

✅ Summary

    Deque = Double-ended queue

    You can insert/delete at both ends

    Has specialized forms: input-restricted and output-restricted

    Powerful for performance-critical tasks like sliding window problems

'''


class Deque:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def append(self,item):
        self.items.append(item)
        
    def appendleft(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
            
    def popleft(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
        
    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]
        
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.items[-1]
        
        
dq = Deque()
dq.append(10)
dq.appendleft(5)
dq.append(15)

print(dq.pop())        # 15
print(dq.popleft())    # 5
print(dq.peek_front()) # 10
print(dq.peek_rear())  # 10

        
            
#  Array-Based (Fixed-Size)
class ArrayDeque:
    def __init__(self, size):
        self.deque = [None] * size
        self.size = size
        self.front = -1
        self.rear = 0

    def insertFront(self, item):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            print("Deque is Full")
            return
        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.deque[self.front] = item

    def insertRear(self, item):
        if (self.front == 0 and self.rear == self.size - 1) or (self.rear == self.front - 1):
            print("Deque is Full")
            return
        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.deque[self.rear] = item
