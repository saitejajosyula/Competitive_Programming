# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def onlyEvenDigits(l, m):

	if m >= len(l):

		return l
	
	else:

		a = 0

		n = l[m]

		while n > 0:

			x = n % 10

			if a == 0 and x % 2 == 0:

				a = x
			
			elif x % 2 == 0:

				a *= 10
				a = a + n% 10
			
			n = n // 10
		
		n = a
		a= 0

		while n > 0:

			if a == 0:

				a = n % 10
			
			else:

				a = a * 10

				a = a + n % 10
			
			n = n // 10
		
		l[m] = a
	
	return onlyEvenDigits(l, m+1)


def fun_recursion_onlyevendigits(l):

	onlyEvenDigits(l,0)
	return l
	
	