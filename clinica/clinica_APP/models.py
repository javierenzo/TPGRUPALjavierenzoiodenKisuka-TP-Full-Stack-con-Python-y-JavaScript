from django.db import models

# Create your models here.


class Gerente(models.Model):
    nombreGerent = models.CharField(max_length=64)
    apellidoGerent = models.CharField(max_length=64)
    dniGerent = models.IntegerField()
    telefonoGerent = models.IntegerField()
    usuarioGerent = models.CharField(max_length=64)
    contraseGerent = models.CharField(max_length=64)


class Tecnico(models.Model):
    nombreTecnico = models.CharField(max_length=64)
    apellidoTecnico = models.CharField(max_length=64)
    dniTecnico = models.IntegerField()
    telefonoTecnico = models.IntegerField()
    usuarioTecnico = models.CharField(max_length=64)
    contraseTenico = models.CharField(max_length=64)


class Vendedor (models.Model):
    nombreVendedor  = models.CharField(max_length=64)
    apellidoVendedor  = models.CharField(max_length=64)
    dniVendedor  = models.IntegerField()
    telefonoVendedor  = models.IntegerField()
    usuarioVendedor = models.CharField(max_length=64)
    contraseVendedor = models.CharField(max_length=64)


class Secretaria (models.Model):
    nombreSecretaria = models.CharField(max_length=64)
    apellidoSecretaria = models.CharField(max_length=64)
    dniSecretaria = models.IntegerField()
    telefonoSecretaria = models.IntegerField()
    usuarioSecretaria = models.CharField(max_length=64)
    contrasSecretaria = models.CharField(max_length=64)


class Medico(models.Model):
    nombreMed = models.CharField(max_length=64)
    apellidoMed = models.CharField(max_length=64)
    dniMed = models.IntegerField()
    telefonoMed = models.IntegerField()
    usuarioMed = models.CharField(max_length=64)
    contrasMed = models.CharField(max_length=64)
