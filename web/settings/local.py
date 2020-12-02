from web.settings.base import *

DEBUG = True

ALLOWED_HOSTS += ['localhost', '0.0.0.0', '127.0.0.1']

INSTALLED_APPS += [
    'django_extensions',
]
