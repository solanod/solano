#crear tablas
from django.db import models
from django.contrib.auth.models import User
class Usuario (models.Model):
    identificacion = models.PositiveIntegerField(max_length=100,db_column="identificacion")
    Nombres = models.CharField(max_length=100,blank=True,null=True)
    Apellidos = models.CharField(max_length=100,blank=True,null=True)
    Tipo_de_documento = models.CharField(max_length=100,blank=True,null=True)
    Telefono = models.IntegerField(max_length=100,blank=True,null=True)
    Pais = models.ForeignKey("Pais",null=True,blank=True)
    Departamento = models.ForeignKey("Departamento",null=True,blank=True)
    Municipio = models.ForeignKey("Municipio",null=True,blank=True)
    foto = models.ImageField(imagen="imagen/",null=True,blank=True)
    Login = models.OneToOneField(User,on_delete=models.CASCADE,db_column="login_id")


class Pais (models.Model):
    id = models.AutoField()
    Nombre = models.CharField(max_length=100,blank=True,null=True)
    Departamento=models.ForeignKey("Departamento",null=True,blank=True)
class Departamento (models.Model):
    id = models.AutoField()
    Nombre = models.CharField(max_length=100,blank=True,null=True) 
class Municipio(models.model):
    id = models.AutoField()
    Nombre = models.CharField(max_length=100,blank=True,null=True)  
        
# Create your models here.
