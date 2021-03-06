from django.db import models
from datetime import datetime


class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=40)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution", auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Visible", default=False)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)

    def est_recent(self):
        """
        :return: True si l'aticle a été publié dans les 30 dernier jours
        """
        return self.date < datetime.now() and (datetime.now() - self.date).days < 30

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['date']

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    """ Modèle pour les commentaires. A vous de l'écrire ! """
    pseudo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contenu = models.CharField(max_length=500)
    is_visible = models.BooleanField(verbose_name="Visible", default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='commentaires')

    def __str__(self):
        return self.contenu

    class Meta:
        ordering = ['-date_creation']

