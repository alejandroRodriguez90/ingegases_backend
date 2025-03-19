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
    
    def post(selft, request):
        #quiero que siempre el rol_id sea 2
        request.data['rol_id'] = 2
        usuario = UsuarioSerializers(data=request.data)
        if usuario.is_valid():
            usuario.save()
            return Response(usuario.data, status=status.HTTP_201_CREATED)
        return Response(usuario.errors, status=status.HTTP_400_BAD_REQUEST)



