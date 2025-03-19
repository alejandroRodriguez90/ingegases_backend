from django.urls import path
from .views import UsuarioView


urlpatterns = [
    path('usuarios', UsuarioView.as_view())
]


