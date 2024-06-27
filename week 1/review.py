# Write a recursive function to check if a given string is a palindrome

# def recursive(s):
#     if s == [1]:
#         return 0
#     else:
#         return s[-1] + recursive(s[-1:])




# string = 'malayalam'
# print(recursive(string))


def binary_search(arr,key,high,low):
    if low > high:
        return -1
    mid = low+high//2
    while low <= high:
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
        return binary_search(arr,key,high,low)



arr = [1,2,3,4,5,6,7,8]
result = binary_search(arr,2,low=0,high=len(arr)-1)
print(result)