import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import CategoryFactory, BrandFactory, ProductFactory, RegularFactory, GoldenFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(RegularFactory)
register(GoldenFactory)

@pytest.fixture
def api_client():
    return APIClient()