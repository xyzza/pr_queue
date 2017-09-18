from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class OrderedDeveloper(models.Model):
    """Always ordered by email"""

    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 2

    CategoryEnum = (
        (JUNIOR, 'junior'),
        (MIDDLE, 'middle'),
        (SENIOR, 'senior'),
    )

    email = models.EmailField("dev's email", max_length=150, primary_key=True)
    name = models.CharField("dev's name", max_length=150)
    is_active = models.BooleanField('Is active')
    category = models.SmallIntegerField(choices=CategoryEnum)

    class Meta:
        ordering = ['email']


class ActiveDeveloperManager(models.Manager):
    """Returns only active developers"""
    def get_queryset(self):
        return super(ActiveDeveloperManager, self).get_queryset().filter(
            is_active=True)


@python_2_unicode_compatible
class ActiveDeveloper(OrderedDeveloper):
    """Always only active developers"""
    objects = ActiveDeveloperManager()

    class Meta:
        proxy = True


@python_2_unicode_compatible
class Project(models.Model):

    code = models.CharField('Project code', primary_key=True, max_length=100)
    name = models.CharField('Project', max_length=200)
    developers = models.ManyToManyField(ActiveDeveloper)

    def get_developers(self):
        return self.developers.all()
