import json
import pytest
from rest_framework.authtoken.models import Token

pytestmark = pytest.mark.django_db

class TestCategoryApi:
    endpoint = '/api/category/'
    content = {
            'name': 'boaaacategory1'
        }
    def test_category_status(self, category_factory, regular_factory, api_client):
        user = regular_factory()
        category_factory.create_batch(5)
        api_client.force_authenticate(user=user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200


    def test_category_post(self, golden_factory, api_client):
        user = golden_factory()
        api_client.force_authenticate(user=user)

        response = api_client.post(self.endpoint, data=self.content)
        assert response.status_code == 201

    def test_category_permissions(self, category_factory, regular_factory, golden_factory, api_client):
        user = regular_factory()
        user2 = golden_factory()
        api_client.force_authenticate(user=user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        response = api_client.post(self.endpoint, data=self.content)
        assert response.status_code == 403
        api_client.force_authenticate(user=user2)
        response = api_client.post(self.endpoint, data=self.content)
        assert response.status_code == 201

class TestBrandApi:
    endpoint = '/api/brand/'

    def test_brand_status(self, brand_factory, category_factory, golden_factory, api_client):
        user = golden_factory()
        api_client.force_authenticate(user=user)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200

    def test_brand_post(self, brand_factory, category_factory, golden_factory, api_client):
        category = category_factory()
        user = golden_factory()
        api_client.force_authenticate(user=user)
        content = {
            'name': 'brandzz',
            'category': category.id,
        }
        response = api_client.post(self.endpoint, data=content)
        assert response.status_code == 201
