def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    if type(text) == str:
        text_bytes = text.encode()
    else:
        text_bytes = text
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text

# Pruebas de la función
# Cifrado de un texto
text = "747d7370690509540703560402040f56085756045754570f540105050f5700040601555153"
key = "21276"
cipher_text = xor_cipher(bytes.fromhex(text), key)
# Si los bytes son texto legible, se puede decodificar a UTF-8
decoded_text = cipher_text.decode('utf-8')
print("FLAG 21276 -> ",decoded_text)