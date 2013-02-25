from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def collections(request):
    return render(request, 'collections.html')

def category(request):
    return render(request, 'product/category.html')

def products(request):
    return render(request, 'product/products.html')

def product_detail(request):
    return render(request, 'product/product-detail.html')

def shopping_bag(request):
    return render(request, 'checkout/shopping-bag.html')

