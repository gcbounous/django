from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from .models import Article, Categorie


class ListeArticles(ListView):
    """
    # url(r'^$', views.ListeArticles.as_view(), name="accueil"),
    """
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 5
    queryset = Article.objects.filter(is_visible=True)

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListeArticles, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context


class ListeArticlesByCategorie(ListeArticles):
    """
    # url(r'^/categorie?(?P<id>\d+)$', views.ListeArticlesByCategorie.as_view(), name="blog_liste"),
    """
    def get_queryset(self):
        return Article.objects.filter(categorie__id=self.kwargs['id'])


class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"
    # queryset = Article.objects.filter(is_visible=True)

    def get_object(self, **kwargs):
        # Nous récupérons l'objet, via la super-classe
        article = super(LireArticle, self).get_object()
        # article.nb_vues += 1  # Imaginons un attribut « Nombre de vues »
        article.save()
        return article  # Et nous retournons l'objet à afficher


def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.

    # url(r'^$', views.accueil, name='accueil'),
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]
    categories = Categorie.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles, 'categories': categories})


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
