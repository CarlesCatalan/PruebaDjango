from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Mensaje
from .forms import MensajeForm


@login_required
def mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.name = request.user
            nuevo_mensaje.save()
            return redirect('mensaje')
    else:
        form = MensajeForm()

    mensajes = Mensaje.objects.all().order_by('-fecha')
    return render(request, 'mensajes/mensaje.html', {
        'form': form,
        'mensajes': mensajes,
    })
