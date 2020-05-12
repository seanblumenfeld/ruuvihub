from web.settings.base import *

ALLOWED_HOSTS += [os.environ['DOMAIN']]
