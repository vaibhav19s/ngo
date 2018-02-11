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
    url(r'^signupNGO/ngo_page/cangote.html/$', views.ngo_info, name='signupNGO/ngo_page/cangote.html'),
    url(r'^signupNGO/$', views.signupNGO, name='signupNGO'),
    url(r'^accounts/profile/$', views.index, name='accounts/profile'),

    url(r'^(?P<ngo_id>[0-9]+)/$' , views.viewpage , name ='viewpage'),

    url(r'^(?P<event_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    #url(r'^register/$', views.register, name='register'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),
    #url(r'^events/(?P<filter_by>[a-zA_Z]+)/$', views.events, name='events'),
    #url(r'^create_ngo/$', views.create_ngo, name='create_ngo'),
    #url(r'^(?P<ngo_id>[0-9]+)/create_event/$', views.create_event, name='create_event'),
    #url(r'^(?P<ngo_id>[0-9]+)/delete_event/(?P<event_id>[0-9]+)/$', views.delete_event, name='delete_event'),
    #url(r'^(?P<ngo_id>[0-9]+)/favorite_ngo/$', views.favorite_ngo, name='favorite_ngo'),
    #url(r'^(?P<ngo_id>[0-9]+)/delete_ngo/$', views.delete_ngo, name='delete_ngo'),

]
