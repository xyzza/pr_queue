from __future__ import unicode_literals
from django.contrib import admin
from .models import AllDevelopers, DevelopersQueue, ProductQueue

admin.site.register((AllDevelopers, DevelopersQueue, ProductQueue))
