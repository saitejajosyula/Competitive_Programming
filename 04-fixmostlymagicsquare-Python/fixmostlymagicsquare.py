# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):

	lis = []

	for i in L:

		j = 0

		j = j + sum(i)

		lis.append(j)
	
	if(len(lis) != len(set(lis))):

		k = max(lis) - min(lis)

		largest = max(lis)

		for i in lis:

			if i == largest:

				ind = lis.index(max(lis))
		
		a = L[ind]

		b = a.index(max(a))

		a[b] = max(a) - k

		L[ind] = a

		return L