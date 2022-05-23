from django.contrib import admin
from django.urls import path
from marveldcmovies.views import MoviesAPIView, MovieAPIView, SearchMovieAPIView, MyTokenObtainPairView
from marveldcmovies.views import PopularMoviesAPIView, MoviesByIdsAPIView, TheatersForMovieAPIView
from marveldcmovies.views import MovieTheatersAPIView, MovieTheaterAPIView, MostPopularMovieTheaterAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/movies/', MoviesAPIView.as_view()),
    path('api/movies/<int:load_from>/<int:load_to>/', MoviesAPIView.as_view()),
    path('api/movies/getmovieslistbyids/', MoviesByIdsAPIView.as_view()),
    path('api/popularmovies/', MoviesAPIView.as_view()),
    path('api/movie/<str:searched_id>/', MovieAPIView.as_view()),
    path('api/movies/popular/', PopularMoviesAPIView.as_view()),
    path('api/movietheaters/', MovieTheatersAPIView.as_view()),
    path('api/movietheaters/popular/', MostPopularMovieTheaterAPIView.as_view()),
    path('api/movietheaters/<str:searched_title>/', MovieTheaterAPIView.as_view()),
    path('api/theatersformovie/<str:movie_to_search_theaters>/', TheatersForMovieAPIView.as_view()),
    path('api/searchmovie/<str:query>/', SearchMovieAPIView.as_view()),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]