cifrado = bytes.fromhex("747d7370690509540703560402040f56085756045754570f540105050f5700040601555153")
clave = b"21276"
resultado = [cifrado[i] ^ clave[i % len(clave)] for i in range(len(cifrado))]

print("Primeros 15 bytes descifrados:", bytes(resultado[:15]).decode())