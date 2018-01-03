from django.contrib import admin
from .models import Track, Driver, TrackDriver, Bet

admin.site.register(Track)
admin.site.register(Driver)
admin.site.register(TrackDriver)
admin.site.register(Bet)