from django.contrib import admin
from . models import Movie, Theatre, Show, Booking

admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Show)
admin.site.register(Booking)
# Register your models here.
