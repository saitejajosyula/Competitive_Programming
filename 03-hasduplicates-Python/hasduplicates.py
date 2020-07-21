# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

from itertools import chain

def hasduplicates(L):
	# Your code goes here
	lis = sum(L, [])
	
	res = []

	for i in lis:
		if i not in res:
			res.append(i)
	
	if len(lis) == len(res):
		return False
	else:
		return True