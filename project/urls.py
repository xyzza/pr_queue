from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from rest.urls import urlpatterns as rest_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += rest_urls
