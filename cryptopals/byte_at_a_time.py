from Crypto.Cipher import AES
import os
import encrypt as enc
from block_size_detection import *

keylength = 16 
key =  os.urandom(keylength)

random_key =''

def exploit ():
	pt = ''

	block_len,cipher_len,block_count=block_size_detection(key,random_key)
	for i in range (1,cipher_len+1) :
		user = 'a' * (cipher_len - i)
		required = enc.encrption(user , key)
		for j in range (128):
			re_user = 'a' * len(user) + pt + chr(j)  
			found = enc.encrption(re_user , key)
			if required[:len(re_user)] == found[:len(re_user)] :
				pt += chr(j)
				break	
	print('\nHere\'s your flag : \n')
	print(pt)
	#print(pt.decode('utf-8'))	
exploit()





