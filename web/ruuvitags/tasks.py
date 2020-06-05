import logging

from huey import crontab
from huey.contrib.djhuey import periodic_task

from web.ruuvitags.models import Event

logger = logging.getLogger(__name__)


@periodic_task(crontab(minute='30'))
def free_up_db_space():
    logger.info('START: free_up_db_space')
    rows_to_keep = 9000
    if Event.objects.count() < rows_to_keep:
        logger.info('END: free_up_db_space')
        return

    delete_older_than = Event.objects.all().order_by('-created')[rows_to_keep - 1].created
    events_to_delete = Event.objects.filter(created__lte=delete_older_than)
    logger.info(
        f'Deleting {events_to_delete.count()} events older than {delete_older_than}.'
    )
    events_to_delete.delete()
    logger.info('END: free_up_db_space')
