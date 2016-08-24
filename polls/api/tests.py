from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from polls.models import Question,Choice
import datetime
from django.utils import timezone
from .serializers import QuestionSerializer,ChoiceSerializer

class QuestionCreateTest(APITestCase):
    def test_create_question(self):
        """
        Ensure we can create a new Question object.
        """
        url = reverse('create_question')
        data = {'question_text': 'Favourite meal?','pub_date': timezone.now()}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.get().question_text, 'Favourite meal?')


class QuestionReadDeleteTest(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text="Favourite Football team?",pub_date= timezone.now())
        # self.data = {'question_text': 'Favourite meal?','pub_date': timezone.now()}

    def test_read_question_detail(self):
        response = self.client.get(reverse('question_detail', args=[self.question.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_question_list(self):
        response = self.client.get(reverse('question_index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_question(self):
        response = self.client.delete(reverse('question_detail',args=[self.question.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class QuestionUpdateTest(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text="Favourite Basketball team?",pub_date= timezone.now())
        self.data = QuestionSerializer(self.question).data
        self.data.update({'question_text': 'Changed Question'})

    def test_update_question(self):
        response = self.client.put(reverse('question_detail', args=[self.question.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ChoiceCreateTest(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text="Favourite Football player?",pub_date= timezone.now())
        # self.data = {'question_text': 'Favourite meal?','pub_date': timezone.now()}

    def test_create_choice(self):
        """
        Ensure we can create a new Choice object.
        """
        url = reverse('create_choice')
        data = {'question': self.question.id, 'choice_text' :'Cristiano Ronaldo','votes': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Choice.objects.get().choice_text, 'Cristiano Ronaldo')


class ChoiceReadDeleteTest(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text="Favourite Football player?",pub_date= timezone.now())
        self.choice=Choice.objects.create(question=self.question, choice_text="Cristiano Ronaldo", votes=1000)
        # self.data = {'question_text': 'Favourite meal?','pub_date': timezone.now()}

    def test_read_choice_detail(self):
        response = self.client.get(reverse('choice_detail', args=[self.choice.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_choice_list(self):
        response = self.client.get(reverse('choice_index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_choice(self):
        response = self.client.delete(reverse('choice_detail',args=[self.choice.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ChoiceUpdateTest(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text="Favourite Football player?", pub_date=timezone.now())
        self.choice = Choice.objects.create(question=self.question, choice_text="Cristiano Ronaldo", votes=1000)
        self.data = ChoiceSerializer(self.choice).data
        self.data.update({'choice_text': 'Lionel Messi'})

    def test_update_choice(self):
        response = self.client.put(reverse('choice_detail', args=[self.choice.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
