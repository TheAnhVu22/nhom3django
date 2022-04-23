from django.shortcuts import render
from product.models import Product

# Create your views here.

def frontpage(request):
    newest_products = Product.objects.order_by('id')[0:8]
    hot_product = Product.objects.all()[0:8]
    context = {
        'newest_products': newest_products,
        'hot_product': hot_product,
    }
    return render(request, 'core/frontpage.html', context)


def contactpage(request):
    return render(request, 'core/contact.html')