import io
import pandas as pd
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe

from .models import Tarea
from .forms import TareaForm


def listatareas(request):
    search = request.GET.get('search', '')
    if search:
        tareas = Tarea.objects.filter(nombre__icontains=search) | Tarea.objects.filter(
            descripcion__icontains=search)
    else:
        tareas = Tarea.objects.all()
    return render(request, 'tareas/listatareas.html', {'tareas': tareas, 'search': search})


@login_required
def creartarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/creartarea.html', {'form': form})


@login_required
def completartarea(request, tarea_id):
    if request.method != 'POST':
        return render(request, 'tareas/listatareas.html', {
            'tareas': Tarea.objects.all(),
            'error': 'Solo se puede completar una tarea por POST.'
        })
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.completada_por = request.user
    tarea.save()
    return redirect('tareas')


def tareas_db(request):
    qs = Tarea.objects.all().order_by('id')
    df = pd.DataFrame(list(qs.values()))
    total = len(df)

    if df.empty:
        html_table = '<p>No hay tareas.</p>'
    else:
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                try:
                    df[col] = df[col].dt.tz_localize(None)
                except Exception:
                    pass
        html_table = df.to_html(
            index=False, classes='table table-striped', escape=False)

    return render(request, 'tareas/tareas_db.html', {
        'html_table': mark_safe(html_table),
        'total': total,
    })


@login_required
def generarexcel(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.error(request, 'No estás autorizado para descargar el Excel.')
        return redirect('home')

    from mensajes.models import Mensaje
    from encuestas.models import Encuesta
    from posts.models import Post

    df_mensajes = pd.DataFrame(list(Mensaje.objects.all().values()))
    df_tareas = pd.DataFrame(list(Tarea.objects.all().values()))
    df_encuestas = pd.DataFrame(list(Encuesta.objects.all().values()))
    df_posts = pd.DataFrame(list(Post.objects.all().values()))

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
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="datos.xlsx"'
    return response
