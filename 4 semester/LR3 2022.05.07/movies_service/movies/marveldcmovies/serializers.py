from rest_framework import serializers


class MovieShortenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    movie_id = serializers.CharField(max_length=50)
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    poster_image_link = serializers.CharField(max_length=500)
