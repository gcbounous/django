from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^url/$', views.nouvelle_url, name='url'),
    url(r'^url/(?P<code>\w{6})/', views.redirect_url, name='redirect_url'),
    url(r'urls/', views.voir_urls, name='urls'),
]
