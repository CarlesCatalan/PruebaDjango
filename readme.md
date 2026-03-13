# PruebaDjango - Django Practice Project

Un proyecto práctico de Django 5.2 para aprender gestión de usuarios, tareas, encuestas, análisis de datos con pandas y consumo de APIs externas.

## Características

-  **Autenticación & Perfiles**: Login, registro y perfiles de usuario con foto
-  **Gestión de Tareas**: Crear, listar, completar y buscar tareas
-  **Sistema de Mensajes**: Escribir y leer mensajes/libro de visitas
-  **Encuestas**: Crear encuestas, calcular satisfacción, gráficos con pandas
-  **Análisis de Datos**: Exportar datos a Excel, gráficos interactivos
-  **APIs Externas**: Consumir OpenWeather para mostrar clima
-  **Seguridad**: CSRF protection, validación de propiedades, POST-only en acciones

## Instalación rápida

### Prerequisites
- Python 3.11+
- pip

### Setup

1. **Clona o descarga el proyecto**
```bash
cd PruebaDjango
```

2. **Crea un entorno virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instala dependencias**
```bash
pip install -r requirements.txt
```

4. **Configura variables de entorno**
```bash
cp .env.example .env
# Edita .env y añade tu API key de OpenWeather (opcional)
```

5. **Aplica migraciones**
```bash
python manage.py migrate
```

6. **Crea un superusuario**
```bash
python manage.py createsuperuser
```

7. **Ejecuta el servidor**
```bash
python manage.py runserver
```

8. **Accede al proyecto**
- Home: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## Páginas disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Inicio (menú principal) |
| `/posts/` | Lista de posts |
| `/tareas/` | Lista de tareas con búsqueda |
| `/tareas/crear/` | Crear nueva tarea |
| `/mensajes/` | Libro de visitas |
| `/encuesta/` | Encuestas y estadísticas |
| `/clima/` | Clima actual (API externa) |
| `/generarexcel/` | Descargar datos en Excel (admin) |
| `/perfil/` | Perfil del usuario |
| `/perfil/editar/` | Editar perfil y foto |
| `/login/` | Iniciar sesión |
| `/registro/` | Crear cuenta |
| `/admin/` | Panel de administración |

## Tecnologías

- **Backend**: Django 5.2.12
- **Base de datos**: SQLite (desarrollo)
- **Análisis**: pandas, matplotlib, seborn
- **Exportación**: xlsxwriter
- **API**: requests
- **Imágenes**: Pillow

## Estructura del proyecto

```
PruebaDjango/
├── home/                         # App: páginas de inicio y ejemplos
├── tareas/                       # App: gestión de tareas (modelos, vistas, templates)
├── mensajes/                     # App: libro de visitas / mensajes
├── encuestas/                    # App: encuestas y estadísticas
├── usuarios/                     # App: usuarios, perfiles y middleware
├── posts/                        # App: posts y comentarios
├── clima/                        # App: consumo OpenWeather
├── blog/                         # Carpeta histórica con recursos estáticos/plantilla base
├── PruebaDjango/                 # Configuración del proyecto
│   ├── settings.py               # Settings
│   ├── urls.py                   # URLs raíz
│   └── wsgi.py / asgi.py         # ASGI/WSGI
├── manage.py                     # CLI de Django
├── requirements.txt              # Dependencias
├── .env.example                  # Variables de entorno (plantilla)
├── .gitignore                    # Gitignore
└── readme.md                     # Este archivo
```

## Ejercicios prácticos incluidos

- Convertir acciones a POST seguro (CSRF)
- Crear perfil de usuario (OneToOne con foto)
- Usar pandas para estadísticas
- Exportar a Excel con múltiples hojas
- Consumir API externa (OpenWeather)
- Búsqueda en tareas

## Manuales

- **Django docs**: https://docs.djangoproject.com/en/5.2/
- **pandas docs**: https://pandas.pydata.org/docs/
- **OpenWeather API**: https://openweathermap.org/api

## Contribuir

Este es un proyecto de prueba para estudiar el framework de Django. Puede contener errores o prácticas mejorables ya que está orientado al aprendizaje. Al ser un proyecto de práctica, no se necesita ninguna contribución.

## Licencia

Libre para uso educativo.

---

**Última actualización**: Marzo 2026