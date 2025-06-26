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