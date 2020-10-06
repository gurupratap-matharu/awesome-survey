from django.test import TestCase
from django.urls import resolve, reverse
from surveys.models import Survey
from surveys.tests.factories import SurveyFactory
from surveys.views import SurveyList
from users.tests.factories import UserFactory


class SurveyListTests(TestCase):
    def setUp(self):
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

        self.survey_1 = SurveyFactory(author=self.user_1)
        self.survey_2 = SurveyFactory(author=self.user_1)
        self.survey_3 = SurveyFactory(author=self.user_2)

    def test_survey_list_resolves_surveylistview(self):
        view = resolve(reverse('survey_list'))
        self.assertEqual(view.func.__name__, SurveyList.as_view().__name__)

    def test_survey_list_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('survey_list'))
        no_response = self.client.get('/survey_list/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'surveys/survey_list.html')
        self.assertEqual(no_response.status_code, 404)

    def test_survey_list_works_for_logged_in_user(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse('survey_list'))
        no_response = self.client.get('/survey_list/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_list.html')
        self.assertContains(response, 'Survey')
        self.assertContains(response, self.survey_1.title)
        self.assertContains(response, self.survey_2.title)
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_survey_list_does_not_show_surveys_of_other_users(self):
        self.client.force_login(self.user_2)
        response = self.client.get(reverse('survey_list'))
        no_response = self.client.get('/survey_list/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_list.html')
        self.assertNotContains(response, self.survey_1.title)
        self.assertNotContains(response, self.survey_2.title)
        self.assertContains(response, self.survey_3.title)
        self.assertEqual(no_response.status_code, 404)


class SurveyDetailTests(TestCase):
    pass


class SurveyUpdateTests(TestCase):
    pass


class SurveyDeleteTests(TestCase):
    pass
