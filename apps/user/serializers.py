from rest_framework import serializers
from .models import Usuario, Rol

class UsuarioSerializers(serializers.ModelSerializer):
    rol = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id','nombre', 'correo', 'usuario', 'contrasena', 'rol']

class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'