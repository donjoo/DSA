class Heap:
    def __init__(self,is_min_heap = True):
        self.heap = []
        self.is_min_heap = is_min_heap

    def build_heap(self,arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n//2-1,-1,-1):
            self.heapify(i,n)

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)


    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0,len(self.heap))
        return root

    
    def heapify_up(self,index):
        parent_index = (index-1)//2
        if index > 0 and self.should_swap(parent_index,index):
            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
            self.heapify_up(parent_index)

    def heapify(self,index,heap_size):
        left = 2 *index + 1
        right = 2 * index + 2
        smallest_or_largest = index

        if left < heap_size and self.should_swap(index,left):
            smallest_or_largest = left
        if right < heap_size and self.should_swap(index,right):
            smallest_or_largest =right
        if smallest_or_largest != index:
            self.heap[index],self.heap[smallest_or_largest] = self.heap[smallest_or_largest],self.heap[index]
            self.heapify(smallest_or_largest,heap_size)

    
        
    def should_swap(self,parent_index,child_index):
        if self.is_min_heap:
            return self.heap[parent_index] >self.heap[child_index]
        else:
            return self.heap[parent_index]  < self.heap[child_index]
        
    def get_root(self):
        if not self.heap:
            return None
        return self.heap[0]
    

    def heap_sort(self):
        n = len(self.heap)
        for i in range(n//2-1,-1,-1):
            self.heapifysort(i,n)
        
        for i in range(n-1,0,-1):
            self.heap[i],self.heap[0] = self.heap[0],self.heap[i]
            self.heapifysort(0,i)

    def heapifysort(self,i,n):
        left = 2 * i + 1
        right = 2* i + 2
        largest = i

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapifysort(largest,n)

min_heap = Heap()
min_heap.build_heap([3,6,8,5,2])
print('min heap:',min_heap.heap)

min_heap.insert(1)
print("min heap afer insertion of 1:",min_heap.heap)
min_heap.heap_sort()
print(min_heap.heap,'sortttttttttttttt')

max_heap = Heap(is_min_heap=False)
max_heap.build_heap([3,6,8,5,2])
print('min heap:',max_heap.heap)

max_heap.insert(1)
print("min heap afer insertion of 1:",max_heap.heap)

print(max_heap.get_root())

max_heap.heap_sort()
print(max_heap.heap,'max_heapsortttttttttttttt')