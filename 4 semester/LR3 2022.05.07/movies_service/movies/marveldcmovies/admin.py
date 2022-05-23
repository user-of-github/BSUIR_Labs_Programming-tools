from django.contrib import admin

from .models import Movie, MovieTheater, CinematicUniverse

admin.site.register(Movie)
admin.site.register(MovieTheater)
admin.site.register(CinematicUniverse)
