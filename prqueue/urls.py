# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from .rest import rest_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += rest_urls