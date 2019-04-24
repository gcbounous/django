from django.shortcuts import render, get_object_or_404, redirect

from .forms import NouvelleURLForm
from .models import MiniURL


def nouvelle_url(request):
    sauvegarde = False
    form = NouvelleURLForm(request.POST or None)
    if form.is_valid():
        mini_url = MiniURL()
        mini_url.url_longue = form.cleaned_data["url"]
        mini_url.pseudo_createur = form.cleaned_data["pseudo"]
        mini_url.code = generer(15)
        mini_url.save()
        sauvegarde = True

    return render(request, "url.html", {'form': form, 'sauvegarde': sauvegarde})


def voir_urls(request):
    urls = MiniURL.objects.all().order_by('-nombre_acces')
    return render(request, "list_urls.html", {'urls': urls})


def redirect_url(request, code):
    mini_url = get_object_or_404(MiniURL, code=code)
    mini_url.nombre_acces += 1
    mini_url.save()
    return redirect(mini_url.url_longue)


import random
import string


def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

    return ''.join(aleatoire)
