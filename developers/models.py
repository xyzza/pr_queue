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
        return u"{0} ({1})".format(self.name, self.email)


class Product(models.Model):
    """
    # TODO: Rename class to "DeveloperQueue"
    Group of developers united by some reason
    Chunk of ordered developers. They rotating one by one
    """
    _current = models.SmallIntegerField(u'current developers index',
                                        default=0, editable=True)
    name = models.CharField(u'DeveloperQueue name', max_length=100)
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
    dev_queue = models.ManyToManyField(Product)
    receivers = models.ManyToManyField(Developer)

    def __unicode__(self):
        return self.name