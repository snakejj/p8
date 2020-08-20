from django import forms


class SearchForm(forms.Form):
    productsearched = forms.CharField(label="")