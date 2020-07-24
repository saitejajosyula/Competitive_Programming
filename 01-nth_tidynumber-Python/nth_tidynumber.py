# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def tidynumber(n):

    prev = 10

    while(n):

        rem = n % 10

        n = n // 10

        if rem > prev:

            return False
        
        prev = n

    return True 

def fun_nth_tidynumber(n):
    
    lis = []

    for i in range(2900):

        if tidynumber(i) :
            
            lis.append(i)
    
    return lis[n+1]