"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	
	less = []

	equal = [] 

	greater = []

	if len(array) > 1:

		pivot = array[0]

		for x in array:

			if x < pivot:
				less.append(x)
			
			elif x == pivot:

				equal.append(x)
			else:

				greater.append(x)
			
		return sorted(less) + equal + sorted(greater)
	
	else:
		return array



