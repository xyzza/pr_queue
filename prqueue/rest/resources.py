# coding: utf-8
from rest_framework import viewsets
# app imports
from prqueue.developers.models import AllDevelopers, ProductQueue, DevelopersQueue
from .serializers import (DeveloperSerializer, ProductQueueSerializer,
                          DevelopersQueueSerializer)


class DeveloperViewSet(viewsets.ModelViewSet):

    queryset = AllDevelopers.all_objects.all()
    serializer_class = DeveloperSerializer


class DevelopersQueueViewSet(viewsets.ModelViewSet):

    queryset = DevelopersQueue.objects.all()
    serializer_class = DevelopersQueueSerializer


class ProductQueueViewSet(viewsets.ModelViewSet):

    queryset = ProductQueue.objects.all()
    serializer_class = ProductQueueSerializer