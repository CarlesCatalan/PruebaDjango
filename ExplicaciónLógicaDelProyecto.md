Voy a prepararte un documento técnico muy completo en formato Markdown, basado en tu código real, con explicaciones por módulos y fragmentos comentados. Primero voy a leer los archivos clave del proyecto (settings, modelos, vistas, rutas, forms, templates y utilidades) para que quede exacto y útil para exponerlo.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango)

Read memory

Ahora voy a mapear todos los archivos relevantes de la app para cubrir arquitectura, flujo de datos y seguridad de extremo a extremo en el documento.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/PruebaDjango)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/static/blog)

Siguiente paso: leer la configuración global y el enrutado para explicar cómo arranca Django y cómo se conectan las URLs con tus vistas.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/PruebaDjango/settings.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/manage.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/apps.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/PruebaDjango/urls.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/urls.py)

Ya tengo clara la configuración base: carga de .env, media files, middleware propio, context processor de perfil y rutas principales. Ahora voy con modelos, formularios, vistas y señales para explicar la lógica de negocio y el flujo completo de cada pantalla.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/models.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/context_processors.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/forms.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/views.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/signals.py)

Voy a revisar ahora middleware, admin y plantillas para documentar también comportamiento visual, permisos y puntos donde puede fallar (como perfil/foto por defecto).

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/middleware.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/admin.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/tests.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/__init__.py)

Ya está la parte backend principal; me falta leer las plantillas para explicarte el flujo de UI y cómo encaja cada vista con los formularios. Luego te redacto el `.md` final completo.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/base.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/creartarea.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/home.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/listatareas.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/mensaje.html)

Perfecto, ya confirmé la parte de tareas/mensajes y el fallback de imagen por defecto. Voy con encuestas, perfil, login/registro y clima para cerrar la guía funcional completa.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/perfil.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/editar_perfil.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/login.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/encuesta.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/registro.html)

Última lectura de contexto: páginas auxiliares, estilos y dependencias para dejarte una explicación muy “de presentación” y no solo técnica de backend.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/clima.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/listaposts.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/saludo.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/templates/blog/saludoform.html)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/blog/static/blog/styles.css)

Voy a cerrar con la parte operativa (dependencias, .gitignore, ASGI/WSGI y entorno) para que el documento también te sirva al explicarlo en instalación y despliegue.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/.env.example)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/PruebaDjango/asgi.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/PruebaDjango/wsgi.py)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/.gitignore)

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/requirements.txt)

Solo me queda revisar pandas_info.md para incorporar en el documento una explicación coherente de por qué usas pandas y cómo se aplica en encuestas/exportación.

