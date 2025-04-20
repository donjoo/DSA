def jagged_array(num_rows):
    jagged_array = []
    for i in range(num_rows):
        row = [j for j in range(i+1)]
        jagged_array.append(row)
    return jagged_array

jagged_array = jagged_array(5)
for row in jagged_array:
    print(row)



def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr



arr = [1,2,3,4,5,6]
print(reverse_array(arr),'iiiiiiiiiii')


def reverse_arr(arr):
    return arr[::-1]
arr = [1,2,3,4,5,6]

print(reverse_arr(arr))