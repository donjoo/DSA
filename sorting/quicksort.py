"""
Quicksort is a highly efficient and widely used sorting algorithm 
that follows the divide-and-conquer paradigm. It works by 
selecting a 'pivot' element from the array and partitioning the 
other elements into two sub-arrays, according to whether they are 
less than or greater than the pivot. The sub-arrays are then sorted 
recursively.



Time Complexity

    Best Case: O(nlog⁡n)O(nlogn)
    Average Case: O(nlog⁡n)O(nlogn)
    Worst Case: O(n2)O(n2) (occurs when the smallest or largest element is always chosen as the pivot)

Space Complexity

    Space Complexity: O(log⁡n)O(logn) due to the recursive call stack




🛠️ PIVOT STRATEGIES

    Last element (simple)

    First element

    Middle element

    Random element (prevents worst case)

    Median of three (robust and fast)



✅ ADVANTAGES OF QUICKSORT
Advantage	Explanation
🔥 Very Fast in Practice	Quicksort is one of the fastest sorting algorithms for average cases. It often outperforms other algorithms like Merge Sort and Heap Sort.
🧠 Efficient Time Complexity	Average and best-case time complexity is O(n log n).
💾 In-place Sorting	Requires no extra space (unlike Merge Sort), so space complexity is O(log n) (for recursion stack).
📦 Good Cache Performance	Works well with memory caches due to sequential memory access.
🧩 Divide-and-Conquer Approach	Can be parallelized and is naturally recursive, making it elegant and modular.
🔀 Random Pivoting Prevents Worst Case	You can easily avoid worst-case behavior by choosing the pivot randomly.
    


❌ DISADVANTAGES OF QUICKSORT
Disadvantage	Explanation
💥 Worst Case is O(n²)	If the pivot always picks the largest or smallest element (like in sorted arrays), performance degrades heavily.
❌ Not Stable	Equal elements may get reordered because it swaps elements around, so it can’t guarantee original order is preserved.
🌀 Recursive — Risk of Stack Overflow	For very large arrays or bad pivot choices, the recursion can go too deep, causing stack overflow.
🧠 Harder to Implement In-Place	In-place version (with pointers and partitioning) is more complex than simple sorting algorithms like Bubble or Selection.
🔁 Performance Depends on Pivot Choice	A poor pivot choice can drastically affect performance, unlike Merge Sort which always guarantees O(n log n).






"""







# def pivot_point(list1,first,last):
#     pivot = list1[first]
#     left = first+1
#     right = last
#     while True:
#         while left <= right and list1[left] <= pivot:
#             left = left+1
#         while left <= right and list1[right] >= pivot:
#             right = right-1
#         if right < left:
#             break
#         else:
#             list1[left],list1[right]= list1[right],list1[left]
#     list1[first],list1[right] = list1[right],list1[first]
#     return right 


# def quicksort(list1,first,last):
#     if first < last:
#         p = pivot_point(list1,first,last)
#         quicksort(list1,first,p-1)
#         quicksort(list1,p+1,last)


# list1 = [56,23,76,32,21,8]
# n = len(list1)
# quicksort(list1,0,n-1)
# print(list1)











# import random 

# def pivot_point(list1,first,last):
#     rindex = random.randint(first,last)
#     list1[rindex],list1[last] = list1[last],list1[rindex]
#     pivot = list1[first]
#     left = first+1
#     right = last
#     while True:
#         while left <= right and list1[left] <= pivot:
#             left = left+1
#         while left <= right and list1[right] >= pivot:
#             right = right-1
#         if right < left:
#             break
#         else:
#             list1[left],list1[right]= list1[right],list1[left]
#     list1[first],list1[right] = list1[right],list1[first]
#     return right 


# def quicksort(list1,first,last):
#     if first < last:
#         p = pivot_point(list1,first,last)
#         print(p,list1,'pppppp')
#         quicksort(list1,first,p-1)
#         print(list1,'lefttttt')
#         quicksort(list1,p+1,last)
#         print(list1,'rightttt')

