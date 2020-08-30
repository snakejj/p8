from django.contrib.auth.models import AnonymousUser

from .. import views
from .. import forms
from django.contrib.auth.forms import AuthenticationForm

from django.test import RequestFactory
import pytest
from mixer.backend.django import mixer
from django.contrib.sessions.middleware import SessionMiddleware
pytestmark = pytest.mark.django_db


class TestLoginView:

    def test_if_login_view_is_working(self):
        mixer.blend('auth.User', username='usernametest', password='testpass321dsq8')
        data = {'username': 'usernametest', 'password': 'testpass321dsq8'}
        req = RequestFactory().post('/', data=data)
        resp = views.login(req)
        assert resp.status_code == 200, 'Should log in a user'


class TestProfileView:
    def test_if_profile_view_is_working(self):
        req = RequestFactory().get('/')
        resp = views.profile(req)
        assert resp.status_code == 200, 'Should display the profil page'


class TestSignUpView:
    # def test_if_form_in_view_sign_up_is_working(self):
    #     data = {
    #         'username':'toto',
    #         'first_name':'myfirstname',
    #         'last_name':'mylastname',
    #         'email': 'myemail@mail.com',
    #         'password1':'mypassword01',
    #         'password2':'mypassword01'
    #     }
    #
    #     form = forms.SignUpForm(data=data)
    #     assert form.is_valid() is True, 'Should be invalid if not data given'

    def test_if_view_sign_up_is_working(self):
        req = RequestFactory().get('/')
        resp = views.signup(req)
        assert resp.status_code == 200, 'Is callable by guests, with a invitation to log in to use this functionality'


