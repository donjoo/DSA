

def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if arr[i] != arr[min_ind]:
            arr[i],arr[min_ind] = arr[min_ind],arr[i]
    return arr

arr = [56,3,5,2,76,5,0]
print(selectionsort(arr))




def selection(arr):
    n = len(arr)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1,n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if arr[i] != arr[min_ind]:
            arr[i],arr[min_ind] = arr[min_ind],arr[i]
    return arr
