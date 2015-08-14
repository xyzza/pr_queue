# coding: utf-8
from collections import defaultdict

from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from django.conf import settings

from developers.queue import send_all_assignments


logger = get_task_logger(__name__)


# TODO: make this time configurable
_schedule = defaultdict(hour=5, minute=42, day_of_week=[1, 2, 3, 4, 5])
if settings.DEBUG:
    _schedule = defaultdict(minute='*/2')

@periodic_task(
    run_every=(crontab(**_schedule)),
    name='apply_assignments',
    ignore_result=True,
)
def apply_assignments():
    logger.info("Sending all assignments")
    send_all_assignments()