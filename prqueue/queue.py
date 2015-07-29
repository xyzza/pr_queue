# coding: utf-8
from developers.models import ProductQueue, Developer


def get_all_jobs():
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
        assigned_officers.append(u"developer {} from queue {}".format(
            duty_officer.__unicode__(),
            dev_q.name
        ))
    return u''.join(assigned_officers)


def increase_duty_counter(job):
    for dev_q in job.dev_queue.all():
        dev_q.set_current_by_offset(1)


def apply_assignment(dev, assignment):
    print u"Developer == {} == \nGet the assignment {}".format(dev, assignment)


def process_job(job):
    """
    Process current job
    :param job:
    :return:
    """

    for dev in job.receivers.all():
        assignment = get_dev_assignments(dev, job)
        apply_assignment(dev, assignment)
    increase_duty_counter(job)


def process_all():
    """
    main task, thaw will be executed async
    """
    all_jobs = get_all_jobs()
    for job in all_jobs:
        process_job(job)