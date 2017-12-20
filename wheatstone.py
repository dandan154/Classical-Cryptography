#!/usr/bin/python3

from copy import deepcopy
from collections import OrderedDict

#Assign cipher key
keyword = "PLAYFAIREXAMPLE"
keyword = keyword.upper()

#Define base alphabet matrix
alphamat = [['A', 'B', 'C', 'D', 'E'],
['F','G','H','I','K'],
['L','M','N','O','P'],
['Q','R','S','T','U'],
['V','W','X','Y','Z']]

dim = 5
#size = sum(len(x) for x in alphamat)


encmat = deepcopy(alphamat)


unqkey = ''.join(OrderedDict.fromkeys(keyword))

i=0
for x in range(0,dim):
    for y in range(0, dim):
        if i < len(unqkey):
            encmat[x][y] = unqkey[i]
            i += 1

###DEBUGGING###
#print(encmat)
#print(alphamat)
#print(size)
#print(unqkey)

plntxt = input("Enter the message you wish to encrypt: ")
#print(plntxt)
