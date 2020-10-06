import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='surveys')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('survey_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('survey_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('survey_delete', args=[str(self.id)])

    def get_link(self):
        return self.get_absolute_url()

    def can_update(self, user):
        return user.is_superuser or self.author == user

    def can_delete(self, user):
        return user.is_superuser or self.author == user


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.CharField(max_length=200)

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
