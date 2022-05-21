from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']


class IssueTokenRequestSerializer(serializers.Serializer):
    model = User

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class TokenSeriazliser(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']