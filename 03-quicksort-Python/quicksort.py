"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	
	lo  = 0

	hi = array.length - 1

	pi = partition(array, lo, hi) # selecting pivot element

	quicksort(array, lo, pi-1) #sorts elements left to pivot

	quicksort(array, pi+1, hi) #sorts elements right to pivot


def partition(array, low, high):
	
	pivot = array[high]

	i = low - 1

	for j in range(low, high):

		if array[i] <= array[pivot]:
			i = i + 1

			array[i], array[j] = array[j], array[i]
	
	array[i+1], array[high] = array[high], array[i+1]

	return i + 1




