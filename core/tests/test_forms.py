from .. import forms


class TestSearchForm:
    def test_form(self):
        form = forms.SearchForm(data={'product_searched':''})
        assert form.is_valid() is False, 'Should be invalid if not data given'

        form = forms.SearchForm(data={'product_searched': 'Nutella'})
        assert form.is_valid(), 'Should be valid'
