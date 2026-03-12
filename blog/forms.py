from django import forms
from blog.models import Encuesta, Mensaje, Tarea, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SaludoForm(forms.Form):
    nombre = forms.CharField(label='Introduce tu nombre', max_length=50)


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion']


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['texto']


class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['opinion', 'satisfaccion']


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto', 'bio']
