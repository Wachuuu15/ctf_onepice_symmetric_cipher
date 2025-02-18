import os
import random
import numpy as numpy
from PIL import Image, ImageDraw
from scripts.utils.poneglyph_content import get_challenges_texts
import hashlib
import piexif

active_challenges = {
    "luffy": True, #1
    "zoro": False, #2
    "usopp": False, #3
    "sanji": False, #4
    "nami": False, #5
    "robin": False, #6
}


# Función para crear imágenes "poneglyph"
def create_poneglyph_image(text, filename):   
    # Abrir la imagen de la lista de "poneglyphs"
    img = Image.open(poneglyphs[filename])
    d = ImageDraw.Draw(img)
    
    # Agregar texto visible en la imagen
    d.text((10, 10), text, fill=(255, 255, 0))
    
    # Verificar si la imagen tiene EXIF
    exif_data = img.info.get('exif')
    
    if exif_data:
        exif_dict = piexif.load(exif_data)
    else:
        # Si no hay EXIF, inicializamos un diccionario vacío
        exif_dict = piexif.load(piexif.dump({}))
    
    # Agregar el texto como metadato EXIF (campo Artist o UserComment)
    exif_dict['0th'][piexif.ImageIFD.Artist] = text.encode('utf-8')  # Usando 'Artist' para almacenar el texto
    
    # Convertir los metadatos a formato EXIF
    exif_bytes = piexif.dump(exif_dict)
    
    # Guardar la imagen con el texto visible y los metadatos
    img.save(f"challenges/{filename}/poneglyph.jpeg", exif=exif_bytes)

# Función para cifrar un texto con XOR
def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    text_bytes = text.encode()  # Convertir el texto a bytes
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text

# Copia el archivo Dockerfile a la carpeta del reto
def create_docker_file(docker_file, challenge):
    with open(docker_file, "r") as file:
        content = file.read()
    
    with open(f"challenges/{challenge}/Dockerfile", "w") as file:
        file.write(content)

# Copia el script de carpetas aleatorias a la carpeta del reto
def create_random_folders_script(challenge):
    with open("scripts/utils/random_folders.py", "r") as file:
        content = file.read()
    
    with open(f"challenges/{challenge}/random_folders.py", "w") as file:
        file.write(content)

# Función para generar los retos
def build_challenges():
    # remove old challenges directory
    os.system("rm -rf challenges")

    # Generar las flags y cifrados
    for challenge, text in texts.items():
        # Verificar si el reto está activo
        if active_challenges[challenge] == False:
            continue
        # Cifrar el texto con el id del estudiante
        cipher_text = xor_cipher(text, student_id)

        # Directorio para el reto
        challenge_dir = f"challenges/{challenge}" 

        # Crear directorio si no existe
        os.makedirs(challenge_dir, exist_ok=True)

        # Generar imagen "poneglyph"
        create_poneglyph_image(cipher_text.decode('utf-8'), challenge)
        # Copiar el Dockerfile template
        create_docker_file(docker_files[challenge],challenge)
        # Copiar el script de carpetas aleatorias
        create_random_folders_script(challenge)

        # Guardar la flag
        flag_student_challenge = f"{student_id}_{challenge}_{random_number}"
        flag_hash = hashlib.md5(flag_student_challenge.encode()).hexdigest()
        flag = f"FLAG_{flag_hash}"
        flag_xored = xor_cipher(flag, student_id).decode('utf-8')
        
        
        # Cifrar flag con student_id
        
        with open(f"{challenge_dir}/flag.txt", "w") as flag_file:
            if challenge == "luffy":
                flag_file.write(flag_xored)
            else:
                flag_file.write(flag)



random_number = random.randint(0, 5)
# Solicitar el carné del estudiante
student_id = input("Ingrese su carné: ")
texts_list = get_challenges_texts(random_number)
# Definir las imágenes "poneglyphs"
poneglyphs = {
    "luffy": "scripts/poneglyphs/luffy.jpeg",
    "zoro": "scripts/poneglyphs/zoro.jpeg",
    "usopp": "scripts/poneglyphs/ussop.jpeg",
    "sanji": "scripts/poneglyphs/sanji.jpeg",
    "nami": "scripts/poneglyphs/nami.jpeg",
    "robin": "scripts/poneglyphs/robin.jpeg",
}
# Definir los textos para los retos
texts = {
    "luffy": texts_list[0],
    "zoro": texts_list[1],
    "usopp": texts_list[2],
    "sanji": texts_list[3],
    "nami": texts_list[4],
    "robin": texts_list[5],
}
# Dockerfiles
docker_files = {
    "luffy": "scripts/dockerfiles/luffy/Dockerfile",
    "zoro": "scripts/dockerfiles/zoro/Dockerfile",
    "usopp": "scripts/dockerfiles/usopp/Dockerfile",
    "sanji": "scripts/dockerfiles/sanji/Dockerfile",
    "nami": "scripts/dockerfiles/nami/Dockerfile",
    "robin": "scripts/dockerfiles/robin/Dockerfile",
}

build_challenges()
print("Retos generados con éxito!")