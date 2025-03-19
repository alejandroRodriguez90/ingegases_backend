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
        # Obtener el rol con ID 2
        try:
            rol = Rol.objects.get(id=2)
        except Rol.DoesNotExist:
            return Response({"error": "El rol con ID 2 no existe"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el usuario con el rol predefinido
        usuario_data = request.data.copy()
        usuario_data['rol'] = rol.id

        usuario = UsuarioSerializers(data=usuario_data)
        if usuario.is_valid():
            usuario.save(rol=rol)
            return Response(usuario.data, status=status.HTTP_201_CREATED)

        return Response(usuario.errors, status=status.HTTP_400_BAD_REQUEST)






