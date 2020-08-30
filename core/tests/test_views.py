from .. import views

from django.test import RequestFactory
import pytest
pytestmark = pytest.mark.django_db


class TestCoreView:
    def test_if_home_view_is_working(self):
        req = RequestFactory().get('/')
        resp = views.home(req)
        assert resp.status_code == 200, 'Is callable by anyone'

    def test_if_legal_notice_view_is_working(self):
        req = RequestFactory().get('/')
        resp = views.legal_notice(req)
        assert resp.status_code == 200, 'Is callable by anyone'


