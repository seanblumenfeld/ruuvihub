import logging

from huey.contrib.djhuey import db_task

from web.core.exceptions import RuuvihubException
from web.ruuvitags.models import Event, StructuredEvent

logger = logging.getLogger(__name__)


@db_task()
def create_structured_event(event: Event) -> StructuredEvent:
    if not isinstance(event.data, dict):
        raise RuuvihubException(
            detail='Expected event.data to be a dict. Cannot create StructuredEvent',
            code=400
        )

    if event.data['data_format'] in StructuredEvent.DataFormat.values:
        structured_event = StructuredEvent(
            event=event,
            data_format=event.data['data_format'],
            humidity=event.data['humidity'],
            temperature=event.data['temperature'],
            pressure=event.data['pressure'],
            acceleration=event.data['acceleration'],
            acceleration_x=event.data['acceleration_x'],
            acceleration_y=event.data['acceleration_y'],
            acceleration_z=event.data['acceleration_z'],
            tx_power=event.data['tx_power'],
            battery=event.data['battery'],
            movement_counter=event.data['movement_counter'],
            measurement_sequence_number=event.data['measurement_sequence_number'],
            mac=event.data['mac']
        )
        structured_event.save()
        return structured_event

    raise RuuvihubException(
        detail=f"Unknown event format {event.data['data_format']}. Cannot create StructuredEvent",
        code=400
    )
