# # hepify
# # wiliems method
# # heapq

# import heapq

# heap = [4,2,67]
# heapq.heapify(heap)

# heapq.heappush(heap,10)
# heapq.heappush(heap,22)
# heapq.heappush(heap,12)
# heapq.heappush(heap,13)
# print(heap,'dfsfs')

# heapq.heappush(heap,10)
# print(heap)

# heapq.heappop(heap)

# print(heapq.heappushpop(heap,99))   
# print(heap)
# print(heapq.heapreplace(heap,999))
# print(heap)
# print(heapq.nsmallest(3,heap))
# print(heapq.nlargest(2,heap))





# list1 = [(1,'ria'),(4,'siaaa'),(3,'jiya')]
# heapq.heapify(list1)
# print(list1)
# for i in range(len(list1)):
#     print(heapq.heappop(list1))




class Heap:
    def __init__(self,is_min_heap = True):
        self.heap = []
        self.is_min_heap = is_min_heap

    def build_heap(self,arr):
        self.heap = arr[:]
        n=len(self.heap)
        for i in range(n//2-1,-1,-1):
            print(i,n,'hhhhhhh')
            self.heapify(i,n)

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify(0,len(self.heap))
        return root
    
    


    def heapify_up(self,index):
        parent_index = (index-1)//2
        if index > 0 and self.should_swap(parent_index,index):
            self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
            self.heapify_up(parent_index)

    
    def heapify(self,index,heap_size):      #1,5
        left = 2 * index +1  #3
        right = 2 * index + 2 #4
        smallest_or_largest = index #1

        if left < heap_size and self.should_swap(smallest_or_largest,left): #1,3
            smallest_or_largest = left

        if right < heap_size and self.should_swap(smallest_or_largest,right): #1,4,
            smallest_or_largest=right

        if smallest_or_largest != index:
            self.heap[index],self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
            self.heapify(smallest_or_largest,heap_size)


    def should_swap(self,parent_index,child_index):
        if self.is_min_heap:
            print('self.heap[parent_index]',self.heap[parent_index],',,,,self.heap[child_index]',self.heap[child_index])
            return self.heap[parent_index] > self.heap[child_index]
        else:
            return self.heap[parent_index] < self.heap[child_index]
     
    def heap_sort(self):
        n = len(self.heap)
        for i in range(n//2-1,-1,-1):
            self.heapifysort(i,n)

        for i in range(n-1,0,-1):
            self.heap[i],self.heap[0] = self.heap[0],self.heap[i]
            self.heapifysort(0,i)
    

    def heapifysort(self,i,n):
        left = 2 *i +1
        right = 2 * i +2
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
# print('min heap:',min_heap.heap)

# min_heap.insert(1)
# print("min heap afer insertion of 1:",min_heap.heap)
min_heap.heap_sort()
print('sort',min_heap.heap)




# def heap_sort(arr):
#     n = len(arr)

#     for i in range(n//2-1,-1,-1):
#         heapifysort(arr,n,i)

#     for i in range(n-1,0,-1):
#         arr[i],arr[0] = arr[0],arr[i]
#         heapifysort(arr,i,0)

# def heapifysort(arr,n,i):
#     largest = i
#     left = 2 * i +1
#     right = 2 * i +2

#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right

#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]
#         heapifysort(arr,n,largest)




# arr = [12, 11, 13, 5, 6, 7]
# heap_sort(arr)
# print("Sorted array using Heap Sort:", arr) 

