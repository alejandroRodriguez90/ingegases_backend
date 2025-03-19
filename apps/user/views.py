from django.shortcuts import render
from .models import Usuario, Rol
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializers, RolSerializers

class UsuarioView (APIView):
    def get(selft, request):
        usuarios = Usuario.objects.all()
        usuarios = UsuarioSerializers(usuarios, many=True)
        return Response(usuarios.data)

    def post(self, request):
        try:
            # Obtener el rol con ID 2
            rol = Rol.objects.get(id=2)
        except Rol.DoesNotExist:
            return Response({"error": "El rol con ID 2 no existe"}, status=status.HTTP_400_BAD_REQUEST)

        # Copiar request.data para modificarlo
        usuario_data = request.data.copy()

        # Crear el usuario con el rol asignado
        usuario = Usuario(
            nombre=usuario_data['nombre'],
            correo=usuario_data['correo'],
            usuario=usuario_data['usuario'],
            contrasena=usuario_data['contrasena'],
            rol_id=rol
        )

        usuario.save()


        usuario_serializado = UsuarioSerializers(usuario)
        return Response(usuario_serializado.data, status=status.HTTP_201_CREATED)
    

class UsuarioLogin(APIView):
    def post(selft, request):
        email = request.data.get("correo")
        password = request.data.get("contrasena")
        usuario = Usuario.objects.get("correo")

        if usuario is None:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        if usuario.contrasena != password:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)

        usuario_serializado = UsuarioSerializers(usuario)
        return Response(usuario_serializado.data)


        






