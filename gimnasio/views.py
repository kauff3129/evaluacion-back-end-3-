from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Socio
from .forms import SocioForm

class SocioListView(ListView):
    model = Socio
    template_name = 'gimnasio/socio_list.html'
    context_object_name = 'socios'
    # Optimización obligatoria para evitar problema N+1
    queryset = Socio.objects.select_related('plan').all()


class SocioDetailView(DetailView):
    model = Socio
    template_name = 'gimnasio/socio_detail.html'
    context_object_name = 'socio'
    queryset = Socio.objects.select_related('plan')


class SocioCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'gimnasio/socio_form.html'
    success_url = reverse_lazy('socio_list')
    success_message = "✅ El socio '%(nombre)s' fue inscrito exitosamente en el gimnasio."


class SocioUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'gimnasio/socio_form.html'
    success_url = reverse_lazy('socio_list')
    success_message = "✅ Los datos del socio '%(nombre)s' fueron actualizados correctamente."


class SocioDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Socio
    template_name = 'gimnasio/socio_confirm_delete.html'
    context_object_name = 'socio'
    success_url = reverse_lazy('socio_list')
    success_message = "🗑️ El registro del socio ha sido eliminado del sistema."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)