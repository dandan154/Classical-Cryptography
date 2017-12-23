
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
	keyword -- keyword that shifts the square - string
	square -- polybius square - character list

	Returns:
	shift -- shifted polybius square - character list
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
	plntxt -- text that is to be encrypted via the square - string
	square -- polybius square - character list

	Returns:
	ciptxt --ciphered plaintext - character list
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
	ciptxt -- ciphertext to be converted through the use of the square - string
	square -- polybius square - character list

	Returns:
	plntxt -- decrypted ciphertext - character list
   	"""
	#Get dimensions of polybius square
	dim = int(math.sqrt(len(square)))

	#Parse through ciphertext and convert to characters
	plntxt=[]
	for x in range(0, int(len(ciptxt)/2)):

		#Get individual values of coordinates & convert to index lookup
		ind = (int(ciptxt[(x*2)]) - 1) * dim + (int(ciptxt[x*2 + 1]) - 1)

		#Add new character to decrypted plaintext
		plntxt.append(square[ind])

	return plntxt

def bifid_enc(plntxt,square):
	"""
	Encrypt a plaintext string using a polybius square via Bifid encryption.

	Arguments:
	plntxt -- plaintext to be ciphered - string
	square -- polybius square - character list

	Returns:
	ciptxt -- ciphered plaintext - string
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
	Decrypt a ciphertext string using a polybius square via Bifid decryption.

	Arguments:
	ciptxt -- ciphertext to be decrypted - string
	square -- polybius square - character list

	Returns:
	plntxt -- decrypted plaintext - string
	"""
	#Run ciphertext through standard polybius encryption to get coordinates
	plntxt = enc(ciptxt, square)

	#Seperate each axis' coordinates into seperate rows
	pln_str = "".join(plntxt)
	row_top=list(pln_str[0:int(len(pln_str)/2)])
	row_bottom=list(pln_str[int(len(pln_str)/2):len(pln_str)])

	#Match original X and Y coordinates together
	pln_str=""
	for x in range(0, len(row_top)):
		pln_str += (row_top[x] + row_bottom[x])

	#Convert coordinate pairs into characters
	plntxt = dec(pln_str,square)

	return plntxt

def nihlist_enc(plntxt, key, square):
	"""
	Encrypt a plaintext string using a polybius square via Nihlist ciphering.

	Arguments:
	plntxt -- plaintext to be encrypted - string
	key --	used to encrypt text - string
	square -- polybius square - character list

	Returns:
	ciptxt -- list of encypted characters - integer list
	"""
	plen = len(plntxt)	#plaintext length
	klen = len(key)		#key length

	#Repeat key to match plaintext length
	if(plen > klen):
		key = (key * (int(plen/klen) + 1))
		key = key[0:plen]

	#Get polybius square integer representations of key and plaintext
	ciptxt = list(map(int, enc(plntxt, square)))
	keylist = list(map(int, enc(key, square)))

	#Add key and plaintext polybius integer values together
	for x in range(0, plen):
		ciptxt[x] = ciptxt[x] + keylist[x]

	return ciptxt

def nihlist_dec(ciptxt, key, square):
	"""
	Decrypt a ciphertext string using a polybius square via Nihlist decryption.

	Arguments:
	ciptxt -- list of ciphertext to be decrypted - integer list
	key -- used to decrypt text - string
	square -- polybius square - character list

	Returns:
	plntxt -- decrypted plaintext - string
	"""
	clen = len(ciptxt)	#ciphertext length
	klen = len(key)		#key length

	#Repeat key to match ciphertext length
	if(clen > klen):
		key =  (key * (int(clen/klen) + 1))
		key = key[0:clen]

	#Prepare key for arithmetic
	keylist = list(map(int, enc(key, square)))

	#Get original plaintext values
	for x in range(0, clen):
		ciptxt[x] = ciptxt[x] - keylist[x]

	#Convert plaintext integers to characters
	ciptxt = list(map(str, ciptxt))
	plntxt = dec("".join(ciptxt), square)
	plntxt = "".join(plntxt)

	return plntxt
###TESTING###
#print(nihlist_dec([37, 106, 62, 36, 67, 47, 86, 26, 104, 53, 62, 77, 27, 55, 57, 66, 55, 36, 54, 27]
#,"RUSSIAN", keyword_shift("ZEBRAS", polybius_five)))

#print(enc("THE",polybius_five))
#print(dec("".join(enc("THE",polybius_five)), polybius_five))
