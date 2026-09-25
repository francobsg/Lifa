# LIFA - AI Digital Assistant

<p align="center">
<b>Life Intelligence Framework Assistant</b>
</p>

LIFA es un asistente digital basado en inteligencia artificial diseñado para interpretar solicitudes del usuario y ejecutar acciones mediante módulos especializados.

El proyecto explora la integración entre modelos de lenguaje, automatización y herramientas digitales mediante una arquitectura modular y extensible.

Actualmente se encuentra en desarrollo como proyecto personal enfocado en inteligencia artificial aplicada y creación de soluciones digitales.

---

## ✨ Características principales

- Procesamiento de lenguaje natural mediante modelos de IA.
- Interpretación de intenciones del usuario.
- Arquitectura modular para nuevas funcionalidades.
- Integración con APIs externas.
- Gestión de información mediante base de datos local.
- Módulos independientes para distintas capacidades.

---

## 🧠 Arquitectura

```
Usuario
   |
   v
Interfaz
   |
   v
LIFA Core
   |
   +----------------+
   |                |
   v                v
Módulos         Servicios externos

 - Calendario
 - Correo
 - Clima
 - Web
 - Matemática
```

---

## 🛠️ Tecnologías utilizadas

### Backend
- Python
- FastAPI
- SQLite
- APIs REST

### Inteligencia Artificial
- Gemini API
- Procesamiento de lenguaje natural
- Clasificación de intenciones

### Integraciones
- Servicios externos mediante APIs
- Automatización de tareas

---

## 📂 Estructura

```
ProyectoLifa/

├── lifa_server.py
├── lifa_core.py
├── lifa_database.py
├── lifa_calendar.py
├── lifa_mail.py
├── lifa_clima.py
├── lifa_web.py
├── lifa_math.py
├── lifa_interfaz.py
│
├── .env.example
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Instalación

```bash
git clone https://github.com/TU_USUARIO/ProyectoLifa.git
cd ProyectoLifa

python -m venv .venv
```

Activar entorno virtual:

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear `.env` basado en `.env.example` y completar las credenciales necesarias.

---

## ▶️ Ejecución

```bash
python lifa_server.py
```

---

## 🔐 Seguridad

El proyecto utiliza variables de entorno para información sensible.

No se incluyen:
- API Keys
- Tokens
- Credenciales personales
- Datos privados

Cada usuario debe configurar sus propias credenciales.

---

## 👨‍💻 Autor

Franco B.  
Estudiante de Ingeniería en Informática.

---

## 📜 Licencia

Este proyecto utiliza GNU General Public License v3.0.

Consulta el archivo `LICENSE` para más información.
