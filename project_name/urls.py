from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('{{ project_name }}.views',
    url(r'^$', 'home', name='home'),
    url(r'about.html', 'about', name='about'),
)
