# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

def digitCounter(num):
	
	temp = num
	count = 0
	while temp > 0:
		temp  = temp // 10
		count = count + 1
	return count

def fun_carrylessadd(x, y):

	lenX = digitCounter(x)
	lenY = digitCounter(y)

	length = max(lenX, lenY)

	total = 0

	for i in range(0, length):

		currX = (x // 10 ** i) % 10
		currY = (y // 10 ** i) % 10

		adjX = currX * 10 ** i
		adjY = currY * 10 ** i

		currtotal = (adjY + adjX) % 10 ** (i+1)

		total = total + currtotal

	return total
	

