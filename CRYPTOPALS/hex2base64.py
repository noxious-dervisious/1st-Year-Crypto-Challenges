from __future__ import print_function
from builtins import input
import base64
pt=input("Enter a hex encoded string : ")
hex2alpha = pt.decode('hex')
alpha2base64 = base64.b64encode(hex2alpha)
print("The base64 encoded string is : ",alpha2base64)
# for the verification of the cryptopal challenge questions application
result= "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
if alpha2base64 == result :
	print("ok")