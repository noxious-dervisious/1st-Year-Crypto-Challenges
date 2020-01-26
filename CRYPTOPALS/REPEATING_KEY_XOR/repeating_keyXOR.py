def reapeting_key_xor (pt,key) :
	index= 0
	ct = '' 
	for ch in pt:
		ct += str(hex(ord(ch) ^ ord(key[index])))
		if index + 1 == len(key):
			index=0
		else :
			index += 1
	return ct.replace('0x','')
def main():
	# pt = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	# key = "ICE"
	# output = reapeting_key_xor(pt,key)
	# print(output)
	# result = "b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
	# print(len(output),len(result))
	# if output == result :
	# 	print("OK")
	pt = 'ATGCAAGGTCTCTTGACCCAGTGGATACTAAATGCCTGGAAGGTAGCATACTAG'
	key = 'GCACUCUCCGGAUGAU'
	output = reapeting_key_xor(pt,key)
	print(output)
main()
