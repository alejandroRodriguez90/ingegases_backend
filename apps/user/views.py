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
        serializers = UsuarioSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)