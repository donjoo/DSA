'''


# A Circular Queue is a linear data structure that follows 
FIFO (First In First Out) but connects the last position back
to the first to form a circle. It's more memory-efficient 
than a regular queue because it reuses the empty space left 
after dequeuing.

🧠 Why Circular Queue?

In a normal queue:

    Once the rear reaches the end (size - 1), we can't insert anymore even if there’s space at the beginning.

In a circular queue:

    We wrap around using modulo: (rear + 1) % size.

    Makes better use of the allocated memory.


 '''


 class CircularQueue:
    def __init__(self, size):  # ✅ fixed __init__
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")  # ✅ fixed print
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
