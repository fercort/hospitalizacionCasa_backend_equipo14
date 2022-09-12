from django.db import models

# Create your models here.
class pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    #id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion= models.CharField(max_length=100)
    telefono= models.CharField(max_length=30)
    contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=30)

class medicos (models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    telefono= models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100)
    
class signos_vitales(models.Model):
    id_signo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    valor_maximo = models.IntegerField()
    valor_minimo= models.IntegerField()
    recomendacion = models.CharField(max_length=100)

class historias_clinicas(models.Model):
    id_historia_clinica = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(pacientes, related_name="historias_pacientes", on_delete=models.CASCADE)
    id_medico = models.ForeignKey(medicos, related_name= "historia_medico", on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    observaciones = models.CharField(max_length=200)
    recomendaciones = models.IntegerField()
 

class historias_signos(models.Model):
    id_historia = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    id_paciente = models.ForeignKey(pacientes, related_name="historia_paciente", on_delete=models.CASCADE)
    id_signo= models.ForeignKey(signos_vitales, related_name= "historia_signo_vitales", on_delete=models.CASCADE)
    valor_signo = models.IntegerField()
   
    
