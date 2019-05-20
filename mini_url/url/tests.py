from django.test import TestCase
from django.urls import reverse

from .models import MiniURL


def creer_url():
    mini = MiniURL(url="heet://foo.bar", code=MiniURL.generer(6), pseudo="Maxime")
    mini.save()
    return mini


class MiniURLTests(TestCase):
    def test_liste(self):
        """ Vérifie si une URL sauvegardée est bien affichéé """
        mini = creer_url()
        reponse = self.client.get(reverse('url.views.voir_urls'))

        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, mini.url)
        self.assertQuerysetEqual(reponse.context['minis'], [repr(mini)])

    def test_nouveau_redirection(self):
        """ Vérifie la redirection d'un ajout d'URL """
        data = {
            'url': 'http://www.djangoproject.com',
            'pseudo': 'Jean Dupont',
        }

        reponse = self.client.post(reverse('url.views.nouvelle_url'), data)
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('url.views.voir_urls'))

    def test_nouveau_ajout(self):
        """
        Vérifie si après la redirection l'URL ajoutée est bien dans la liste
        """
        data = {
            'url': 'http://www.crepes-bretonnes.com',
            'pseudo': 'Amateur de crêpes',
        }

        reponse = self.client.post(reverse('url.views.nouvelle_url'), data, follow=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, data['url'])
