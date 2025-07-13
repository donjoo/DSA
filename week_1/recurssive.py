"""
Recursion

    The term Recursion can be defined as the process of defining something in terms of itself. 
    In simple words, it is a process in which a function calls itself directly or indirectly. 

    Advantages of using recursion

        # A complicated function can be split down into smaller sub-problems utilizing recursion.
        # Sequence creation is simpler through recursion than utilizing any nested iteration.
        # Recursive functions render the code look simple and effective.

    Disadvantages of using recursion

        # A lot of memory and time is taken through recursive calls which makes it expensive for use.
        # Recursive functions are challenging to debug.
        # The reasoning behind recursion can sometimes be tough to think through.

        

  *** If the base case is missing or wrong, recursion will cause:

        Stack overflow / infinite recursion

        Maximum recursion depth error *** 




A special form of recursion where the recursive call is the last operation in the function. 
Python does not optimize tail recursion.




    """


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
# print(fibonacci(7),'fibonacci')  # Output: 13
n_terms = 7
for i in range(n_terms):
    print(fibonacci(i))



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  

print("Factorial of 5:", factorial(6)) 
print("Factorial of 0:", factorial(0))  


# def list_sum(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + list_sum(arr[1:]) 
def list_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + list_sum(arr[1:])

arr1 = [1, 2, 3, 4, 5]
print("Sum of elements in arr1:", list_sum(arr1))  

arr2 = [10, 20, 30, 40, 50]
print("Sum of elements in arr2:", list_sum(arr2))  

arr3 = []
print("Sum of elements in arr3:", list_sum(arr3)) 



def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, high, key)  
        else:           
            return binary_search(arr, low, mid - 1, key) 
    else:
        return -1  

arr = [2, 4, 6, 8, 10, 12, 14]
key = 10
index = binary_search(arr, 0, len(arr) - 1, key)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")



# Write a recursive function to check if a given string is a palindrome

def recusion(s):
    if len(s)<=1:
        return True
    
    if s[0]==s[-1]:
        return recusion(s[1:-1])
    return False
s = "A man, a plan, a canal, Panama"

cleaned_s = ''.join(e.lower() for e in s if e.isalnum())
print(recusion(cleaned_s),'recursion')



def pal_recursion(s):
    if len(s)<=1:
        return True
    if s[0] == s[-1]:
        return pal_recursion(s[1:-1])
    return False 

s = 'malayalamm'
cleaned = ''.join(e.lower() for e in s if e.isalnum())
print(pal_recursion(cleaned),'cleaned')



#  reverse an array
def reverse_arr(arr,left,right):
    if left >= right:
        return arr
    
    arr[left], arr[right]=arr[right],arr[left]

    return reverse_arr(arr,left + 1,right-1)

arr = [1,2,3,4,5,6,7]
print(reverse_arr(arr,0,len(arr)-1))













def re_reverse_arr(arr,left,right):
    if left >= right:
        return arr
    arr[left],arr[right] = arr[right],arr[left]

    return re_reverse_arr(arr,left +1,right-1)


def arrr(arr):
    return re_reverse_arr(arr,0,len(arr)-1)

arr = [1,2,3,4,5,6,7,8,9]
print(arrr(arr))





# def powerset_recursive(s):
#     if not s:
#         return [set()]
#     print(s,'s')
#     elem = s.pop()
#     subsets = powerset_recursive(s)
#     print(subsets,'subsets')
#     s.add(elem)

#     new_subsets = [subset | {elem} for subset in subsets]
#     print(new_subsets,'new_subsets')
#     return  subsets + new_subsets

# s = {1,2,3}
# print(powerset_recursive(s))




def power_set_recursive(s):
    if not s:
        return [[]]
    
    first_elem = s[0]
    rest = s[1:]

    subsets = power_set_recursive(rest)
    print(subsets)

    return subsets + [[first_elem] + subset for subset in subsets]

s = [1,2,3]
print("Power Set (Recursive):", power_set_recursive(s))




# ✅ String Permutations (All possible rearrangements of characters)

#     Given a string, generate all permutations (reorderings) of its characters.
def permute(s):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path + remaining[i], remaining[:i] + remaining[i+1:])

    backtrack("", s)
    return result

# Example
print(permute("abc"))







''''________________------------------------________________________--------------------------_______________________'''


