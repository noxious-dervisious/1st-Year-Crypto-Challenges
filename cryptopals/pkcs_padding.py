def padding (pt,block_size=16) :
	length = len(pt)
	padding = block_size - (length % block_size)
	ct = pt + (chr(padding))*padding 
	return ct

def unpadding (ct,block_size=16) :
	unpad = ord(list(ct)[-1])
	return ct[:-unpad]

#print(len(unpadding(padding("YELLOW SUBMARINE",20),20)))