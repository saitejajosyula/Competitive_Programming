# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math

def isprime(n):

	if n <= 3:

		return True
	
	if n % 2 == 0 or n % 3 == 0:

		return False

	x = 5

	while x <= math.sqrt(n):

		if n % x == 0 or n % (x+2) == 0:

			return False
		
		x = x + 6
	
	return True


def nthcircularprime(n):
	# Your code goes here

	count = 0

	temp = 2

	while count < n:

		if isprime(temp):

			s = str(temp)

			boolean = True

			for i in range(1, len(s)):

				s = s[1:] + s[0]

				if not isprime(int(s)):
					boolean = False

					break
			
			if boolean:

				count = count + 1
		
		temp = temp + 1
	
	return temp - 1
