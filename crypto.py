import polybius
import playfair
import caesar

import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("text", help="The text to be ran through the encryption scheme", type=str)
parser.add_argument("-k", "--key", help="Insert the key used to decrypt or encrypt the given string", default="", type=str)
parser.add_argument("-e", "--encrypt", help="perform an encryption function", action="store_true")
parser.add_argument("-d", "--decrypt", help="perform a decryption function", action="store_true")
parser.add_argument("-c", "--cipher", choices=['caesar', 'polybius', 'bifid', 'nihlist', 'trifid', 'playfair'], default='caesar', help="defines the encryption scheme to use when processing key and text", type=str)
parser.add_argument("-s", "--square", help="defines the keyword by which a polybius square/trifid cube is shifted", default="", type=str)
parser.add_argument("-g", "--group", help="defines the size of the stages in which a plaintext is ciphered (trifid only)", default=0, type=int)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()


def formatter(x):
    x = x.upper()
    x = x.replace(' ','')
    x = x.replace('J','I')
    print(x)
    if not x.isalpha():
        x = ""
    print(x)
    return x

def enc_list(text, key, cipher, square, group):
    output=""
    #Encryption Methods
    if cipher == "caesar":
        try:
            key=int(key)
            output = "".join(caesar.enc(list(text.upper()), key))
        except ValueError:
            output="Incorrect key value entered: for caesar ciphers, use an integer key"

    elif cipher == "polybius":
        output = " ".join(polybius.enc(formatter(text), (polybius.keyword_shift(formatter(square), polybius.polybius_five))))

    elif cipher == "bifid":
        output = "".join(polybius.bifid_enc(formatter(text), (polybius.keyword_shift(formatter(square), polybius.polybius_five))))

    elif cipher == "trifid":
        if group > 0:
            output = polybius.trifid_enc(formatter(text), polybius.keyword_shift(formatter(square), polybius.trifid), group)

    elif cipher =="nihlist":
        output= " ".join(polybius.nihlist_enc(text, key, polybius.keyword_shift(square, polybius.polybius_five)))

    elif cipher == "playfair":
        print("playfair")
    return output

def dec_list(text, key, cipher, square, group):
    output=""
    #Encryption Methods
    if cipher == "caesar":
        try:
            key=int(key)
            output = "".join(caesar.dec(list(text), key))
        except ValueError:
            output="Incorrect key value entered: for caesar ciphers, use an integer key"

    elif cipher == "polybius":
        output = "".join(polybius.dec(text, (polybius.keyword_shift(square, polybius.polybius_five))))

    elif cipher == "bifid":
        output = "".join(polybius.bifid_dec(text, (polybius.keyword_shift(square, polybius.polybius_five))))

    elif cipher == "trifid":
        output = polybius.trifid_dec(text, polybius.keyword_shift(square, polybius.trifid), group)

    elif cipher =="nihlist":
        output= " ".join(polybius.nihlist_dec(text, key, polybius.keyword_shift(square, polybius.polybius_five)))

    elif cipher == "playfair":
        print("playfair")

    return output


output=""
if args.verbose:

    #Display encryption scheme
    print("ENCRYPTION: " + (args.cipher).upper())

    #Display key value
    if args.key != "":
        print("KEY: " + args.key)

    #Display group size
    if args.group > 0:
        print("GROUPING: " + str(args.group))

    output += "CIPHERTEXT: "

if args.decrypt:
    output += dec_list(args.text, args.key, args.cipher, args.square, args.group)
else:
    output += enc_list(args.text, args.key, args.cipher, args.square, args.group)

print(output)
