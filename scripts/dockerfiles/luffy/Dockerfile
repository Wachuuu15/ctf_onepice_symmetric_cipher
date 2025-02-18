# Usamos una imagen base de Ubuntu
FROM ubuntu:22.04

# Evitar interactividad en la instalación de paquetes
# ARG DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    sudo \
    python3 \
    python3-pip \
    python3-dev \
    git \
    vim \
    nano \
    curl \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Crear un usuario "luffy" y darle una contraseña
RUN useradd -ms /bin/bash luffy && echo "luffy:onepiece" | chpasswd && adduser luffy sudo

# Deshabilitamos el acceso directo como root para que los alumnos no inicien con permisos de administrador
RUN passwd -l root

# Establecer el directorio de trabajo
WORKDIR /home/luffy

# Copiar los archivos del reto dentro del contenedor
COPY ./flag.txt /home/luffy/flag.txt
COPY ./poneglyph.jpeg /home/luffy/poneglyph.jpeg
COPY ./random_folders.py /home/luffy/random_folders.py

# Run random_folders.py
RUN python3 /home/luffy/random_folders.py

# Da permisos de ejecución al script
RUN chmod +x /home/luffy/move_flag.sh
RUN chmod +x /home/luffy/move_image.sh

# Ejecuta el script
RUN /home/luffy/move_flag.sh
RUN /home/luffy/move_image.sh

# Eliminar el script de python
RUN rm /home/luffy/random_folders.py
RUN rm /home/luffy/move_flag.sh
RUN rm /home/luffy/move_image.sh

# Cambiar la propiedad de los archivos al usuario luffy
RUN chown -R luffy:luffy /home/luffy

# Cambiar al usuario "luffy" por defecto
USER luffy

EXPOSE 8000 
# Script de inicio
CMD ["bash"]