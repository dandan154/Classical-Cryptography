#!/usr/bin/python3

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
            print(1)
        elif(choice == 2):
            print(2)

        elif(choice == 0):
            print("goodbye!")
        else:
            print("please try again!")
