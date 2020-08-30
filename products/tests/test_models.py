import pytest
from mixer.backend.django import mixer
from mock import patch

from products.models import Product

pytestmark = pytest.mark.django_db


class TestCategory:
    def test_model(self):
        obj = mixer.blend('products.Category', pk=4)
        assert obj.pk == 4, 'Should create a Category instance'


class TestProduct:
    def test_model(self):
        obj = mixer.blend('products.Product', pk=80808080)
        assert obj.pk == 80808080, 'Should create a Product instance'


class TestProductManager:

    @pytest.fixture
    def product_fixture(self):
        product = mixer.blend('products.Product', code=11111111111111)
        return product

    def test_create_products_from_openfoodfacts(self, product_fixture):
        content_of_the_first_row_in_product_database = Product.objects.all()[0]
        assert content_of_the_first_row_in_product_database == product_fixture, 'Should save products in database'


