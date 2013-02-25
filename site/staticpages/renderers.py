from django_medusa.renderers import StaticSiteRenderer

class StaticPagesRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            '/',
            '/collections.html',
            '/category.html',
            '/products.html',
            '/product-detail.html',
            '/shopping-bag.html',
        ])

renderers = [
    StaticPagesRenderer,
]
