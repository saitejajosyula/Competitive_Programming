# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	s = str(abs(n))

	if len(s) == 1 or len(s) == 2 and s[0] != s[1]:
		return False
	
	ind = -1

	for i in range(len(s)):
		if(s[i] == ind) :
			return True
		
		ind = s[i]
	return False

