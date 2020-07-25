# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):

	a = s1.count(s2)

	if a == 0:

		return s1
	
	elif a == 1:

		s = ""

		first = s1.find(s2)
		last = first + len(s2)

		s = s1[0:first] + s3 + s1[last:]

		return s
	
	else:

		s = s1
		
		for i in range(c):

			first = s.find(s2)
			last = first + len(s2)

			s = s[0:first] + s3 + s[last:]

		return s

