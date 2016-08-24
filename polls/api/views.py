from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from polls.models import Choice,Question
from .serializers import QuestionSerializer,ChoiceSerializer


class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreate(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceCreate(CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

