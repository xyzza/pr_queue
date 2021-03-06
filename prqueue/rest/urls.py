# coding: utf-8
from django.conf.urls import include, url
from rest_framework import routers

from .resources import (DeveloperViewSet,
                        ProductQueueViewSet, DevelopersQueueViewSet)


router = routers.DefaultRouter()
router.register(r'developer', DeveloperViewSet)
router.register(r'dev-queue', DevelopersQueueViewSet)
router.register(r'product', ProductQueueViewSet)


urlpatterns = ([
    url(r'^', include(router.urls)),
])
