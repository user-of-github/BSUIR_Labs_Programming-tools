from rest_framework import views
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Movie, MovieTheater
from .serializers import MovieShortenSerializer, MovieFullSerializer, MovieTheaterSerializer
from django.db.models import F


class MoviesAPIView(views.APIView):
    STATUS_SUCCESS_RETURNED: str = 'Successfully returned movies'
    STATUS_SUCCESS_BUT_RETURNED_LESS: str = 'Successfully returned, but only available part'
    STATUS_ERROR_INVALID_QUERY: str = 'Nothing to return. Invalid query'

    def get(self, request: Request, load_from: int = 0, load_to: int = 3) -> Response:
        response: dict = dict()

        all_movies = Movie.objects.all()

        real_load_to: int = min(len(all_movies), max(0, load_to + 1))

        if 0 <= load_from <= real_load_to <= len(all_movies):
            response['success'] = True
            response['data'] = MovieShortenSerializer(all_movies[load_from:real_load_to], many=True).data
            response['howManyLeft'] = len(all_movies) - real_load_to

            if real_load_to - 1 != load_to:
                response['status'] = MoviesAPIView.STATUS_SUCCESS_BUT_RETURNED_LESS
            else:
                response['status'] = MoviesAPIView.STATUS_SUCCESS_RETURNED
        else:
            response['success'] = False
            response['data'] = list()
            response['status'] = MoviesAPIView.STATUS_ERROR_INVALID_QUERY
            response['howManyLeft'] = 0

        return Response(response)


class MovieAPIView(views.APIView):
    def get(self, request: Request, searched_id: str) -> Response:
        response: dict = dict()

        found_in_database = Movie.objects.filter(movie_id=searched_id)

        if len(found_in_database) == 0:
            response['success'] = False
            response['data'] = None
        elif len(found_in_database) == 1:
            found_in_database.update(visits_count=F('visits_count') + 1)
            response['success'] = True
            response['data'] = MovieFullSerializer(found_in_database[0]).data

        return Response(response)


class PopularMoviesAPIView(views.APIView):
    DEFAULT_POPULAR_MOVIES_COUNT: int = 4

    def get(self, request: Request) -> Response:
        all_movies = Movie.objects.all()

        return_count: int = min(PopularMoviesAPIView.DEFAULT_POPULAR_MOVIES_COUNT, len(all_movies))

        popular_movies = all_movies.order_by('-visits_count')[:return_count]

        return Response({'data': MovieShortenSerializer(popular_movies, many=True).data})


class MovieTheatersAPIView(views.APIView):
    def get(self, request: Request) -> Response:
        return Response({'data': MovieTheaterSerializer(MovieTheater.objects.all(), many=True).data})


class MovieTheaterAPIView(views.APIView):
    def get(self, request: Request, searched_title: str) -> Response:
        response: dict = dict()

        found_in_database = MovieTheater.objects.filter(title=searched_title)

        if len(found_in_database) == 0:
            response['success'] = False
            response['data'] = None
        elif len(found_in_database) == 1:
            found_in_database.update(visits_count=F('visits_count') + 1)
            response['success'] = True
            response['data'] = MovieTheaterSerializer(found_in_database[0]).data

        return Response(response)
