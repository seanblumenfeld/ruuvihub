import factory
from django.utils import timezone


class BaseMetaFactory(factory.DjangoModelFactory):
    class Meta:
        abstract = True

    created = factory.LazyFunction(timezone.now)
    updated = factory.LazyFunction(timezone.now)
