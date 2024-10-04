from django.db import models

#DEFINIMOS LOS MODELOS

#PAIS
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

#Metodo especial de Python define como se debe representar
#Un objeto cuando se convierte en una cadena, ejemplo
#Si tenemos un objeto pais con el nombre de "Guatemala", cuando
#Lo imprimamos solo simplemente mostrara "Guatemala"
    def __str__(self):
        return self.nombre
    
#DEPARTAMENTO
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    #Campo FK, relacion entre pais y departamento M:1
    #Cada departamento esta asociado a un pais especifico
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#MUNICIPIO
class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre