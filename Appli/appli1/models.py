from django.db import models

# Create your models here.

class Fichier(models.Model):
    file = models.FileField(upload_to='files')

class Enregistrement (models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
