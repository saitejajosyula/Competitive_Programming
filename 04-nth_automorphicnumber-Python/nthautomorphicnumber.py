# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isautomorphic(n):

	sq = n ** 2

	while n > 0:

		if n % 10 != sq % 10:
			
			return False
		
		n = n // 10

		sq = sq // 10
	
	return True

def nthautomorphicnumbers(n):
	# Your code goes here
	
	lis = []

	for i in range(200000):

		if isautomorphic(i):
			
			lis.append(i)
	
	return lis[n-1]