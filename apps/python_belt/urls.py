print '*'*25, 'APPS URLS.PY', '*'*25
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup ),
    url( r'^login$', views.login ),
    url( r'^logout$', views.logout ),
    url( r'^quotes$', views.quotes ),
    url( r'^quotes/(?P<id>\d+)/fav$', views.quote_fav ),
    url( r'^quotes/(?P<id>\d+)/unfav$', views.quote_unfav ),
    url( r'^quotes/(?P<id>\d+)/destroy$', views.quote_destroy ),
    url( r'^quotes/create$', views.quote_create ),
    url( r'^users/(?P<id>\d+)/show$', views.user_show ),
]
