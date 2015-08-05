# coding: utf-8
from django.db import models


class ActiveDeveloperManager(models.Manager):
    """
    Exclude all non active developers from all query
    """
    def get_queryset(self):
        return super(ActiveDeveloperManager, self).get_queryset().filter(
            is_active=True)


class Developer(models.Model):
    """
    Represent developer, who manage pull requests
    """
    # we need only active developers
    objects = ActiveDeveloperManager()

    name = models.CharField(u"dev's name", max_length=150)
    email = models.EmailField(u"dev's email", max_length=150)
    is_active = models.BooleanField(u'Is active')

    class Meta:
        # Ordering is matter for get_by_offset functions
        # you shouldn't change it
        ordering = ['name']

    def __unicode__(self):
        return u"{} ({}) active:{}".format(self.name, self.email,
                                           self.is_active)


class AllDevelopers(Developer):

    all_objects = models.Manager()

    class Meta:
        proxy = True

class DevelopersQueue(models.Model):
    """
    Group of developers united by some reason
    Chunk of ordered developers. They rotating one by one
    """
    _current = models.SmallIntegerField(u'current developers index',
                                        default=0, editable=False)
    name = models.CharField(u'DevelopersQueue name', max_length=100)
    developer = models.ManyToManyField(u'Developer')

    def get_dev_by_offset(self, offset):
        """
        If offset is 0 - return current developer in queue
        If offset is 1 - return next developer in queue
        :param offset: positive int
        :return: Developer object
        """
        assert offset >= 0
        _index = self._current + offset
        if _index < self.developer.count():
            return self.developer.all()[_index]

        return self.developer.all()[0]

    def set_current_by_offset(self, offset):
        """
        :param offset: int
        :return: None
        """
        assert offset is 1
        _new_current = self._current + offset
        if _new_current > self.developer.count() - 1:
            _new_current = 0
        self._current = _new_current
        self.save()

    def __unicode__(self):
        return self.name


class ProductQueue(models.Model):
    """
    Group of DeveloperQueue
    """

    name = models.CharField(u'Product queue', max_length=255)
    dev_queue = models.ManyToManyField(DevelopersQueue)
    receivers = models.ManyToManyField(Developer)

    def __unicode__(self):
        return self.name