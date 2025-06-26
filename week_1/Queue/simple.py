# 1. 🚦 What is a Queue?

# A Queue is a linear data structure that follows the FIFO (First In, First Out) principle.

#     Think of a queue at a ticket counter: the person who gets in first is served first.

# 2. 🧱 Types of Queues
# 1. Simple Queue

#     Basic FIFO queue.

#     Insertion from rear, deletion from front.

# 2. Circular Queue

#     The last position is connected to the first to make a circle.

#     Efficient memory usage (no "wasted" space at the front).

# 3. Priority Queue

#     Elements are dequeued based on priority, not just order.

#     Can be implemented using heaps.

# 4. Deque (Double Ended Queue)

#     Insertion and deletion from both ends.

#     Can be input restricted or output restricted.


# 5. 🛠️ Applications of Queue

#     CPU Scheduling

#     Printer Queue

#     Breadth-First Search (BFS)

#     Handling Requests (IO Buffers, Web Servers)

#     Cache (LRU)





class Queue:
    
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return 'Queue  is empty'
        else:
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0



# 💡 What is a Manual Queue?

# A manual queue is not an official term, but it generally refers to:

#     ✅ A queue implemented manually from scratch, without using built-in data structures like Python's list, deque, or libraries like queue.Queue.

# 📌 Characteristics of a Manual Queue:

#     Uses a fixed-size array (e.g., [None] * size)

#     Maintains front and rear pointers to track insertion and removal

#     Requires manual handling of:

#         Queue overflow (is full)

#         Queue underflow (is empty)

#         Pointer updates

#     Often used to learn core data structures and used in coding interviews




class Queue:
    def __init__(self,size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size
        
    def enqueue(self,item):
        if self.rear == self.size - 1:
            print('Queue is fulll')
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.Queue[self.rear] = item
        
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return 
        item = self.queue[self.front]
        self.front += 1
        return item
        