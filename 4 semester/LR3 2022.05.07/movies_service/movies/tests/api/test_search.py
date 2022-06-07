import pytest
from rest_framework.test import APIClient
from marveldcmovies.models import Movie

client: APIClient = APIClient()


@pytest.mark.django_db
def test_search_movies_theaters():
    Movie.objects.create(title='tEst', year=2016, date_from='2019-06-06', date_to='2020-05-13',
                         movie_id='testmovie',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='teSt3', year=2016, date_from='2019-06-06', date_to='2020-05-13',
                         movie_id='testmovie3',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    Movie.objects.create(title='TEST2', year=2016, date_from='2019-06-06', date_to='2020-05-13',
                         movie_id='testmovie2',
                         poster_image_link='', rating=5, age_restriction=13, duration=42)

    response = client.get('/api/searchmovie/2016/')
    assert response.status_code == 200
    assert len(response.data['data']) == 3