Read [](file:///c%3A/Users/usuario/PROYECTOS/PruebaDjango/pandas_info.md)

Sí. Te dejo un **Markdown definitivo**, muy extenso, basado en tu código real, para que lo puedas usar como guía de estudio y para explicar el proyecto.

---

# Guía técnica completa de PruebaDjango (explicación profunda del código)

## 0) Objetivo del proyecto

**PruebaDjango** es un proyecto de práctica con Django que combina:

- autenticación de usuarios
- perfil con foto y bio
- CRUD parcial de tareas
- libro de mensajes
- encuestas con estadísticas
- exportación a Excel
- consumo de API externa (OpenWeather)
- uso de pandas + matplotlib dentro de vistas web

No es solo “un blog”: es un laboratorio de funcionalidades típicas de una app web real.

---

## 1) Mapa real del código (archivos clave)

- Entrada del proyecto: manage.py
- Configuración global: settings.py
- URLs raíz: urls.py
- App principal: apps.py
- Rutas de la app: urls.py
- Modelos: models.py
- Formularios: forms.py
- Vistas: views.py
- Señales de perfil: signals.py
- Context processor de perfil: context_processors.py
- Middleware anti-cache HTML: middleware.py
- Layout base HTML: base.html
- Estilos: styles.css
- Variables de entorno ejemplo: .env.example
- Dependencias: requirements.txt
- Exclusiones Git: .gitignore

---

## 2) Flujo de arranque de Django (qué pasa cuando ejecutas runserver)

### 2.1 Punto de entrada CLI

```python
# manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PruebaDjango.settings')
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
```

### Explicación
1. Define qué archivo de settings usar.
2. Lanza el comando que pidas (`runserver`, `migrate`, etc.).
3. Django carga apps, middleware, urls, templates, BD.

---

## 3) Configuración global (settings.py) explicada a fondo

### 3.1 Carga de entorno y valores sensibles

```python
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-...')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
```

### Qué significa
- `load_dotenv()` permite leer variables desde .env.
- Si falta .env, usas valores por defecto (útil en desarrollo, peligroso en producción si no se controla).
- API key del clima se inyecta por entorno.

---

### 3.2 Apps instaladas y middleware

```python
INSTALLED_APPS = [
    ...
    'blog',
]

MIDDLEWARE = [
    ...
    'blog.middleware.DisableHtmlCacheMiddleware',
]
```

### Qué aporta
- blog concentra toda la lógica de negocio.
- Middleware propio desactiva cache HTML (evita páginas antiguas al usar atrás del navegador tras logout).

---

### 3.3 Templates + context processor global

```python
'context_processors': [
    ...
    'blog.context_processors.user_profile',
],
```

### Resultado práctico
Ese context processor mete `profile` en **todas** las plantillas.  
Gracias a eso, en base.html puedes pintar foto y datos del usuario sin pasarlo manualmente desde cada vista.

---

### 3.4 Estáticos y media

```python
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

- `STATIC_URL`: CSS/JS/imagenes de app.
- `MEDIA_*`: archivos subidos por usuarios (foto de perfil).

En urls.py se sirven media en desarrollo con `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` cuando `DEBUG=True`.

---

## 4) Modelo de datos (models.py) y su diseño

## 4.1 `Post`

```python
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
```

- Modelo básico para pruebas de listado.
- Sirve para aprender render de colecciones en template.

---

## 4.2 `Tarea`

```python
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    completada_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
```

- Tiene estado (`completada`) y autor de completado (`completada_por`).
- Muy útil para explicar relación con `User`.

---

## 4.3 `Mensaje`

```python
class Mensaje(models.Model):
    name = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
```

- Libro de visitas simple.
- Guarda autor + contenido + timestamp automático.

---

## 4.4 `Encuesta`

```python
class Encuesta(models.Model):
    contacto = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=200)
    satisfaccion = models.IntegerField(choices=[(1,'Muy insatisfecho'), ... , (5,'Muy satisfecho')])
    fecha = models.DateTimeField(auto_now_add=True)
```

- Guarda feedback y valoración numérica.
- El campo `choices` impone valores válidos.

---

## 4.5 `Profile`

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    @property
    def foto_url(self):
        if self.foto:
            return self.foto.url
        return None
```

- Extiende `User` sin tocar tabla auth de Django.
- `OneToOne`: un perfil por usuario.
- `ImageField` guarda ruta, archivo real en profiles.

---

## 5) Formularios (forms.py): validación y mapeo modelo-template

## 5.1 ModelForms
- `TareaForm` → `Tarea`
- `MensajeForm` → `Mensaje`
- `EncuestaForm` → `Encuesta`
- `ProfileForm` → `Profile`

Esto te evita validar campo por campo manualmente.

---

## 5.2 Registro personalizado con validación extra

```python
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email
```

### Por qué está bien
- Reutiliza seguridad de `UserCreationForm` (password1/password2).
- Añade regla de negocio: email único.

---

## 6) Rutas (urls.py): cómo entra cada petición

En urls.py defines endpoints como:

- `/blog/home/` → `home`
- `/blog/tareas/` → `listatareas`
- `/blog/tareas/crear/` → `creartarea`
- `/blog/tareas/completar/<id>/` → `completartarea`
- `/blog/mensajes/` → `mensaje`
- `/blog/encuesta/` → `encuesta`
- `/blog/perfil/` y `/blog/perfil/editar/`
- `/blog/clima/`
- `/blog/generarexcel/`

Y usas `LoginView` / `LogoutView` de Django auth para login/logout.

---

## 7) Vistas (views.py) explicadas en profundidad

## 7.1 Home y vistas básicas

```python
def home(request):
    return render(request, 'blog/home.html')
```

- Vista mínima de navegación.
- Menú central hacia todo el proyecto.

---

## 7.2 Clima (API externa con `requests`)

```python
url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
response = requests.get(url, timeout=5)
```

### Comportamiento
- Llama a OpenWeather para Palma.
- Si `200`, construye diccionario `clima_info`.
- Si error HTTP o excepción de red, renderiza mensaje de error.

