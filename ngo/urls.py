from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^landpage/', include('landpage.urls')),
    url(r'^', include('landpage.urls')),
]
