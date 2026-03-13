from .forms import EncuestaForm
from .models import Encuesta
import base64
import io

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

matplotlib.use('Agg')


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
            if Encuesta.objects.filter(contacto=request.user).exists():
                messages.warning(
                    request,
                    'Ya has enviado tu opinión. Solo se permite una encuesta por usuario.'
                )
                return redirect('encuesta')
            nueva_encuesta = form.save(commit=False)
            nueva_encuesta.contacto = request.user
            nueva_encuesta.save()
            messages.success(
                request, '¡Gracias! Tu opinión se ha enviado correctamente.')
            return redirect('encuesta')
        messages.error(
            request, 'No se pudo enviar la encuesta. Revisa los campos del formulario.')
    else:
        form = EncuestaForm()

    return render(request, 'encuestas/encuesta.html', {
        'form': form,
        'encuestas': encuestas,
        'promedio': promedio,
        'grafico': grafico,
    })
