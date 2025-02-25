import os
import random
import numpy as numpy
from PIL import Image, ImageDraw
import hashlib
import piexif

# Definir las imágenes "poneglyphs"
poneglyphs = {
    "luffy": "resources/poneglyphs/luffy.jpeg",
    "zoro": "resources/poneglyphs/zoro.jpeg",
    "usopp": "resources/poneglyphs/usopp.jpeg",
    "sanji": "resources/poneglyphs/sanji.jpeg",
    "nami": "resources/poneglyphs/nami.jpeg",
    "robin": "resources/poneglyphs/robin.jpeg",
}


# Función para crear imágenes "poneglyph"
def create_poneglyph_image(text, challenge, password, location):
    # Abrir la imagen de la lista de "poneglyphs"
    img = Image.open(poneglyphs[challenge])
    d = ImageDraw.Draw(img)

    # Agregar texto visible en la imagen
    d.text((10, 10), text, fill=(255, 255, 0))

    # Verificar si la imagen tiene EXIF
    exif_data = img.info.get("exif")

    if exif_data:
        exif_dict = piexif.load(exif_data)
    else:
        # Si no hay EXIF, inicializamos un diccionario vacío
        exif_dict = piexif.load(piexif.dump({}))

    # Agregar el texto como metadato EXIF (campo Artist o UserComment)
    exif_dict["0th"][piexif.ImageIFD.Artist] = text.encode(
        "utf-8"
    )  # Usando 'Artist' para almacenar el texto

    # Convertir los metadatos a formato EXIF
    exif_bytes = piexif.dump(exif_dict)

    # Guardar la imagen con el texto visible y los metadatos
    img.save(f"challenges/{challenge}/poneglyph.jpeg", exif=exif_bytes)
    # Guardar un zip de la imagen con password
     
    os.system(f"zip -P {password} -r {location}/poneglyph.zip challenges/{challenge}/poneglyph.jpeg")
    # Eliminar la imagen original
    os.system(f"rm challenges/{challenge}/poneglyph.jpeg")
