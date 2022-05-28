import pytest
from rest_framework.test import APIClient
from marveldcmovies.models import Comment


client: APIClient = APIClient()


@pytest.mark.django_db
def test_popular_movie_theaters():
    response = client.get('/api/comments/getcommentslistbyids/?ids=')
    assert response.status_code == 200
