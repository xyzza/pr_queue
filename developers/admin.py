# coding: utf-8
from django.contrib import admin
from .models import Developer, Product

admin.site.register((Developer, Product))
