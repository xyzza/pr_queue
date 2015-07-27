# coding: utf-8
from developers import models


def get_dev_per_products():
    """
    :return: dict. keys - products, values - set of product developers
    """
    q = models.Product.objects.filter(
        developer__is_active=True
    ).values_list('name', 'developer__name', 'developer__email')

    result = {}

    for k, dev, email in q:
        result.setdefault(k, set()).add((dev, email))
    return result


def _send_mail(dev, msg):
    """
    sends a message throw email to developer
    :dev - developer object
    : msg - text string
    :return:
    """
    print "send {0} to {1}...".format(msg, dev)


def broadcast(dev_kv):
    """
    send messages to each developer in dev_list
    :param dev_kv: - dict, key - dev, value - message to send
    :return:
    """

    for dev, msg in dev_kv.iteritems():
        _send_mail(dev, msg)