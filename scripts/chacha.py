from Crypto.Cipher import ChaCha20

# cifrado en hexadecimal
cifrado_hex = "afc8c49520c01776355dead482b0f9c4ccb24aa391aa0c10f037f87d2306d63818bdb7e989"
cifrado = bytes.fromhex(cifrado_hex)

def generate_key_nonce(user_id):
    key = (user_id.encode() * 32)[:32]  # Clave de 32 bytes
    nonce = (user_id.encode() * 8)[:8]  # Nonce de 8 bytes (deberían ser 12, pero el código usa 8)
    return key, nonce

# clave carne
user_id = "21276"
key, nonce = generate_key_nonce(user_id)

nonce += b"\x00"*4  # Añadimos 4 bytes nulos para llegar a 12 ya que el codigo de referencia solo usa 8

try:
    cipher = ChaCha20.new(key=key, nonce=nonce[:8])
    flag_descifrada = cipher.decrypt(cifrado)
    print(f"Flag descifrada: {flag_descifrada.decode()}")
except Exception as e:
    print(f"Error al descifrar: {e}")