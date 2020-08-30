from django.shortcuts import render
from .forms import SearchForm


def home(request):
    search_form = SearchForm(request.GET)
    return render(request, 'core/pages/home.html', {'title': "Page d'acceuil", 'search_form': search_form})


def legal_notice(request):
    return render(request, 'core/pages/mentions_legales.html', {
        'title': "Mentions légales",
        'header_title': "Mentions légales"})
