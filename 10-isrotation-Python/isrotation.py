# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	a = str(x)
	b = str(y)

	len1 = len(a)
	len2 = len(b)

	temp = ''

	if len1 != len2:
		return False

	if a == b[::-1]:
		return True

	temp = a + a

	if temp.count(b) > 0:

		return True
	else:
		return False