# coding: utf-8
from .models import ProductQueue
from .utils import send_mail


def get_products_queues():
    return ProductQueue.objects.all()


def get_dev_assignments(dev, job):
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


def increase_duty_counter(job):
    for dev_q in job.dev_queue.all():
        dev_q.set_current_by_offset(1)


def process_product(product_queue):
    """
    :param product_queue: ProductQueue object
    """

    for dev in product_queue.receivers.all():
        assignment = get_dev_assignments(dev, product_queue)
        send_mail(dev.email, assignment)
    increase_duty_counter(product_queue)


def send_all_assignments():
    """
    Main entry point.
    Initiate process of assigning and sending messages.
    """
    all_product_queues = get_products_queues()
    for product_queue in all_product_queues:
        process_product(product_queue)