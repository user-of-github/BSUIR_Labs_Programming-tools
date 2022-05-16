from rest_framework import serializers


class MovieShortenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    movie_id = serializers.CharField(max_length=50)
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    poster_image_link = serializers.CharField(max_length=500)


class MovieFullSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    year = serializers.IntegerField()
    movie_id = serializers.CharField(max_length=50)
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    rating = serializers.IntegerField()
    poster_image_link = serializers.CharField(max_length=500)
    duration = serializers.IntegerField()
    age_restriction = serializers.IntegerField()


class MovieTheaterSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=300)
    location = serializers.CharField(max_length=600)
    photo = serializers.CharField(max_length=600)

