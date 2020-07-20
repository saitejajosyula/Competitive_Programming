# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):

	d = {}
	
	for char in s:

		if char in d:
			d[char] += 1
		else:
			d[char] = 1
	value = sorted(d.values(), reverse = True)

	for key, val in d.items():

		if val == value[n-1]:
			return key



