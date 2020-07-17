# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here

	if len(str1) != len(str2):
		return False

	if str1 == (str2)[::-1]:
		return True


	clock = ""
	# clock = clock + str1[9:] + str1[:9]
	clock = str2[len(str2)-1:]+ clock + str2[:len(str2)-1]

	anticlock = ""

	anticlock = anticlock + str2[len(str2)-2:] + str2[:len(str2)-2]

	return clock == str1 or anticlock == str1
	
	if str1.index('J') != str2.index('J'):
		
		ant_clock = ""
		ch = str1.index('J')
		
		ant_clock = ant_clock + str1[ch:] + str1[:ch]
		
		return ant_clock == str2
		