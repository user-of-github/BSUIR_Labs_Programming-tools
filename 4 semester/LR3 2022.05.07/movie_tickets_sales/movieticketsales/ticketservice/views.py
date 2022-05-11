from django.forms import model_to_dict
from rest_framework import views
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Movie


class MoviesAPIView(views.APIView):
    def get(self, request: Request) -> Response:
        response: list = list()

        for item in Movie.objects.all():
            response.append(model_to_dict(item))

        return Response({'posts': response})


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

