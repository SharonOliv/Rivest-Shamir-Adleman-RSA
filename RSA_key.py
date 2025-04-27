import random
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(bits=8):
    while True:
        num = random.randint(2**(bits-1), 2**bits - 1)
        if is_prime(num):
            return num

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

# Key Generation
public_key, private_key = generate_keys()
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")