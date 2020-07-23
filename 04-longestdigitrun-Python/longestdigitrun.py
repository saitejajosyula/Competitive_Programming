# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	
	n = abs(n)

	l = 1
	l = n % 10

	r = 1

	index = n
	count = 1

	while index != 0:

		index = index //10

		count = count + 1
	
	if count == 1:
		return 1
	
	for i in range(count):

		flag = n % 10
		n = n//10

		flag1 = n % 10

		if flag == flag1:

			r = r + 1
		
		elif r > l:
			l = r
			ld = flag
			r = 1

		elif r == l and flag < ld:
			ld = flag
			r = 1
		
		else:
			r = 1
	
	return ld



