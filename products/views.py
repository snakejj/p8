from django.shortcuts import render
from products.models import Product


def product_details(request):
    product = Product.objects.filter(pk=request.GET.get("code"))[0]
    print(product)

    return render(request, 'products/product.html', {
        'product': product,
    })
