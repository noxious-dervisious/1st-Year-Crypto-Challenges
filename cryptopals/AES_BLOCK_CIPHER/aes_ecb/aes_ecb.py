from Crypto.Cipher import AES
import base64 

key = "YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)

file = open('aes_txt.txt').read()
file = base64.b64decode(file)

plaintext = cipher.decrypt(file)

print(plaintext)