from django import forms


class SearchForm(forms.Form):
    product_searched = forms.CharField(label="produit a chercher")