import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import FormMixin

from surveys.forms import QuestionForm
from surveys.models import Survey

logger = logging.getLogger(__name__)


class SurveyList(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'surveys/survey_list.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class SurveyDetail(FormMixin, DetailView):
    model = Survey
    form_class = QuestionForm
    context_object_name = 'survey'
    template_name = 'surveys/survey_detail.html'
    success_message = 'Question successfully added!'

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def form_valid(self, form):
        form.instance.survey = self.get_object()
        form.save()
        messages.success(self.request, self.success_message)
        logger.info('saved question with form... %s', form)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SurveyCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Survey
    fields = ('title', 'description',)
    template_name = 'surveys/survey_form.html'
    success_message = '%(title)s created successfully!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SurveyUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Survey
    template_name = 'surveys/survey_update_form.html'
    success_message = '%(title)s updated successfully!'


class SurveyDelete(LoginRequiredMixin, DeleteView):
    model = Survey
    template_name = 'surveys/survey_confirm_delete.html'
    success_message = 'Survey deleted successfully!'
    success_url = reverse_lazy('pages:home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
