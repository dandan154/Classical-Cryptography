#!/usr/bin/python3

from copy import deepcopy
from collections import OrderedDict

#Assign cipher key
keyword = "PLAYFAIREXAMPLE"
#keyword = keyword.upper()

#Define base alphabet matrix
alphamat = ['A','B','C','D','E',
'F','G','H','I','K',
'L','M','N','O','P',
'Q','R','S','T','U',
'V','W','X','Y','Z']


dim = 5     #key table matrix width
buf = 'X'   #buffer character for ciphertext preparation

#size = sum(len(x) for x in alphamat)

#prepare cipher matrix with initial values
cipmat = deepcopy(alphamat)

#remove repeated characters from keyword
unqkey = ''.join(OrderedDict.fromkeys(keyword))

#create list from key
key = list(unqkey)

#Assign unique letters of key to cipher matrix
i=0
for x in range(0,len(unqkey)):
            cipmat[x] = unqkey[x]

#for x in range(i,size)


#Get user plaintext to be encrypted
plntxt = input("Enter the message you wish to encrypt: ")

#Prepare plaintext for ciphering - remove whitespace and capitalize letters
plntxt = plntxt.replace(" ", "")
plntxt = plntxt.upper()
ciptxt = list(plntxt)

#Insert buffer between repeated letters
for x in range(1, len(ciptxt)):
    if ciptxt[x] == ciptxt[x-1]:
        ciptxt.insert(x,buf)

#ensure that blocks of 2 can be created
if (len(ciptxt)%2) == 1:
    ciptxt.append(buf)

###DEBUGGING###
print(cipmat)
#print(alphamat)
#print(size)
#print(unqkey)
print(ciptxt)
#print(plntxt)
