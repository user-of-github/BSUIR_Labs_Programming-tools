from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    movie_id = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    rating = models.SmallIntegerField()
    poster_image_link = models.CharField(max_length=500)
    duration = models.SmallIntegerField()
    age_restriction = models.SmallIntegerField()
    visits_count = models.IntegerField(default=0)


class MovieTheater(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    location = models.CharField(max_length=600)
    photo = models.CharField(max_length=600, default='photo')
    visits_count = models.IntegerField(default=0)
