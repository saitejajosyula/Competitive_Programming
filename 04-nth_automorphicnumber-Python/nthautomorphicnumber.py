# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isautomorphic(n):

	n1 = str(n)

	s = n ** 2 

	sqr = str(s)

	l = sqr[(-1 * len(n1)):]

	return n1 == l

def nthautomorphicnumbers(n):
	# Your code goes here
	
	lis = []

	for i in range(10):

		if isautomorphic(i):
			
			lis.append(i)
	
	
	count = 4

	temp1 = 5
	temp2 = 6

	while count < n+2:

		counter = 1

		while True:

			s1 = str(counter) + str(temp1)

			if isautomorphic(int(s1)):
				break
				
			counter += 1
		
		temp1 = int(str(counter) + str(temp1))

		lis.append(temp1)

		counter = 1

		while True:

			s2 = str(counter) + str(temp2)

			if isautomorphic(int(s2)) :
				break
				
			counter += 1
		
		temp2 = int(str(counter) + str(temp2))

		lis.append(temp2)

		count = count + 2
	
	lis.sort()

	return lis[n-1]