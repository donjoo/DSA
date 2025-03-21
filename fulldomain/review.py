def binary_search(arr,low,high,key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            return binary_search(arr,mid + 1,high,key)
        else:
            return binary_search(arr,low,mid-1,key)
    else:
        return False
    





arr = [2,5,4,8,6,1]
arr = sorted(arr)
result = binary_search(arr,0,len(arr),1)
print(result)