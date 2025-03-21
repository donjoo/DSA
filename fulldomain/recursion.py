def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
print(fibonacci(7))





def factorial(n):
    if n == 0:
        return 0
    else:
        return n * factorial(n - 1)
    
print(factorial(5))



def list_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + list_sum(arr[1:])
    



def binary_search(arr, low , high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, high , key)
        else:
            return binary_search(arr, low , mid - 1, key)
    else :
        return -1
    




def recursion(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return recursion(s[1: -1])
    return False


s = "A man is human"

cleaned = ''.join(e.lower() for e in s if e.isalnum())
print(cleaned)
print(recursion(cleaned))





def reverse_arr(arr,left,right):
    if left >= right:
        return arr
    
    arr[left],arr[right] = arr[right],arr[left]

    return reverse_arr(arr,left+1,right-1)


arr = [1,2,3,4,5,6,7]
print(reverse_arr(arr,0,len(arr)-1))





def powerset(s):
    if not s:
        return [set()]
    print(s,'s')
    elem = s.pop()
    subsets = powerset(s)
    print(subsets,'jj')
    s.add(elem)


    new_subsets = [subset | {elem} for subset in subsets]
    # print('new',new_subsets)
    return subsets + new_subsets

s = {1,2,3}
print(powerset(s))






def power_set_recursive(s):
    if not s:
        return [[]]
    
    first_elem = s[0]
    rest = s[1:]

    subsets = power_set_recursive(rest)
    print(subsets)

    return subsets + [[first_elem] + subset for subset in subsets]




def power_set_re(s):
    if not s:
        return [[]]
    
    first_elem = s[0]
    rest = s[1:]

    subsets = power_set_re(rest)

    return  subsets + [[first_elem] + subset for subset in subsets]

s = [1,2,3]
print(',,,,',power_set_re(s))























def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fionacii(n-1) + finbana(n - 1)