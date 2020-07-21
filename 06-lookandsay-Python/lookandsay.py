# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	if a == []:
		return []

	lis = []
	start = 0
	current = a[0]
	for i in range(len(a)):

		if a[i] != current:

			length = len(a[start:i])

			lis = lis + [(length, current)]

			current= a[i]
			start = i
		
		if i == len(a) - 1:
			length = len(a[start:])
			lis = lis + [(length, current)]

	return lis