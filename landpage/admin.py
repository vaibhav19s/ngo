from django.contrib import admin
from .models import Ngo
from .models import Event

admin.site.register(Ngo)
admin.site.register(Event)