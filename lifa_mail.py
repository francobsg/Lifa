import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

# Cargamos las credenciales
load_dotenv()
EMAIL_USER = os.getenv("LIFA_EMAIL_USER")
EMAIL_PASS = os.getenv("LIFA_EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("LIFA_IMAP_SERVER")

def leer_correos_importantes():
    """Conecta al correo, lee los mensajes no leídos y busca palabras clave."""
    try:
        # 1. Conexión segura al servidor IMAP
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        
        # Seleccionamos la bandeja de entrada (Inbox)
        mail.select("inbox")
        
        # 2. Buscamos solo correos NO LEÍDOS (UNSEEN)
        status, mensajes = mail.search(None, "UNSEEN")
        id_lista = mensajes[0].split()
        
        correos_filtrados = []
        palabras_clave = ["oferta", "universidad", "trabajo", "prueba", "modificación"]
        
        # 3. Analizamos los últimos 5 correos no leídos para no saturar
        for i in id_lista[-5:]:
            res, msg_data = mail.fetch(i, "(RFC822)")
            for respuesta_parte in msg_data:
                if isinstance(respuesta_parte, tuple):
                    msg = email.message_from_bytes(respuesta_parte[1])
                    
                    # Decodificamos el asunto
                    asunto, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(asunto, bytes):
                        asunto = asunto.decode(encoding if encoding else "utf-8")
                        
                    # Verificamos si alguna palabra clave está en el asunto
                    asunto_min = asunto.lower()
                    if any(palabra in asunto_min for palabra in palabras_clave):
                        correos_filtrados.append(asunto)
                        
        mail.logout()
        return {"status": "success", "alertas": correos_filtrados}

    except Exception as e:
        return {"status": "error", "mensaje": str(e)}

# --- PRUEBA LOCAL DEL MÓDULO ---
if __name__ == "__main__":
    print("=== PROBANDO MÓDULO DE CORREO ===")
    resultados = leer_correos_importantes()
    print(resultados)