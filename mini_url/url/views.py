from django.shortcuts import render, get_object_or_404, redirect

from .forms import NouvelleURLForm
from .models import MiniURL


def nouvelle_url(request):
    if request.method == "POST":
        form = NouvelleURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(voir_urls)
    else:
        form = NouvelleURLForm()

    return render(request, "url.html", {'form': form})


def voir_urls(request):
    urls = MiniURL.objects.order_by('-nb_acces')
    return render(request, "list_urls.html", locals())


def redirect_url(request, code):
    mini_url = get_object_or_404(MiniURL, code=code)
    mini_url.nb_acces += 1
    mini_url.save()
    return redirect(mini_url.url)
