# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math

def sumOfdigits(n):

    t = 0

    while n > 0:

        rem = n % 10

        t = t + rem

        n = n // 10
    
    return t


def isprime(n):

    if n > 1:

        for i in range(2, n):

            if n % i == 0:

                return False
            
        return True
    
    return False

def sumOfFactors(n):

    lis = []

    while n % 2 == 0 and n > 0:

        lis.append(int(2))

        n = n /2

    for i in range(3, int(math.sqrt(n))+1, 2):

        while n % i == 0:

            lis.append(int(i))

            n = n/i
    
    if n > 2:

        lis.append(int(n))

    total = 0

    for i in lis:

        if len(str(i)) == 1:

            total = total + i
        
        elif len(str(i)) > 1 and i is not n:

            total = total + sumOfdigits(i)
    return total


def smith(n):

    if sumOfdigits(n) == sumOfFactors(n):

        return True
    
    else:

        return False

def fun_nth_smithnumber(n):

    lis = []

    for i in range(1, 500):

        if smith(i) and not isprime(i):

            lis.append(i)
    
    return lis[n]