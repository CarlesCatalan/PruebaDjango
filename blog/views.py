from django.http import HttpResponse
import pandas as pd
import requests

from PruebaDjango.settings import OPENWEATHER_API_KEY
from .models import Mensaje, Post, Tarea, Encuesta, Profile
import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EncuestaForm, MensajeForm, SaludoForm, TareaForm, RegistroForm, ProfileForm
import base64
import io
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI, necesario para Django


# Create your views here.

# Home


def home(request):
    return render(request, 'blog/home.html')

# Ver clima (API externa)


def clima(request):
    ciudad = 'Palma'
    api_key = OPENWEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            clima_info = {
                'ciudad': ciudad,
                'temperatura': data['main']['temp'],
                'descripcion': data['weather'][0]['description'],
                'icono': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            }
            return render(request, 'blog/clima.html', {'clima': clima_info})
        else:
            error = f"Error al obtener datos del clima: {response.status_code}"
            return render(request, 'blog/clima.html', {'error': error})
    except requests.exceptions.RequestException as e:
        error = f"Error de conexión: {e}"
        return render(request, 'blog/clima.html', {'error': error})


# Encuestas


@login_required
def encuesta(request):
    encuestas = []
    promedio = None
    grafico = None
    if request.user.is_staff or request.user.is_superuser:
        encuestas = Encuesta.objects.order_by('-fecha')
        total_satisfaccion = sum(item.satisfaccion for item in encuestas)
        cantidad = encuestas.count()
        promedio = round(total_satisfaccion / cantidad,
                         2) if cantidad else None

        # Crear gráfico de barras de satisfacción mostrando todos los niveles
        niveles = [1, 2, 3, 4, 5]
        etiquetas = ['Muy insatisfecho', 'Insatisfecho',
                     'Neutral', 'Satisfecho', 'Muy satisfecho']
        if cantidad > 0:
            df = pd.DataFrame(list(encuestas.values('fecha', 'satisfaccion')))
            conteo = df['satisfaccion'].value_counts().reindex(
                niveles, fill_value=0)
            plt.figure(figsize=(7, 4))
            sns.barplot(x=conteo.index, y=conteo.values, palette='viridis')
            plt.title('Satisfacción')
            plt.xlabel('Nivel de satisfacción')
            plt.ylabel('Número de respuestas')
            plt.xticks(ticks=range(len(niveles)),
                       labels=etiquetas, rotation=20)
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            grafico = base64.b64encode(buf.getvalue()).decode('utf-8')
            plt.close()

    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            # Control: solo una encuesta por usuario
            if Encuesta.objects.filter(contacto=request.user).exists():
                return render(request, 'blog/encuesta.html', {
                    'form': form,
                    'encuestas': encuestas,
                    'promedio': promedio,
                    'grafico': grafico,
                    'error': 'Ya has enviado tu opinión.'
                })
            encuesta = form.save(commit=False)
            encuesta.contacto = request.user
            encuesta.save()
            return redirect('encuesta')
    else:
        form = EncuestaForm()
    return render(request, 'blog/encuesta.html', {
        'form': form,
        'encuestas': encuestas,
        'promedio': promedio,
        'grafico': grafico,
    })


# Registros


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'blog/registro.html', {'form': form})


# Mensajes


@login_required
def mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.name = request.user
            mensaje.save()
            return redirect('mensaje')
    else:
        form = MensajeForm()

    mensajes = Mensaje.objects.all().order_by('-fecha')
    return render(request, 'blog/mensaje.html', {
        'form': form,
        'mensajes': mensajes,
    })

# Tareas


def listatareas(request):
    search = request.GET.get('search', '')
    if search:
        tareas = Tarea.objects.filter(nombre__icontains=search) | Tarea.objects.filter(
            descripcion__icontains=search)
    else:
        tareas = Tarea.objects.all()
    return render(request, 'blog/listatareas.html', {'tareas': tareas, 'search': search})


@login_required
def creartarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TareaForm()
    return render(request, 'blog/creartarea.html', {'form': form})


@login_required
def completartarea(request, tarea_id):
    if request.method != 'POST':
        return render(request, 'blog/listatareas.html', {
            'tareas': Tarea.objects.all(),
            'error': 'Solo se puede completar una tarea por POST.'
        })
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.completada_por = request.user
    tarea.save()
    return redirect('tareas')


@login_required
def generarexcel(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')

    # Extraer datos de todos los modelos
    df_mensajes = pd.DataFrame(list(Mensaje.objects.all().values()))
    df_tareas = pd.DataFrame(list(Tarea.objects.all().values()))
    df_encuestas = pd.DataFrame(list(Encuesta.objects.all().values()))
    df_posts = pd.DataFrame(list(Post.objects.all().values()))

    # Eliminar timezone de columnas datetime
    for df in [df_mensajes, df_tareas, df_encuestas, df_posts]:
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = df[col].dt.tz_localize(None)

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_mensajes.to_excel(writer, index=False, sheet_name='Mensajes')
        df_tareas.to_excel(writer, index=False, sheet_name='Tareas')
        df_encuestas.to_excel(writer, index=False, sheet_name='Encuestas')
        df_posts.to_excel(writer, index=False, sheet_name='Posts')
    buffer.seek(0)

    response = HttpResponse(
        buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="datos.xlsx"'
    return response


@login_required
def perfil(request):
    profile = getattr(request.user, 'profile', None)
    return render(request, 'blog/perfil.html', {'profile': profile})


@login_required
def editar_perfil(request):
    # Asegurar que solo el propietario pueda editar su perfil
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/editar_perfil.html', {'form': form})


# Primeras pruebas de vistas

def saludo(request):
    return render(request, 'blog/saludo.html')


def listapost(request):
    posts = Post.objects.all()
    return render(request, 'blog/listaposts.html', {'posts': posts})


def saludoform(request):
    if request.method == 'POST':
        form = SaludoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            return render(request, 'blog/saludo.html', {'nombre': nombre})
    else:
        form = SaludoForm()
    return render(request, 'blog/saludoform.html', {'form': form})
