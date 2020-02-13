from web.settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3'
}

REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'
