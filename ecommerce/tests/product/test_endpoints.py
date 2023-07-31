import json
import pytest

pytestmark = pytest.mark.django_db

class TestCategoryApi:
    endpoint = '/api/category/'
    
    def test_category_status(self, category_factory, api_client):
        category_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

    def test_category_post(self, category_factory, api_client):
        content = {
            'name': 'boaaacategory1'
        }
        response = api_client().post(self.endpoint, data=content)
        assert response.status_code == 201

class TestBrandApi:
    endpoint = '/api/brand/'

    def test_brand_status(self, brand_factory, api_client):
        brand_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

    def test_brand_post(self, brand_factory, api_client):
        content = {
            'name': 'brandzz',
        }
        response = api_client().post(self.endpoint, data=content)
        print('gon')
        print(response.content)
        assert response.status_code == 201
