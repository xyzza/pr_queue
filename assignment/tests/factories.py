import factory
from ..models import OrderedDeveloper


class DeveloperFactory(factory.DjangoModelFactory):
    class Meta:
        model = OrderedDeveloper

    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    name = factory.Faker('first_name')
    is_active = True
    category = OrderedDeveloper.JUNIOR


class NotActiveDeveloperFactory(DeveloperFactory):

    is_active = False


class JuniorDeveloperFactory(DeveloperFactory):

    category = OrderedDeveloper.JUNIOR


class MiddleDeveloperFactory(DeveloperFactory):

    category = OrderedDeveloper.MIDDLE
