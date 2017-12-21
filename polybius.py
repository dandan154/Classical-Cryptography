
from collections import OrderedDict
import math

#default polybius square with 6x6 dimensions
polybius_six = ["A","B","C","D","E","F",
"G","H","I","J","K","L",
"M","N","O","P","Q","R",
"S","T","U","V","W","X",
"Y","Z","0","1","2","3",
"4","5","6","7","8","9"]

#default polybius square with 5x5 dimensions
polybius_five = ['A','B','C','D','E',
'F','G','H','I','K',
'L','M','N','O','P',
'Q','R','S','T','U',
'V','W','X','Y','Z']

#default uppercase alphabet
alphabet = ['A','B','C','D','E',
'F','G','H','I','K',
'L','M','N','O','P',
'Q','R','S','T','U',
'V','W','X','Y','Z']

#single digit integers in string format
digits = ["0","1","2","3","4","5","6","7","8","9"]

def keyword_shift(keyword, square):

	#get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	#remove repeated characters and add to list
	shift=list(''.join(OrderedDict.fromkeys(keyword)))

	if(dim == 5):

		#determine the remaining characters to be added to square
		rmdr = list(set(alphabet) - set(shift))

		rmdr.sort()		#sort characters alphabetically

		#combine keyword with remaining characters
		shift += rmdr

	elif(dim == 6):

		#determine the remaining characters to be added to square
		char = list(set(alphabet) - set(shift))
		dgt = list(set(digits) - set(shift))

		char.sort() 	#sort characters alphabetically
		dgt.sort()		#sort digits lowest to highest

		#combine remaining letters with digits - letters first
		rmdr = char + dgt

		#combine keyword with remaining characters
		shift += rmdr

	return shift 

keyword_shift("BIGTEST",polybius_six)
