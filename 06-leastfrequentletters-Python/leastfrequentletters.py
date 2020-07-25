# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

import string

def leastfrequentletters(s):
	# Your code goes here

	if len(s) == 0:

		return ''
	
	s = s.lower()

	a = string.ascii_lowercase

	i = 0

	m = 1000

	out = ''

	while i < 26:

		count = s.count(a[i])

		if m > count > 0 :

			m = count

			out = a[i]
		
		elif m == count:
			out = out + a[i]
		
		i = i + 1
	
	if out == '':

		return out
	
	return out
	
