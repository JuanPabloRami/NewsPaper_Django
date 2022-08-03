from django.db import models

class Noticias(models.Model):
    idNoticia = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    imgNoticia = models.ImageField(upload_to="noticias",null = True)
    categoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

class Publicidad(models.Model):
    idAd = models.BigAutoField(primary_key=True)
    imgAd = models.ImageField(upload_to="publicidad",null = True)
    placement  = models.CharField(max_length=10)




