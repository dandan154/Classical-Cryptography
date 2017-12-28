# Classical Cryptography
A selection of classical cryptographic techniques

## Cipher List

* Polybius Square
  * Bifid
  * Trifid (Missing Decryption)
  * Nihlist
  * ADFGVX (not implemented)
* Caesar
* Playfair
* Rail fence (not implemented)

## Example Usage

Perform a ROT13 cipher shift on a simple plaintext:
```
python3 cipher.py "HELLO WORLD" -c caesar -e -k 13
```

Decipher polybius coordinate numbers using a standard polybius square:
```
python3 crypto.py "23153131345234423114" -c polybius -d
```
Encrypt a plaintext using the key "HELLO" and a polybius square shifted with the keyword "WORLD":
```
python3 crypto.py HELLOWORLD -c nihlist -k HELLO -s WORLD
```
