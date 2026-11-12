from django.urls import path

from . import views

urlpatterns = [
    path("", views.IncidenciaListView.as_view(), name="lista_incidencias"),
    path("nueva/", views.IncidenciaCreateView.as_view(), name="nueva_incidencia"),
]