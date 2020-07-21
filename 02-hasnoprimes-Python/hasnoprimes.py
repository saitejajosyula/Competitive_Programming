# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):

	lis = sum(l, [])

	for i in lis:
		c = 0
		for j in range(2, i):
			if i % j == 0:
				c = 1
				break
	
	if c == 0:
		return False
	
	else:
		return True