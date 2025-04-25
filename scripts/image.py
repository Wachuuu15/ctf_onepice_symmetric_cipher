from PIL import Image
import requests
from io import BytesIO

# Descargar la imagen
response = requests.get("http://localhost:8083/poneglyph.jpeg")
img = Image.open(BytesIO(response.content))

# Extraer metadatos
artist_cifrado = img.getexif().get(315, "")
print("Texto cifrado:", artist_cifrado)

def xor_decrypt(cifrado, clave):
    return bytes([ord(c) ^ ord(clave[i % len(clave)]) for i, c in enumerate(cifrado)]).decode('utf-8', errors='ignore')

# Descifrar con carné
clave = "21276"  
texto_descifrado = xor_decrypt(artist_cifrado, clave)
print("\nTexto descifrado:", texto_descifrado)