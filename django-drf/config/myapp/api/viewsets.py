from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView)
from myapp.models import Question, Choice
from .serializer import QuestionSerializer, ChoiceSerializer
# from .permissions import IsOwnerOrReadOnly


# List Views
class QuestionListAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceListAPIView(ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


# Detail Views
class QuestionDetailAPIView(RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer   
    # permission_classes = (IsOwnerOrReadOnly,)


class ChioceDetailAPIView(RetrieveUpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer  
    # permission_classes = (IsOwnerOrReadOnly,) 