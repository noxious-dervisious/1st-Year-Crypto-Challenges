from Crypto.Cipher import AES
import os
from pkcs_padding import *
from hashlib import md5

keylength = 16

KEY = os.urandom(keylength)
IV = os.urandom(keylength)

class AESCipher :
	def __init__(self,key):
		self.key = md5(key).digest()
	def encrypt_CBC(self,payload,IV):
		lock = AES.new(self.key,AES.MODE_CBC,IV)
		prepond = "comment1=cooking%20MCs;userdata="
		postpond = ";comment2=%20like%20a%20pound%20of%20bacon"
		payload = list(payload)
		for i in range (len(payload)) :
			if payload[i] == ';' or payload[i] == '=':
				payload[i] = "#"
		payload = ''.join(payload)
		ciphertext = prepond + payload + postpond
		ciphertext = padding(ciphertext)
		ciphertext = lock.encrypt(ciphertext)
		return ciphertext

	def decrypt_CBC(self,ciphertext,IV):
		lock = AES.new(self.key,AES.MODE_CBC,IV)
		plaintext = lock.decrypt(ciphertext)
		plaintext = unpadding(plaintext)
		if ";admin=True;" in plaintext:
			return True
		else :
			return False

aescipher = AESCipher(KEY)
payload = ";admin=True;"
ciphertext = aescipher.encrypt_CBC(payload,IV)

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
	if aescipher.decrypt_CBC(ciphertext,IV) :
		print("Welcome Admin")
	else :
		print("Alert there's an attack")
exploit()
