# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def isUgly(n):

    flag = True
    
    while n != 1:

        if n % 5 == 0:

            n = n//5
        
        elif n % 3 == 0:

            n = n//3
        
        elif n % 2 == 0:

            n = n //2

        else:

            flag = False
            break
    
    return flag

def fun_nth_uglynumber(n):

    if n == 0:

        return 1

    i = 2

    count = 1

    while n > count :

        i = i + 1

        if isUgly(i):

            count = count + 1
        
    return i
