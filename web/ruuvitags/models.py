import json

from django.core.exceptions import ValidationError
from django.db import models

from web.common.abstract_models import UpdatedCreatedMetaModel


def is_json_deserializable(value):
    try:
        json.loads(value)
    except json.decoder.JSONDecodeError as e:
        raise ValidationError(e.args)


class Events(UpdatedCreatedMetaModel):
    data = models.TextField(blank=False, null=False, validators=[is_json_deserializable])
