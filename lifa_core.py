import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Cargamos las variables de entorno
load_dotenv()

# Inicializamos el cliente oficial de Gemini
client = genai.Client()

def procesar_con_gemini(texto_usuario: str):
    """
    Recibe un texto y utiliza la API de Gemini para extraer la intención 
    y los parámetros en formato JSON estrictamente estructurado.
    """
    prompt_sistema = """
    Eres el núcleo de procesamiento de intenciones para LIFA, un asistente personal.
    Analiza la entrada del usuario y clasifícala estrictamente en una de las siguientes intenciones (intent):
    - 'crear_evento' (para calendario)
    - 'revisar_correo' (para correos)
    - 'consultar_mapa' (para direcciones o rutas)
    - 'consultar_clima' (para preguntar por el clima, temperatura o pronóstico)
    - 'desconocido' (si no encaja en ninguna)

    Devuelve ÚNICAMENTE un objeto JSON válido con los campos:
    - "intent": la intención detectada.
    - "parametros": un diccionario con datos extraídos como título, fecha, hora, lugar, ciudad o categoría si aplican.
    """

    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=f"Entrada del usuario: '{texto_usuario}'",
            config=types.GenerateContentConfig(
                system_instruction=prompt_sistema,
                response_mime_type="application/json",
                temperature=0.1
            ),
        )
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}