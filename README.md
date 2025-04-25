# CTF_ONEPICE_SYMMETRIC_CIPHER
<a id="readme-top"></a>

<!--
PROJECT DESCRIPTION
-->
## 📜 Descripción

CTF_ONEPICE_SYMMETRIC_CIPHER un repositorio diseñado para conocer y practicar conceptos básicos de cifrados simétricos como:
 
- XOR básico
- RC4
- Análisis estadístico
- PRNG inseguro
- Chacha20
- Cifrado combinado

Link de referencia:
https://locano-uvg.github.io/ctf_onepice_symmetric_cipher/

## 📦 Requisitos

- Comandos básicos de Linux
- Docker
- Docker Compose
- Python


## 🚀 Instalación y Ejecución
1. Se clono este repositorio e instala los requistos:

```bash
git clone https://github.com/tu_usuario/CTF_INTRO_CIFRADOS.git
cd CTF_INTRO_CIFRADOS
```

2. Instalar dependencias
```bash
pip3 install -r scripts/requirements.txt
```

3. Ejecuta el script de python

```bash
python generate_challenges
```

4. Ejecuta el docker compose

```bash
sudo docker compose up -d
```

5. Valida que las imagenes esten activas

```bash
docker ps  
```

6. Dentro del contenedor se crearon 6 retos, ejecutalos individualmente

- luffy_challenge 🤠
- zoro_challenge 🏴‍☠️
- usopp_challenge 🎯
- nami_challenge 🌊
- sanji_challenge 🔥
- robin_challenge 📜

<!-- CREAR UNA TABLA -->
|**Usuario**|**Reto**|**Nivel**|**Objetivo**|
|-------------|-----------------------|-----------|---------------------------------------------------------------------------------------|
| Luffy 🤠| XOR | 🟢 Facil | Encontrar la flag cifrada en un poneglyph.txt, aplicando XOR con su carné como clave. |
| Zoro 🏴‍☠️ | Rompiendo RC4 | 🟡 Medio  | |
| Usopp 🎯| Stream Cipher Custom  | 🟡 Medio | |
| Nami 🌊 | ChaCha20 Playground   | 🟡 Medio | |

El primer reto a resolver es una aventura con Luffy, se inició sesión utilizando la contraseña onepiece

```bash
su luffy
password: onepiece
```

```bash
docker exec -it {challengeX_ctf} bash
```

7. Al encontrar la imagen se pudo extrar usando un web server then enter to the mapping port

```bash
python3 -m http.server 8080
```
- luffy_challenge 8081
- zoro_challenge  8082
- nami_challenge 8083
- usopp_challenge 8086

