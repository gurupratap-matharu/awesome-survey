from django import forms
from django.forms import inlineformset_factory

from surveys.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', ]
