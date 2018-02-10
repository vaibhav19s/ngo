from django.conf.urls import include,url
from . import views

app_name = 'landpage'

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^(?P<ngo_id>[0-9]+)/$' , views.detail , name ='detail'),
    url(r'^(?P<event_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^events/(?P<filter_by>[a-zA_Z]+)/$', views.events, name='events'),
    url(r'^create_ngo/$', views.create_ngo, name='create_ngo'),
    url(r'^(?P<ngo_id>[0-9]+)/create_event/$', views.create_event, name='create_event'),
    url(r'^(?P<ngo_id>[0-9]+)/delete_event/(?P<event_id>[0-9]+)/$', views.delete_event, name='delete_event'),
    url(r'^(?P<ngo_id>[0-9]+)/favorite_ngo/$', views.favorite_ngo, name='favorite_ngo'),
    url(r'^(?P<ngo_id>[0-9]+)/delete_ngo/$', views.delete_ngo, name='delete_ngo'),

]
