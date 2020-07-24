# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

import math 

def ispronic(n):

	i = 0

	a = int(math.sqrt(n))
	while i <= a:

		if n == i * (i+1) :

			return True
		
		i = i + 1
	
	return False

def nthpronicnumber(n):
	# Your code goes here
	
	lis = []

	for i in range(3000):

		if ispronic(i):

			lis.append(i)
	
	return lis[n]