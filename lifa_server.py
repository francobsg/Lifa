from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from lifa_clima import consultar_clima
from lifa_web import consultar_wikipedia
from lifa_math import resolver_matematica

# Importamos el núcleo de IA y nuestras utilidades modulares
from lifa_core import procesar_con_gemini
from lifa_calendar import agregar_evento
from lifa_mail import leer_correos_importantes # <--- NUEVA UTILIDAD
from lifa_interfaz import obtener_html_interfaz

# Cargamos variables de entorno y seguridad
load_dotenv()
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
LIFA_TOKEN = os.environ.get("LIFA_CLIENT_TOKEN")

def verificar_token(api_key_header: str = Security(api_key_header)):
    if api_key_header != LIFA_TOKEN:
        raise HTTPException(status_code=403, detail="Acceso denegado: Token inválido.")
    return api_key_header

app = FastAPI(
    title="LIFA Core Server",
    description="Servidor central de LIFA conectado al núcleo de Gemini y utilidades.",
    version="1.5"
)

class PeticionUsuario(BaseModel):
    texto: str

@app.post("/procesar", dependencies=[Depends(verificar_token)])
def procesar_comando(peticion: PeticionUsuario):
    texto_recibido = peticion.texto
    
    # 1. Pasamos el texto a Gemini para estructurarlo
    resultado_ia = procesar_con_gemini(texto_recibido)
    
    # Si Gemini falla, devolvemos el error
    if "error" in resultado_ia:
        return {"status": "error", "mensaje": resultado_ia["error"]}
    
    # 2. ENRUTADOR DE UTILIDADES (El comportamiento Plug & Play)
    intent = resultado_ia.get("intent")
    parametros = resultado_ia.get("parametros", {})
    respuesta_utilidad = {}
    
    # Verificamos qué módulo usar según el intent
    if intent == "crear_evento":
        titulo = parametros.get("titulo", "Sin título")
        fecha = parametros.get("fecha", "Sin fecha")
        hora = parametros.get("hora", "Sin hora")
        notas = parametros.get("notas", "")
        respuesta_utilidad = agregar_evento(titulo, fecha, hora, notas)
        
    elif intent == "revisar_correo":
        respuesta_utilidad = leer_correos_importantes()
        
    elif intent == "consultar_clima":
        ciudad = parametros.get("ciudad") or parametros.get("lugar", "Santiago")
        respuesta_utilidad = consultar_clima(ciudad)
        
    elif intent == "consulta_web":
        busqueda = parametros.get("termino_busqueda", "")
        respuesta_utilidad = consultar_wikipedia(busqueda)
        
    elif intent == "resolver_matematica":
        expresion = parametros.get("expresion", "")
        respuesta_utilidad = resolver_matematica(expresion)
        
    elif intent == "desconocido":
        respuesta_utilidad = {"status": "warning", "mensaje": "No estoy seguro de qué acción tomar con esto."}
    else:
        respuesta_utilidad = {"status": "info", "mensaje": f"El módulo para la acción '{intent}' aún no ha sido integrado."}
        
    # 3. Devolvemos el reporte completo
    return {
        "status": "success",
        "texto_original": texto_recibido,
        "analisis_ia": resultado_ia,
        "accion_ejecutada": respuesta_utilidad
    }
# --- INTERFAZ WEB LIGERA ---
@app.get("/app", response_class=HTMLResponse)
def cargar_interfaz_web():
    # Llama a la función del archivo lifa_interfaz.py
    return obtener_html_interfaz()