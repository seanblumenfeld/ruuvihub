import logging

from django.contrib.admin import models as admin_models
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from web.ruuvitags.models import Event

logger = logging.getLogger(__name__)


def purge_old_events(rows_to_keep=8000):
    if Event.objects.count() < rows_to_keep:
        return

    delete_older_than = Event.objects.all().order_by('-created')[rows_to_keep - 1].created
    rows_to_delete = Event.objects.filter(created__lte=delete_older_than)
    logger.info(
        f'Deleting {rows_to_delete.count()} events older than {delete_older_than}.'
    )
    rows_to_delete.delete()


def purge_old_admin_logs(rows_to_keep=1000):
    if admin_models.LogEntry.objects.count() < rows_to_keep:
        return

    delete_older_than = admin_models.LogEntry.objects.all().order_by(
        '-action_time')[rows_to_keep - 1].action_time
    rows_to_delete = admin_models.LogEntry.objects.filter(action_time__lte=delete_older_than)
    logger.info(
        f'Deleting {rows_to_delete.count()} logs older than {delete_older_than}.'
    )
    rows_to_delete.delete()


@db_periodic_task(crontab(minute='0', hour='8'))
def free_up_db_space():
    logger.info('START: free_up_db_space')
    purge_old_events()
    purge_old_admin_logs()
    logger.info('END: free_up_db_space')
