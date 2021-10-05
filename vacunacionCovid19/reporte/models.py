from django.db import models

# Create your models here.
class Persona(models.Model): # class persona extends models.Model
    id_persona= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100,blank= False,null=False)
    apellido= models.CharField(max_length=100,blank= False,null=False)
    vacunado=models.BooleanField(default=False)
    fecha_nacimiento= models.DateField()



class Vacuna(models.Model):
    id_vacuna= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=20)
    productor= models.CharField(max_length=40)
    cuantas_dosis= models.IntegerField()

class Vacunacion(models.Model):
    id_vacunacion=models.AutoField(primary_key=True)
    persona= models.ForeignKey(Persona,on_delete=models.CASCADE)
    vacuna= models.ForeignKey(Vacuna,on_delete=models.CASCADE)
    lugar_vacunacion= models.CharField(max_length=50)
    fecha_vacunacion= models.DateField()
    dosis= models.IntegerField()
    lote_vacuna= models.CharField(max_length=10,blank=False,null=False)
    


