from django.test import TestCase


def get_all_developers():
    """
    Return a list of all developers with no exclusions

    :return: a list of developer_id's of Developer model
    """
    return [1, ]


def get_developers_on_a_project(project):
    """
    Return a list of developers, that work on project

    :param project: project_id of a Project model
    :return: a list of developer_id's of Developer model
    """

    # perform a request to data storage

    return [1, ]


def get_developers_in_a_category(category):
    """
    Return a list of developers, in a category

    :param category: CategoryEnum value
    :return: a list of developer_id's of Developer model
    """
    return [1, ]


def get_developers_in_action(workday):
    """
    Return a list of developers, that available for work on a date

    :param workday: date
    :return: a list of developer_id's of Developer model
    """
    return [1, ]


class AssignmentTest(TestCase):

    def setUp(self):
        pass

    def test_get_all_developers(self):
        pass

    def test_get_developers_on_a_project(self):
        pass

    def test_get_developers_in_a_category(self):
        pass

    def test_get_developers_in_action(self):
        pass
