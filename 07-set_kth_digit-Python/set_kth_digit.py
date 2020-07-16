# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):

	a = str(n) 
	ch = str(d) 

	lis = [i for i in a]

	new_lis = []
	for i in reversed(lis):
		new_lis.append(i)

	lis[k] = ch 

	new = "".join(new_lis)[::-1]

	return int(new)

