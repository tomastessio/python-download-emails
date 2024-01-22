import os
from dotenv import load_dotenv
import email
import imaplib
from pathlib import Path

load_dotenv()

email_address = 'tu_mail_de_prueba'
password = os.getenv("PASSWORD")

# Conectarse al servidor IMAP de Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(email_address, password)

# Seleccionar el buzón (en este caso, la bandeja de entrada)
mail.select("inbox")

# Buscar todos los correos electrónicos en la bandeja de entrada
status, messages = mail.search(None, "ALL")
messages = messages[0].split()

# Iterar sobre los mensajes y descargar archivos adjuntos .xlsx
for mail_id in messages:
    _, msg_data = mail.fetch(mail_id, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])

    print(f'From: {msg["From"]}')
    print(f'Subject: {msg["Subject"]}')
    print(f'Date: {msg["Date"]}')
    
    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get("Content-Disposition") is None:
            continue

        filename = part.get_filename()
        if filename:
            filename_bytes = email.header.decode_header(filename)[0][0]
            filename_str = filename_bytes.decode('utf-8') if isinstance(filename_bytes, bytes) else filename_bytes
            filename = Path(filename_str)
            if filename.suffix.lower() == '.xlsx':
                # Guardar el archivo adjunto .xlsx
                with open(filename, "wb") as f:
                    f.write(part.get_payload(decode=True))
                print(f'Archivo adjunto {filename} descargado.')

    print('-' * 50)

# Cerrar la conexión
mail.logout()



