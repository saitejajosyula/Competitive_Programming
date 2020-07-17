# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	
	length = len(a)

	if a == []:
		return None
	
	if length%2 ==0:

		result = a[length//2]
		result1 = a[length//2 - 1]
		median = (result+result1)/2
	else:
		median = a[length//2]

	return median