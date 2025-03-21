def insertionsort(list1):
    for i in range(1,len(list1)):
        current_elem = list1[i]
        pos = i

        while current_elem < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos - 1]
            pos = pos - 1
        list1[pos] = current_elem

        