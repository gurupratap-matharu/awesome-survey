from django.test import TestCase
from django.urls import resolve, reverse
from pages.views import AboutPageView, ContactPageView, HomePageView


class HomePageTests(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('pages:home'))
        no_response = self.client.get('/homes/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertContains(response, 'Home')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_home_page_resolves_homepageview(self):
        view = resolve(reverse('pages:home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(TestCase):
    def test_about_page_works(self):
        response = self.client.get(reverse('pages:about'))
        no_response = self.client.get('/About/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
        self.assertContains(response, 'About')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_about_page_resolves_aboutpageview(self):
        view = resolve(reverse('pages:about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


class ContactPageTests(TestCase):
    def test_contact_page_works(self):
        response = self.client.get(reverse('pages:contact'))
        no_response = self.client.get('/contact-us/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')
        self.assertContains(response, 'Contact')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_contact_page_resolves_contactpageview(self):
        view = resolve(reverse('pages:contact'))
        self.assertEqual(view.func.__name__, ContactPageView.as_view().__name__)
