#!/bin/bash

echo "===CAESAR TEST==="
python3 crypto.py HELLO -k 13
python crypto.py URYYB -k 13 -d
echo ''
echo "===POLYBIUS TEST==="
python3 crypto.py HELLO -c polybius -s WORLD
python3 crypto.py 3224141412 -c polybius -s WORLD -d
echo ''
echo "===BIFID TEST==="
python3 crypto.py HELLOWORLD -c bifid -s HELLO
python3 crypto.py HHAOEEMRRM -c bifid -s HELLO -d
echo ''
echo "==TRIFID TEST==="
python3 crypto.py HELLOWORLD -c trifid -s HELLO -g 5
echo "---NO DECRYPT YET---"
echo ''
echo "==PLAYFAIR TEST==="
python3 crypto.py HELLOWORLD -c playfair -k WORLD
python3 crypto.py KBRYDRORLDRZ -c playfair -k WORLD -d
