# Locked Dungeons 2 from SWAMPCTF

This is a two-step challenge:

First, we have to create a modified encrypted output that, when decrypted, contains "get_modflag_md5":
```python
if "get_modflag_md5" in dec_recv_str:
            next_level = True
            sys.stdout.write("Dungeon goes deeper..\n")
            sys.stdout.flush()
```
Once we are through this stage, we have to extract the flag, by submitting up to 500 encrypted values, and getting the md5 hash of the decrypted value back:
```python
dec_recv_str = aescipher.decrypt_wrapper(enc_recv_str)
            sys.stdout.write(b64encode(md5(dec_recv_str).digest()))
            sys.stdout.write("\n")
```

First things first: this challenge uses AES in CBC mode, with a random key and IV for each connection.Now we need to understand a few things about AES CBC mode first before procceding with anything.

![blockdiagramdecryption](https://github.com/noxious-dervisious/Begineer-s-Challenge/blob/master/CTF%20Challenges/LockedDungeoons2/Images/CBC_decryption.png)
![blockdiagramencryption](https://github.com/noxious-dervisious/Begineer-s-Challenge/blob/master/CTF%20Challenges/LockedDungeoons2/Images/CBC_encryption.png)

For the first part of the challenge, we need to insert get_modflag_md5 into the decrypted data. To do so, we use the knowledge that send_modflag_enc will be part of the decrypted data. To simplify things, we will assume the decrypted data will have the form send_modflag_encflag{.....}. The same method can be extended to situations where send_modflag_enc is in another block.

First, note that we are using AES, which means a 16-byte block size. send_modflag_enc is exactly 16 bytes. Now, let's take a look at how CBC decryption works. We know the decrypted contents of the first block is send_modflag_enc, we know the encrypted first block and we know the IV. Decryption of the first block works as follows: 
```decrypted_block = AES_Decrypt_block(encrypted_block) ^ IV ``` 
i.e., 
``` 'send_modflag_enc' = AES_Decrypt_block(encrypted_block) ^ IV``` .
However, we can also modify the IV, which means we can directly control the decrypted block. If we choose 
```newIV = oldIV ^ 'send_modflag_enc' ^ 'get_modflag_md5 '```,
then we find that

```python
def aes_cbc_bit_flip_attack(IV):
	present = "send_modflag_enc"
	desired = "aget_modflag_md5"

	present = list(present)
	desired = list(desired)
	IV = list(IV)

	for i in range (len(IV)):
		IV[i] = chr(ord(desired[i]) ^ ord(IV[i]) ^ ord(present[i]))
	return ''.join(IV)
```

The above function generates the required message for me.

After we get Dungeon goes deeper.. as result, we can continue with the second part of the challenge: extracting the flag. For this, we first take a more detailed look at the decryption method:
```python
def decrypt_wrapper(self, encoded_enc_str):
    enc_str = b64decode(encoded_enc_str)
    return self.__decrypt(enc_str[16:], enc_str[:16])

def __decrypt(self, enc_str, iv):
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    decrypted_str = cipher.decrypt(enc_str)
    decrypted_str = unpad(decrypted_str)
    return decrypted_str
    
unpad = lambda inp: inp[:-ord(inp[-1])]
```
Where the unpad method looks interesting: this implements a very basic form of PKCS7 unpadding, without any validation (e.g. validating that the result is ≤ 16 bytes, that all removed padding bytes contain the same value). Note that this validation is generally not useful, as the data should have been MACed to begin with.

What this means is that as long as we can change the last byte to be e.g. length-1, we get the md5 hash of the first character of the plaintext data. We can then easily enumerate the md5 hashes, get the first character, and repeat with all subsequent characters.

The easiest way to do this is to add two blocks to the ciphertext: aaaaaaaaaaaaaaaX aaaaaaaaaaaaaaa, where we change X to be every possible byte. This means that the decrypted last byte will be ```plain_last_byte = AES_Decrypt(last_block)[-1] ⊕ X```, and because ```AES_Decrypt(last_block)[-1]``` is constant, plain_last_byte will take every value (although we will not know which value corresponds to which value of X).

This scenerio perfectly depicts the application of ```byte-byte decryption of a CBC encryption ```

For further reference please refer my [exploit](https://github.com/noxious-dervisious/1st-Year-Crypto-Challenges/blob/master/CTF_Challenges/LockedDungeoons2/exploit.py)
