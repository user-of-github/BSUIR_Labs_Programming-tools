from django.contrib import admin
from django.urls import path

from ticketservice.views import MoviesAPIView, MovieAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', MoviesAPIView.as_view()),
    path('api/movie/', MovieAPIView.as_view())
]
