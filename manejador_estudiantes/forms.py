from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'colegio',
            'nombre',
            'documento',
            'curso',
            'edad',
        ]
        labels = {
            'colegio': 'Colegio',
            'nombre': 'Nombre',
            'documento': 'Documento',
            'curso': 'Curso',
            'edad': 'Edad',
        }