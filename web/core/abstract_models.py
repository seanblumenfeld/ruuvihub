from uuid import uuid4

from django.db import models
from django.utils import timezone


class BaseMetaModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(editable=False, default=timezone.now)

    @property
    def id_str(self):
        return str(self.id)

    class Meta:
        abstract = True
