from django.shortcuts import render
from favorites.models import Favorites
from products.models import Product
from django.contrib import messages


def favorites(request):
    empty = False
    if request.POST:
        form = request.POST or None

        user = request.user.id
        product = form.get('product')
        substitute = form.get('substitute')

        Favorites.objects.create(user_id=user, product_id=product, substitute_id=substitute)
        messages.success(request, "Produit ajouté avec succès !")

    results = Favorites.objects.all()

    # This is in case there are no favorites yet
    try :
        i=0
        for result in results:
            if result.user_id == request.user.id:
                i=1
                break
        if i == 0:
            empty = True
    except IndexError:
        empty = True

    list_products = []
    list_substitutes = []

    for result in results:
        if result.user_id == request.user.id:
            product = Product.objects.filter(pk=result.product_id)[0]
            substitute = Product.objects.filter(pk=result.substitute_id)[0]
            list_products.append(product)
            list_substitutes.append(substitute)

    return render(request, 'favorites/favorites.html', {
        'title': "Mes aliments",
        'favorites': zip(list_products,list_substitutes),
        'empty': empty,
    })
