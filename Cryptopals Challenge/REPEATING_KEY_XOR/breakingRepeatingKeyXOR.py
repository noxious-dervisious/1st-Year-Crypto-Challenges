from __future__ import division
from english_attack import *
from base64 import *

def hammingDistance(arg1,arg2):
	hammingDistance = 0
	for b1 ,b2 in zip(arg1,arg2):
		difference = ord(b1) ^ ord(b2)
		hammingDistance += sum([1 for bit in bin(difference) if bit == '1'])
	return hammingDistance

#print(hammingDistance('this is a test','wokka wokka!!!'))

def key_length (ciphertext):
	normalise = []
	#hamDistanceList =[]	
	for keylength in range (2,41) :
		avg = []
		start = 0
		end =start + keylength
		while (1):
			chunk_1 = ciphertext[start:end] 
			chunk_2 = ciphertext[start+keylength:end+keylength]
			if len(chunk_1) > len(chunk_2):
				break
			hamDistance = hammingDistance(chunk_1,chunk_2)
			# hamDistanceList.append(hamDistance)  
			# print(hamDistanceList[0])
			avg.append(hamDistance/keylength)
			start = start+keylength
			end = start + keylength
		#print(sum(avg),len(avg))
		result = {
		'key' : keylength,
		'avg_distance' : sum(avg)/len(avg)
		}
		normalise.append(result)
	return sorted(normalise,key = lambda x: x['avg_distance'])[0]

def breaking_repeating_keyXOR (ciphertext,key_length = []):			
	keylength = key_length['key']
	key = ''
	for i in range (keylength):
		chunk = ""
		for j in range (i,len(ciphertext),keylength) :
			chunk += ciphertext[j]
		key += chr(exploit(chunk))
	print("The key is ({}) of keylength {} \nThe plaintext is : \n ".format(key,keylength))
	simple = reapeting_key_xor(ciphertext,key)
	return simple

def main():
	file = open('repeatingXOR.txt').read().strip()
	#file = open('gaintXOR.txt').read().strip()
	#ciphertext = b64decode(file).rep
	ciphertext = b64decode(file)
	#ciphertext = file.decode('hex')
	#print(key_length(ciphertext))
	print(breaking_repeating_keyXOR(ciphertext,key_length(ciphertext)))

main()
