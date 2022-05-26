from django.urls import path
from myapp.api.viewsets import QuestionDetailAPIView, QuestionListAPIView, ChioceDetailAPIView, ChoiceListAPIView

urlpatterns = [
    path('question-list', QuestionListAPIView.as_view(), name='question_list'),
    path('question-detail/<int:pk>', QuestionDetailAPIView.as_view(), name='question_detail'),
    path('choice-list', ChoiceListAPIView.as_view(), name='choice_list'),
    path('choice-detail/<int:pk>', ChioceDetailAPIView.as_view(), name='choice_detail'),
]