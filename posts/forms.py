from django import forms
from .models import ComentarioPost


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioPost
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe un comentario...'}),
        }
