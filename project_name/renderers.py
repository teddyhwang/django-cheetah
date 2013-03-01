from django_medusa.renderers import StaticSiteRenderer

class StaticPagesRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            '/',
            '/about.html',
        ])

renderers = [
    StaticPagesRenderer,
]
