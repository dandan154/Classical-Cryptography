#!/usr/bin/python3

from collections import OrderedDict

def enc(plntxt, rail):
    plntxt = list(plntxt)
    cyc = (rail*2)-2        #number of characters in a cycle
    ciptxt=[]

    #Add characters to ciphertext based on the rail that they are on
    for x in range (0, rail):
        for y in range (0, len(plntxt)):
            #Add character to cipher if it matches current rail
            if (y%cyc == x):
                ciptxt.append(plntxt[y])
            #Work back up rails and add appropriate characters
            elif(y % cyc > (rail-1)):
                if(y%(rail-1) == x):
                    ciptxt.append(plntxt[y])

    return ciptxt

def dec(ciptxt, rail):

    size =len(ciptxt)               #number of characters in ciphertext
    railwidth = int(length/rail)    #number of cycles that occur
    cyc = (rail*2)-2                #number of characters in a cycle

    plntxt=[]

def menu():
    print("""===RAIL FENCE CIPHER===
    1. Encrypt
    2. Decrypt
    0. Quit
    """)
    choice = True
    while(choice != 0):
        choice = int(input("please select: "))

        if(choice == 1):
            enc("WEAREDISCOVEREDFLEEATONCE",3)
        elif(choice == 2):
            dec("WECRLTEERDSOEEFEAOCAIVDEN",3)
        elif(choice == 0):
            print("goodbye!")
        else:
            print("please try again!")

menu()
