# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):

	if n > 1:

		for i in range(2, n):

			if n % i == 0:

				return False
		return True
	
	return False

def rotateNumber(n):

	temp = n

	flag = 0

	while temp != 0:

		temp = temp // 10

		flag = flag + 1

	
	n1 = n % 10

	n2 = n // 10

	return n1 * (10 ** (flag  + 1)) + n2

def isCircularPrime(n):

	if n == 0:

		return False
	
	temp = n
	flag = 0

	while temp != 0:

		temp = temp // 10

		flag = flag + 1
	
	for i in range(flag):

		if not isprime(n):
			return False
		
		n = rotateNumber(n)
	
	return True

def nthcircularprime(n):
	# Your code goes here
	
	lis = []

	for i in range(20000):

		if isCircularPrime(i):
			lis.append(i)
	
	return lis[n]