from django.urls import path, re_path
from . import views


urlpatterns = [
    path(r'url/', views.nouvelle_url, name='url'),
    path(r'urls/', views.voir_urls, name='urls'),
    re_path(r'^url/(?P<code>\w+)/', views.redirect_url, name='urls'),
]
