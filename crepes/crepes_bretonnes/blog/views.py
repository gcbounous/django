from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime

from .models import Article


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'accueil.html', {'derniers_articles': articles})


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """

    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'lire.html', {'article': article})


def view_article(request, id_article):
    if id_article > 100:
        raise Http404

    # return HttpResponse(Vous avez demandé l'article n° {0} !".format(id_article))
    return redirect(view_redirection)


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def list_articles(request, year, month=1):
    return HttpResponse('Articles de %s/%s' % (year, month))


def date_actuelle(request):
    return render(request, 'date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'addition.html', locals())
