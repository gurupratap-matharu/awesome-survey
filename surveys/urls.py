from django.urls import path

from surveys.views import (SurveyCreate, SurveyDelete, SurveyDetail,
                           SurveyList, SurveyUpdate)

urlpatterns = [
    path('', SurveyList.as_view(), name='survey_list'),
    path('create/', SurveyCreate.as_view(), name='survey_create'),
    path('<uuid:pk>/', SurveyDetail.as_view(), name='survey_detail'),
    path('<uuid:pk>/update/', SurveyUpdate.as_view(), name='survey_update'),
    path('<uuid:pk>/delete/', SurveyDelete.as_view(), name='survey_delete'),
]
