from django.shortcuts import render
from products.models import Product


def product_details(request):
    code = request.GET.get("code")
    product = Product.objects.filter(pk=code)[0]

    return render(request, 'products/product.html', {
        'product': product,
    })
