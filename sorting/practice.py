print('hello')
def partition(list1,first,last):
    pivot = list1[last]
    left = first
    right = last-1
    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if left >  right:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[left],list1[last]=list1[last],list1[left]
    return left

def quicksot(list1,first,last):
    if first < last:
        p = partition(list1,first,last)
        quicksot(list1,first,p-1)
        quicksot(list1,p+1,last)




list1 = [4,23,1,6,33,9]
n = len(list1)
quicksot(list1,0,n-1)
print(list1)


def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)

        i = 0
        j = 0
        k = 0
        while i <len(left_list) and j <len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i +=1
                k+=1
            else:
                list1[k] = right_list[j]
                j +=1
                k+=1

        while i < len(left_list):
            list1[k] = left_list[i]
            i +=1
            k =+1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k+=1


arr = [2,7,4,1,8,5,6]
mergesort(arr)
print(arr)




def mmergesort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)


        i =0
        j =0
        k =0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i +=1
                k +=1
            else:
                list1[k] = right_list[j]
                j +=1
                k+=1

        while i < len(left_list):
            list1[k] = left_list[i]
            i +=1
            k+=1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1

kkk = [3,6,4,1,9,2]
kk = mmergesort(kkk)
print(kkk)