# coding: utf-8
from celery.utils.log import get_task_logger

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from developers.queue import send_all_assignments


logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/2')),
    name='test_apply',
    ignore_result=True,
)
def test_apply():
    logger.info("Sending assignments")
    send_all_assignments()