from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, TemplateView

from pages.forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ContactPageView(SuccessMessageMixin, FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_message = 'Thanks! We have received your message!'
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class AboutPageView(SuccessMessageMixin, FormView):
    template_name = 'pages/about.html'
    form_class = ContactForm
    success_message = 'Thanks! We have received your message!'
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class IndexPageView(TemplateView):
    template_name = 'pages/index.html'
