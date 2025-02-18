import os
import random
import array
import string

ARCOS = [
    "East Blue",
    "Alabasta",
    "Skypiea",
    "Water 7",
    "Sabaody Archipelago",
    "Fishman Island",
    "Pirate Island",
    "Dressrosa",
    "Zou",
    "Wano",
    "Whole Cake Island",
]

# Hacer un shuffle the ARCOS
random.shuffle(ARCOS)
random_size = random.randint(5, len(ARCOS))
ARCOS = ARCOS[:random_size]

LUGARES_ONEPIECE = {
    "East Blue": [
        "Romance Dawn",
        "Shells Town",
        "Orange Town",
        "Syrup Village",
        "Baratie",
        "Arlong Park",
        "Loguetown",
    ],
    "Alabasta": ["Rainbase", "Yuba", "Nanohana", "Katorea", "Spiders Cafe", "Alubarna"],
    "Skypiea": [
        "Angel Beach",
        "Upper Yard",
        "Shandora",
        "Pumpkin Cafe",
        "Heaven's Gate",
    ],
    "Water 7": [
        "Blue Station",
        "Shift Station",
        "Carpenters' Cafe",
        "Galley-La Headquarters",
        "Franky House",
    ],
    "Sabaody Archipelago": [
        "Grove 1",
        "Grove 24",
        "Grove 41",
        "Grove 66",
        "Grove 80",
        "Grove 109",
    ],
    "Fishman Island": [
        "Coral Hill",
        "Gyoverly Hills",
        "Mermaid Cove",
        "Coral Mansion",
        "Gyoncorde Plaza",
    ],
    "Pirate Island": [
        "Pirate's Cove",
        "Pirate's Tavern",
        "Pirate's Hideout",
        "Pirate's Den",
        "Pirate's Ship",
    ],
    "Dressrosa": [
        "Acacia",
        "Corrida Colosseum",
        "Flower Hill",
        "Royal Palace",
        "Toy House",
    ],
    "Zou": [
        "Right Belly Fortress",
        "Left Belly Fortress",
        "Right Hind Leg",
        "Left Hind Leg",
        "Right Fore Leg",
        "Left Fore Leg",
    ],
    "Wano": ["Kuri", "Udon", "Flower Capital", "Ringo", "Onigashima"],
    "Whole Cake Island": [
        "Sweet City",
        "Cacao Island",
        "Caramel Mountain",
        "Whole Cake Chateau",
        "Liqueur Island",
    ],
}
CASAS_ONEPIECE_CON_NOMBRES = {
    "Romance Dawn": ["Casa de Makino", "Casa de Luffy", "Casa de Shanks"],
    "Shells Town": ["Casa de Rika", "Casa de Morgan", "Casa de Helmeppo"],
    "Orange Town": ["Casa de Boodle", "Casa de Nami", "Casa de Gaimon"],
    "Syrup Village": ["Casa de Usopp", "Casa de Kaya", "Casa de Merry"],
    "Baratie": ["Casa de Zeff", "Casa de Sanji", "Casa de Patty"],
    "Arlong Park": ["Casa de Arlong", "Casa de Nami", "Casa de Genzo"],
    "Loguetown": ["Casa de Bell-mère", "Casa de Smoker", "Casa de Dragon"],
    "Rainbase": ["Casa de Vivi", "Casa de Igaram", "Casa de Crocodile"],
    "Yuba": ["Casa de Toto", "Casa de Kohza", "Casa de Pell"],
    "Nanohana": ["Casa de Toto", "Casa de Kohza", "Casa de Pell"],
    "Katorea": ["Casa de Toto", "Casa de Kohza", "Casa de Pell"],
    "Spiders Cafe": ["Casa de Nico Robin", "Casa de Miss All Sunday", "Casa de Mr. 0"],
    "Alubarna": ["Casa de Vivi", "Casa de Igaram", "Casa de Crocodile"],
    "Angel Beach": ["Casa de Conis", "Casa de Pagaya", "Casa de Gan Fall"],
    "Upper Yard": ["Casa de Enel", "Casa de Nami", "Casa de Aisa"],
    "Shandora": ["Casa de Montblanc Norland", "Casa de Calgara", "Casa de Robin"],
    "Pumpkin Cafe": ["Casa de Conis", "Casa de Pagaya", "Casa de Gan Fall"],
    "Heaven's Gate": ["Casa de Enel", "Casa de Nami", "Casa de Aisa"],
    "Blue Station": ["Casa de Paulie", "Casa de Lucci", "Casa de Iceburg"],
    "Shift Station": ["Casa de Paulie", "Casa de Lucci", "Casa de Iceburg"],
    "Carpenters' Cafe": ["Casa de Paulie", "Casa de Lucci", "Casa de Iceburg"],
    "Galley-La Headquarters": ["Casa de Paulie", "Casa de Lucci", "Casa de Iceburg"],
    "Franky House": ["Casa de Franky", "Casa de Iceburg", "Casa de Luffy"],
    "Grove 1": ["Casa de Rayleigh", "Casa de Shakky", "Casa de Keimi"],
    "Grove 24": ["Casa de Rayleigh", "Casa de Shakky", "Casa de Keimi"],
    "Grove 41": ["Casa de Rayleigh", "Casa de Shakky", "Casa de Keimi"],
    "Grove 66": ["Casa de Rayleigh", "Casa de Shakky", "Casa de Keimi"],
    "Grove 80": ["Casa de Rayleigh", "Casa de Shakky", "Casa de Keimi"],
    "Grove 109": ["Casa de Rayleigh", "Casa de Shakky", "Casa de Keimi"],
    "Coral Hill": ["Casa de Otohime", "Casa de Shirahoshi", "Casa de Neptune"],
    "Gyoverly Hills": ["Casa de Otohime", "Casa de Shirahoshi", "Casa de Neptune"],
    "Mermaid Cove": ["Casa de Otohime", "Casa de Shirahoshi", "Casa de Neptune"],
    "Coral Mansion": ["Casa de Otohime", "Casa de Shirahoshi", "Casa de Neptune"],
    "Gyoncorde Plaza": ["Casa de Otohime", "Casa de Shirahoshi", "Casa de Neptune"],
    "Pirate's Cove": ["Casa de Gol D. Roger", "Casa de Whitebeard", "Casa de Shanks"],
    "Pirate's Tavern": ["Casa de Gol D. Roger", "Casa de Whitebeard", "Casa de Shanks"],
    "Pirate's Hideout": [
        "Casa de Gol D. Roger",
        "Casa de Whitebeard",
        "Casa de Shanks",
    ],
    "Pirate's Den": ["Casa de Gol D. Roger", "Casa de Whitebeard", "Casa de Shanks"],
    "Pirate's Ship": ["Casa de Gol D. Roger", "Casa de Whitebeard", "Casa de Shanks"],
    "Acacia": ["Casa de Riku Dold III", "Casa de Viola", "Casa de Rebecca"],
    "Corrida Colosseum": ["Casa de Riku Dold III", "Casa de Viola", "Casa de Rebecca"],
    "Flower Hill": ["Casa de Riku Dold III", "Casa de Viola", "Casa de Rebecca"],
    "Royal Palace": ["Casa de Riku Dold III", "Casa de Viola", "Casa de Rebecca"],
    "Toy House": ["Casa de Sugar", "Casa de Trebol", "Casa de Doflamingo"],
    "Right Belly Fortress": [
        "Casa de Nekomamushi",
        "Casa de Inuarashi",
        "Casa de Kawamatsu",
    ],
    "Left Belly Fortress": [
        "Casa de Nekomamushi",
        "Casa de Inuarashi",
        "Casa de Kawamatsu",
    ],
    "Right Hind Leg": ["Casa de Nekomamushi", "Casa de Inuarashi", "Casa de Kawamatsu"],
    "Left Hind Leg": ["Casa de Nekomamushi", "Casa de Inuarashi", "Casa de Kawamatsu"],
    "Right Fore Leg": ["Casa de Nekomamushi", "Casa de Inuarashi", "Casa de Kawamatsu"],
    "Left Fore Leg": ["Casa de Nekomamushi", "Casa de Inuarashi", "Casa de Kawamatsu"],
    "Kuri": ["Casa de Oden", "Casa de Kozuki Hiyori", "Casa de Kozuki Momonosuke"],
    "Udon": ["Casa de Oden", "Casa de Kozuki Hiyori", "Casa de Kozuki Momonosuke"],
    "Flower Capital": [
        "Casa de Oden",
        "Casa de Kozuki Hiyori",
        "Casa de Kozuki Momonosuke",
    ],
    "Ringo": ["Casa de Oden", "Casa de Kozuki Hiyori", "Casa de Kozuki Momonosuke"],
    "Onigashima": ["Casa de Kaido", "Casa de Orochi", "Casa de Yamato"],
    "Sweet City": ["Casa de Big Mom", "Casa de Pudding", "Casa de Katakuri"],
    "Cacao Island": ["Casa de Big Mom", "Casa de Pudding", "Casa de Katakuri"],
    "Caramel Mountain": ["Casa de Big Mom", "Casa de Pudding", "Casa de Katakuri"],
    "Whole Cake Chateau": ["Casa de Big Mom", "Casa de Pudding", "Casa de Katakuri"],
    "Liqueur Island": ["Casa de Big Mom", "Casa de Pudding", "Casa de Katakuri"],
}

