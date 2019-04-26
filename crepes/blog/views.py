from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm
from .models import Article


def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})


def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article = get_object_or_404(Article, slug=slug)
    commentaires = article.commentaires.filter(is_visible=True)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(lire_article, slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/lire_article.html',
                  {
                      'article': article,
                      "commentaires": commentaires,
                      "comment_form": comment_form
                  }
                  )
