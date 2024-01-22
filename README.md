# Script para Descargar Archivos Adjuntos de Correos Electrónicos

Este script de Python utiliza el protocolo IMAP para conectarse a tu cuenta de Gmail, leer correos electrónicos y descargar archivos adjuntos con la extensión '.xlsx'. También evita la descarga de archivos duplicados.

## Requisitos

- Python 3.x
- Bibliotecas Python: `imaplib`, `email`, `base64`, `pathlib`

## Configuración

1. Asegúrate de tener una cuenta de Gmail activa.
2. Habilita la autenticación de dos factores en tu cuenta de Gmail y genera una contraseña de aplicación [aquí](https://myaccount.google.com/apppasswords).
3. Crea un archivo `.env` en el mismo directorio que el script y agrega las siguientes líneas:

PASSWORD=tu_contraseña_de_aplicación_generada

4. Instala las dependencias utilizando el siguiente comando `pip install python-dotenv`

## Uso

Ejecuta el script `python main.py`

## Notas
Mantener tu contraseña de aplicación en un lugar seguro y no la compartas públicamente.


