# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from .rest import router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]