# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.

import math

def isKaprekarNumber(n):

    if n < 1:
        return False

    if n == 1:

        return True

    l = len(str(n**2))

    for i in range(1, l):

        a = n**2 // 10 ** i
        b = n**2 % 10 ** i

        if b != 0 and a+b == n:

            return True
        
    return False

def fun_nearestkaprekarnumber(n):
    
    count = -1

    while True:

        count = count + 1

        if isKaprekarNumber(n-count) == True :

            return n - count
        elif isKaprekarNumber(n+count) == True:
            return n + count