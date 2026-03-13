from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Profile
from .forms import RegistroForm, ProfileForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            messages.success(
                request,
                f'Cuenta creada correctamente. ¡Bienvenido/a, {user.username}!'
            )
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def perfil(request):
    profile = getattr(request.user, 'profile', None)
    return render(request, 'usuarios/perfil.html', {'profile': profile})


@login_required
def editar_perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
