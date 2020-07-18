# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isadditiveprime(n):

	if(isprime(n)):
		s = str(n)

		num = 0

		for i in s:

			num = num + int(i)

		if isprime(num):
			return True

		return False
	return False

def isprime(n):

	if n > 1:

		for i in range(2, n):
			if n % i == 0:
				return False
		return True
	return False


def fun_nth_additive_prime(n):
	lis = [i for i in range(200) if isadditiveprime(i)]

	return lis[n]