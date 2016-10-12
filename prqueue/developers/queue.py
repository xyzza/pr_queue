# coding: utf-8
from .models import ProductQueue
from .utils import send_mail


def _get_dev_assignments(dev, job):
    assigned_officers = []
    for dev_q in job.dev_queue.all():
        # try to get current duty officer from the developers queue
        duty_officer = dev_q.get_dev_by_offset(0)
        if duty_officer == dev:
            # recipient equals to duty_officer, try to get next
            duty_officer = dev_q.get_dev_by_offset(1)
            # if he the only one in that queue we will take him
        assigned_officers.append(u"{}".format(duty_officer.full_name))
    return u"Hello, {}!\n It's [{}] on duty in [{}]".format(
        dev.full_name, u' '.join(assigned_officers), job.name)


def _increase_duty_counter(job):
    for dev_q in job.dev_queue.all():
        dev_q.set_current_by_offset(1)


def _process_product(product_queue):
    """
    :param product_queue: ProductQueue object
    """
    for dev in product_queue.receivers.all():
        assignment = _get_dev_assignments(dev, product_queue)
        send_mail(dev.email, assignment, product_queue.name)
    _increase_duty_counter(product_queue)


def send_assignments(product_ids=None):
    """
    Main entry point.
    Send assignments for all products or only for chosen products
    :param product_ids: tuple of product ids - optional
    """
    product_queues = ProductQueue.objects.all()
    if product_ids:
        product_queues = product_queues.filter(pk__in=product_ids)
    for product_queue in product_queues:
        _process_product(product_queue)