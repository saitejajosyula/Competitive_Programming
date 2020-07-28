# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):

	if len(s1) == len(s2):

		output = ""

		for i in range(len(s2)):

			output = output + s1[i] + s2[i]
		
		return output
	

	elif len(s1) < len(s2):

		output = ""

		for i in range(len(s1)):

			output = output + s1[i] + s2[i]
		
		output = output + s2[(len(s2) - len(s1)-1):]

		return result
	
	else:

		if " " in s1:
			x = s1.split(" ")[0]
			y = s1.split(" ")[1]

			if len(x) > len(y) :

				output = ""
				for i in range(len(s2)):
					output = output + x[i]+s2[i]
				
				output = output + x[(len(s2)- len(x)):]
				output = output +" "+y

				return output
		
		else:

			output = ""

			for i in range(len(s2)):
				output = output + s1[i]+s2[i]

			output = output + s1[(len(s1)-len(s2))-2:]
			return output