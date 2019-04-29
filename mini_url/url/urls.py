from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^url/$', views.nouvelle_url, name='nouvelle_url'),
    url(r'^url/$', views.URLCreate.as_view(), name='nouvelle_url'),
    url(r'^url/editer/(?P<code>\w{6})/$', views.URLUpdate.as_view(), name='edit_url'),
    url(r'^url/supprimer/(?P<code>\w{6})$', views.URLDelete.as_view(), name='delete_url'),
    url(r'^url/(?P<code>\w{6})/', views.redirect_url, name='redirect_url'),
    url(r'urls/', views.voir_urls, name='urls'),
]
