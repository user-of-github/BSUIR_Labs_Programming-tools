import pytest
from rest_framework.test import APIClient
from marveldcmovies.models import MovieTheater


client: APIClient = APIClient()


@pytest.mark.django_db
def test_movies():
    response = client.get('/api/movies/')

    data = response.data
    assert data['success'] == True
    assert response.status_code == 200


@pytest.mark.django_db
def test_movies_2():
    response = client.get('/api/movies/0/0/')

    data = response.data
    assert data['success'] == True
    assert response.status_code == 200


@pytest.mark.django_db
def test_popular_movies():
    response = client.get('/api/popularmovies/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_not_found_movie():
    response = client.get('/api/movie/unknownmovie/')
    assert response.status_code == 200
    assert response.data['success'] == False