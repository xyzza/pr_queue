#coding: utf-8
from django.db import models


class Developer(models.Model):
    """
    Represent developer, who manage pull requests
    """
    name = models.CharField(u"dev's name", max_length=150)
    email = models.EmailField(u"dev's email", max_length=150)
    is_active = models.BooleanField(u'Is active')
    on_duty = models.BooleanField(u'Developer is busy',
                                  default=False, editable=False)

    def __unicode__(self):
        return u"{0} ({1})".format(self.name, self.email)


class Product(models.Model):
    """
    Represent a software product, or some module or unit of responsibility
    """
    name = models.CharField(u'Product name', max_length=100)
    developer = models.ManyToManyField('Developer')

    def __unicode__(self):
        return self.name