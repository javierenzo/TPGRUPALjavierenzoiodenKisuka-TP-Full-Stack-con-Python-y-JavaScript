from django.db import models
# import paquete.modulo1
# import app_pacientes.models
from app_pacientes.models import Paciente
from clinica_APP.models import Medico
# Create your models here.

class Turno(models.Model):
    fecha_turno = models.DateField()
    paciente_T = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="paciente")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="paciente")


