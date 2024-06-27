""" 
Scan through the unsorted data looking for the smallest remaining element thenswap 
 it into the position immediatly following the sorted data.Repeat untill finished.

# Time Complexity
#     Best Case: O(n2)
#     Average Case: O(n2)
#     Worst Case: O(n2)

# Space Complexity

#     Space Complexity: O(1)(in-place sorting)


Key Points

    In-Place: Selection sort does not require additional storage, 
    as it sorts the list in place.

    Not Stable: Selection sort is not a stable sort, meaning it does 
    not preserve the relative order of equal elements.

    Simple but Inefficient: Due to its O(n2)O(n2) time complexity, 
    selection sort is inefficient for large lists compared to more 
    advanced algorithms like quicksort or mergesort.

Selection sort is mostly used for educational purposes to demonstrate 
the concept of sorting algorithms, and it's not often used in practice 
for large datasets due to its inefficiency.

ot efficient for large datasets due to its O(n2)O(n2) time complexity, 
"""

# num = int(input("how many numbers"))
# arr = [int(input("enter number")) for x in range(num)]
arr = [56,3,5,2,76,5,0]
# # for i in range(len(arr)-1):
# #     min_val = min(arr[i:])
# #     min_ind = arr.index(min_val,i)
# #     if arr[i] != arr[min_val]
# #     arr[i],arr[min_ind] = arr[min_ind],arr[i]
# #     print(arr)

# print(arr,'huhuh')



for i in range(len(arr)-1):
    m_ind = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[m_ind]:
            m_ind = j
    if arr[i] != arr[m_ind]:
            arr[i],arr[m_ind] = arr[m_ind],arr[i]
print(arr,'geg')






# Implement Selection Sort on a List of Strings


# def selection_sort_strings(arr):
#     n = len(arr)
#     for i in range(n):
#         m_indx = i
#         for j in range(i + 1,n):
#             if arr[j] < arr[m_indx]:
#                 m_indx = j

#         arr[i],arr[m_indx] = arr[m_indx],arr[i]
#     return arr

# arr = ['apple','orange','banannananan','qwiiii','jack']
# print(selection_sort_strings(arr))




def selection_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        min_indx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i],arr[min_indx] = arr[min_indx],arr[i]
    return arr

arr = ['apple','orange','banannananan','qwiiii','jack']
print(selection_sort_strings(arr))




def selecttion_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1,n):
            if arr[j] > arr[max_idx]:
                max_idx=j
        arr[i],arr[max_idx] = arr[max_idx],arr[i]
    return arr


arr=[2,4,6,1,3,5,9]
print(selecttion_sort_desc(arr))



def selection_sort_tuples(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if arr[j][0] < arr[min_ind][0]:
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
    return arr


arr = [(1,3),(4,1),(2,5),(5,0),(3,2)]
print(selection_sort_tuples(arr))



def selection_tuple(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if arr[j][1] < arr[min_ind][1]:
                min_ind = j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    return arr

arr = [(1,3),(4,1),(2,5),(5,0),(3,2)]
print(selection_tuple(arr))

