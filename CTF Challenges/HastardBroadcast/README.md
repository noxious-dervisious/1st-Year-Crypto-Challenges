# Hastad's Broadcast Attack

We will start by discussing the simplest form of Hastad's Broadcast Attack on unpadded messages and then generalise the attack on linearly padded messages using Coppersmith's Theorem.

## Hastad's Broadcast Attack on unpadded messages
Suppose Alice sends an unpadded message M to `k` people P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>k</sub> each using a same small public key exponent `e` and different moduli `N` for ith individual, the public key for ith individual (N<sub>i</sub>, e). The attack states that as soon as `k >= e`, the message M is no longer secure and we can recover it easily using [Chinese Remainder Theorem](https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html).

Let us understand this attack using an example: Alice sends a message `M` to 3 three different people using the same public key exponent `e = 3`. Let the ciphertext received by `i`th receiver be C<sub>i</sub> where C<sub>i</sub> = M<sup>3</sup> mod N<sub>i</sub>. We have to assume that **gcd(N<sub>i</sub>, N<sub>j</sub>) == 1** where `i != j`

We can now write:

![equation](https://github.com/noxious-dervisious/Begineer-s-Challenge/blob/master/CTF%20Challenges/HastardBroadcast/1.gif)  
![equation](https://github.com/noxious-dervisious/Begineer-s-Challenge/blob/master/CTF%20Challenges/HastardBroadcast/2.gif)  
![equation](https://github.com/noxious-dervisious/Begineer-s-Challenge/blob/master/CTF%20Challenges/HastardBroadcast/3.gif)  

Thus we can get the following by solving using Chinese Remainder Theorem:  
![equation](https://github.com/noxious-dervisious/Begineer-s-Challenge/blob/master/CTF%20Challenges/HastardBroadcast/4.gif)  
where b<sub>i</sub> = N/N<sub>i</sub>, b<sub>i</sub><sup>'</sup> = b<sub>i</sub><sup>-1</sup> mod N<sub>i</sub> and N = N<sub>1</sub>\* N<sub>2</sub>\* N<sub>3</sub>. Since we know that M < N<sub>i</sub> (If our message M is larger than the modulus N, then we won't get the exact message when we decrypt the ciphertext, we will get an equivalent message instead, which is not favourable).   
Therefore we can write M < N<sub>1</sub>N<sub>2</sub>N<sub>3</sub>. We can easily calculate `M` now by directly taking the `cube root` of M<sup>3</sup> to get `M`.

You can find an implementation of this attack here: [exploit.py](exploit.py)

## So what am I suppose to do with this ?
```
1. Calculate N = n1\*n2\*...
2. Calculate each element T[j] as per the above conditions using CRT
3. Assign P.<x> = PolynomialRing(Zmod(N))
4. g[j] = (i*(2^m) + x)^e - c, where the message is padded using the above conditions
5. Assign g = Sum_of(T[j] * g[j])
6. Check if g is a monic polynomial, if not transform it into a monic polynomial
7. Find small roots of g and check if that is the flag
```
Before you start with this challenge I want you to know about something else known as Small Public Key Exponent attack.

# Small Public Key Exponent Attack

Let’s say Alice wants to share a small message M (a symmetric key) over an insecure channel. She encrypts it using RSA. n is chosen from strong primes and is quite big but she chose e=3.
It wouldn’t be a problem if she had used padding but it’s obviously not the case. You intercept the message and deduce from the public key that it was computed like so :

   &nbsp;<img src="https://render.githubusercontent.com/render/math?math=c = m^{3}modN">

But because M is small, <img src="https://render.githubusercontent.com/render/math?math=m^{3}"> < N
 so it wasn’t affected by the modulo. You just need to compute the third root of C to get the original message.
