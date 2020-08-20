from django.shortcuts import render

def search_results(request):

    return render(request, 'search/resultats.html', {'title': "Page de resultats",})