# Blinding Attack on Digital Signature using RSA

## Introduction to the concept

Before moving into this challenge we will look into what happens in a Digital Signature and What is this blinding attack.

### Digital Signature using RSA

How Signing Works
For any RSA public/private key triple, He, d, nL, the key mathematical fact is that the encryption and decryption
functions are inverses of one another. That is, if
**f(m) = m^e mod n is the encryption function (which is public)**
and
**g(m) = m^d mod n is the the decryption function (which is private)**,
then
**f(g(m)) = m and g(f(m)) = m**

The idea behind a digital signature using RSA is that f is a function that is known to everyone, but only you know yourdecryption function. In order for Alice to sign a message, m, sends gAHmL together with an indication that the messageis from Alice. When Bob gets it, he sees that the message is from Alice and applies her public encryption function, fA,
to gAHmL and will get m. If Claude tries to send a spoofed message, m', purportedly from Alice to Bob, he has no wayof being successful since he doesn’t know gA.
You can sign a message without encrypting it. In the scheme described inthis section, anyone can intercept Alice’ssigned message and read it because her public key is known.

### Blinding Attack on Digital Signature using RSA.

One of the simplest blind signature schemes is based on RSA signing. A traditional RSA signature is computed by raising the message m to the secret exponent d modulo the public modulus N. The blind version uses a random value r, such that r is relatively prime to N (i.e. gcd(r, N) = 1). r is raised to the public exponent e modulo N, and the resulting value r^e mod N is used as a blinding factor. The author of the message computes the product of the message and blinding factor, i.e.:

![image1]

and sends the resulting value {\displaystyle m'}m' to the signing authority. Because r is a random value and the mapping r^e mod N is a permutation it follows that r^e mod  N is random too. This implies that m' does not leak any information about m. The signing authority then calculates the blinded signature s' as:

![image2]

s' is sent back to the author of the message, who can then remove the blinding factor to reveal s, the valid RSA signature of m:

![image3]

This works because RSA keys satisfy the equation ![image5]
and thus,

![image4]

hence s is indeed the signature of m.

In practice, the property that signing one blinded message produces at most one valid signed messages is usually desired. This means one vote per signed ballot in elections, for example. This property does not hold for the simple scheme described above: the original message and the unblinded signature is valid, but so is the blinded message and the blind signature, and possibly other combinations given a clever attacker. A solution to this is to blind sign a cryptographic hash of the message, not the message itself.