import math


def is_prime(n):
    if n <=1 :
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5,int(math.sqrt(n)) + 1,6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True




def is_primeres(n,divisor =None):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if divisor is None:
        divisor = int(math.sqrt(n))
    if divisor < 2:
        return True
    if n % divisor  == 0:
        return False
    
    return is_primeres(n,divisor - 1)