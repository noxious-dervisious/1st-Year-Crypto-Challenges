# My Simple Cipher 

As the name suggest this is a simple cipher involving a couple of mathematical operations which we need to reverse in order to obtain our flag. But in this challenge we know a few things like this time we know what’s the key length (it’s set to 13 using the assert len(key) == 13) and we know the message format i.e message = flag + "|" + key. Now we have to exploit this “ | ” given to us.

Now we know this is the equation which encrypts the flag :

 **```encrypted += chr((ord(message[i]) + ord(key[i % len(key)]) + ord(encrypted[i])) % 128)```**

Here there are basically two variables and one equation which is impossible to solve. But we can easily reduce this equation to a one variable one equation format using the “ | ” as we know the position of this which we can back substitute into the equation so as to obtain an equation of one variable that will solve up to give me  one more element in the key. Now again we have a new character which we can use to find one more character of the key.And will soon discover the whole key and once we have the key its not at all difficult to solve the above equation and get the whole message.

Now for that key I wrote a small part script :
```python
j = 21
for i in range (key_length):
	key[j % 13 ] = chr((ord(ciphertext[j+1]) - ord(message[j]) - ord(ciphertext[j])) % 128)
	message[flag_len + 1 + j%13] = key[j%13]
	j = flag_len + 1 + j%13
key = "".join(key)
```
I have used the fact that our key length is 13 to device this simple equation which can get me the key.
Now using the following script I got the whole message 
```python
for alpha in range (len(message)-1):
  message[alpha] = chr((ord(ciphertext[alpha+1]) - ord(key[alpha % key_length]) -ord(ciphertext[alpha])) % 128)
  message = "".join(message)
```
Now this above highlighted expression will help us get the whole message.

You can get the exploit I wrote for this challenge in [here](https://github.com/noxious-dervisious/1st-Year-Crypto-Challenges/blob/master/CTF_Challenges/mysimplecipher/exploit_simple_cipher.py)
