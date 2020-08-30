import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestFavorites:
    def test_model(self):
        obj = mixer.blend('favorites.Favorites')
        assert obj.substitute is not None, 'Should create a Favorites instance'
