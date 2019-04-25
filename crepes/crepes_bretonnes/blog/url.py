from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.accueil, name='accueil'),
    path(r'article/<int:id>-<slug:slug>', views.lire, name='lire'),
    # path(r'^articles/(?P<tag>.+)', views.view_article_by_tag),
    path(r'articles/(?P<year>\d{4})/(?P<month>[01]?\d)', views.list_articles),
    path('redirection', views.view_redirection),

    path('contact/', views.nouveau_contact, name='contact'),
    path('contacts/', views.voir_contacts, name='contacts'),

    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]