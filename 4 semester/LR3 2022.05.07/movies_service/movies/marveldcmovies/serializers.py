from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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

# Useful post about authorization
# https://habr.com/ru/post/512746/


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
