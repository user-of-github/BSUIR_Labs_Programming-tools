from rest_framework import serializers

from marveldcmovies.models import MovieTheater, Movie


class MovieShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'movie_id', 'date_from', 'date_to', 'poster_image_link']


class MovieFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['id', 'visits_count']


class MovieTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTheater
        exclude = ['visits_count', 'id']

