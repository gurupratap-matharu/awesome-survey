import factory
from surveys.models import Survey
from users.tests.factories import UserFactory


class SurveyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Survey
    title = factory.Faker('catch_phrase')
    description = factory.Faker('text')
    author = factory.SubFactory(UserFactory)
