from Crypto.Cipher import AES
import base64 

def xor_func(key,IV):
	block = ''
	for i in range (len(key)) :
		block += chr(ord(key[i]) ^ ord(IV[i]))
	return block
		
key = "YELLOW SUBMARINE"
keylength = len(key)
IV = chr(0) * keylength

ct = base64.b64decode(open('aes_cbc.txt').read())

ct_list=[]
ct_list += [ct[i:i+keylength] for i in range (0,len(ct),keylength)]

pt = ""

for block in ct_list:
	cipher = AES.new(key,AES.MODE_ECB)
	pt += xor_func(cipher.decrypt(block),IV)
	IV = block

print(pt)