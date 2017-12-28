#!/usr/bin/python3

from copy import deepcopy
from collections import OrderedDict

###PREPARE TEXT FOR PARSING###
def prepare_text(x):

    x = x.upper()
    x = x.replace(' ','')
    x = x.replace('J','I')

    return x

###CIPHER MATRIX CREATION###
def create_matrix():
    global ciptxt, cipmat, keyword
    #Define base alphabet matrix
    alphamat = ['A','B','C','D','E',
    'F','G','H','I','K',
    'L','M','N','O','P',
    'Q','R','S','T','U',
    'V','W','X','Y','Z']


    #Prepare cipher matrix with initial values
    cipmat = deepcopy(alphamat)

    #Remove repeated characters from keyword
    unqkey = ''.join(OrderedDict.fromkeys(keyword))

    #Create list from key
    key = list(unqkey)

    #Assign unique letters of key to cipher matrix
    for x in range(0,len(unqkey)):
                cipmat[x] = unqkey[x]

    #Create list of remaining letters not in the key
    rmdr = list(set(alphamat) - set(key))

    #Order remaining letters alphabetically
    rmdr.sort()

    #Assign remaining letters to cipher matrix
    for x in range(len(unqkey),len(cipmat)):
        cipmat[x] = rmdr[x-len(unqkey)]


###ENCRYPTION###
def enc():
    global ciptxt, cipmat


    wid = 5     #key table matrix width
    buf = 'X'   #buffer character for ciphertext preparation

    #Insert buffer between repeated letters
    for x in range(1, len(ciptxt)):
        if ciptxt[x] == ciptxt[x-1]:
            ciptxt.insert(x,buf)

    #ensure that blocks of 2 can be created
    if (len(ciptxt) % 2) == 1:
        ciptxt.append(buf)

    #split up the ciphertext into blocks of 2
    tmp =[]
    for x in range(0, len(ciptxt) // 2):
        tmp.append(ciptxt[(x*2)] + ciptxt[(x*2)+1])
    ciptxt = tmp

    #transform the text based on cipher matrix
    for x in range(0,len(ciptxt)):

        block = ciptxt[x]   #select block

        #seperate values of chosen block
        a = block[0]
        b = block[1]

        #determine position of each value in cipher matrix
        a_x = cipmat.index(a) % wid
        a_y = cipmat.index(a) // wid
        b_x = cipmat.index(b) % wid
        b_y = cipmat.index(b) // wid

        #If each value is on the same row, assign to the value to the right
        if(a_y == b_y):
            if(a_x > 3):
                a_x = 0
            else:
                a_x += 1

            if(b_x > 3):
                b_x = 0
            else:
                b_x += 1
        #If both values are in the same column, assign to the value below
        elif(a_x == b_x):
            if(a_y > 3):
                a_y = 0
            else:
                a_y += 1

            if(b_y > 3):
                b_y = 0
            else:
                b_y += 1
        #If both x and y values are different, swap x values
        else:
            a_x, b_x = b_x, a_x

        #Replace existing block with newly ciphered one
        a = cipmat[(a_y*wid)+a_x]
        b = cipmat[(b_y*wid)+b_x]
        ciptxt[x] = a + b

###DECRYPTION###
def dec():
    global cipin, cipmat

    wid = 5     #key table matrix width
    buf = 'X'   #buffer character for ciphertext preparation

    #split up the ciphertext into blocks of 2
    tmp =[]
    for x in range(0, len(cipin) // 2):
        tmp.append(cipin[(x*2)] + cipin[(x*2)+1])
    cipin = tmp

    #transform the text based on cipher matrix
    for x in range(0,len(cipin)):

        block = cipin[x]   #select block

        #seperate values of chosen block
        a = block[0]
        b = block[1]

        #determine position of each value in cipher matrix
        a_x = cipmat.index(a) % wid
        a_y = cipmat.index(a) // wid
        b_x = cipmat.index(b) % wid
        b_y = cipmat.index(b) // wid

        #If each value is on the same row, assign to the value to the left
        if(a_y == b_y):
            if(a_x < 1):
                a_x = 4
            else:
                a_x -= 1

            if(b_x < 1):
                b_x = 4
            else:
                b_x -= 1
        #If both values are in the same column, assign to the value above
        elif(a_x == b_x):
            if(a_y < 1):
                a_y = 4
            else:
                a_y -= 1

            if(b_y < 1):
                b_y = 4
            else:
                b_y -= 1
        #If both x and y values are different, swap x values
        else:
            a_x, b_x = b_x, a_x

        #Replace existing block with newly ciphered one
        a = cipmat[(a_y*wid)+a_x]
        b = cipmat[(b_y*wid)+b_x]
        cipin[x] = a + b
