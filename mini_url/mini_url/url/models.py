from django.db import models


class MiniURL(models.Model):
    url_longue = models.URLField(unique=True)
    code = models.CharField(unique=True, max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    pseudo_createur = models.CharField(max_length=100, blank=True)
    nombre_acces = models.IntegerField(default=0)
