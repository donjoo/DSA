def Shellsort(alist):
    gap = len(alist)//2
    print(gap,'gap')
    while gap >0:
        for index in range(gap,len(alist)):
            print(index,'index')
            current_element = alist[index]
            pos = index
            print(gap,'gappll')
            print(current_element,'current_element')
            print(pos,'pos')
            while pos>=gap and current_element < alist[pos-gap]:
                alist[pos] = alist[pos-gap]
                pos = pos-gap
                print(pos,'pppos')
            alist[pos]=current_element
            print(alist,'ll')
        gap = gap//2
        print(gap,'gapppp')

list1 = [4,5,1,8,3,6]
Shellsort(list1)
print(list1)

