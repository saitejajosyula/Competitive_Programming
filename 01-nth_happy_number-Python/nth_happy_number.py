# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def squaresum(n):

	s = 0

	while n >0 :
		s = s + (n % 10) * (n % 10)
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

def fun_nth_happy_number(n):
	return 0
