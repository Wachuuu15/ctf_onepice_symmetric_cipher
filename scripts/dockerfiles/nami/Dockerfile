# Usamos una imagen base de Ubuntu
FROM ubuntu:22.04

# Evitar interactividad en la instalación de paquetes
ARG DEBIAN_FRONTEND=noninteractive

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

# Crear un usuario "nami" y darle una contraseña
RUN useradd -ms /bin/bash nami && echo "nami:onepiece" | chpasswd && adduser nami sudo

# Deshabilitamos el acceso directo como root para que los alumnos no inicien con permisos de administrador
RUN passwd -l root

# Establecer el directorio de trabajo
WORKDIR /home/nami

# Copiar los archivos del reto dentro del contenedor

COPY ./flag.txt /home/nami/flag.txt
COPY ./poneglyph.jpeg /home/nami/poneglyph.jpeg

# Cambiar la propiedad de los archivos al usuario nami
RUN chown -R nami:nami /home/nami

# Cambiar al usuario "nami" por defecto
USER nami

EXPOSE 8000 
# Script de inicio
CMD ["bash"]