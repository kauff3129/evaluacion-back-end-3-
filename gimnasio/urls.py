from django.urls import path
from .views import (
    SocioListView,
    SocioDetailView,
    SocioCreateView,
    SocioUpdateView,
    SocioDeleteView,
)

urlpatterns = [
    path('', SocioListView.as_view(), name='socio_list'),
    path('socio/<int:pk>/', SocioDetailView.as_view(), name='socio_detail'),
    path('socio/nuevo/', SocioCreateView.as_view(), name='socio_create'),
    path('socio/<int:pk>/editar/', SocioUpdateView.as_view(), name='socio_update'),
    path('socio/<int:pk>/eliminar/', SocioDeleteView.as_view(), name='socio_delete'),
]