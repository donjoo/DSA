# take the element immediatly following the sorted data ,scan through the sorted daa to find the place to put it and ut it there ,,Reapeat untill finished
"""


Insertion sort is a simple and intuitive sorting algorithm that builds the final sorted array 
one element at a time. It is much like sorting playing cards in your hands: you take one card at a 
time and place it in its correct position relative to the already sorted cards.

Time Complexity

    Best Case: O(n)O(n) (when the array is already sorted)
    Average Case: O(n2)O(n2)
    Worst Case: O(n2)O(n2) (when the array is sorted in reverse order)

Space Complexity

    Space Complexity: O(1)O(1) (in-place sorting)



Best case: Already sorted → one pass, no shifts → O(n)

Worst case: Reversed order → lots of shifts → O(n²)

Space Complexity: O(1) — In-place algorithm




✅ Advantages

    Easy to implement

    Efficient for small or nearly sorted arrays

    Stable (preserves order of equal elements)

    Online algorithm: Can sort as elements arrive

❌ Disadvantages

    Not efficient for large datasets

    Performance degrades quickly with size

📚 Real-Life Analogy

Imagine sorting playing cards in your hand:

    Start with one card.

    Pick up the next card and place it in the correct position.

    Repeat until all cards are sorted.



🧮 Use Cases

    Small arrays

    Nearly sorted data

    Online sorting problems (e.g., inserting elements as they stream in)

"""






def Insertionsort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1

        while key < list[j] and j >= 0:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key 


list1 = [2,4,7,3,1,5]
Insertionsort(list1)
print(list1)




def Insertionsort(my_list):
    for index in range(1,len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element < my_list[pos-1] and pos >0:
            my_list[pos] = my_list[pos-1]
            pos = pos-1
        my_list[pos] = current_element


list1 = [2,4,7,3,1,5]
Insertionsort(list1)
print(list1)





# def Insertionsort(my_list):
#     for index in range(1,len(my_list)):
#         current_element = my_list[index]
#         pos = index
#         while current_element > my_list[pos-1] and pos >0:
#             my_list[pos] = my_list[pos-1]
#             pos = pos-1
#         my_list[pos] = current_element


# list1 = [2,4,7,3,1,5]
# Insertionsort(list1)
# print(list1)


def INsersoort(list1):
    for index in range(1,len(list1)):
        current_element = list1[index]
        pos = index 
        while current_element < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos-1]
            pos = pos-1
        list1[pos] = current_element
        

list1 = [2,4,7,3,1,5]
INsersoort(list1)
print(list1,'ggtgtgt')



def index(list1):
    for index in range(1,len(list1)):
        current_element = list1[index]
        pos = index
        while current_element < list1[pos-1] and pos>0:
            list1[pos] = list1[pos-1]
            pos = pos-1
        list1[pos]=current_element



list1 = [3,5,1,4,2,8,6]
index(list1)
print(list1)
