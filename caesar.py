#!/usr/bin/python3

alphabet = ['A','B','C','D','E','F','G',
'H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

def enc(plntxt, key):
    for x in range(0, len(plntxt)):
        if plntxt[x] in alphabet:
            plntxt[x] = alphabet[(alphabet.index(plntxt[x]) + key) % len(alphabet)]
    return plntxt

def dec(plntxt, key):
    for x in range(0, len(plntxt)):
        if plntxt[x] in alphabet:
            plntxt[x] = alphabet[(alphabet.index(plntxt[x]) - key) % len(alphabet)]
    return plntxt

def menu():
    print("""===CAESAR CIPHER===
    1. Encrypt
    2. Decrypt
    0. Quit
    """)
    choice = True
    while(choice != 0):
        try:
            choice = int(input("please select: "))

            if(choice == 1):
                key = int(input("Enter the rotation value(key): "))
                plntxt = input("Enter the text you want to encrypt: ")
                plntxt = plntxt.upper()
                plntxt = list(plntxt)
                ciptxt = enc(plntxt, key)

                print("Key: " + str(key))
                print("Ciphertext: " + ''.join(ciptxt))

            elif(choice == 2):
                key = int(input("Enter the rotation value(key): "))
                plntxt = input("Enter the text you want to encrypt")
                plntxt = plntxt.upper()
                plntxt = list(plntxt)
                ciptxt = enc(plntxt, key)

                print("Key: " + str(key))
                print("Plaintext: " + ''.join(ciptxt))

            elif(choice == 0):
                print("goodbye!")
            else:
                print("please try again!")
        except ValueError:
            print("Please use a numeric value")

menu()
