from django.db import models


class produit(models.Model):
    nom = models.CharField(max_length=30)
    prix = models.FloatField()
