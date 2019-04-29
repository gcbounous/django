from django.conf.urls import include, url
from django.views.generic import ListView

from blog.models import Article
from . import views


urlpatterns = [
    # url(r'^$', views.accueil, name='accueil'),
    # url(r'^$', ListView.as_view(model=Article,
    #                             context_object_name="dernier_articles",
    #                             template_name="blog/accueil.html")),
    url(r'^$', views.ListeArticles.as_view(), name="accueil"),
    url(r'^categorie/(?P<id>\d+)$', views.ListeArticlesByCategorie.as_view(), name="blog_categorie"),

    url(r'^(?P<slug>.+)$', views.lire_article, name='blog_slug_lire'),
    url(r'^article/(?P<pk>\d+)$', views.lire_article, name='blog_id_lire'),

]

