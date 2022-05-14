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
    