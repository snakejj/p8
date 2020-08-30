from django.contrib.auth.models import AnonymousUser

from .. import views

from django.test import RequestFactory
import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestSearchView:
    def test_if_view_search_results_is_displaying_results_when_search_find_a_result(self):
        objproduct = mixer.blend('products.Product', product_name="Nutella", nutrition_grade_fr="e", category_id=2)
        obj_better_product =mixer.blend('products.Product', product_name="Nuts", nutrition_grade_fr="d", category_id=2)
        get = {"product_searched": "nute"}
        req = RequestFactory().get('/', data=get)
        resp = views.search_results(req)
        assert resp.status_code == 200 , 'Should displays results'

    def test_if_view_search_results_is_working_when_search_term_gives_no_results(self):
        obj = mixer.blend('products.Product', product_name="Nutella")
        get = {"product_searched": "pringles"}
        req = RequestFactory().get('/', data=get)
        resp = views.search_results(req)
        assert resp.status_code == 200 , 'Should displays results page with a message saying "no results founds"'

    def test_if_view_search_results_is_working_even_without_search(self):
        req = RequestFactory().get('/')
        resp = views.search_results(req)
        assert resp.status_code == 200, 'Should displays results page with an invitation to use the search form'
