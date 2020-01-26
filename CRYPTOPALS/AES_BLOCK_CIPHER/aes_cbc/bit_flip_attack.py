from Crypto.Cipher import AES
import os
from encrypt import encrypt_CBC as enc
from encrypt import decrypt_CBC as dec

keylength = 16

key = os.urandom(keylength)
IV = os.urandom(keylength)

payload = ";admin=True;"
ciphertext = enc(payload,key,IV)

def exploit():
	cipher_block = []
	global ciphertext
	for i in range (0,len(ciphertext),keylength):
		cipher_block.append(ciphertext[i:i+keylength])
	required = list(cipher_block[1])
	cipher_block.remove(cipher_block[1])
	required[0] = chr(ord('#')^ord(required[0])^ord(';'))
	required[6] = chr(ord('#')^ord(required[6])^ord('='))
	required[11] = chr(ord('#')^ord(required[11])^ord(';'))
	required = ''.join(required)
	cipher_block.insert(1,required)
	ciphertext = ''.join(cipher_block)
	plaintext = dec(ciphertext,key,IV)
	if ";admin=True;" in plaintext:
		print("Logged in as Admin")
	else :
		print("Sorry try again")

exploit()