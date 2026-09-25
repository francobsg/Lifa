import requests
import os
from dotenv import load_dotenv

# Cargamos las credenciales desde el .env
load_dotenv()
WEATHER_API_KEY = os.getenv("LIFA_WEATHER_API_KEY")

def consultar_clima(ciudad: str):
    """
    Consulta el clima actual de una ciudad usando la API de OpenWeatherMap.
    """
    if not WEATHER_API_KEY:
        return {"status": "error", "mensaje": "Falta la API Key de OpenWeatherMap (LIFA_WEATHER_API_KEY) en el .env"}

    # URL configurada para sistema métrico (Celsius) y español
    url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": ciudad,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        respuesta = requests.get(url, params=parametros).json()

        if respuesta.get("cod") == 200:
            clima_desc = respuesta["weather"][0]["description"]
            temp = round(respuesta["main"]["temp"])
            humedad = respuesta["main"]["humidity"]
            nombre_ciudad = respuesta["name"]

            return {
                "status": "success",
                "ciudad": nombre_ciudad,
                "temperatura": temp,
                "descripcion": clima_desc,
                "humedad": humedad,
                "mensaje": f"El clima actual en {nombre_ciudad} es de {temp}°C con {clima_desc} y {humedad}% de humedad."
            }
        else:
            return {"status": "error", "mensaje": f"Error al buscar el clima: {respuesta.get('message')}"}

    except Exception as e:
        return {"status": "error", "mensaje": str(e)}

# --- PRUEBA LOCAL DEL MÓDULO ---
if __name__ == "__main__":
    print("=== PROBANDO MÓDULO DE CLIMA ===")
    ciudad_test = "Puerto Montt"
    print(f"Consultando el clima para: {ciudad_test}...\n")
    print(consultar_clima(ciudad_test))