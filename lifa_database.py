import sqlite3
import os

# Nombre del archivo físico de la base de datos
DB_NAME = "lifa_data.db"

def conectar_db():
    """Crea y devuelve la conexión a la base de datos SQLite."""
    # check_same_thread=False permite que FastAPI consulte la DB sin bloquearse
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def inicializar_tablas():
    """Crea las tablas base si no existen. Aquí escalarás el sistema en el futuro."""
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Tabla 1: Calendario (Punto 3.1)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos_calendario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT,
            notas TEXT,
            estado TEXT DEFAULT 'pendiente'
        )
    ''')

    # Tabla 2: Logs del Sistema (Registro general de actividad)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs_sistema (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
            modulo TEXT NOT NULL,
            mensaje TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()
    print("Base de datos creada y tablas inicializadas correctamente.")

# Prueba de ejecución directa para crear el archivo
if __name__ == "__main__":
    print("=== INICIALIZANDO BASE DE DATOS DE LIFA ===")
    inicializar_tablas()