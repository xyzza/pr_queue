# coding: utf-8
from django.contrib import admin
from .models import AllDevelopers, DevelopersQueue, ProductQueue

admin.site.register((AllDevelopers, DevelopersQueue, ProductQueue))
