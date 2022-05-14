from django.forms import model_to_dict
from rest_framework import views
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Movie
from .serializers import MovieShortenSerializer


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
    def get(self, request: Request) -> Response:
        query_parameter_id: str = request.query_params.get('id')

        found_in_database: list = Movie.objects.filter(movie_id=query_parameter_id)

        if len(found_in_database) == 0:
            movie_to_return = None
        else:
            movie_to_return = model_to_dict(found_in_database[0])

        return Response(movie_to_return, headers={
            'Access-Control-Allow-Methods': 'GET, POST, PUT',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*'
        })
