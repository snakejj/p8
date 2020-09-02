from mixer.backend.django import mixer
from django import urls
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import pytest


@pytest.mark.django_db
def test_if_login_view_is_working_with_proper_credentials(client):
    """Tests logging in and logging out"""
    # Create a fake user
    user = mixer.blend('auth.User', username='my_username')
    user.set_password('my_password123')
    user.save()

    login_url = urls.reverse('users:login')
    resp = client.post(login_url, {
        'username': 'my_username',
        'password': 'my_password123'
    })

    assert resp.status_code == 302 and resp.url == urls.reverse('core:home'), 'Should redirect to the home page'
    assert Session.objects.count() == 1, 'Should create a session for the logged in users'

@pytest.mark.django_db
def test_if_login_view_is_working_with_improper_credentials(client):
    """Tests logging in and logging out"""
    # Create a fake user
    user = mixer.blend('auth.User', username='my_username')
    user.set_password('my_password123')
    user.save()

    login_url = urls.reverse('users:login')
    resp = client.post(login_url, {
        'username': 'my_username',
        'password': 'improper_password'
    })

    assert resp.status_code == 200, 'Should refresh the page'
    assert not Session.objects.exists(), 'Should not be any session if login failed'

@pytest.mark.django_db
def test_if_logout_view_is_working(client):
    test_if_login_view_is_working_with_proper_credentials(client)
    assert Session.objects.count() == 1, 'The function called should results in a session before attempting logout'

    logout_url = urls.reverse('users:logout')
    resp = client.get(logout_url)

    # Similar to the login view, the logout view redirects to the login page
    assert resp.status_code == 302 and resp.url == urls.reverse('core:home'), 'Should redirect to the home page'
    assert not Session.objects.exists(), 'Should be no more sessions left after logging out'


def test_if_signup_view_is_working(client):
    signup_url = urls.reverse('users:signup')
    resp = client.get(signup_url)
    assert resp.status_code == 200, 'Is callable by anyone'


@pytest.mark.django_db
def test_if_signup_view_is_working_when_signing_up(client):
    signup_url = urls.reverse('users:signup')
    resp = client.post(signup_url,{
        'username': 'my_username',
        'first_name': 'firstname',
        'email': 'dsqijdsqdsq@mail.com',
        'password1': 'my_password123',
        'password2': 'my_password123'
    })

    assert resp.status_code == 302 and resp.url == urls.reverse('users:profile'), 'Should redirect to the profile page'
    assert Session.objects.count() == 1, 'Should create a session for the new logged in users'


def test_if_profile_view_is_working(client):
    profile_url = urls.reverse('users:profile')
    resp = client.get(profile_url)
    assert resp.status_code == 200, 'Is callable by anyone'




#
#
#
#
# @pytest.mark.django_db
# def test_register(client):
#     """Registers a user and verifies their last login date is correct"""
#     register_url = urls.reverse('user:register')
#     resp = client.post(register_url, {
#         'username': 'my_username',
#         'password1': 'my_password123',
#         'password2': 'my_password123'
#     })
#
#     # The registration view should redirect us to our home page
#     assert resp.status_code == 302
#     assert resp.url == urls.reverse('home')
#
#     # There should be a user with 'my_username'
#     user = User.objects.get(username='my_username')
#     # The user's last login time should be set to the current time
#     assert user.last_login == dt.datetime(2019, 1, 26, 7)
