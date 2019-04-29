from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import MiniURLForm
from .models import MiniURL


def nouvelle_url(request):
    """
    - url(r'^url/$', views.nouvelle_url, name='nouvelle_url'),
    """
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(voir_urls)
    else:
        form = MiniURLForm()

    return render(request, "url/new_url.html", {'form': form})


def voir_urls(request):
    urls = MiniURL.objects.order_by('-nb_acces')
    return render(request, "url/list_urls.html", locals())


def redirect_url(request, code):
    mini_url = get_object_or_404(MiniURL, code=code)
    mini_url.nb_acces += 1
    mini_url.save()
    return redirect(mini_url.url)


class URLCreate(CreateView):
    model = MiniURL
    template_name = 'url/new_url.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(voir_urls)


class URLUpdate(UpdateView):
    model = MiniURL
    template_name = 'url/new_url.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(voir_urls)

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, code=code)

    def form_valid(self, form):
        self.object = form.save()
        # Envoi d'un message à l'utilisateur
        # messages.success(self.request, "Votre profil a été mis à jour avec succès.")
        return HttpResponseRedirect(self.get_success_url())


class URLDelete(DeleteView):
    model = MiniURL
    context_object_name = "mini_url"
    template_name = 'url/supprimer.html'
    success_url = reverse_lazy(voir_urls)

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, code=code)
