# Django settings for ecommerce project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1', )

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/ugc-media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'www', 'media')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, '..', 'media'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l+gd#))e1_ckdy(nhy3*m6xfqsx0yq+0=+ht(ungc01zxod5(t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ecommerce.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ecommerce.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '..', 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_medusa',
    'pipeline',
    'require',
    'staticpages',
    'ecommerce',
)

from ecommerce.settings_pipeline import *

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

# Combine require storage and pipeline storage
STATICFILES_STORAGE = 'staticpages.storage.RequirePipelineStorage'
# STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
# STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

# The baseUrl to pass to the r.js optimizer.
REQUIRE_BASE_URL = 'js'

# The name of a build profile to use for your project, relative to REQUIRE_BASE_URL.
# A sensible value would be 'app.build.js'. Leave blank to use the built-in default build profile.
REQUIRE_BUILD_PROFILE = 'build/build.js'

# The name of the require.js script used by your project, relative to REQUIRE_BASE_URL.
REQUIRE_JS = '../lib/requirejs/require.js'

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {
    'config/homepage': {
        'out': '../compiled/js/homepage.min.js',
        'build_profile': 'build/homepage.js',
    },
}

# Whether to run django-require in debug mode.
REQUIRE_DEBUG = DEBUG

# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: node or rhino.
REQUIRE_ENVIRONMENT = "node"

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"

MEDUSA_DEPLOY_DIR = os.path.join(PROJECT_PATH, '..', 'www')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}