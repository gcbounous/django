from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^(?P<slug>.+)$', views.lire_article, name='blog_lire'),
]
