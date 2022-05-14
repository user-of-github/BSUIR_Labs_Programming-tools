from django.contrib import admin
from django.urls import path

from marveldcmovies.views import MoviesAPIView, MovieAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/movies/', MoviesAPIView.as_view()),
    path('api/movies/<int:load_from>/<int:load_to>/', MoviesAPIView.as_view()),

    path('api/popularmovies/', MoviesAPIView.as_view()),

    path('api/movie/<str:movie_id>/', MovieAPIView.as_view())
]
