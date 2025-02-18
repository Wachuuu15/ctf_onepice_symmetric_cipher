
from PIL import Image
import piexif

def extraer_texto_metadata(imagen_path):
    # Abrir la imagen
    img = Image.open(imagen_path)
    
    # Obtener los metadatos EXIF
    exif_dict = piexif.load(img.info.get('exif', b''))
    
    # Obtener el texto almacenado en 'Artist' (o en el campo que elegimos)
    texto = exif_dict['0th'].get(piexif.ImageIFD.Artist)
    if texto:
        return texto.decode('utf-8')
    return None

# Función para cifrar un texto con XOR
def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    text_bytes = text.encode()  # Convertir el texto a bytes
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text
    
# Uso del código para descifrar la imagen
# Ejemplo de uso
image_path = "challenges/luffy/poneglyph.jpeg"
student_id = input("Introduce tu carné para descifrar el mensaje: ")
texto_cifrado = extraer_texto_metadata(image_path)
decrypted_text = xor_cipher(texto_cifrado, student_id)
print(decrypted_text)

