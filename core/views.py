from django.shortcuts import render


def home(request):

    return render(request, 'core/pages/home.html', {'title': "Page d'acceuil",})


def legal_notice(request):

    return render(request, 'core/pages/mentions_legales.html', {
        'title': "Mentions légales",
        'header_title': "Mentions légales",})
