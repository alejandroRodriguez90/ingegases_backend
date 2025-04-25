from django.db import models



class Rol (models.Model):
    descripcion = models.CharField(max_length=55)

    class Meta():
        db_table ='rol'


class Usuario(models.Model):
    nombre = models.CharField(max_length=55)
    correo = models.CharField(max_length=99)
    contrasena = models.CharField(max_length=8)
    usuario = models.CharField(max_length=55)
    rol_id = models.ForeignKey(Rol,on_delete=models.CASCADE)

    class Meta():
        db_table ='usuario'

