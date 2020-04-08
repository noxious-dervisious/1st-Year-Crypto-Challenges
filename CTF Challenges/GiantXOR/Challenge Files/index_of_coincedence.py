from __future__ import division
def indexOFcoincidence(ciphertext):
	IC = []
	text_size = len(ciphertext)
	for i in range (len(ciphertext)):
		count_match = 0
		if ciphertext[i] == " ":
			continue
		for j in range (i,len(ciphertext)): 
			if ciphertext[i] == ciphertext[j]:
				count_match += 1
		ciphertext = ciphertext.replace(ciphertext[i]," ")
		count_avg = count_match * (count_match - 1)
		IC.append(count_avg)
	if text_size == 1 :
		return 1
	indexOFcoincidence= sum(IC)/(text_size * (text_size-1))
	return indexOFcoincidence


#message = "THEREARETWOWAYSOFCONSTRUCTINGASOFTWAREDESIGNONEWAYISTOMAKEITSOSIMPLETHATTHEREAREOBVIOUSLYNODEFICIENCIESANDTHEOTHERWAYISTOMAKEITSOCOMPLICATEDTHATTHEREARENOOBVIOUSDEFICIENCIESTHEFIRSTMETHODISFARMOREDIFFICULT"
#message = "a"
#print(indexOFcoincidence(message))
