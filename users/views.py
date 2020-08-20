from django.shortcuts import render


def profile(request):

    return render(request, 'users/profil.html', {'title': "Page de profil",})

