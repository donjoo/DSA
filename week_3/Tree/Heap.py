'''


🌳 What is a Heap?

A Heap is a complete binary tree that satisfies the heap property.

There are two types:

    Max Heap: Parent node is always greater than or equal to its children

    Min Heap: Parent node is always less than or equal to its children

    ✅ Complete binary tree = All levels filled except possibly the last, filled left to right



🛠️ Heap Properties
Feature	                        Description
Shape Property	                Must be a complete binary tree
Heap Property	                Max Heap: parent ≥ children
Min Heap:                       parent ≤ children
Efficient Access	            Top element (max/min) is always at the root





✅ Real-World Use Cases
Use Case	                        Why Heap is Used
🔼 Priority Queues	                Get highest/lowest priority
🧮 Heap Sort	                    Sorting in O(n log n)
🧠 Dijkstra’s Algorithm	            Select min-distance node
🗓 OS Schedulers	                Schedule high-priority tasks
💬 Autocomplete	                    Top-k frequent strings































'''


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left = 2*i + 1
            right = 2*i + 2
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
