#!/usr/bin/python3

from collections import OrderedDict

def enc(plntxt, rail):
    plntxt = list(plntxt)
    cyc = (rail*2)-2
    ciptxt=[]

    for x in range (0, rail):
        print(x)
        for y in range (0, len(plntxt)):
            if (y%cyc == x):
                ciptxt.append(plntxt[y])
            elif(y % cyc > (rail-1)):
                if(y%(rail-1) == x):
                    ciptxt.append(plntxt[y])

    print("Ciphertext: " + ''.join(ciptxt))

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
            #WECRLTEE RDSOEEFEAOCAIVDEN
        elif(choice == 2):
            print(2)

        elif(choice == 0):
            print("goodbye!")
        else:
            print("please try again!")

menu()
