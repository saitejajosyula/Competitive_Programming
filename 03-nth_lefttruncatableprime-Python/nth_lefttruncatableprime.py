# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.

import math

def isprime(n):

    if n > 1:

        for i in range(2, n):

            if n % i == 0:

                return False
        return True
    
    return False

def digitcount(n):

    n = abs(n)

    count = 1

    while n > 10:

        n = n // 10

        count = count + 1

    return count

def LeftTruncatablePrime(n):

    if isprime(n) == False or str(n).__contains__("0"):
        return False
    
    else:
        x = digitcount(n)

        for i in range(1, x):

            m = n % (10**x)
        
            if isprime(m) == False:
                return False
        
        return True


def fun_nth_lefttruncatableprime(n):

    lis = []

    for i in range(4000):
        if LeftTruncatablePrime(i):
            lis.append(i)
    
    return lis[n]