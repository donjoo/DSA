'''

A Priority Queue is an abstract data type similar to a regular queue or stack,
 but where each element is associated with a priority, and elements are served based on priority.

    In a regular queue, elements are processed in FIFO (First-In-First-Out) order.

    In a priority queue, the element with highest priority is dequeued first (regardless of insertion 
    order).



🔶 Types of Priority Queues
Type	Behavior
Max Priority Queue	Highest priority value is dequeued first
Min Priority Queue	Lowest priority value is dequeued first
🔸 Real-life Examples

    CPU Scheduling: High-priority processes get CPU time first.

    Hospital ER: Patients with more serious conditions are treated earlier.

    Event Simulation Systems: Next event is based on smallest timestamp (min-heap).
'''




#  Min Priority Queue
import heapq

class MinPriorityQueue:
    def __init__(self):
        self.heap = []
        
    def enqueue(self,priority, item):
        heapq.heappush(self.heap, (priority,item))
        
    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
        
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
        
    def is_empty(self):
        return len(self.heap) == 0
        
        
pq = MinPriorityQueue()
pq.enqueue(3,"task C")
pq.enqueue(1, 'Task A')
pq.enqueue(2, "Task B")


while not pq.is_empty():
    priority, task = pq.dequeue()
    print(f"Processing {task} with priority {priority}")
            


# Max Priority Queue

import heapq

class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, priority, item):
        heapq.heappush(self.heap, (-priority, item))  # Negate priority for max-heap

    def dequeue(self):
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return -priority, item  # Convert back to positive
        return None

    def peek(self):
        if self.heap:
            priority, item = self.heap[0]
            return -priority, item
        return None

    def is_empty(self):
        return len(self.heap) == 0

# Example
pq = MaxPriorityQueue()
pq.enqueue(3, "Task C")
pq.enqueue(1, "Task A")
pq.enqueue(2, "Task B")

while not pq.is_empty():
    priority, task = pq.dequeue()
    print(f"Processing {task} with priority {priority}")









# using Listt


class MaxPriorityQueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        # Just append at the end
        self.queue.append((priority, item))

    def dequeue(self):
        if not self.queue:
            return None

        # Find the index of the item with the highest priority
        max_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[max_index][0]:
                max_index = i

        # Remove and return the item with the highest priority
        return self.queue.pop(max_index)

    def peek(self):
        if not self.queue:
            return None
        max_item = max(self.queue, key=lambda x: x[0])
        return max_item

    def is_empty(self):
        return len(self.queue) == 0

pq = MaxPriorityQueueList()
pq.enqueue(2, "Low-priority task")
pq.enqueue(5, "High-priority task")
pq.enqueue(3, "Medium-priority task")

while not pq.is_empty():
    priority, task = pq.dequeue()
    print(f"Processing {task} (priority: {priority})")
