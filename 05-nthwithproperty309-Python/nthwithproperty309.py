# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def iswithproperty309(n):

	i = 0

	n = n**5

	temp = n

	count = 0

	while n > 0:

		if i != n % 10:

			n = n // 10
		
		elif i == n % 10:

			count = count + 1

			n = temp

			i = i + 1

			if count > 9:
				return True
	return False

def nthwithproperty309(n):
	# Your code goes here

	i = -1

	c = 0

	while i < n:

		c = c + 1

		if iswithproperty309(c):
			i = i+1
	
	return c
	