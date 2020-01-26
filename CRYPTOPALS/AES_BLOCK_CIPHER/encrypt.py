from Crypto.Cipher import AES
from base64 import *
from pkcs_padding import *

def encrption (user,key,random = '') :
	cipher = AES.new(key,AES.MODE_ECB)
	flag = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
	pt = padding(str(random) + user + str(b64decode(flag)))
	ct = cipher.encrypt(pt)
	return ct

def encrypt_CBC(payload,key,IV):
	lock = AES.new(key,AES.MODE_CBC,IV)
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

def decrypt_CBC(ciphertext,key,IV):
	lock = AES.new(key,AES.MODE_CBC,IV)
	plaintext = lock.decrypt(ciphertext)
	plaintext = unpadding(plaintext)
	return plaintext

