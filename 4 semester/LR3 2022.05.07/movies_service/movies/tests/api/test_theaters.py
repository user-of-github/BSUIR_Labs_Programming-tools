import pytest
from rest_framework.test import APIClient
from marveldcmovies.models import MovieTheater

client: APIClient = APIClient()


@pytest.mark.django_db
def test_movie_theaters():
    response = client.get('/api/movietheaters/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_popular_movie_theaters():
    response = client.get('/api/movietheaters/popular/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_popular_movie_theaters():
    MovieTheater.objects.create(title='testtheater', address='online', location='online', photo='nophoto', telephone='+375375375')
    response = client.get('/api/movietheaters/testtheater/')
    assert response.status_code == 200
    assert response.data['data']['title'] == 'testtheater'


@pytest.mark.django_db
def test_not_existing_movie_theater():
    response = client.get('/api/movietheaters/notexisting/')
    assert response.status_code == 200
    assert response.data['success'] == False