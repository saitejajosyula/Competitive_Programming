# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

import math
def almostEqual(x, y, epsilon = 10**-8):
	return abs(x-y) < epsilon

def recursion_powersof3ton(n):
	# Your code goes here
	
	if n < 1:
		return None
	
	elif n == 1:
		return [1]
	
	elif n > 1 and n < 9:

		return ([1] + [3])
	
	n = n//1

	n = int(n)

	if almostEqual(3 ** int(round(math.log(n, 3))), n):
		return recursion_powersof3ton((n//1)-1) + [n]
	
	else:
		return recursion_powersof3ton((n//1)-1)

