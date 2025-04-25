from Crypto.Cipher import ARC4
from binascii import unhexlify

cifrado = unhexlify("f89f73d86a1011db32625f6a219855c0d87bada7dd6fe030d75c2a45f5b478aec9b823dc73")
texto_plano_supuesto = b"FLAG{"

keystream = bytes([c ^ p for c, p in zip(cifrado[:5], texto_plano_supuesto)])
print(f"Posible keystream inicial: {keystream.hex()}")


claves_comunes = [
    b"secret",
    b"password",
    b"rc4key",
    b"onepiece",
    b"zoro",
    b"luffy",
    b"21276"  # carné
]

for clave in claves_comunes:
    try:
        rc4 = ARC4.new(clave)
        descifrado = rc4.decrypt(cifrado)
        if b"FLAG" in descifrado:
            print(f"Clave posible: {clave}")
            print(f"Texto descifrado: {descifrado}")
            break
    except:
        continue