### Qué puedes explicar en entrevista
- Integración de servicio externo.
- Manejo de timeout y excepciones.
- No romper UX aunque API falle.

---

## 7.3 Encuesta: formulario + analítica + control de duplicado

```python
if Encuesta.objects.filter(contacto=request.user).exists():
    return render(..., {'error': 'Ya has enviado tu opinión.'})
```

### Lógica completa
1. Solo usuarios autenticados (`@login_required`).
2. Staff/superuser ven histórico + gráfico + promedio.
3. Usuario normal puede enviar una sola encuesta.
4. Tras POST válido, redirige para evitar reenvío al recargar (patrón PRG).

---

### Generación de gráfico con pandas + matplotlib

```python
df = pd.DataFrame(list(encuestas.values('fecha', 'satisfaccion')))
conteo = df['satisfaccion'].value_counts().reindex([1,2,3,4,5], fill_value=0)
conteo.plot(kind='bar', color='skyblue')
...
grafico = base64.b64encode(buf.getvalue()).decode('utf-8')
```

### Qué estás haciendo aquí
- ORM → DataFrame.
- Conteo por niveles de satisfacción 1..5.
- Gráfico embebido en HTML como `data:image/png;base64,...` (sin guardar archivo físico).

---

## 7.4 Mensajes (libro de visitas)

```python
if request.method == 'POST':
    form = MensajeForm(request.POST)
    if form.is_valid():
        mensaje = form.save(commit=False)
        mensaje.name = request.user
        mensaje.save()
        return redirect('mensaje')
```

- Solo usuarios logueados pueden publicar.
- Lista ordenada descendente por fecha.
- Usa ModelForm y patrón PRG.

---

## 7.5 Tareas: búsqueda + creación + completado seguro por POST

### Búsqueda por querystring

```python
search = request.GET.get('search', '')
if search:
    tareas = Tarea.objects.filter(nombre__icontains=search) | Tarea.objects.filter(descripcion__icontains=search)
else:
    tareas = Tarea.objects.all()
```

- Filtro por nombre o descripción.
- `icontains` hace búsqueda case-insensitive.

### Completado con protección de método

```python
if request.method != 'POST':
    return render(..., {'error': 'Solo se puede completar una tarea por POST.'})
```

- Evita cambiar estado por GET.
- Correcto para integridad y seguridad CSRF (junto con token en template).

---

## 7.6 Exportación Excel para admin

```python
if not request.user.is_staff and not request.user.is_superuser:
    return redirect('home')
```

```python
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    df_mensajes.to_excel(writer, index=False, sheet_name='Mensajes')
    df_tareas.to_excel(writer, index=False, sheet_name='Tareas')
    df_encuestas.to_excel(writer, index=False, sheet_name='Encuestas')
    df_posts.to_excel(writer, index=False, sheet_name='Posts')
```

### Qué hace bien
- Restringe acceso por rol.
- Exporta múltiples hojas en un solo archivo.
- Normaliza columnas datetime para evitar problemas de timezone en Excel.

---

## 7.7 Perfil y edición de perfil

```python
profile, created = Profile.objects.get_or_create(user=request.user)
form = ProfileForm(request.POST, request.FILES, instance=profile)
```

- Si perfil no existe, lo crea.
- Soporta subida de imagen (`request.FILES` + `multipart/form-data` en template).
- Garantiza edición solo del perfil del usuario logueado.

---

## 8) Señales y perfil automático

En signals.py:

