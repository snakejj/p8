from django.shortcuts import render
from favorites.models import Favorites
from products.models import Product
from django.contrib import messages
from django.db import IntegrityError


def _add_favorites(request):

    if request.POST:
        form = request.POST or None

        user = request.user.id
        product = form.get('product')
        substitute = form.get('substitute')

        try:
            Favorites.objects.create(user_id=user, product_id=product, substitute_id=substitute)
            messages.success(request, "Produit ajouté avec succès !", fail_silently=True)
        except IntegrityError:
            already_exists = True
            messages.warning(
                request,
                "Cette combinaison produit-substitut existe deja dans vos aliments!",
                fail_silently=True
            )
            return already_exists


def _return_favorites():
    return Favorites.objects.all()


def favorites(request):
    empty = False

    _add_favorites(request)

    results = _return_favorites()

    # If there are at least 1 favorites for the user, change the var empty to True
    i = 0
    for result in results:
        if result.user_id == request.user.id:
            i = 1
            break
    if i == 0:
        empty = True

    list_products = []
    list_substitutes = []

    # This loop add data to the lists only if the user is connected and has favorites
    for result in results:
        if result.user_id == request.user.id:
            product = Product.objects.filter(pk=result.product_id)[0]
            substitute = Product.objects.filter(pk=result.substitute_id)[0]
            list_products.append(product)
            list_substitutes.append(substitute)

    return render(request, 'favorites/favorites.html', {
        'title': "Mes aliments",
        'favorites': zip(list_products, list_substitutes),
        'empty': empty,
    })
