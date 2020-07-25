# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):

	c = s1.count(s2)

	if c == 0:

		return s1
	
	elif c == 1:

		STR = ""

		first = s1.find(s2)
		last = first + len(s2)

		STR = s1[0:first] + s3 + s1[last:]

		return STR
	
	else:

		STR = s1
		
		for x in range(c):

			first = STR.find(s2)
			last = first + len(s2)

			STR = STR[0:first] + s3 + STR[last:]

		return STR

