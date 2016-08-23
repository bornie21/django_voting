from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView

from polls.models import Choice,Question
from .serializers import QuestionSerializer,ChoiceSerializer

class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdate(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDelete(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreate(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceUpdate(UpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDelete(DestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceCreate(CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer