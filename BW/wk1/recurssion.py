



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


    







def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5)) 
print("Factorial of 0:", factorial(0))  




def list_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + list_sum(arr[1:])





def binary_search(arr, low,high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] ==  key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, mid +1, high, key)
        else:
            return binary_search(arr,low,mid - 1, key)
    else :
        return - 1



def recusion(s):
    if len(s) <= 1:
        reuturn True
    if s[0] == s[-1]:
        return recursion(s[1:-1])
    return False

s = 'malayalamm'
cleaned_s = ''.join(e.lower() for e in s if e.isalnum())





def reverse_arr(arr,left,right):
    if left >=right:
        return arr
    arr[left],arr[right] = arr[right],arr[left]

    return reverse_arr(arr,left + 1,right - 1)




def powerset(s):
    if not s:
        return [[]]

    first_elem = s[0]
    rest = s[1:]


    subsets = powerset(rest)

    return subsets + [[first_elem] + subset for subset in subsets]
    