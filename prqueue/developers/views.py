# coding: utf-8
from django.http import JsonResponse
from .queue import send_assignments


def send_assignment(request, product_id):
    """
    send assignments only for chosen product
    :param request:
    :param product_id: Product object id
    :return: operation result
    """
    send_assignments((product_id, ))
    return JsonResponse({'success': 'true'})
