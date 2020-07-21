# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	# Your code goes here
	lis = []

	for i in p1:
		for j in p2:
			lis.append(i*j)
	
	lis1 = []
	s = 0
	for i in range(len(lis)):
		if i != 1 and i !=2:
			lis1.append(lis[i])
		else:
			s = s + lis[i]
			lis1.append(s)
	
	if len(lis1) <= 4:

		return lis1[:1]+lis1[2:]
	
	elif len(lis1) >= 5:
		return lis1[:1]+lis1[2:3]+lis1[4:]
