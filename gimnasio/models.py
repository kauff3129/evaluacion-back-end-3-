from django.db import models

class PlanMembresia(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Plan")
    descripcion = models.TextField(blank=True, verbose_name="Descripción y Beneficios")
    duracion_meses = models.PositiveIntegerField(default=1, verbose_name="Duración (Meses)")

    class Meta:
        verbose_name = "Plan de Membresía"
        verbose_name_plural = "Planes de Membresía"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.duracion_meses} meses)"


class Socio(models.Model):
    plan = models.ForeignKey(
        PlanMembresia,
        on_delete=models.RESTRICT,
        related_name='socios',
        verbose_name="Plan Contratado"
    )
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    mensualidad_pagada = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        verbose_name="Monto Pagado ($)"
    )
    fecha_inscripcion = models.DateField(verbose_name="Fecha de Inscripción")
    activo = models.BooleanField(default=True, verbose_name="Membresía Activa")

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"
        ordering = ['-fecha_inscripcion', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.rut})"