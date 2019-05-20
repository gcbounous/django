from django.test import TestCase
from datetime import datetime, timedelta
from .models import Article


class ArticleTests(TestCase):
    def test_est_recent_avec_futur_article(self):
        """
        Vérifier si la méthode est_recent d'un Article ne renvoie
         pas True si l'article a sa date de publication dans le futur
        """
        futur_article = Article(date=datetime.now() + timedelta(days=20))
        self.assertFalse(futur_article.est_recent())



class UnTest(TestCase):

    @classmethod  # <- setUpClass doit être une methode de classe, attention!
    def setUpTestData(cls):
        Categorie.objects.create(titre="Par défaut")

    def setUp(self):
        self.une_variable = "Salut!"

    def test_verification(self):
        self.assertEqual(self.une_variable, "Salut!")
        self.assertTrue(Categorie.objects.filter(titre="Par défaut").exists())