# list1 = [56,23,76,32,21,8,23]
# n = len(list1)
# quicksort(list1,0,n-1)
# print(list1)


list1 = [56,23,1,32,21,8]
def pivot_point(list1,first,last):
    pivot = list1[last]
    left = first
    right = last-1
    print(pivot,left,right)
    while True:
        while left <= right and list1[left] <= pivot:
            print(list1[left],'left')
            left = left+1
        while left <= right and list1[right] >= pivot:
            print(list1[right],'right')
            right = right-1
        if right < left:
            break
        else:
            print(list1,'listtttt')
            list1[left],list1[right]= list1[right],list1[left]
            print(list1,'listtt444')
    print(list1,'liiiii')
    list1[last],list1[left] = list1[left],list1[last]
    print(list1,'55555555')
    return left 


def quicksort(list1,first,last):
    if first < last:
        p = pivot_point(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)

list1 = [56,23,1,32,21,8]
n = len(list1)
quicksort(list1,0,n-1)
print(list1) 

# 32,23,76,56,8



# import statistics

# def pivot_point(list1,first,last):
#     low = list1[first]
#     high = list1[last]
#     mid = (first  + last)//2
#     pivot_val = statistics.median([low,list1[mid],high])

#     if pivot_val == low:
#         pindex = first
#     elif pivot_val == high:
#         pindex = last
#     else:
#         pindex = mid

#     list1[last],list1[pindex] = list1[pindex],list1[last]
#     pivot = list1[last]
#     left = first
#     right = last-1
#     while True:
#         while left <= right and list1[left] <= pivot:
#             left = left+1
#         while left <= right and list1[right] >= pivot:
#             right = right-1
#         if right < left:
#             break
#         else:
#             list1[left],list1[right]= list1[right],list1[left]
#     list1[last],list1[left] = list1[left],list1[last]
#     return left 


# def quicksort(list1,first,last):
#     if first < last:
#         p = pivot_point(list1,first,last)
#         print(p,list1,'pppppp')
#         quicksort(list1,first,p-1)
#         print(list1,'lefttttt')
#         quicksort(list1,p+1,last)
#         print(list1,'rightttt')

# list1 = [56,23,76,32,21,8]
# n = len(list1)
# quicksort(list1,0,n-1)
# print(list1)



# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr)//2]
#         print(pivot,'pivottttt')
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quicksort(left) + middle + quicksort(right)
    

# arr = [3,6,8,10,1,2,9]
# print(quicksort(arr),'qqqqqqqqqqqqqqqqqqq')





# def quicksort_inplace(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         print(pi,'pipipiipi')
#         quicksort_inplace(arr, low, pi - 1)
#         quicksort_inplace(arr, pi + 1, high)

# def partition(arr, low, high):
#     pivot = arr[high]
#     print(high,'highhhh')
#     print(arr,'piarr')
#     print(pivot,'pivot')
#     i = low - 1
#     print(i,'i')
#     for j in range(low, high):
#         print(arr[j])
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     print(arr,'arrrrr')
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     print(arr,'arr')
#     return i + 1

# # Example usage
# arr = [3, 6, 8, 10, 1, 2, 1]
# quicksort_inplace(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)


# # 1,6,8,10,3,2,1

# # 1,1,8,10,3,2,6



# def pivot_point(list1,first,last):
#     pivot =list1[last]
#     left = first
#     right = last-1
#     while True:
#         while left <= right and list1[left] <= pivot:


# def quick_sort(list1,first,last):
#     if first <last:
#         p = pivot_point(list1,first,last)
#         quicksort(list1,first,p-1)
#         quicksort(list1,p+1,last)


# list1 = [34,5,66,1,2,9,43]
# n = len(list1)
# quicksort(list1,0,n-1)
