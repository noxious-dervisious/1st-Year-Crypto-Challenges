#!/usr/bin/env python

import argparse
from hashlib import sha256
from Crypto.Cipher import AES
import os
import sys

BLOCK_SIZE = 16
PAD_LIMIT = 48
KEY = os.urandom(16)

pad_len = lambda inp: (BLOCK_SIZE - len(inp) % BLOCK_SIZE)
pad = lambda inp: inp + chr(pad_len(inp))*pad_len(inp)


class AESCipher:
    def __init__(self, key):
        self.key = sha256(key).digest()

    def encrypt(self, raw):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return "".join("{:02x}".format(ord(c)) for c in cipher.encrypt(raw))

    def mod_pad(self, inp, flag_size):
        input_len = len(inp)
        if input_len > PAD_LIMIT:
            excess_len = input_len - PAD_LIMIT
            if excess_len > flag_size:
                padded_inp = inp[flag_size:flag_size + PAD_LIMIT]
            else:
                padded_inp = inp[:flag_size - excess_len] + inp[flag_size:]
            return padded_inp
        else:
            padded_inp= pad(inp)
            return padded_inp

    def mod_encrypt(self, raw, flag_size):
        raw = self.mod_pad(raw, flag_size)
        encrypted_data = self.encrypt(raw)
        return encrypted_data
def exploit():
    cipher_len = 0
    user_input = ''
    prev_len = len(aescipher.mod_encrypt(flag + user_input, flag_size).decode('hex'))
    print(prev_len)
    n = 1
    pt = ''
    while 1 :
        user_input = 'a' * n
        cipher_len = len(aescipher.mod_encrypt(flag + user_input, flag_size).decode('hex'))
        print(cipher_len)
        if cipher_len != prev_len :
            cipher_len = (cipher_len -16) - n
            break 
        n += 1
    print(cipher_len,prev_len)
    for  i in range (cipher_len):
        user_input = 'a'*(47-i)
        prev_cipher = aescipher.mod_encrypt(flag + user_input, flag_size).decode('hex')
        for j in range (128):
            user_input = chr(j) + 'a'*(47-i)
            cur_cipher = aescipher.mod_encrypt(flag + user_input, flag_size).decode('hex')
            if prev_cipher[:cipher_len-1] == cur_cipher[:cipher_len-1]:
                pt += chr(j)
                break
    print(pt)

if __name__ == "__main__":
    with open("flag.txt") as fp:
        flag = fp.read()
    #flag = "ctf{challenge_done_asdgfgsfhdaaaaaaaaaaaaaaaaaa}"
    # flag = open('flag.txt').read().strip()
    # print(len(flag))
    flag_size = len(flag)
    print(flag_size)
    if flag_size >  PAD_LIMIT:
        print("Flag is too big")
        exit(1)
    aescipher = AESCipher(key=KEY)
    req_count = 0
 #    while req_count < 0x1900:
 #        req_count += 1
 #        user_input = raw_input()
 #        if len(user_input) > 0x64:
 #            continue
 #        sys.stdout.write(aescipher.mod_encrypt(flag + user_input, flag_size))
	# sys.stdout.write('\n')
	# sys.stdout.flush()
    exploit()
