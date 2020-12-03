import factory
from django.utils import timezone
from factory.django import DjangoModelFactory


class BaseMetaFactory(DjangoModelFactory):
    class Meta:
        abstract = True

    created = factory.LazyFunction(timezone.now)
    updated = factory.LazyFunction(timezone.now)
