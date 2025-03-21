

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        print(i)
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j +1] = arr[j + 1], arr[j]
                swapped = True
            else:
                pass
        if not swapped:
            return arr
        
    

arr = [5,2,8,1,3,4,9,6]
print('ghgvvggh',bubble_sort(arr))




def bubble_sort_strings(arr):
    n = len(arr)
    print('n',n)
    for i in range(n-1,0,-1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = ["apple", "orange", "banana", "grape", "pear"]
print(bubble_sort_strings(arr))




def bubble_sort(s):
    n = len(s)
    for i in range(n-1,0,-1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr






def bub_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j],arr[j + 1]
                swapped = True
        if not swapped:
            break
    return arr


    