from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'year',
                  'movie_id',
                  'date_from', 'date_to',
                  'rating', 'poster_image_link',
                  'duration', 'age_restriction'
                  )
