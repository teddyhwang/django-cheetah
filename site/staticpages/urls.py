from django.conf.urls.defaults import *


urlpatterns = patterns('staticpages.views',
    url(r'^$', 'home', name='home'),
    url(r'collections.html', 'collections', name='collections'),
    url(r'category.html', 'category', name='category'),
    url(r'products.html', 'products', name='products'),
    url(r'product-detail.html', 'product_detail', name='product-detail'),
    url(r'shopping-bag.html', 'shopping_bag', name='shopping-bag'),
)
