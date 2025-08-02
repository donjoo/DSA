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
    def __init__(self, array=None):
        self.heap = array[:] if array else []
        if self.heap:
            self.build_heap()

    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2
    def _parent(self, i): return (i - 1) // 2

    def build_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify_down(i)

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def _heapify_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0] if self.heap else None

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def delete(self, index):
        if index >= len(self.heap):
            return None
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(index)
        self._heapify_up(index)

    def size(self):
        return len(self.heap)

    def heap_sort(self):
        result = []
        temp = MinHeap(self.heap[:])
        while temp.size() > 0:
            result.append(temp.extract_min())
        return result
