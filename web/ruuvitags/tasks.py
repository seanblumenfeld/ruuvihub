import logging

from django.utils import timezone
from huey import crontab
from huey.contrib.djhuey import periodic_task

from web.ruuvitags.models import Event

logger = logging.getLogger(__name__)


@periodic_task(crontab(minute='0', hour='16'))
def free_up_db_space():
    logger.info('START: free_up_db_space')

    max_rows_to_delete = 1000
    dont_delete_newer_than_datetime = timezone.now() - timezone.timedelta(days=4)
    total_objects = Event.objects.count()

    if total_objects < 1:
        logger.info('END: free_up_db_space')
        return

    rows_to_delete = min(total_objects - 1, max_rows_to_delete)
    delete_older_than_datetime = min(
        Event.objects.all().order_by('created')[rows_to_delete].created,
        dont_delete_newer_than_datetime
    )

    events_to_delete = Event.objects.filter(created__lte=delete_older_than_datetime)

    logger.info(
        f'Deleting {events_to_delete.count()} events older than {delete_older_than_datetime}.'
    )
    events_to_delete.delete()

    logger.info('END: free_up_db_space')
