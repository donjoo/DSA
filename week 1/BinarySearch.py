
'''Binary search is an efficient algorithm for 
finding a target 
value within a sorted array or list. 
It follows a divide-and-conquer approach, 
repeatedly dividing the search range in half 
until it either finds 
the target or determines it is not present.

'''
def BinarySearch(list,key):
    low = 0
    high = len(list)-1
    found = False
    print(len(list))
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



def binary_recs(arr,low,high,target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_recs(arr,mid + 1,high,key)
        else:
            return binary_recs(arr,low,mid -1,key)
    else:
        return -1
    



def BInaysearch(list,target):
    low = 0
    high = len(list)
    found = False
    while low <= high and not found:
        mid = (low + high) //2
        if list[mid] == target:
            found = True
        elif target < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if found :
        print("element is found")
    else:
        print("not foundddddd")    

