from django.contrib import admin
from django.urls import path
from marveldcmovies.views import MoviesAPIView, MovieAPIView, PopularMoviesAPIView, MovieTheatersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', MoviesAPIView.as_view()),
    path('api/movies/<int:load_from>/<int:load_to>/', MoviesAPIView.as_view()),
    path('api/popularmovies/', MoviesAPIView.as_view()),
    path('api/movie/<str:searched_id>/', MovieAPIView.as_view()),
    path('api/movies/popular/', PopularMoviesAPIView.as_view()),
    path('api/movietheaters', MovieTheatersAPIView.as_view()),
]
