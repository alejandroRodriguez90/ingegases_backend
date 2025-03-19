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
    def post(self, request):
        email = request.data.get("correo")
        password = request.data.get("contrasena")
        
        usuario = Usuario.objects.filter(correo=email)
        print(usuario)
        if usuario:
            if usuario[0].contrasena == password:
                return Response({"mensaje": "Usuario autenticado"}, status=status.HTTP_200_OK)
            else:
                return Response({"mensaje": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)



        






