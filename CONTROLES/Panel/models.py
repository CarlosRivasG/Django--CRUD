from django.db import models

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(null=False)
    f_nacimiento = models.DateField(null=False)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table ='usuarios'