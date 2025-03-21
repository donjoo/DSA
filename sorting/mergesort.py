"""
Merge sort is a classic divide-and-conquer algorithm used for sorting arrays or lists. It's known for its stable performance and guaranteed O(nlog⁡n)O(nlogn) time complexity, making it efficient for large datasets. Here’s a detailed explanation of how merge sort works:


The merge operation is the key part of merge sort where two sorted arrays are combined into a single sorted array. It involves comparing elements from both arrays and appending them to a new array in sorted order.


Performance

    Time Complexity: Merge sort guarantees O(nlog⁡n)O(nlogn) time complexity in all cases, making it suitable for large datasets.
    Space Complexity: Merge sort requires additional space proportional to the size of the input array for storing temporary sublists during the merge phase, resulting in O(n)O(n) space complexity.

Advantages and Disadvantages




    Advantages:
        Stable sorting algorithm (preserves the relative order of equal elements).
        Efficient and predictable O(nlog⁡n)O(nlogn) performance.
        Suitable for sorting linked lists as well as arrays.

    Disadvantages:
        Requires additional memory for merging sublists, leading to higher space complexity compared to in-place algorithms like quicksort.
        Slower constant factors compared to quicksort due to the additional merging step.


"""






def mergesort(list1):
    if len(list1) > 1:
        mid =len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)

        i = 0
        j = 0
        k = 0
        while i <len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k] = right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            list1[k]= right_list[j]
            j+=1
            k+=1






arr = [3,654,2,6,4,12,7]
mergesort(arr)
print(arr)












def mmergesort(list1):
    if len(list1) > 1:
        mid =len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mmergesort(left_list)
        mmergesort(right_list)

        i = 0
        j = 0
        k = 0
        while i <len(left_list) and j<len(right_list):
            if left_list[i]>right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k] = right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            list1[k]= right_list[j]
            j+=1
            k+=1


                 

rrr = [3,654,2,6,4,12,7]
mmergesort(rrr)
print(rrr)