def shellsort(list1):
    gap = len(list1)//2
    while gap >0:
        for index in range(gap,len(list1)):
            current_elem = list1[index]
            pos = index

            while pos >= gap and current_elem < list1[pos - gap]:
                list1[pos] = list1[pos - gap]
                pos = pos - gap

            list1[pos] = current_elem
        gap = gap//2



list1 = [4,5,1,8,3,6]
shellsort(list1)





