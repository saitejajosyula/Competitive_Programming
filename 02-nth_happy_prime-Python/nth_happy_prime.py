# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def squaresum(n):

	s = 0

	while n >0 :

		rem = n % 10
		s = s + (rem **2)
		n = n// 10
	
	return s

def ishappynumber(n):

	if n <= 0:
		return False
	
	if n == 1:
		return True

	total = squaresum(n)

	while(total != 4) :

		total = squaresum(total)

		if total == 1:
			return True
	return False

def isprime(n):

	if n > 1:

		for i in range(2, n):
			if n % i == 0:
				return False
		return True
		
	return False

def fun_nth_happy_prime(n):
	
	lis = [i for i in range(100) if (ishappynumber(i) and isprime(i))]
	return lis.__getitem__(n)
