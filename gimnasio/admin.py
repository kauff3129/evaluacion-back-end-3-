from django.contrib import admin
from .models import PlanMembresia, Socio

@admin.register(PlanMembresia)
class PlanMembresiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'duracion_meses', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('id', 'rut', 'nombre', 'plan', 'mensualidad_pagada', 'fecha_inscripcion', 'activo')
    list_filter = ('plan', 'activo', 'fecha_inscripcion')
    search_fields = ('rut', 'nombre', 'email')