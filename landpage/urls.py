from django.conf.urls import include,url
from . import views

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin


app_name = 'landpage'

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^homepage/$', views.homepage, name='homepag'),
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^FAQ/$', views.FAQ, name='FAQ'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),


    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login.html'}, name='logout'),
    url(r'^logout/login.html/$', views.index, name='logout/login.html'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signupNGO/ngo_page/cangote.html/$', views.index, name='signupNGO/ngo_page/cangote.html'),
    url(r'^signupNGO/$', views.signupNGO, name='signupNGO'),
    url(r'^accounts/profile/$', views.index, name='accounts/profile'),

    url(r'^(?P<ngo_id>[0-9]+)/$' , views.viewpage , name ='viewpage'),
    url(r'^ngochange/$', views.ngochange, name='ngochange'),

    url(r'^(?P<event_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),


]
