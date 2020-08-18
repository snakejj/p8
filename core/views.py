from django.shortcuts import render


def home(request):

    return render(request, 'pages/home.html', {'title': "Page d'acceuil",})