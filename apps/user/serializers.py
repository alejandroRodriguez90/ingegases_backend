from rest_framework import serializers
from .models import Usuario, Rol

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo' , 'usuario', 'contrasena']

class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'