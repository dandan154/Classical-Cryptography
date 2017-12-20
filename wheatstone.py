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
for x in range(0,len(unqkey)):
            cipmat[x] = unqkey[x]

#create list of remaining letters not in the key
rmdr = list(set(alphamat) - set(key))

#ensure alphabetical order of remaining letters
rmdr.sort()

for x in range(len(unqkey),len(cipmat)):
    cipmat[x] = rmdr[(x-len(unqkey))]

print(cipmat)

#Get user plaintext to be encrypted
plntxt = input("Enter the message you wish to encrypt: ")

#Prepare plaintext for ciphering - remove whitespace, replace Js and capitalize letters
plntxt = plntxt.upper()
plntxt = plntxt.replace(' ', '')
plntxt = plntxt.replace('J','I')
ciptxt = list(plntxt)

#Insert buffer between repeated letters
for x in range(1, len(ciptxt)):
    if ciptxt[x] == ciptxt[x-1]:
        ciptxt.insert(x,buf)

#ensure that blocks of 2 can be created
if (len(ciptxt)%2) == 1:
    ciptxt.append(buf)

###DEBUGGING###
#print(cipmat)
#print(alphamat)
#print(size)
#print(unqkey)
#print(ciptxt)
#print(plntxt)
