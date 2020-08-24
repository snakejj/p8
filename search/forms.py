from django import forms


class FavoritesForm(forms.Form):
    product = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quel produit substituer ?'}),)