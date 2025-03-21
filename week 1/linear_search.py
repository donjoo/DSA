
'''
It works by checking each element in the array sequentially, 
from the beginning to the end, until it finds the target or 
reaches the end of the list.
'''








def search(list,key):
    list2=[]
    flag = False
    for i in range(len(list)):
        if list[i]==key:
            flag = True
            list2.append(i)

    if flag:
            for i in list2:
                print("key found at index",i)
    else:
         print("not found")





list = [7,8,3,2,4,1,3,9,6,3,4]
now = [1,2,3,4,5,6]
print(len(now))
key = int(input('enter the key:'))
search(list,key)




def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 20, 30, 40, 50]
target = 30
print("Index of", target, ":", linear_search(arr, target)) 


arr = [1, 3, 5, 7, 9]
target = 8
print("Index of", target, ":", linear_search(arr, target)) 










