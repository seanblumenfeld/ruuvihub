import factory

from web.tests.factories.base import BaseMetaFactory
from web.users.models import User


class UserFactory(BaseMetaFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user-{n}')
    email = factory.Sequence(lambda n: f'user{n}@test.com')
