# Solution to AdveRSArial Cypto (Infant)

This challenge is a great introduction to the RSA encryption system. It forces you to understand the real concept behind instead of just using online tools to get the solution.

First, let's take a look at how the RSA encryption works:

## RSA Key Generation

1. **Choose two large prime numbers** $p$ and $q$

    These numbers are used to generate the keys.

2. **Compute $n$**:

   $n = p \times q$

   The value $n$ will be part of both the public and private keys.

3. **Compute Euler's Totient function** $\phi(n)$, where:
   
   $\phi(n) = (p - 1) \times (q - 1)$
   

4. **Choose the public key exponent $e$** such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.
   
   In most cases $e$ will be 65537.

5. **Compute the private key exponent $d$**, which is the modular inverse of $e$ modulo $\phi(n)$:
   
   $d \equiv e^{-1} \ (\text{mod} \ \phi(n))$
   
   This means $d \times e \mod \phi(n) = 1$.

## RSA Encryption

Given a public key $(e, n)$ and a message $m$:

1. **Convert the message** $m$ into a number smaller than $n$, using an encoding scheme like ASCII or UTF-8.

2. **Encrypt the message** by computing:
   
   $c = m^e \ (\text{mod} \ n)$
   
   where $c$ is the ciphertext.

## RSA Decryption

Given the private key $(d, n)$ and a ciphertext $c$:

1. **Decrypt the ciphertext** by computing:
   
   $m = c^d \ (\text{mod} \ n)$
   
   where $m$ is the original message in its numeric form.

## Example

For example, if:
- $p = 61$
- $q = 53$
- $e = 17$

Then:
1. Compute $n = 61 \times 53 = 3233$.
2. Compute $\phi(n) = (61 - 1) \times (53 - 1) = 3120$.
3. Compute $d = 2753$, such that $17 \times 2753 \equiv 1 \ (\text{mod} \ 3120)$.

To encrypt the message $m = 65$:

$c = 65^{17} \ (\text{mod} \ 3233) = 2790$


To decrypt the ciphertext $c = 2790$:

$m = 2790^{2753} \ (\text{mod} \ 3233) = 65$

## How do we solve the challenge ?

In our case, we have n, e, and c (like in many RSA challenges). So how do we crack it ?

When we look at the python script that were used to encrypt the flag, we can see that `n = getStrongPrime(2048)`.

The ***getStrongPrime*** function gives you a prime number, but n should be the multiplication of two prime number instead !

To find the private key $d$, we need to find $\phi(n)$. But $\phi(n) = (p - 1) \times (q - 1)$, which we cannot get since we didn't generate $p$ and $q$.

This the breach in the code, because by definition, $\phi(n)$ is equal to the amount of $k < n$ where $\gcd(k, n) = 1$.

So if $n$ is prime, $\phi(n) = n - 1$ and we can simply compute the private key $d$ !

## Getting the flag with python

Finally, in our python script, we redefine n, e and c using the `output.txt`, then we do this:

```python
phi_n = n - 1 # Because n is a prime number
d = pow(e, -1, phi_n) # Computes the private key
m = pow(c, d, n) # Retreive the message

print(long_to_bytes(m).decode()) # Prints the message in ASCII

```

And we have our flag: `FCSC{d0bf88291bcd488f28a809c9ae79d53da9caefc85b3790f57615e61c70a45f3c}`