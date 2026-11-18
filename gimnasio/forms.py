from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['plan', 'rut', 'nombre', 'email', 'mensualidad_pagada', 'fecha_inscripcion', 'activo']
        widgets = {
            'plan': forms.Select(attrs={'class': 'form-select'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 19.123.456-7'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.cl'}),
            'mensualidad_pagada': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'placeholder':'Ej: 65000 (sin puntos)'}),
            'fecha_inscripcion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }