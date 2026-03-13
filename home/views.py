from django.shortcuts import render
from .forms import SaludoForm


def home(request):
    return render(request, 'home/home.html')


def saludo(request):
    return render(request, 'home/saludo.html')


def saludoform(request):
    if request.method == 'POST':
        form = SaludoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            return render(request, 'home/saludo.html', {'nombre': nombre})
    else:
        form = SaludoForm()
    return render(request, 'home/saludoform.html', {'form': form})