NOMBRE_ARCHIVO_OCULTO = "flag.txt"  # Nombre del archivo oculto
CONTENIDO_ARCHIVO_OCULTO = "FLAG{LABERINTO_COMPLETADO}"  # Contenido del archivo oculto


# Función para crear el laberinto de carpetas
def generar_laberinto(ruta_base):
    carpetas_creadas = []

    for x in ARCOS:
        ruta_arco = os.path.join(ruta_base, x)
        if not os.path.exists(ruta_arco):
            os.mkdir(ruta_arco)
        for lugar in LUGARES_ONEPIECE[x]:
            ruta_lugar = os.path.join(ruta_arco, lugar)
            if not os.path.exists(ruta_lugar):
                os.mkdir(ruta_lugar)
            for casa in CASAS_ONEPIECE_CON_NOMBRES[lugar]:
                ruta_actual_casa = os.path.join(ruta_lugar, casa)
                if not os.path.exists(ruta_actual_casa):
                    os.mkdir(ruta_actual_casa)
                carpetas_creadas.append(ruta_actual_casa)

    return carpetas_creadas


# Función para colocar el archivo oculto en una carpeta aleatoria
def colocar_archivo_oculto(carpetas, nombre_archivo, contenido):
    carpeta_elegida = random.choice(carpetas)
    ruta_archivo = os.path.join(carpeta_elegida, nombre_archivo)
    with open(ruta_archivo, "w") as archivo:
        archivo.write(contenido)
    print(f"Archivo oculto colocado en: {ruta_archivo}")


def crear_archivos_con_ruta(carpetas):
    # Obtener 2 rutas aleatorias
    ruta_aleatoria_1 = random.choice(carpetas)
    ruta_aleatoria_2 = random.choice(carpetas)

    with open("move_flag.sh", "w") as archivo:
        archivo.write(
            "#!/bin/bash\n" f'ruta="{ruta_aleatoria_1}"\n' 'mv flag.txt "$ruta"\n'
        )

    with open("move_image.sh", "w") as archivo:
        archivo.write(
            "#!/bin/bash\n" f'ruta="{ruta_aleatoria_2}"\n' 'mv poneglyph.jpeg "$ruta"\n'
        )


# Directorio base del laberinto
def main():
    # Eliminar el laberinto si ya existe
    if os.path.exists("ONEPIECE"):
        os.system("rm -r ONEPIECE")

    ruta_base = os.path.join(os.getcwd(), "ONEPIECE")
    if not os.path.exists(ruta_base):
        os.mkdir(ruta_base)

    carpetas = generar_laberinto(ruta_base)
    crear_archivos_con_ruta(carpetas)
    print("Laberinto generado con éxito.")


if __name__ == "__main__":
    main()
