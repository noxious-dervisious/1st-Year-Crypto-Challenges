from __future__ import print_function
from builtins import input
pt=input("Enter the string to be xor'd : ").decode('hex')
xor=input("Enter the string to be xor'd against : ").decode('hex')
ct=""
ct_hex=""
for i in range (len(pt)) :
	ct+=chr(ord(pt[i]) ^ ord(xor[i]))
	ct_hex+=str(hex((ord(pt[i]) ^ ord(xor[i])))).replace('0x','')
print("Ascii string after xor'em : ",ct)
print("Hex string after xor'em : ",ct_hex)
 # verify the cryptopal challenge
result = "746865206b696420646f6e277420706c6179"
if ct_hex == result :
 	print("OK")

