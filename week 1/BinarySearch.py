def BinarySearch(list,key):
    low = 0
    high = len(list)-1
    found = False
    while low <= high and not found:
        mid = (low + high)//2
        if list[mid] == key:
            found = True
        elif key < list[mid]:
            high = mid-1
        else:
            low = mid + 1
    if found:
        print("key is found")
    else:
        print("key not found")


listt = [3,4,12,5,87]
listt.sort()
key = int(input('enter the value: '))
BinarySearch(listt,key)




def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
print("Index of", target, ":", binary_search(arr, target)) 

arr = [1, 3, 5, 7, 9]
target = 6
print("Index of", target, ":", binary_search(arr, target))
