import random
from binascii import unhexlify

def generate_keystream(seed, length):
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(length)])

def decrypt(ciphertext_hex):
    cipherbytes = unhexlify(ciphertext_hex)
    
    # Probamos primero con el carné como semilla
    seed_candidates = [21276, 2127, 212, 21, 2] + list(range(10000))
    
    for seed in seed_candidates:
        keystream = generate_keystream(seed, len(cipherbytes))
        plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])
        
        if plaintext.startswith(b'FLAG_'):
            print(f"\n[+] FLAG ENCONTRADA con semilla {seed}:")
            return plaintext.decode()
        elif b'FLAG{' in plaintext:
            print(f"\n[+] FLAG alternativa encontrada con semilla {seed}:")
            return plaintext.decode()
    
    return "No se encontró la flag con las semillas probadas"

# mensaje cifrado
cifrado = "a77742694e1853d04f6b6c6ed5c5df7f186e0362ce4a14d9164b71bd10f9ce8db14f05d13d"

# Descifrar
resultado = decrypt(cifrado)
print(resultado)