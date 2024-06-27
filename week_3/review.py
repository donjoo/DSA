# def DFS(node,visited,graph):
 
#     if node not in graph:
#         print("node not present in graph")
#         return
#     else:
#         if not node in visited:
#             visited.add(node)
#             node = graph[node]
#             DFS()


# def dfs(node,graph):
#     if node not in graph:
#         print("not present")
#         return
#     visited = []
#     stack = []
#     stack.append(node)
#     while stack:
#         curent = stack.pop()
#         if curent not in visited:
#             print(curent)
#             visited.append(curent)
#             for j in graph[node]:
#                 stack.append(curent)




def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1,-1):
        heapifysort(i,n,arr)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapifysort(0,i,arr)


def heapifysort(index,lar,arr):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index

    if left < lar and arr[left] > arr[largest]:
        largest = left
    if right < lar and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest],arr[index] = arr[index],arr[largest]
        heapifysort(largest,lar,arr)



arr = [3,4,7,1,3,9]
print(arr)
heap_sort(arr)
print(arr)