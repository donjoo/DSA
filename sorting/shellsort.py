def Shellsort(alist):
    gap = len(alist)//2
    while gap >0:
        for index in range(gap,len(alist)):
            current_element = alist[index]
            pos = index
            while pos>=gap and current_element < alist[pos-gap]:
                alist[pos] = alist[pos-gap]
                pos = pos-gap
            alist[pos]=current_element
            gap = gap//2


list1 = [4,5,1,8,3,6]
Shellsort(list1)
print(list1)

