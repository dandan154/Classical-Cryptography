
from collections import OrderedDict
import math

#Default polybius square with 6x6 dimensions
polybius_six = ["A","B","C","D","E","F",
"G","H","I","J","K","L",
"M","N","O","P","Q","R",
"S","T","U","V","W","X",
"Y","Z","0","1","2","3",
"4","5","6","7","8","9"]

#Default polybius square with 5x5 dimensions
polybius_five = ['A','B','C','D','E',
'F','G','H','I','K',
'L','M','N','O','P',
'Q','R','S','T','U',
'V','W','X','Y','Z']

#Default uppercase alphabet
alphabet = ['A','B','C','D','E',
'F','G','H','I','K',
'L','M','N','O','P',
'Q','R','S','T','U',
'V','W','X','Y','Z']

#Single digit integers in string format
digits = ["0","1","2","3","4","5","6","7","8","9"]

def keyword_shift(keyword, square):
	"""
	Create polybius square using keyword.

	Arguments:
	keyword -- string value by which a polybius square is shifted by
	square -- polybius square - character list
    """
	#Get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	#Remove repeated characters and add to list
	shift=list(''.join(OrderedDict.fromkeys(keyword)))

	if(dim == 5):

		#Determine the remaining characters to be added to square
		rmdr = list(set(alphabet) - set(shift))

		rmdr.sort()		#Sort characters alphabetically

		#Combine keyword with remaining characters
		shift += rmdr

	elif(dim == 6):

		#Determine the remaining characters to be added to square
		char = list(set(alphabet) - set(shift))
		dgt = list(set(digits) - set(shift))

		char.sort()		#Sort characters alphabetically
		dgt.sort()		#Sort digits lowest to highest

		#Combine remaining letters with digits - letters first
		rmdr = char + dgt

		#Combine keyword with remaining characters
		shift += rmdr

	return shift

def enc(plntxt,square):
	"""
	Encrypt a string using a given polybius square.

	Arguments:
	plntxt -- string value of text that is to be encrypted via the square
	square -- polybius square - character list
    """
	#Get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	ciptxt=[]
	for x in range(0,len(plntxt)):

		#Get list position of current character
		ind = square.index(plntxt[x])

		char_x = int(ind/dim)+1		#X coordinate of character
		char_y = (ind%dim)+1		#Y coordinate of character

		#Combine coordinate values into string and add to ciphertext
		ciptxt.append(str(char_x) + str(char_y))

	return ciptxt

def dec(ciptxt, square):
	"""
	Decrypt a ciphertext string using a given polybius square.

	Arguments:
	ciptxt -- ciphertext to be converted through the use of the square
	square -- polybius square - character list
   	"""
	#Get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	#Parse through ciphertext and convert to characters
	tmp=[]
	for x in range(0, int(len(ciptxt)/2)):

		#Get individual values of coordinates & convert to index lookup
		ind = (int(ciptxt[(x*2)]) - 1) * dim + (int(ciptxt[x*2 + 1]) - 1)

		#Add new character to decrypted plaintext
		tmp.append(square[ind])

	ciptxt = tmp

	return ciptxt

def bifid_enc(plntxt,square):
	"""
	Encrypt a plaintext string using a polybius square using Bifid encryption.

	Arguments:
	plntxt -- plaintext to be ciphered
	square -- polybius square - character list
	"""
	#Run plaintext through standard polybius encryption to get coordinates
	ciptxt = enc(plntxt, square)

	row_top=[]		#List of every character's Y coordinate
	row_bottom=[]	#List of every character's X coordinate

	#Seperate each character's coordinates into rows
	for x in range(0, len(ciptxt)):
		block = ciptxt[x]
		row_top.append(block[0])
		row_bottom.append(block[1])

	#Merge rows to create new ciphertext
	ciptxt = row_top + row_bottom

	#Merge single axis values into coordinate pairs
	tmp=[]
	for x in range(0, len(row_top)):
		 tmp.append(''.join(ciptxt[(x * 2):(x * 2 + 2)]))
	ciptxt = tmp

	#Get character representations of coordinates
	ciptxt = dec("".join(ciptxt),square)

	return ciptxt

def bifid_dec(ciptxt,square):
	"""
	Decrypt a ciphertext string using a polybius square using Bifid encryption.

	Arguments:
	ciptxt -- ciphertext to be decrypted
	square -- polybius square - character list
	"""
bifid_enc("ABCDE", polybius_five)
