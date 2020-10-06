from django import forms
from django.core.mail import send_mail

from surveys.models import Question


class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = ['question_text']
