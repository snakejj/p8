from django import forms


class SearchForm(forms.Form):
    product_searched = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quel produit substituer ?'}),)
