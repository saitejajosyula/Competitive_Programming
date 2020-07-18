# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def isPrime(n):
	if n > 1:
		for i in range(2, n):
			if n % i == 0:
				return False
		return True
	return False

def isPalindrome(n):

	s = str(n)

	return n == int(s[::-1])


def fun_nth_palindromic_prime(n):

	lis = [i for i in range(12500) if isPalindrome(i) and isPrime(i)]
	return lis[n]
	