def pivot_point(list1,first,last):
    pivot = list1[last]
    left = first
    right = last -1 
    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]


    list1[left],list1[last] = list1[last],list1[left]
    return left



def quick_sort(list1,first,last):
    if first < last:
        
        p = pivot_point(list1,first,last)

        quick_sort(list1,first,p - 1)
        quick_sort(list1,p + 1,last)


list1 = [56,23,1,32,21,8]
quick_sort(list1,0,len(list1)-1)
print(list1)

















def pivot(list1,first,last):
    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[left],list1[last] = list1[last],list1[left]
    return left


def quick(list1,first,last):
    if first < last:
        p = pivot_point(list1,first,last)

        quick_sort(list1,first,p-1)
        quick_sort(list1,p + 1,last)

        