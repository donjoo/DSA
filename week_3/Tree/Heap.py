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








🌱 Heapify

Heapify is the process of restoring the heap property starting from a given node.
There are two ways to apply it:


1️⃣ Bottom-Up Heapify (used in Build Heap)
🔹 Concept:

    Start from the last non-leaf node and work upwards to the root.

    At each step, call heapify_down to push values down if needed.

📌 Why:

    Used to build a heap from an unsorted array efficiently in O(n) time.

    Takes advantage of the fact that leaf nodes are already heaps.

📊 Steps:

    Identify the last non-leaf node: (n//2 - 1)

    Loop backwards to index 0, calling heapify_down for each.

-----------

2️⃣ Top-Down Heapify (used in Insert)
🔹 Concept:

    Start from a newly inserted element (bottom of the heap).

    Move upwards, swapping with the parent until heap property is restored.

📌 Why:

    Used during insert operations in O(log n) time.

📊 Steps:

    Insert new value at the end.

    Compare with parent — if heap property is violated, swap.

    Continue until reaching the root or no violation.








🌱 What is a DEPQ?

A Double-Ended Priority Queue (DEPQ) is a priority queue where you can efficiently:

    Get & remove the minimum element

    Get & remove the maximum element

📌 You can think of it as a priority queue with both ends accessible —
like a combination of a min-heap and a max-heap in one structure.











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




class MaxHeap:
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
            largest = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def _heapify_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0] if self.heap else None

    def extract_max(self):
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
        temp = MaxHeap(self.heap[:])
        while temp.size() > 0:
            result.append(temp.extract_max())
        return result







class DEPQ:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)
        self.data.sort()  # Simplest approach — O(n), can be optimized

    def find_min(self):
        return self.data[0] if self.data else None

    def find_max(self):
        return self.data[-1] if self.data else None

    def delete_min(self):
        return self.data.pop(0) if self.data else None

    def delete_max(self):
        return self.data.pop() if self.data else None

    def size(self):
        return len(self.data)

    def display(self):
        print(self.data)
