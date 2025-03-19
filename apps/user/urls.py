from django.urls import path
from .views import UsuarioView, UsuarioLogin


urlpatterns = [
    path('usuarios', UsuarioView.as_view()),
    path('login', UsuarioLogin.as_view()),
]