```python
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### Qué resuelve
Al crear un usuario, se crea su `Profile` automáticamente.

En apps.py, el método `ready()` importa signals para registrar receptores al arrancar.

---

## 9) Context processor + plantilla base: disponibilidad global del perfil

En context_processors.py:

```python
def user_profile(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
    return {'profile': profile}
```

En base.html:

```django
{% if profile.foto %}
    <img src="{{ profile.foto.url }}" alt="Foto" width="40" class="profile-pic">
{% else %}
    <img src="{% static 'blog/usuario-default.jpg' %}" alt="Foto" width="40" class="profile-pic">
{% endif %}
```

### Resultado
- Cabecera coherente en toda la app.
- Si no hay foto subida, usa imagen predeterminada (`usuario-default.jpg`).

---

## 10) Frontend (templates + CSS) y experiencia de usuario

## 10.1 Estructura de plantillas
- Base común con header y bloque `content`.
- Cada vista hereda base con `{% extends 'blog/base.html' %}`.
- Navegación interna clara (`top-links`, menú home).

## 10.2 Estilos
En styles.css:
- variables CSS (`--primary`, `--border`, etc.)
- tarjetas (`.card`)
- badges de estado (`.badge-ok`, `.badge-warn`)
- diseño limpio y consistente

---

## 11) Seguridad implementada (y su alcance real)

### Lo que sí tienes
- `CsrfViewMiddleware` activo.
- Tokens CSRF en formularios.
- `@login_required` en acciones privadas.
- Acción sensible de completar tarea solo por POST.
- Restricción de exportación Excel a admin/staff.
- .env ignorado por Git y .env.example compartido.

### Lo que podrías reforzar
- Validators de contraseña están comentados.
- En producción deberías activar checklist de deploy y endurecer settings (`DEBUG=False`, hosts estrictos, etc.).

---

## 12) Variables de entorno y colaboración entre equipos

En .env.example:

```env
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
OPENWEATHER_API_KEY=
```

### Buena práctica aplicada
- El repositorio comparte la estructura de variables.
- Cada desarrollador crea su .env local.
- No se filtran secretos en Git (por .gitignore).

---

## 13) Dependencias y rol de cada una

En requirements.txt:
- `Django`: framework web.
- `python-dotenv`: carga .env.
- `requests`: cliente HTTP para OpenWeather.
- `pandas`: análisis y manipulación tabular.
- `matplotlib`: generación de gráficos.
- `xlsxwriter`: exportación Excel.
- `Pillow`: soporte de imágenes para `ImageField`.

---

## 14) Flujo completo de casos de uso (para explicarlo “de punta a punta”)

## Caso A: Registro de usuario
1. Usuario abre `/blog/registro/`.
2. `RegistroForm` valida credenciales y email único.
3. Se crea `User`.
4. Señal `post_save` crea `Profile`.
5. Usuario ya puede loguearse y editar perfil.

## Caso B: Subida de foto de perfil
1. Usuario entra en `/blog/perfil/editar/`.
2. `ProfileForm` recibe `request.POST + request.FILES`.
3. Guarda imagen en profiles.
4. base.html muestra foto real o fallback default.

## Caso C: Encuesta con analítica
1. Usuario envía opinión y satisfacción.
2. Se bloquea duplicado por usuario.
3. Admin entra a encuesta y ve:
   - listado histórico
   - promedio
   - gráfico barras base64 generado dinámicamente

## Caso D: Exportar datos
1. Admin pulsa “Generar Excel”.
2. Vista crea DataFrames desde ORM.
3. Escribe cada modelo en una hoja.
4. Responde con descarga `datos.xlsx`.

---

## 15) Cosas importantes para defender el código en una explicación oral

- **Arquitectura MVT** real: modelos, formularios, vistas y templates desacoplados.
- **Seguridad mínima sólida**: auth + CSRF + POST en acciones de estado.
- **Perfil de usuario extendido sin tocar auth interna** (OneToOne + signals).
- **Integración de data tooling dentro de web app** (pandas/matplotlib).
- **Gestión de secretos correcta** con .env.example + .env ignorado.
- **Experiencia de usuario consistente** por base.html + context processor.

---

## 16) Limitaciones actuales (honestas) y mejoras naturales

### Limitaciones observables
- No hay tests implementados en tests.py.
- `STATIC_URL = 'static/'` funciona, pero en muchos setups se usa `'/static/'`.
- Password validators desactivados en settings para simplificar.

### Mejoras recomendables
- Añadir tests de vistas clave (`encuesta`, `completartarea`, `generarexcel`).
- Mejorar permisos por objeto (si en futuro cada tarea tuviera propietario).
- Añadir paginación en listados de mensajes/encuestas.
- Añadir manejo explícito de API key ausente en vista de clima.

---

## 17) Resumen final en una frase

Tu proyecto es una **app Django educativa muy completa**, que demuestra autenticación, perfiles con media, formularios robustos, seguridad básica correcta, consumo de APIs y analítica/exportación de datos en un flujo web real.

---

Si quieres, en el siguiente paso te preparo una **versión 2 de este MD en formato “guion para exponer en clase/entrevista”** (más narrativa, con orden de discurso y preguntas típicas con respuesta).