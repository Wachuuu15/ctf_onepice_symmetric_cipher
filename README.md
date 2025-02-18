
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

## 📦 Requisitos

- Comandos básicos de Linux
- Docker
- Docker Compose
- Python


## 🚀 Instalación y Ejecución
1. Clona este repositorio e instala los requistos:

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

6. Dentro del contenedor se crearán 6 retos, ejecutalos individualmente

- luffy_challenge
- zoro_challenge
- nami_challenge
- sanji_challenge
- robin_challenge
- usopp_challenge

```bash
docker exec -it {challengeX_ctf} bash
```

7. Al encontrar la imagen puedes extrarla usando un web server then enter to the mapping port

```bash
python3 -m http.server 8080
```
- luffy_challenge 8081
- zoro_challenge  8082
- nami_challenge 8083
- sanji_challenge 8084
- robin_challenge 8085
- usopp_challenge 8086



## 📝 Tips para Resolver los Desafíos
1.	Explora los archivos del sistema
```bash
- Muchas pistas pueden estar escondidas en lugares comunes como:
  - Mensajes del sistema (A veces los administradores dejan mensajes útiles o pistas ahí.)
    - Revisa el archivo /etc/motd (Mensaje del Día) 
  - Logs de autenticación
    - Examina /var/log/auth.log para identificar intentos de acceso fallidos o información sospechosa.
  - Archivos de configuración ocultos
    - Busca en directorios como /etc o carpetas específicas de los usuarios
```

2. Revisa los usuarios y sus archivos
	Identifica los usuarios en el sistema con:
  ```bash
cat /etc/passwd
```
3. Explora los directorios personales en /home/. Revisa archivos ocultos con:
  ```bash
ls -la /home/<usuario>
```
4. Busca archivos que parezcan interesantes, como
  ```bash
 .flag.txt, .hidden, .instrucciones,o incluso archivos con permisos inusuales.
```


## 👥 Contribuciones
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:
1. Realiza un fork del repositorio.
2.	Crea una nueva rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
3.	Haz commit de tus cambios (git commit -m 'Añadir nueva funcionalidad').
4.	Haz push a la rama (git push origin feature/nueva-funcionalidad).
5.	Abre un Pull Request.

### Developer's

<a href="https://github.com/locano">
  <img width='75' src="https://avatars.githubusercontent.com/u/16949087?v=4" alt="Ludwing Cano" />
</a>

* [![Linkedin][Linkedin]][Linkedin-lud]
* [![GitHub][GitHub]][GitHub-lud]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>

## 📞 Contacto
Si tienes preguntas o comentarios, puedes contactarnos a traves de nuestras redes sociales:

* [![Instagram][Instagram]][Instagram-url]
* [![Website][Website]][Website-url]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[Redux]: https://img.shields.io/badge/Redux-764ABC?style=flat&logo=redux&logoColor=white
[Redux-url]: https://redux.js.org/
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[MongoDB]: https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.npmjs.com/package/mongodb
[Node.js]: https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white
[Node-url]: https://nodejs.org/en/
[Reveal-js]: https://img.shields.io/badge/Reveal.js-339933?style=flat&logo=reveal.js&logoColor=white
[Reveal-url]: https://revealjs.com/
[Python]: https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Instagram]: https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white
[Instagram-url]: https://www.instagram.com/ludwing238/
[Instagram]: https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white
[Instagram-url]: https://www.instagram.com/ludwing238/
[Website]: https://img.shields.io/website?url=https://lc2tech.com/
[Website-url]: https://lc2tech.com/
[AntDesign]: https://img.shields.io/badge/-Ant%20Design-333333?style=flat&logo=ant-design&logoColor=0170FE
[AntDesign-url]: https://ant.design/
[Chartjs]: https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white
[Chartjs-url]: https://github.com/reactchartjs/react-chartjs-2
[Linkedin-lud]: https://www.linkedin.com/in/ludwing-cano238
[Linkedin]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Github-lud]: https://github.com/locano
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
