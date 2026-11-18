# Bitácora de Uso de Inteligencia Artificial (Formato RTCF)

- **Asignatura:** Programación Back End (TI3041) - Evaluación Sumativa 3 (Hito 3)
- **Asistente IA Utilizado:** Google Gemini
- **Temática del Proyecto:** Sistema de Gestión de Gimnasio (`IronGym`)

---

## Prompt 1: Diseño de Interfaz Front-End para Catálogo y Ficha de Socio

- **Rol (R):** Actúa como un desarrollador Full-Stack experto en Django Template Language (DTL) y diseño responsivo con Bootstrap 5.
- **Tarea (T):** Diseña las plantillas HTML `socio_list.html` y `socio_detail.html` que hereden de `base.html`, incluyendo visibilidad condicional según el estado de autenticación del usuario (`user.is_authenticated`) y etiquetas de estado para membresías activas e inactivas.
- **Contexto (C):** Estoy desarrollando el Hito 3 de Programación Back End para un gimnasio donde `PlanMembresia` es el modelo padre y `Socio` es el modelo hijo optimizado con `select_related('plan')`. Solo los usuarios autenticados deben visualizar los botones de creación, edición y borrado.
- **Formato (F):** Entrégame bloques de código HTML comentados y estructurados con tarjetas (`card`), tablas responsivas (`table-responsive`) y badges de Bootstrap 5 listos para integrar en la carpeta `templates/gimnasio/`.

---

## Prompt 2: Optimización ORM y Resolución de MRO en Vistas Basadas en Clases

- **Rol (R):** Actúa como un Arquitecto de Software especialista en Django 5 y optimización de consultas relacionales en MySQL.
- **Tarea (T):** Revisa y estructura las Vistas Basadas en Clases (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) garantizando la erradicación del problema N+1 y aplicando protección de rutas junto con notificaciones emergentes al usuario.
- **Contexto (C):** En el archivo `gimnasio/views.py`, necesito consultar el modelo `Socio` trayendo en la misma consulta SQL los datos de `PlanMembresia` mediante `select_related('plan')`. Además, debo aplicar `LoginRequiredMixin` y `SuccessMessageMixin` respetando estrictamente el orden de resolución de métodos (MRO) de Python.
- **Formato (F):** Proporciona el código Python completo de `views.py` aplicando `reverse_lazy` y un método `form_valid` en `DeleteView` para asegurar que el mensaje de confirmación se despliegue en las alertas descartables de Bootstrap 5.
