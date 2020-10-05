from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from surveys.models import Survey


class SurveyList(ListView):
    model = Survey
    template_name = 'surveys/survey_list.html'


class SurveyDetail(DetailView):
    model = Survey
    template_name = 'surveys/survey_detail.html'


class SurveyCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Survey
    fields = ('title', 'description')
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
    success_message = '%s(title) deleted successfully!'
