# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin

from .rest import rest_urls
from .developers import send_assignment


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^send_assignment/(?P<product_id>[0-9]+)/$', send_assignment)
]

urlpatterns += rest_urls