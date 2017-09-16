from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class ActiveDeveloperManager(models.Manager):
    """
    Exclude all non active developers from all query
    """
    def get_queryset(self):
        return super(ActiveDeveloperManager, self).get_queryset().filter(
            is_active=True)


@python_2_unicode_compatible
class Developer(models.Model):
    """
    Represent developer, who manage pull requests
    """
    # we need only active developers
    objects = ActiveDeveloperManager()

    name = models.CharField("dev's name", max_length=150)
    email = models.EmailField("dev's email", max_length=150)
    is_active = models.BooleanField('Is active')

    class Meta:
        # Ordering is matter for get_by_offset functions
        # you shouldn't change it
        ordering = ['name']

    @property
    def full_name(self):
        return "{} ({})".format(self.name, self.email)

    def __str__(self):
        return "{} active:{}".format(self.full_name, self.is_active)


class AllDevelopers(Developer):

    all_objects = models.Manager()

    class Meta:
        proxy = True


@python_2_unicode_compatible
class DevelopersQueue(models.Model):
    """
    Group of developers united by some reason
    Chunk of ordered developers. They rotating one by one
    """
    _current = models.SmallIntegerField('current developers index',
                                        default=0, editable=False)
    name = models.CharField('DevelopersQueue name', max_length=100)
    developer = models.ManyToManyField('Developer')

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

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProductQueue(models.Model):
    """
    Group of DeveloperQueue
    """

    name = models.CharField('Product queue', max_length=255)
    dev_queue = models.ManyToManyField(DevelopersQueue)
    receivers = models.ManyToManyField(Developer)

    def __str__(self):
        return self.name
