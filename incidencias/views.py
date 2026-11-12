from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import IncidenciaForm
from .models import Incidencia


class IncidenciaListView(ListView):
    model = Incidencia
    template_name = "incidencias/lista.html"
    context_object_name = "incidencias"


class IncidenciaCreateView(CreateView):
    model = Incidencia
    form_class = IncidenciaForm
    template_name = "incidencias/formulario.html"
    success_url = reverse_lazy("lista_incidencias")