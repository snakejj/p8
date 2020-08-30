from .. import views

from django.test import RequestFactory
import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestProductView:
    def test_if_view_product_details_is_working(self):
        obj = mixer.blend('products.Product', code=80808080)
        req = RequestFactory().get('/', data={'code':80808080})
        resp = views.product_details(req)
        assert resp.status_code == 200, 'Is callable by anyone'


