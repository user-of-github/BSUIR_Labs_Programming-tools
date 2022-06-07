import datetime

import pytest
from rest_framework.test import APIClient
from marveldcmovies.models import Movie

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
def test_not_found_movie():
    response = client.get('/api/movie/unknownmovie/')
    assert response.status_code == 200
    assert response.data['success'] == False


@pytest.mark.django_db
def test_search_movies():
    response = client.get('/api/searchmovie/kekshrekunknownmovie/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_getting_movie():
    Movie.objects.create(title='test', year=2016, date_from='2019-06-06', date_to='2020-05-13', movie_id='1testmovie',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='test3', year=2016, date_from='2019-06-06', date_to='2020-05-13', movie_id='testmovie3',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='test2', year=2016, date_from='2019-06-06', date_to='2020-05-13', movie_id='testmovie2',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    response = client.get('/api/movie/1testmovie/')

    print('DATA', response.data)

    assert response.status_code == 200
    assert response.data['data']['title'] == 'test'


@pytest.mark.django_db
def test_getting_movie():
    Movie.objects.create(title='test', year=2016, date_from='2019-06-06', date_to='2020-05-13',
                         movie_id='testmovie',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='test3', year=2016, date_from='2019-06-06', date_to='2020-05-13',
                         movie_id='testmovie3',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='test2', year=2016, date_from='2019-06-06', date_to='2020-05-13',
                         movie_id='testmovie2',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    response = client.get('/api/movies/popular/')

    assert response.status_code == 200
    assert len(response.data['data']) == 3


@pytest.mark.django_db
def test_getting_invalid_movie():
    Movie.objects.create(title='test', year=2016, date_from='2019-06-06', date_to='2020-05-13', movie_id='1testmovie',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='test3', year=2016, date_from='2019-06-06', date_to='2020-05-13', movie_id='testmovie3',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='test2', year=2016, date_from='2019-06-06', date_to='2020-05-13', movie_id='testmovie2',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    response = client.get('/api/movies/5/0/')

    assert response.status_code == 200
    assert response.data['success'] == False
