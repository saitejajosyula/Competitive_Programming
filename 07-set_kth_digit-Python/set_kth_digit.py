# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):

	flag = False
	
	if n < 0:

		flag = True

		n = abs(n)

	div = (n//10**k)

	rem = (div % 10) * (10**k)

	add = (10**k) * d

	output = n - rem + add 

	if flag:

		return -1 * output

	else:

		return output


