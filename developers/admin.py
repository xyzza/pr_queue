# coding: utf-8
from django.contrib import admin
from .models import Developer, Product, ProductQueue

admin.site.register((Developer, Product, ProductQueue))
