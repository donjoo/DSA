""" Bubble Sort is a simple sorting algorithm that repeatedly steps
 through the list to be sorted, compares adjacent items, and swaps them if they 
 are in the wrong order. The process is repeated until the list is sorted. 
 Bubble sort is known for its simplicity but is generally considered 
 inefficient for large lists.

 

Time Complexity

    Best Case: O(n) when the list is already sorted (optimizing with a flag to detect no swaps)
    Average Case: O(n2)
    Worst Case: O(n2)


Space Complexity: O(1) (in-place sorting)




Key Points

    Simplicity: Bubble sort is easy to understand and implement.

    Inefficiency: Due to its O(n2)O(n2) time complexity, bubble sort 
    is inefficient for large lists compared to more advanced algorithms 
    like quicksort or mergesort. 
    
    In-Place Sorting: Bubble sort does not require additional storage 
    space, as it sorts the list in place.

    Optimized Version: The algorithm can be optimized by stopping early
    if no swaps are made during a pass, indicating that the list is 
    already sorted.

"""


arr = [63,76,1,5,95,23,2]

for j in range(len(arr)-1,0,-1):
    print(j,'iiiiiiiiiiiiiiiii')
    for i in range(j):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            print(arr)
        else:
            print(arr)
        print()
print(arr,'sortedd')



def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped =True
        if not swapped:
            break 
    return arr
arr = ["apple", "orange", "banana", "grape", "pear"]
print(bubble_sort_strings(arr))



def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [3,6,4,1,2,7]
print(bubble_sort_desc(arr))



def desc_bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr


arrr = [4,1,6,2,7,3,9]
print(desc_bubblesort(arrr))
