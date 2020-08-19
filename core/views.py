from django.shortcuts import render


def home(request):

    return render(request, 'pages/home.html', {'title': "Page d'acceuil",})


def legal_notice(request):

    return render(request, 'pages/mentions_legales.html', {'title': "Mentions légales",})
