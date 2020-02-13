from django.db import models


class UpdatedCreatedMetaModel(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True
