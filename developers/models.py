#coding: utf-8
from django.db import models


class Developer(models.Model):
    """
    Represent developer, who manage pull requests
    """
    name = models.CharField(u"dev's name", max_length=150)
    email = models.EmailField(u"dev's email", max_length=150)
    is_active = models.BooleanField(u'Is active')
    on_duty = models.BooleanField(u'Developer can be chosen to reviewers',
                                  default=False, editable=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u"{0} ({1}) can be chosen ({2})".format(self.name,
                                                       self.email,
                                                       self.on_duty)


class Product(models.Model):
    """
    # TODO: Rename class to "DeveloperQueue"
    Group of developers united by some reason
    Chunk of ordered developers. They rotating one by one
    """
    _current = models.SmallIntegerField(u'current developers index',
                                        default=0, editable=False)
    name = models.CharField(u'DeveloperQueue name', max_length=100)
    developer = models.ManyToManyField(u'Developer')

    def current(self):
        return self.developer.all()[self._current]

    def append(self, dev):
        assert self.id, u'queue must be saved before adding a developers'
        self.developer.add(dev)
        return self.developer.all()

    def next(self):
        """
        Return index of next developer in queue
        :return: int
        """
        self._current += 1
        # TODO: optimization - cut sql query from method
        _curr_count = self.developer.all().count()
        if self._current == _curr_count:
            self._current = 0
        assert self._current < _curr_count
        return self._current

    def set_current(self, current):
        """
        Set given index as current developer index
        :param current: int
        :return: None
        """
        self._current = current
        self.save()

    def __unicode__(self):
        return self.name


class ProductQueue(models.Model):
    """
    Group of DeveloperQueue
    """

    name = models.CharField(u'Product queue', max_length=255)
    dev_queue = models.ManyToManyField(Product)

    def all_developers(self):
        return self.dev_queue.all().values_list(
            'developer', flat=True).distinct()

    def __unicode__(self):
        return self.name