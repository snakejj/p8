from .. import forms


class TestFavoritesForm:
    def test_form(self):
        form = forms.FavoritesForm(data={'product': ''})
        assert form.is_valid() is False, 'Should be invalid if not data given'

        form = forms.FavoritesForm(data={'product': 'Nutella'})
        assert form.is_valid(), 'Should be valid'
