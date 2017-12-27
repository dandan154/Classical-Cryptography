
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

#Default polybius square with 5x5 dimensions
trifid = ['A','B','C','D','E','F','G','H','I',
'J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z','+']

#Default uppercase alphabet - (NO J)
alphabet = ['A','B','C','D','E',
'F','G','H','I','K',
'L','M','N','O','P',
'Q','R','S','T','U',
'V','W','X','Y','Z']

#Single digit integers in string format
digits = ["0","1","2","3","4","5","6","7","8","9"]

#ADFGVX & ADFGX cipher dictionaries
adfgx_dict = {1:"A", 2:"D", 3:"F", 4:"G", 5:"X"}
adfgvx_dict = {1:"A", 2:"D", 3:"F", 4:"G", 5:"V", 6:"X"}

def keyword_shift(keyword, square):
	"""
	Create polybius square using keyword.

	Arguments:
	keyword -- keyword that shifts the square - string
	square -- polybius square/trifid cube - character list

	Returns:
	shift -- shifted polybius square/trifid cube - character list
    """
	#Get dimensions of polybius square
	dim = int(math.sqrt(len(square)))
	mod = math.sqrt(len(square)) % 1

	#Remove repeated characters and add to list
	shift=list(''.join(OrderedDict.fromkeys(keyword)))

	#Trifid Cube
	if(mod > 0):
		#Determine the remaining characters to be added to square
		rmdr = list(set(trifid) - set(shift))

		rmdr.sort()

		if '+' in rmdr:
			rmdr.remove('+')
			rmdr.append('+')

		shift += rmdr

	#5 x 5 polybius square
	elif(dim == 5):

		#Determine the remaining characters to be added to square
		rmdr = list(set(alphabet) - set(shift))

		rmdr.sort()		#Sort characters alphabetically

		#Combine keyword with remaining characters
		shift += rmdr

	#6 x 6 polybius square
	elif(dim == 6):

		#Determine the remaining characters to be added to square
		char = list(set(alphabet) - set(shift))
		dgt = list(set(digits) - set(shift))

		if 'J' not in shift:
			char.append('J')

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

		char_x = ind // dim + 1		#X coordinate of character
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
	row_top=list(pln_str[0:len(pln_str)//2])
	row_bottom=list(pln_str[len(pln_str)//2:len(pln_str)])

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
		key = (key * (plen // klen) + 1)
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
		key =  (key * (clen // klen) + 1)
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

def trifid_enc(plntxt, cube, group_size):
	"""
	Encrypt a plaintext string using Trifid ciphering

	Arguments:
	plntxt -- plaintext string to be encrypted - string
	cube -- used to encrypt text - character list
	group_size -- used to transform ciphertext - integer

	Returns:
	ciptxt -- encrypted ciphertext - string
	"""
	ciptxt=[]
	#Get coordinate values for each character
	for i in range(0, len(plntxt)):
		z = cube.index(plntxt[i]) // 9
		y = cube.index(plntxt[i]) // 3 % 3
		x = cube.index(plntxt[i]) % 3
		ciptxt.append(str(z) + str(y) + str(x))

	#Get no. of groups to split for encryption
	group_no = len(plntxt) // group_size

	#Get leftover group length
	rmdr = len(plntxt) % group_size

	#Cipher each group individually
	for i in range(0, group_no):

		#Declare lists to store individual axis coordinates
		x, y, z = [],[],[]		#

		#Split coordinates of a value into 3 segments
		for j in range(0, group_size):
			val = ciptxt[j + group_size * i]
			z.append(val[0])
			y.append(val[1])
			x.append(val[2])

		#Combine coordinate lists to determine new character arrangement
		x = z + y + x

		#Get new characters from trifid cube
		for j in range(0, group_size):
			ciptxt[group_size*i + j] = cube[(int(x[j*3])*9 + int(x[j*3 + 1])*3 + int(x[j*3 + 2]))]


	#Cipher remaining partial group with regards to its own size
	if (rmdr > 0):

		#Combine coordinate lists to determine new character arrangement
		x, y, z = [],[],[]

		#Split coordinates of a value into 3 segments
		for i in range(0, rmdr):
			val = ciptxt[group_size * group_no + i]
			z.append(val[0])
			y.append(val[1])
			x.append(val[2])

		#Combine coordinate lists to determine new character arrangement
		x = z + y + x

		#Get new characters from trifid cube
		for j in range(0, rmdr):
			ciptxt[group_size * group_no +j] = cube[(int(x[j*3])*9 + int(x[j*3 + 1])*3 + int(x[j*3 + 2]))]

	return "".join(ciptxt)

def trifid_dec(ciptxt, cube, group_size):
	"""
	Encrypt a plaintext string using Trifid ciphering

	Arguments:
	ciptxt -- list of ciphertext to be decrypted - integer list
	cube -- used to encrypt text - character list
	group_size -- used to transform ciphertext - integer

	Returns:
	plntxt -- decrypted plaintext without spaces - string
	"""

	plntxt=[]
	#Get coordinate values for each character
	for i in range(0, len(ciptxt)):
		z = cube.index(ciptxt[i]) // 9
		y = cube.index(ciptxt[i]) // 3 % 3
		x = cube.index(ciptxt[i]) % 3
		plntxt.append(str(z) + str(y) + str(x))

	#Get no. of groups to split for encryption
	group_no = len(plntxt) // group_size

	#Get leftover group length
	rmdr = len(plntxt) % group_size


def adfgvx_enc(ciptxt, key, square):
	print("enc")

def adfgvx_dec(ciptxt, key, square):
	print("enc")

###TESTING###
print(keyword_shift("FELIXMARIEDELASTELLE", trifid))
print(trifid_enc("AIDETOILECIELTAIDERA",keyword_shift("FELIXMARIEDELASTELLE", trifid), 5))
print(trifid_dec("FMJFVOISSUFTFPUFEQQC", keyword_shift("FELIXMARIEDELASTELLE", trifid), 5))

print(adfgvx_dict[1])
