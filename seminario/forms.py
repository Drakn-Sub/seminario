from django import forms
from django.core.exceptions import ValidationError
from .models import Inscrito
import re

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'institucion', 'cantidad_personas', 'telefono', 'estado', 'observacion']  

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():  # Asegúrate de que el teléfono contenga solo números
            raise ValidationError("El teléfono debe contener solo números.")
        if len(telefono) < 10:  # Asegúrate de que el teléfono tenga al menos 10 dígitos
            raise ValidationError("El teléfono debe tener al menos 10 dígitos.")
        return telefono

    def clean_cantidad_personas(self):  
        cantidad_personas = self.cleaned_data.get('cantidad_personas')
        if not (1 <= cantidad_personas <= 30):
            raise ValidationError("El número de personas debe estar entre 1 y 30.")
        return cantidad_personas