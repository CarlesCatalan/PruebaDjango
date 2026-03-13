from django import forms


class SaludoForm(forms.Form):
    nombre = forms.CharField(label='Introduce tu nombre', max_length=50)
