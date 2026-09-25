import wikipedia

# Configuramos Wikipedia en español
wikipedia.set_lang("es")

def consultar_wikipedia(busqueda: str):
    """Busca un término en Wikipedia y devuelve un resumen corto."""
    try:
        # Extraemos un resumen de máximo 2 oraciones para no saturar la interfaz
        resumen = wikipedia.summary(busqueda, sentences=2)
        return {
            "status": "success",
            "busqueda": busqueda,
            "mensaje": resumen
        }
    except wikipedia.exceptions.DisambiguationError as e:
        # Si hay muchas opciones (ej. "Mercurio" -> planeta o elemento)
        opciones = ", ".join(e.options[:3])
        return {"status": "warning", "mensaje": f"El término es muy ambiguo. ¿Te refieres a: {opciones}?"}
    except wikipedia.exceptions.PageError:
        return {"status": "error", "mensaje": f"No encontré información sobre '{busqueda}' en la web."}
    except Exception as e:
        return {"status": "error", "mensaje": f"Error al consultar la web: {str(e)}"}

# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    print("=== PROBANDO MÓDULO WEB ===")
    resultado = consultar_wikipedia("Agujero negro")
    print(resultado["mensaje"])