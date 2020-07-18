# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def isPrime(n):
	if n > 1:
		for i in range(2, n//2+1):
			if n % i == 0:
				return False
			return True


def isPalindrome(n):

	if n == 0:
		return 2
	
	if n == 1:
		return 3

	n = str(n)

	if len(n) <= 1:
		return True
	else:
		return n[0] == n[-1] and isPalindrome(n[1:-1])


def fun_nth_palindromic_prime(n):

	lis = []

	for i in range(3, 1000):
		if isPalindrome(i) and isPrime(i):
			lis.append(i)
	
	return lis.__getitem__(n)
	