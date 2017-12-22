
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
	"""
	Create polybius square using keyword.

	Arguments:
	keyword -- string value by which a polybius square is shifted by
	square -- polybius square - character list
    """
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

		char.sort()		#sort characters alphabetically
		dgt.sort()		#sort digits lowest to highest

		#combine remaining letters with digits - letters first
		rmdr = char + dgt

		#combine keyword with remaining characters
		shift += rmdr

	return shift

def enc(plntxt,square):
	"""
	Encrypt a string using a given polybius square

	Arguments:
	plntxt -- string value of text that is to be encrypted via the square
	square -- polybius square - character list
    """
	#get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	ciptxt=[]
	for x in range(0,len(plntxt)):

		#get list position of current character
		ind = square.index(plntxt[x])

		char_x = int(ind/dim)+1		#get X coordinate of character
		char_y = (ind%dim)+1		#get Y coordinate of character

		#combine coordinate values into string and add to ciphertext
		ciptxt.append(str(char_x) + str(char_y))

	print(" ".join(ciptxt))

	return ciptxt

def dec(ciptxt, square):
	"""
	Decrypt a ciphertext string using a given polybius square

	Arguments:
	ciptxt -- ciphertext to be converted through the use of the square
	square -- polybius square - character list
   	"""
	#get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	#parse through ciphertext and convert to characters
	tmp=[]
	for x in range(0, int(len(ciptxt)/2)):

		#Get individual values of coordinates & convert to index lookup
		ind = (int(ciptxt[(x*2)]) - 1) * dim + (int(ciptxt[x*2 + 1]) - 1)

		#Add new character to decrypted plaintext
		tmp.append(square[ind])

	ciptxt = tmp

	return ciptxt

help(dec)
help(enc)
