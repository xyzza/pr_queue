# coding: utf-8
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include, url
from .resources import product_dev_queue
from .resources import DeveloperViewSet, ProductQueueViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'developer', DeveloperViewSet)
router.register(r'product', ProductQueueViewSet)

urlpatterns = format_suffix_patterns([
    url(r'^product/(?P<pk>[0-9]+)/dev_queue/$',
        product_dev_queue,
        name='product-dev-queue'),
])