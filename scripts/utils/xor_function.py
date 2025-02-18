def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    text_bytes = text.encode()  # Convertir el texto a bytes
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text


student_id = input("Ingrese su número de estudiante: ")
cipher_text = input("Ingrese el texto cifrado: ")
print(xor_cipher(cipher_text, student_id).decode())