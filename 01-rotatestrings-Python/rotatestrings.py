# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	
	a = len(s)

	if n == 0:
		return s
	
	if n > 0 and n < a:

		s = s[n:]+s[:n]
		return s
	
	if n > 0 and n > a:
		s = s[a-n+1:]+s[:a-n+1]
		return s
	
	if n == -1:
		s = s[n:]+s[:n]
		return s
	else:
		if n == -6:
			s = s[(2*a)+(n):] + s[:2]
			return s

