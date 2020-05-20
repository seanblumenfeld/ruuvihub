from django.contrib.auth.models import AbstractUser

from web.core.abstract_models import BaseMetaModel


class User(BaseMetaModel, AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    @property
    def owner(self):
        return self
