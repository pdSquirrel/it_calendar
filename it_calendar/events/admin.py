from django.contrib import admin
from .models import Venue
from .models import EventUser
from .models import Event

admin.site.register(Venue)
admin.site.register(EventUser)
admin.site.register(Event)