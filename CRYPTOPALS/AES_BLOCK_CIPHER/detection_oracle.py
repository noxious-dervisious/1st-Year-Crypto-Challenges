from Crypto.Cipher import AES
import random 
import os
import base64 

keylength = 16

mode = random.choice(['ECB','CBC'])
key = os.urandom(keylength)
IV = os.urandom(keylength)

def encryption_AES (pt) :
	if mode == 'ECB':
		cipher = AES.new(key,AES.MODE_ECB)
	elif mode == 'CBC' :
		cipher = AES.new(key,AES.MODE_CBC,IV)
	ct = cipher.encrypt(pt)
	return ct 

def detection_oracle (ct) :
	ct_list = []
	ct_list += [ct[i:i+keylength] for i in range (0,len(ct),keylength)]
	
	# cipher = AES.new(key,AES.MODE_ECB)

	# block_1 = cipher.decrypt(ct_list[0])
	# block_2 = cipher.decrypt(ct_list[1])
	
	if ct_list[0] == ct_list[1] :
		return 'ECB'
	else :
		return 'CBC'

def main() :
	pt = input("Enter the input : ")
	print("The detection_oracle returns : ",detection_oracle(encryption_AES(pt)))
	print("The original mode : ",mode)
	print("Key : ",key)
	print("IV : ",IV)

main()
