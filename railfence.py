#!/usr/bin/python3

def enc(plntxt, rail):
    print("enc")
def dec(ciptxt, rail):
    print("dec")

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
