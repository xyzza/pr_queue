from django.test import TestCase
from ..models import Project, OrderedDeveloper, ActiveDeveloper
from .factories import (
    JuniorDeveloperFactory,
    MiddleDeveloperFactory,
    NotActiveDeveloperFactory)


def get_all_developers():
    """
    Return a ordered list of Developers

    :return: Developer QuerySet
    """
    developers = OrderedDeveloper.objects.all()
    return developers


def get_developers_on_a_project(project):
    """
    Return a list of developers, that work on project

    :param project: project_id of a Project model
    :return: Developer QuerySet
    """
    project = Project.objects.get(pk=project)
    developers = project.developers.all()
    return developers


def get_developers_in_a_category(category, developers_queryset=None):
    """
    Return a list of developers, in a category

    :param category: CategoryEnum value
    :param developers_queryset: Developer QuerySet
    :return: Developer QuerySet
    """

    if developers_queryset is None:
        developers_queryset = ActiveDeveloper.objects.all()

    developers = developers_queryset.filter(category=category)

    return developers


def get_developers_in_action(workday):
    """
    Return a list of developers, that available for work on a date

    :param workday: date
    :return: a list of developer_id's of Developer model
    """
    developers = ActiveDeveloper.objects.all()

    return developers


class AssignmentTest(TestCase):

    def setUp(self):
        self.not_active_developers = NotActiveDeveloperFactory.create_batch(10)
        self.junior_developers = JuniorDeveloperFactory.create_batch(4)
        self.middle_developers = MiddleDeveloperFactory.create_batch(2)
        self.active_developers = self.junior_developers + self.middle_developers
        self.all_developers = self.active_developers + self.not_active_developers

    def test_get_all_developers(self):
        developers = get_all_developers()
        self.assertEqual(len(self.all_developers), len(developers))

    def test_get_developers_on_a_project(self):
        pass

    def test_get_developers_in_a_category(self):
        juniors = get_developers_in_a_category(OrderedDeveloper.JUNIOR)
        self.assertEqual(len(self.junior_developers), len(juniors))
        middle = get_developers_in_a_category(OrderedDeveloper.MIDDLE)
        self.assertEqual(len(self.middle_developers), len(middle))

    def test_get_developers_in_action(self):
        pass
