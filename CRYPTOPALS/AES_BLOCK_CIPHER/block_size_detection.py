import encrypt as enc
def block_size_detection(key,random_key):
	n = 0
	ct = enc.encrption('A' , key)
	prev_len = len(ct)

	print('[+]trying out possible key sizes')

	while  1:
		ct = enc.encrption('A'*n , key,random_key)
		current_len = len(ct)
		if current_len != prev_len: 
			block_len = current_len - prev_len
			cipher_len = prev_len - n
			block_count = cipher_len % block_len
			print("\n*************Match found*************")
			print('Cipher length found || length = ',cipher_len)
			break
		prev_len = current_len
		n += 1

	return block_len,cipher_len,block_count