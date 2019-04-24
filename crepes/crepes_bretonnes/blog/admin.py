from django.contrib import admin

from .models import Categorie, Article, Contact


class ArticleAdmin(admin.ModelAdmin):
    list_display    = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter     = ('auteur', 'categorie',)
    date_hierarchy  = 'date'
    ordering        = ('date', )
    search_field    = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',), }

    # Configuration du formulaire d'édition
    # fields = ('titre', 'auteur', 'categorie', 'contenu')
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', 'test'],
            'fields': ('titre', 'slug', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu',)
        }),
    )

    # Colones personalisées
    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '{}…'.format(text)
        else:
            return text

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Categorie)
admin.site.register(Contact)
admin.site.register(Article, ArticleAdmin)