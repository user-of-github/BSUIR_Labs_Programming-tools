from django.contrib import admin
from django.urls import path
from marveldcmovies.views import MoviesAPIView, MovieAPIView, SearchMovieAPIView
from marveldcmovies.views import PopularMoviesAPIView, MoviesByIdsAPIView, TheatersForMovieAPIView
from marveldcmovies.views import MovieTheatersAPIView, MovieTheaterAPIView, MostPopularMovieTheaterAPIView
from marveldcmovies.views import user, issue_token


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

    path('api/user/', user, name='user'),
    path('api/login', issue_token, name='issue_token')
]
