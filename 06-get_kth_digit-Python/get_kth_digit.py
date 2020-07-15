# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	
	l = abs(digit)

	a = l % 10**(k+1)
	b = l % 10 **(k)
	c = (a-b) % 10**(k)
	return c