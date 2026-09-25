from lifa_database import conectar_db

def agregar_evento(titulo: str, fecha: str, hora: str, notas: str = ""):
    """Guarda un nuevo evento en la base de datos."""
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        # Insertamos los datos de forma segura
        cursor.execute('''
            INSERT INTO eventos_calendario (titulo, fecha, hora, notas)
            VALUES (?, ?, ?, ?)
        ''', (titulo, fecha, hora, notas))
        
        conexion.commit()
        conexion.close()
        return {"status": "success", "mensaje": f"Evento '{titulo}' guardado correctamente."}
    except Exception as e:
        return {"status": "error", "mensaje": str(e)}

def listar_eventos_pendientes():
    """Devuelve todos los eventos que aún están pendientes."""
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT id, titulo, fecha, hora, notas FROM eventos_calendario WHERE estado = 'pendiente'")
    eventos = cursor.fetchall()
    conexion.close()
    
    # Convertimos los resultados en una lista de diccionarios para que sea más fácil de leer
    lista_eventos = []
    for evt in eventos:
        lista_eventos.append({
            "id": evt[0],
            "titulo": evt[1],
            "fecha": evt[2],
            "hora": evt[3],
            "notas": evt[4]
        })
        
    return lista_eventos

# --- PRUEBA LOCAL DEL MÓDULO ---
if __name__ == "__main__":
    print("=== PROBANDO MÓDULO DE CALENDARIO ===")
    
    # 1. Simulamos guardar el evento que nos dio Gemini antes
    resultado = agregar_evento("Examen de cálculo", "2026-08-28", "10:00", "Llevar calculadora")
    print(resultado)
    
    # 2. Leemos la base de datos para confirmar que se guardó
    print("\n--- Eventos Guardados en la Base de Datos ---")
    eventos = listar_eventos_pendientes()
    for e in eventos:
        print(f"- {e['titulo']} ({e['fecha']} a las {e['hora']})")