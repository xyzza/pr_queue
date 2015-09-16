# coding: utf-8
from rest_framework import routers
from .resources import DeveloperViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'developer', DeveloperViewSet)